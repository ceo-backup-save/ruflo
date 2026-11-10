#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Análise Lotofácil — últimos 100 concursos até 10/11/2026
e trincas formadas apenas por dezenas pares de 1 a 12.

Fonte dos resultados: Caixa Econômica Federal — Loterias
(via dataset ValorFinal, atualizado em 10/11/2026, último concurso 3825
de 09/11/2026; conferido com a API oficial da Caixa para o 3825).
O concurso 3826 (10/11/2026) ainda não havia sido sorteado no momento
da coleta (sorteio às 21h), portanto os últimos 100 concursos realizados
são os de número 3726 a 3825.

Metodologia:
- Lista 1: concursos 3726..3825 (100 concursos), apenas número + 15 dezenas.
- Lista 2: dezenas pares em [1,12] = {2,4,6,8,10,12}; todas as combinações
  de 3 em 3 => C(6,3) = 20 trincas únicas.
- Presença de uma trinca em um concurso = as 3 dezenas da trinca estão
  TODAS contidas nas 15 dezenas sorteadas.
- Contagem = nº de concursos (em 100) em que a trinca está presente.
- Percentual = contagem / 100 * 100.
- Um mesmo concurso pode conter várias trincas ao mesmo tempo
  (ex.: se um concurso tem 5 pares em 1..12, ele contém C(5,3)=10 trincas).
  Por isso a soma das contagens é maior que 100.
"""
import csv
import itertools
from collections import Counter
from pathlib import Path

BASE = Path(__file__).resolve().parent

# concurso, data, dezenas (ordem crescente, como publicado pela Caixa)
CONCURSOS = [
    (3726, "2026-07-03", [2,5,6,7,10,13,14,17,18,19,20,21,22,24,25]),
    (3727, "2026-07-04", [1,2,3,4,5,9,10,11,13,14,16,18,19,22,23]),
    (3728, "2026-07-06", [1,2,3,6,7,8,10,11,16,17,19,21,22,23,25]),
    (3729, "2026-07-07", [1,2,3,5,6,11,12,13,14,15,16,18,20,21,22]),
    (3730, "2026-07-08", [2,3,5,6,8,11,12,13,14,15,16,19,20,21,24]),
    (3731, "2026-07-09", [1,2,4,5,6,7,10,11,12,13,16,17,22,23,25]),
    (3732, "2026-07-10", [2,3,7,8,11,13,16,17,18,19,20,22,23,24,25]),
    (3733, "2026-07-11", [1,2,3,5,7,10,11,12,13,14,16,17,19,22,25]),
    (3734, "2026-07-13", [2,3,5,8,10,12,13,14,15,16,17,19,22,23,25]),
    (3735, "2026-07-14", [3,5,7,12,14,15,16,17,18,20,21,22,23,24,25]),
    (3736, "2026-07-15", [3,4,6,7,8,9,11,12,14,17,18,19,21,22,23]),
    (3737, "2026-07-16", [2,3,5,6,8,9,11,12,13,14,15,17,22,23,25]),
    (3738, "2026-07-17", [2,3,4,5,7,8,10,11,13,14,17,18,20,23,24]),
    (3739, "2026-07-19", [1,4,5,6,9,11,13,15,16,18,19,20,23,24,25]),
    (3740, "2026-07-20", [1,2,5,6,8,9,11,12,13,15,16,17,20,21,22]),
    (3741, "2026-07-21", [2,3,4,5,9,11,12,14,15,16,18,20,21,22,23]),
    (3742, "2026-07-22", [1,4,5,6,9,10,12,13,14,15,16,19,20,21,23]),
    (3743, "2026-07-23", [2,3,4,5,9,10,11,13,15,18,19,20,21,23,25]),
    (3744, "2026-07-24", [1,2,3,5,7,10,14,16,17,18,20,21,22,23,24]),
    (3745, "2026-07-26", [1,2,4,5,6,7,8,9,10,12,13,19,21,22,24]),
    (3746, "2026-07-27", [1,3,4,6,7,8,9,10,14,15,17,18,21,22,24]),
    (3747, "2026-07-28", [1,2,4,5,6,8,9,11,12,13,18,19,21,24,25]),
    (3748, "2026-07-29", [1,4,5,6,8,9,11,13,14,15,17,19,20,22,25]),
    (3749, "2026-07-30", [1,2,3,7,8,9,11,12,14,17,19,21,23,24,25]),
    (3750, "2026-07-31", [1,2,5,6,7,11,12,13,15,18,19,20,22,24,25]),
    (3751, "2026-08-02", [1,2,4,7,8,9,11,12,16,17,18,19,21,23,24]),
    (3752, "2026-08-03", [2,3,6,7,9,10,11,12,13,14,15,16,17,21,24]),
    (3753, "2026-08-04", [1,2,4,6,8,9,14,15,16,17,19,21,22,24,25]),
    (3754, "2026-08-05", [1,3,4,5,7,8,11,12,13,14,16,20,21,23,25]),
    (3755, "2026-08-06", [3,4,5,7,8,9,11,12,16,18,20,22,23,24,25]),
    (3756, "2026-08-07", [2,3,5,6,9,10,11,13,14,15,16,19,20,21,22]),
    (3757, "2026-08-09", [1,2,3,4,6,8,11,12,15,17,20,21,22,23,24]),
    (3758, "2026-08-10", [1,3,4,5,8,9,11,12,13,14,17,18,20,24,25]),
    (3759, "2026-08-11", [1,2,4,5,6,7,9,10,11,12,13,14,17,24,25]),
    (3760, "2026-08-12", [2,4,5,8,9,10,11,13,14,16,19,21,22,24,25]),
    (3761, "2026-08-13", [1,3,6,9,12,13,14,15,16,17,18,21,23,24,25]),
    (3762, "2026-08-14", [1,2,3,4,5,6,9,10,13,16,18,21,22,23,25]),
    (3763, "2026-08-16", [1,2,3,4,5,8,9,14,15,17,20,21,22,23,24]),
    (3764, "2026-08-17", [2,3,4,5,6,7,8,9,12,13,15,18,21,22,25]),
    (3765, "2026-08-18", [1,5,6,10,11,12,13,15,16,17,19,21,22,24,25]),
    (3766, "2026-08-19", [1,2,3,5,8,9,11,13,14,16,17,19,21,23,24]),
    (3767, "2026-08-20", [2,4,6,7,9,10,11,13,14,15,16,20,21,22,23]),
    (3768, "2026-08-21", [2,3,4,5,6,7,10,11,12,14,15,17,20,23,24]),
    (3769, "2026-08-23", [1,2,3,4,5,9,10,11,15,16,17,21,23,24,25]),
    (3770, "2026-08-24", [1,2,4,7,8,12,13,15,16,17,18,19,23,24,25]),
    (3771, "2026-08-25", [2,3,4,5,9,10,11,12,15,16,17,18,21,23,25]),
    (3772, "2026-08-26", [3,5,6,7,8,9,11,12,14,15,18,20,21,23,25]),
    (3773, "2026-08-27", [3,4,7,9,11,13,14,15,17,18,20,21,22,24,25]),
    (3774, "2026-08-28", [1,3,4,5,6,7,9,12,14,15,16,18,19,23,24]),
    (3775, "2026-08-30", [1,4,5,6,8,10,11,12,13,15,17,18,19,23,25]),
    (3776, "2026-08-31", [3,5,7,8,10,14,16,17,18,19,20,21,23,24,25]),
    (3777, "2026-09-01", [3,5,7,8,9,10,12,13,15,19,20,21,22,24,25]),
    (3778, "2026-09-02", [1,2,3,5,6,8,9,10,13,14,16,17,18,20,22]),
    (3779, "2026-09-03", [3,4,5,7,8,10,11,13,14,16,17,19,23,24,25]),
    (3780, "2026-09-15", [1,2,3,4,5,6,7,12,15,16,17,19,21,22,23]),
    (3781, "2026-09-16", [3,5,6,7,8,9,11,12,13,16,19,21,22,24,25]),
    (3782, "2026-09-17", [3,4,5,7,8,11,15,16,17,18,19,20,22,23,25]),
    (3783, "2026-09-18", [1,3,4,5,6,12,14,15,16,17,19,22,23,24,25]),
    (3784, "2026-09-20", [1,2,8,10,11,12,15,16,18,19,20,21,22,24,25]),
    (3785, "2026-09-21", [1,4,7,8,11,12,14,15,17,18,19,22,23,24,25]),
    (3786, "2026-09-22", [1,3,6,7,8,9,12,13,14,16,18,21,23,24,25]),
    (3787, "2026-09-23", [3,4,6,8,10,11,12,13,15,17,19,20,22,23,24]),
    (3788, "2026-09-24", [1,4,5,7,8,9,12,16,17,18,20,21,22,23,24]),
    (3789, "2026-09-25", [6,7,8,9,11,12,13,14,15,16,17,18,19,23,25]),
    (3790, "2026-09-27", [1,3,4,5,6,7,9,11,14,15,16,17,20,21,25]),
    (3791, "2026-09-28", [1,2,4,6,8,9,11,12,13,14,15,16,19,24,25]),
    (3792, "2026-09-29", [2,4,6,7,8,10,11,12,14,15,16,20,23,24,25]),
    (3793, "2026-09-30", [1,3,7,8,10,11,13,14,15,17,19,20,21,24,25]),
    (3794, "2026-10-01", [1,3,4,5,6,8,10,12,13,15,18,19,21,23,24]),
    (3795, "2026-10-02", [1,3,4,5,6,8,10,11,12,13,14,18,19,22,24]),
    (3796, "2026-10-03", [3,4,5,6,7,9,10,11,12,15,16,19,20,21,24]),
    (3797, "2026-10-05", [1,2,3,6,7,8,9,10,13,14,16,18,19,20,23]),
    (3798, "2026-10-06", [1,2,4,5,6,7,8,9,10,11,14,18,19,20,23]),
    (3799, "2026-10-07", [1,3,4,5,7,8,10,12,13,18,19,20,23,24,25]),
    (3800, "2026-10-08", [1,2,3,4,5,7,8,9,10,12,13,14,15,19,21]),
    (3801, "2026-10-09", [3,4,7,8,9,11,12,13,15,17,19,20,21,23,24]),
    (3802, "2026-10-11", [2,3,5,6,9,10,11,12,14,15,19,20,21,23,24]),
    (3803, "2026-10-13", [3,6,7,8,9,11,12,13,15,16,19,20,21,22,23]),
    (3804, "2026-10-14", [1,2,6,7,8,12,14,15,16,17,18,19,21,24,25]),
    (3805, "2026-10-15", [3,5,6,7,8,10,11,13,14,15,19,22,23,24,25]),
    (3806, "2026-10-16", [4,5,6,7,8,9,11,13,16,19,20,21,23,24,25]),
    (3807, "2026-10-18", [1,3,4,7,10,11,13,16,17,19,20,22,23,24,25]),
    (3808, "2026-10-19", [1,4,7,10,12,13,14,15,17,18,19,20,21,22,24]),
    (3809, "2026-10-20", [1,3,4,5,6,8,9,11,17,18,19,20,21,23,25]),
    (3810, "2026-10-21", [1,5,6,7,10,11,14,15,16,17,18,19,20,23,24]),
    (3811, "2026-10-22", [1,3,5,7,8,9,10,11,12,15,16,18,19,23,25]),
    (3812, "2026-10-23", [3,4,5,7,8,11,13,16,17,19,20,21,23,24,25]),
    (3813, "2026-10-24", [4,5,6,8,10,12,13,14,15,16,17,20,22,23,25]),
    (3814, "2026-10-26", [1,4,6,8,9,12,13,15,16,17,18,21,22,24,25]),
    (3815, "2026-10-27", [3,5,6,9,10,11,12,13,14,15,16,17,19,23,25]),
    (3816, "2026-10-28", [1,2,3,4,6,8,13,14,16,17,18,20,22,24,25]),
    (3817, "2026-10-29", [2,6,8,10,11,12,13,15,16,18,19,22,23,24,25]),
    (3818, "2026-10-30", [2,3,4,5,6,12,14,15,16,17,19,20,22,23,24]),
    (3819, "2026-11-01", [1,5,6,7,8,9,11,12,13,14,15,16,22,24,25]),
    (3820, "2026-11-03", [2,3,5,6,11,12,13,14,15,16,21,22,23,24,25]),
    (3821, "2026-11-04", [1,5,6,9,10,12,14,17,18,19,20,21,22,23,25]),
    (3822, "2026-11-05", [1,2,6,7,9,10,12,13,15,17,18,20,21,24,25]),
    (3823, "2026-11-06", [3,6,7,8,10,11,15,16,17,18,20,21,22,23,24]),
    (3824, "2026-11-08", [1,2,3,7,11,12,13,14,15,17,18,19,22,24,25]),
    (3825, "2026-11-09", [1,3,4,5,6,7,8,9,10,14,15,17,19,20,23]),
]

PARES_1_A_12 = [2, 4, 6, 8, 10, 12]
TRINCAS = list(itertools.combinations(PARES_1_A_12, 3))  # 20 trincas


def fmt(dezenas):
    return " ".join(f"{d:02d}" for d in dezenas)


def main():
    # validações
    assert len(CONCURSOS) == 100, len(CONCURSOS)
    assert [c[0] for c in CONCURSOS] == list(range(3726, 3826))
    for num, data, dez in CONCURSOS:
        assert len(dez) == 15 and len(set(dez)) == 15 and all(1 <= d <= 25 for d in dez), num
        assert dez == sorted(dez), num
    assert len(TRINCAS) == 20

    n = len(CONCURSOS)

    # contagem por trinca
    contagem = Counter()
    concursos_por_trinca = {t: [] for t in TRINCAS}
    for num, data, dez in CONCURSOS:
        s = set(dez)
        for t in TRINCAS:
            if set(t) <= s:
                contagem[t] += 1
                concursos_por_trinca[t].append(num)

    # frequência individual das dezenas pares 1..12 (contexto)
    freq_dezena = Counter()
    for _, _, dez in CONCURSOS:
        for d in dez:
            if d in PARES_1_A_12:
                freq_dezena[d] += 1

    # ranking: maior -> menor; desempate pela trinca em ordem crescente
    ranking = sorted(TRINCAS, key=lambda t: (-contagem[t], t))

    # ---- CSV Lista 1 ----
    with open(BASE / "lista1_ultimos_100_concursos.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f, delimiter=";")
        w.writerow(["concurso", "dezenas"])
        for num, data, dez in CONCURSOS:
            w.writerow([num, fmt(dez)])

    # ---- CSV Lista 2 + estatística ----
    with open(BASE / "lista2_trincas_pares_1a12_estatistica.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f, delimiter=";")
        w.writerow(["trinca", "ocorrencias_em_100_concursos", "percentual_%", "concursos_em_que_apareceu"])
        for t in ranking:
            c = contagem[t]
            w.writerow([fmt(t), c, f"{c/n*100:.1f}".replace(".", ","),
                        " ".join(str(x) for x in concursos_por_trinca[t])])

    # ---- Relatório Markdown ----
    linhas = []
    linhas.append("# Lotofácil — Últimos 100 concursos × Trincas pares de 1 a 12")
    linhas.append("")
    linhas.append("**Data de referência:** 10/11/2026  ")
    linhas.append("**Último concurso realizado:** 3825 (09/11/2026) — o concurso 3826, de 10/11/2026, ainda não tinha sido sorteado no momento da coleta (sorteio às 21h).  ")
    linhas.append("**Janela analisada:** concursos **3726 a 3825** (100 concursos, de 03/07/2026 a 09/11/2026).  ")
    linhas.append("**Fonte:** Caixa Econômica Federal — Loterias (dataset ValorFinal atualizado em 10/11/2026, conferido com a API oficial da Caixa).")
    linhas.append("")
    linhas.append("> **Observação sobre o percentual:** o pedido menciona \"10 concursos analisados\", mas a Lista 1 tem 100 concursos. Todos os percentuais abaixo usam a base correta de **100 concursos** (percentual = ocorrências ÷ 100 × 100).")
    linhas.append("")
    linhas.append("---")
    linhas.append("")
    linhas.append("## 1) Lista 1 — Últimos 100 concursos (número + 15 dezenas)")
    linhas.append("")
    linhas.append("| Concurso | Dezenas sorteadas |")
    linhas.append("|---:|---|")
    for num, data, dez in CONCURSOS:
        linhas.append(f"| {num} | {fmt(dez)} |")
    linhas.append("")
    linhas.append("---")
    linhas.append("")
    linhas.append("## 2) Lista 2 — Todas as trincas únicas só com pares de 1 a 12")
    linhas.append("")
    linhas.append("Dezenas pares no intervalo 1–12: **02, 04, 06, 08, 10, 12** (6 dezenas).")
    linhas.append("Combinações de 3 em 3: **C(6,3) = 20 trincas únicas**:")
    linhas.append("")
    for i, t in enumerate(TRINCAS, 1):
        linhas.append(f"{i}. {fmt(t)}")
    linhas.append("")
    linhas.append("---")
    linhas.append("")
    linhas.append("## 3) Comparação / levantamento estatístico")
    linhas.append("")
    linhas.append("**Critério de presença:** uma trinca \"aparece\" em um concurso quando as suas 3 dezenas estão **todas** entre as 15 sorteadas. Um mesmo concurso pode conter várias trincas ao mesmo tempo (se tiver, por exemplo, 5 pares em 1–12, contém C(5,3) = 10 trincas). Por isso a soma das ocorrências (ver abaixo) é maior que 100 — não é um erro, é a natureza da contagem por presença.")
    linhas.append("")
    linhas.append("### 3.1 Ranking completo das 20 trincas (mais → menos prevalente)")
    linhas.append("")
    linhas.append("| # | Trinca | Ocorrências (em 100) | Percentual |")
    linhas.append("|---:|---|---:|---:|")
    for i, t in enumerate(ranking, 1):
        c = contagem[t]
        linhas.append(f"| {i} | {fmt(t)} | {c} | {c/n*100:.0f}% |")
    linhas.append("")
    total_ocorr = sum(contagem.values())
    linhas.append(f"**Soma de todas as presenças:** {total_ocorr} (média de {total_ocorr/n:.2f} trincas pares 1–12 por concurso).")
    linhas.append("")
    linhas.append("### 3.2 Trincas MAIS prevalentes")
    linhas.append("")
    max_c = contagem[ranking[0]]
    for t in [x for x in ranking if contagem[x] == max_c]:
        linhas.append(f"- **{fmt(t)}** — {max_c} vezes ({max_c/n*100:.0f}% dos 100 concursos)")
    linhas.append("")
    linhas.append("### 3.3 Trincas MENOS prevalentes")
    linhas.append("")
    min_c = contagem[ranking[-1]]
    for t in [x for x in ranking if contagem[x] == min_c]:
        linhas.append(f"- **{fmt(t)}** — {min_c} vezes ({min_c/n*100:.0f}% dos 100 concursos)")
    linhas.append("")
    linhas.append("### 3.4 Contexto: frequência de cada dezena par (1–12) nos 100 concursos")
    linhas.append("")
    linhas.append("| Dezena | Nº de concursos em que saiu | Percentual |")
    linhas.append("|---:|---:|---:|")
    for d in sorted(PARES_1_A_12, key=lambda x: -freq_dezena[x]):
        linhas.append(f"| {d:02d} | {freq_dezena[d]} | {freq_dezena[d]/n*100:.0f}% |")
    linhas.append("")
    linhas.append("### 3.5 Leitura dos resultados")
    linhas.append("")
    # texto dinâmico
    top3 = ranking[:3]
    bot3 = ranking[-3:]
    linhas.append(f"- No topo, a trinca **{fmt(top3[0])}** apareceu em **{contagem[top3[0]]}** dos 100 concursos ({contagem[top3[0]]/n*100:.0f}%).")
    linhas.append(f"- Na base, a trinca **{fmt(bot3[-1])}** apareceu em apenas **{contagem[bot3[-1]]}** dos 100 concursos ({contagem[bot3[-1]]/n*100:.0f}%).")
    linhas.append(f"- A amplitude entre a mais e a menos frequente é de {max_c - min_c} concursos ({max_c/n*100:.0f}% contra {min_c/n*100:.0f}%).")
    linhas.append("- Referência teórica: se o sorteio fosse perfeitamente aleatório, cada trinca específica teria probabilidade de aparecer em um concurso de (15/25)×(14/24)×(13/23) ≈ **19,8%**, ou seja, cerca de **20 concursos em 100**. Os valores observados (ver ranking) giram em torno desse patamar, com variações compatíveis com acaso em uma amostra de 100 concursos.")
    linhas.append("")
    linhas.append("> ⚠️ **Aviso importante:** a Lotofácil é um sorteio independente — cada concurso é um novo sorteio, sem memória. A frequência passada de uma trinca **não aumenta nem diminui** a chance dela sair no próximo concurso. Este levantamento é estatística descritiva do passado, não uma previsão nem garantia de acerto.")
    linhas.append("")
    linhas.append("---")
    linhas.append("")
    linhas.append("## Arquivos gerados")
    linhas.append("")
    linhas.append("- `lista1_ultimos_100_concursos.csv` — Lista 1 em CSV (concurso; dezenas).")
    linhas.append("- `lista2_trincas_pares_1a12_estatistica.csv` — Lista 2 com ocorrências, percentual e concursos em que cada trinca apareceu.")
    linhas.append("- `analise_lotofacil.py` — script reproduzível que gerou este relatório.")
    linhas.append("")

    (BASE / "relatorio.md").write_text("\n".join(linhas), encoding="utf-8")

    # resumo no console
    print(f"Concursos: {len(CONCURSOS)} ({CONCURSOS[0][0]}..{CONCURSOS[-1][0]})")
    print(f"Trincas: {len(TRINCAS)}")
    print(f"Soma presenças: {total_ocorr} | média/concurso: {total_ocorr/n:.2f}")
    print("\nRanking (trinca — ocorrências — %):")
    for t in ranking:
        print(f"  {fmt(t)}  {contagem[t]:3d}  {contagem[t]/n*100:4.0f}%")
    print("\nDezenas pares individuais:")
    for d in sorted(PARES_1_A_12, key=lambda x: -freq_dezena[x]):
        print(f"  {d:02d}  {freq_dezena[d]:3d}  {freq_dezena[d]/n*100:4.0f}%")


if __name__ == "__main__":
    main()
