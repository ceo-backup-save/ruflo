#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Análise completa nos últimos 100 concursos (3726..3825):
  - Dezenas individuais (1..25): mais presentes / menos presentes
  - Duplas (C(25,2)=300): mais presentes / menos presentes
  - Trincas (C(25,3)=2300): mais presentes / menos presentes
  - Para cada categoria: frequência (nº de concursos em 100, %), último concurso
    em que apareceu e atraso (3825 - último), ou seja, "mais ausentes" nos dois
    sentidos: menos frequentes E há mais tempo sem aparecer.

Critério de presença:
  - dezena: está nas 15 sorteadas
  - dupla/trinca: TODAS as dezenas estão nas 15 sorteadas
Esperados teóricos (sorteio aleatório):
  - dezena: 15/25 = 60%  -> 60 em 100
  - dupla:  (15/25)*(14/24) = 35,0% -> 35 em 100
  - trinca: (15/25)*(14/24)*(13/23) = 19,78% -> ~19,8 em 100
"""
import csv
import itertools
from collections import Counter
from math import comb, sqrt
from pathlib import Path

from analise_lotofacil import CONCURSOS

BASE = Path(__file__).resolve().parent
ULTIMO = CONCURSOS[-1][0]  # 3825
N = len(CONCURSOS)         # 100


def fmt(t):
    return " ".join(f"{d:02d}" for d in t)


def analisar(combos, nome):
    """combos: lista de tuplas. Retorna lista de dicts ordenada por frequência desc."""
    contagem = Counter()
    ultimo = {}
    for num, data, sorteio in CONCURSOS:
        s = set(sorteio)
        for c in combos:
            if set(c) <= s:
                contagem[c] += 1
                ultimo[c] = num
    linhas = []
    for c in combos:
        cnt = contagem.get(c, 0)
        ult = ultimo.get(c)
        atraso = (ULTIMO - ult) if ult is not None else None
        linhas.append({
            "combo": c,
            "ocorrencias": cnt,
            "percentual": cnt / N * 100,
            "ultimo_concurso": ult,
            "atraso_concursos": atraso,
        })
    linhas.sort(key=lambda x: (-x["ocorrencias"], x["combo"]))
    return linhas


def salvar_csv(linhas, caminho, rotulo):
    with open(caminho, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f, delimiter=";")
        w.writerow([rotulo, "ocorrencias_em_100", "percentual_%", "ultimo_concurso", "atraso_concursos"])
        for r in linhas:
            w.writerow([fmt(r["combo"]), r["ocorrencias"],
                        f"{r['percentual']:.1f}".replace(".", ","),
                        r["ultimo_concurso"] if r["ultimo_concurso"] is not None else "",
                        r["atraso_concursos"] if r["atraso_concursos"] is not None else ""])


def tabela_top_bottom(linhas, k=15):
    top = linhas[:k]
    bottom = linhas[-k:][::-1]  # do menos frequente para cima? mantém ordem crescente de freq
    # bottom em ordem crescente (menos -> mais) para leitura
    bottom_ord = sorted(linhas, key=lambda x: (x["ocorrencias"], x["combo"]))[:k]
    return top, bottom_ord


def main():
    dezenas = [(d,) for d in range(1, 26)]
    duplas = list(itertools.combinations(range(1, 26), 2))
    trincas = list(itertools.combinations(range(1, 26), 3))
    assert len(duplas) == 300 and len(trincas) == 2300

    rank_d = analisar(dezenas, "dezena")
    rank_p = analisar(duplas, "dupla")
    rank_t = analisar(trincas, "trinca")

    salvar_csv(rank_d, BASE / "ranking_dezenas.csv", "dezena")
    salvar_csv(rank_p, BASE / "ranking_duplas.csv", "dupla")
    salvar_csv(rank_t, BASE / "ranking_trincas.csv", "trinca")

    # atraso: maior atraso = há mais tempo sem aparecer (menor último concurso)
    def por_atraso(linhas):
        return sorted([r for r in linhas if r["ultimo_concurso"] is not None],
                      key=lambda x: (-x["atraso_concursos"], x["combo"]))

    atraso_d = por_atraso(rank_d)
    atraso_p = por_atraso(rank_p)
    atraso_t = por_atraso(rank_t)

    # chi-quadrado das dezenas vs esperado 60
    chi2 = sum((r["ocorrencias"] - 60) ** 2 / 60 for r in rank_d)
    # desvios-padrão teóricos
    dp_d = sqrt(N * 0.6 * 0.4)
    dp_p = sqrt(N * 0.35 * 0.65)
    dp_t = sqrt(N * (15/25) * (14/24) * (13/23) * (1 - (15/25) * (14/24) * (13/23)))

    def bloco_tabela(linhas, titulo, esperado, dp, k=15):
        top, bottom = tabela_top_bottom(linhas, k)
        out = []
        out.append(f"### {titulo} — mais presentes (top {k})")
        out.append("")
        out.append("| # | Combinação | Ocorrências | % | Último concurso | Atraso |")
        out.append("|---:|---|---:|---:|---:|---:|")
        for i, r in enumerate(top, 1):
            out.append(f"| {i} | {fmt(r['combo'])} | {r['ocorrencias']} | {r['percentual']:.0f}% | {r['ultimo_concurso']} | {r['atraso_concursos']} |")
        out.append("")
        out.append(f"### {titulo} — menos presentes / mais ausentes (bottom {k})")
        out.append("")
        out.append("| # | Combinação | Ocorrências | % | Último concurso | Atraso |")
        out.append("|---:|---|---:|---:|---:|---:|")
        for i, r in enumerate(bottom, 1):
            out.append(f"| {i} | {fmt(r['combo'])} | {r['ocorrencias']} | {r['percentual']:.0f}% | {r['ultimo_concurso']} | {r['atraso_concursos']} |")
        out.append("")
        out.append(f"Esperado teórico: **{esperado}** em 100 concursos (desvio-padrão ≈ {dp:.1f}).")
        out.append("")
        return out

    L = []
    L.append("# Lotofácil — Dezenas, duplas e trincas mais presentes e mais ausentes (últimos 100 concursos)")
    L.append("")
    L.append("**Janela:** concursos **3726 a 3825** (100 concursos, 03/07/2026 a 09/11/2026) · **Último concurso:** 3825 · **Fonte:** Caixa Econômica Federal — Loterias.")
    L.append("")
    L.append("**Critério:** dezena/dupla/trinca “presente” = todas as suas dezenas estão nas 15 sorteadas. “Mais ausente” é apresentado nos dois sentidos: **menos frequente** nos 100 concursos **e** **maior atraso** (concursos desde a última aparição até o 3825).")
    L.append("")
    L.append(f"**Esperados teóricos (sorteio aleatório):** dezena 60 em 100 (60%) · dupla 35 em 100 (35%) · trinca ~19,8 em 100 (19,78%). Desvios-padrão: dezena ≈ {dp_d:.1f}, dupla ≈ {dp_p:.1f}, trinca ≈ {dp_t:.1f}.")
    L.append("")
    L.append(f"**Teste das dezenas:** chi-quadrado contra o esperado de 60 cada = **{chi2:.1f}** (24 graus de liberdade; valor crítico a 5% ≈ 36,4). Ou seja, a variação entre dezenas está **dentro do esperado pelo acaso** — nenhuma dezena está estatisticamente “quente” ou “fria” de forma convincente nesta janela.")
    L.append("")
    L.append("---")
    L.append("")
    L.append("## 1) Dezenas individuais (25)")
    L.append("")
    L += bloco_tabela(rank_d, "Dezenas", "60", dp_d, k=10)
    L.append("**Maior atraso (dezena há mais tempo sem sair):** " +
             ", ".join(f"{fmt(r['combo'])} (última no {r['ultimo_concurso']}, atraso {r['atraso_concursos']})" for r in atraso_d[:5]) + ".")
    L.append("")
    L.append("---")
    L.append("")
    L.append("## 2) Duplas (300 pares)")
    L.append("")
    L += bloco_tabela(rank_p, "Duplas", "35", dp_p)
    L.append("**Maior atraso (dupla há mais tempo sem aparecer junta):** " +
             ", ".join(f"{fmt(r['combo'])} (última no {r['ultimo_concurso']}, atraso {r['atraso_concursos']})" for r in atraso_p[:5]) + ".")
    L.append("")
    L.append("---")
    L.append("")
    L.append("## 3) Trincas (2.300 trios)")
    L.append("")
    L += bloco_tabela(rank_t, "Trincas", "~19,8", dp_t)
    L.append("**Maior atraso (trinca há mais tempo sem aparecer junta):** " +
             ", ".join(f"{fmt(r['combo'])} (última no {r['ultimo_concurso']}, atraso {r['atraso_concursos']})" for r in atraso_t[:5]) + ".")
    L.append("")
    L.append("---")
    L.append("")
    L.append("## 4) Como ler estes rankings (e o que NÃO concluir)")
    L.append("")
    L.append(f"- **Dezenas:** a mais frequente saiu em {rank_d[0]['ocorrencias']}% dos concursos e a menos em {rank_d[-1]['ocorrencias']}%. Com desvio-padrão de ~{dp_d:.0f}, essa amplitude é compatível com acaso em 25 dezenas.")
    L.append(f"- **Duplas:** a mais frequente apareceu junta em {rank_p[0]['ocorrencias']}% e a menos em {rank_p[-1]['ocorrencias']}% (esperado 35%, dp ~{dp_p:.0f}). Com 300 duplas, os extremos sempre parecem “especiais” — é o efeito de olhar muitos combos ao mesmo tempo (comparações múltiplas).")
    L.append(f"- **Trincas:** a mais frequente apareceu em {rank_t[0]['ocorrencias']}% e a menos em {rank_t[-1]['ocorrencias']}% (esperado ~19,8%, dp ~{dp_t:.0f}). Com 2.300 trincas, o máximo observado (~{rank_t[0]['ocorrencias']}) é o que se espera do maior de 2.300 sorteios aleatórios — não indica que essa trinca tenha mais chance no próximo concurso.")
    L.append("- **Atraso não “cobra”:** uma dupla/trinca há 20 concursos sem aparecer não está “na hora” de sair. Cada concurso é independente; a chance de qualquer dupla específica sair no próximo concurso continua 35% (dupla) / 19,78% (trinca), independentemente do atraso. Atraso longo é normal: com 2.300 trincas, sempre haverá alguma há muitos concursos sem aparecer.")
    L.append("- **Uso correto:** estes rankings descrevem o passado (estatística descritiva). Servem para estudar padrões, montar fechamentos por preferência pessoal ou auditar se os sorteios parecem aleatórios — **não** para prever o próximo sorteio nem para aumentar a chance de acerto.")
    L.append("")
    L.append("## Arquivos")
    L.append("")
    L.append("- `ranking_dezenas.csv` — 25 dezenas com ocorrências, %, último concurso e atraso.")
    L.append("- `ranking_duplas.csv` — 300 duplas, idem.")
    L.append("- `ranking_trincas.csv` — 2.300 trincas, idem.")
    L.append("- `analise_dezenas_duplas_trincas.py` — script reproduzível.")
    L.append("")

    (BASE / "relatorio_dezenas_duplas_trincas.md").write_text("\n".join(L), encoding="utf-8")

    # console
    for nome, rank in (("DEZENAS", rank_d), ("DUPLAS", rank_p), ("TRINCAS", rank_t)):
        print(f"\n=== {nome} ===")
        print("Top 10:")
        for r in rank[:10]:
            print(f"  {fmt(r['combo'])}  {r['ocorrencias']:3d}  {r['percentual']:.0f}%  ult={r['ultimo_concurso']} atraso={r['atraso_concursos']}")
        print("Bottom 10:")
        for r in sorted(rank, key=lambda x: (x["ocorrencias"], x["combo"]))[:10]:
            print(f"  {fmt(r['combo'])}  {r['ocorrencias']:3d}  {r['percentual']:.0f}%  ult={r['ultimo_concurso']} atraso={r['atraso_concursos']}")
    print(f"\nChi2 dezenas: {chi2:.1f} (df=24, crit 5% ~36.4)")
    print(f"Maior atraso dezenas: {[(fmt(r['combo']), r['atraso_concursos']) for r in atraso_d[:5]]}")
    print(f"Maior atraso duplas: {[(fmt(r['combo']), r['atraso_concursos']) for r in atraso_p[:5]]}")
    print(f"Maior atraso trincas: {[(fmt(r['combo']), r['atraso_concursos']) for r in atraso_t[:5]]}")


if __name__ == "__main__":
    main()
