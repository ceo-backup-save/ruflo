#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Nova estratégia: duplas cruzadas pares 1-12 + fixa e excluída simultâneas
+ combinações de 20 dezenas.

Definições (explícitas):
  - Pares 1-12: baixos (1-6) = {02,04,06}, altos (7-12) = {08,10,12}
  - Duplas cruzadas: 1 baixa + 1 alta -> 3x3 = 9 duplas
  - Simultâneo: UM jogo/aposta deve conter a DUPLA FIXA e NÃO conter
    nenhuma dezena da DUPLA EXCLUÍDA. Logo fixa e excluída precisam ser
    DISJUNTAS (sem dezena em comum), senão é impossível (0 jogos).
    Pares ordenados disjuntos: 9 * (2*2) = 36.
  - Combinações de 20 dezenas: apostas que marcam 20 números
    (= 15.504 jogos simples, R$ 54.264,00 a R$ 3,50/jogo simples).
    Com fixa+excluída: 20 números incluem a fixa (2) e excluem a excluída (2),
    os outros 18 vêm das 21 dezenas restantes -> C(21,18)=1.330 apostas
    possíveis por par (fixa,excluída), de C(25,20)=53.130 apostas de 20 no total.
  - Versão simples equivalente (para comparar custo): jogos de 15 com
    fixa+excluída (13 das 21 restantes).

Retorno esperado: por real apostado é SEMPRE ~43-45%, qualquer que seja
a dupla, o tamanho da aposta ou a restrição — por simetria (linearidade).
"""
import csv
import itertools
import random
from collections import Counter
from math import comb
from pathlib import Path

from analise_lotofacil import CONCURSOS

BASE = Path(__file__).resolve().parent
ULTIMO = CONCURSOS[-1][0]
N = len(CONCURSOS)
PRECO_SIMPLES = 3.50
PREMIOS = {11: 7.0, 12: 14.0, 13: 35.0, 14: 1500.0, 15: 2000000.0}
BAIXOS = [2, 4, 6]
ALTOS = [8, 10, 12]
DUPLAS = [(b, a) for b in BAIXOS for a in ALTOS]  # 9


def fmt(t):
    return " ".join(f"{d:02d}" for d in t)


def premio_20bet(overlap):
    """Prêmio total de UMA aposta de 20 dezenas cujo conjunto tem `overlap`
    dezenas em comum com o sorteio (10..15), contando todos os jogos simples
    (subconjuntos de 15) que ela contém. Prêmios 14/15 ilustrativos."""
    total = 0.0
    detalhe = {}
    for h in (11, 12, 13, 14, 15):
        if h <= overlap and (15 - h) <= (20 - overlap):
            n = comb(overlap, h) * comb(20 - overlap, 15 - h)
            detalhe[h] = n
            total += n * PREMIOS[h]
    return total, detalhe


def main():
    assert len(DUPLAS) == 9

    # ---- estatísticas das 9 duplas cruzadas nos 100 concursos ----
    contagem = Counter()
    ultimo = {}
    for num, data, sorteio in CONCURSOS:
        s = set(sorteio)
        for d in DUPLAS:
            if set(d) <= s:
                contagem[d] += 1
                ultimo[d] = num
    rank_duplas = sorted(DUPLAS, key=lambda d: (-contagem[d], d))
    fixa = rank_duplas[0]
    # excluída: a menos frequente DISJUNTA da fixa (senão impossível)
    candidatas_excl = [d for d in rank_duplas[::-1] if not (set(d) & set(fixa))]
    excluida = candidatas_excl[0]

    # ---- pares ordenados disjuntos (fixa, excluída) ----
    pares_disjuntos = [(f, e) for f in DUPLAS for e in DUPLAS if not (set(f) & set(e))]
    assert len(pares_disjuntos) == 36

    # ---- probabilidades exatas aposta de 20 dezenas (sem restrição) ----
    total_20 = comb(25, 20)  # 53.130
    # overlap t = |aposta20 ∩ sorteio15| ; P(t) = C(20,t)*C(5,15-t)/C(25,15)
    p_overlap = {}
    for t in range(10, 16):
        p_overlap[t] = comb(20, t) * comb(5, 15 - t) / comb(25, 15)
    # EV de uma aposta de 20 = 15504 * EV simples
    p_simple = {h: comb(15, h) * comb(10, 15 - h) / comb(25, 15) for h in (11, 12, 13, 14, 15)}
    ev_simple = sum(p_simple[h] * PREMIOS[h] for h in p_simple)
    n_simple_por_20 = comb(20, 15)  # 15.504
    preco_20 = n_simple_por_20 * PRECO_SIMPLES
    ev_20 = n_simple_por_20 * ev_simple

    # ---- cenário simultâneo fixa+excluída (jogos simples de 15) ----
    # P(fixa toda no sorteio E excluída toda fora) p/ duplas disjuntas:
    # sorteio contém fixa (2) e evita excluída (2): C(21,13)/C(25,15)
    p_cenario_jackpot = comb(21, 13) / comb(25, 15)

    # ---- geração de exemplo ----
    rng = random.Random(20261110)
    restantes = [d for d in range(1, 26) if d not in fixa and d not in excluida]  # 21
    assert len(restantes) == 21

    # 20 jogos simples de 15: fixa + 13 das 21
    jogos15 = set()
    while len(jogos15) < 20:
        jogos15.add(tuple(sorted(list(fixa) + rng.sample(restantes, 13))))
    jogos15 = sorted(jogos15)

    # 5 apostas de 20 dezenas: fixa + 18 das 21
    apostas20 = set()
    while len(apostas20) < 5:
        apostas20.add(tuple(sorted(list(fixa) + rng.sample(restantes, 18))))
    apostas20 = sorted(apostas20)

    # ---- CSVs ----
    with open(BASE / "duplas_cruzadas_pares_1a12.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f, delimiter=";")
        w.writerow(["dupla_cruzada", "ocorrencias_em_100", "percentual_%", "ultimo_concurso", "atraso_concursos"])
        for d in rank_duplas:
            w.writerow([fmt(d), contagem[d], f"{contagem[d]:.1f}".replace(".", ","),
                        ultimo[d], ULTIMO - ultimo[d]])

    with open(BASE / "pares_fixa_excluida_disjuntos.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f, delimiter=";")
        w.writerow(["dupla_fixa", "dupla_excluida", "universo_restante", "jogos15_possiveis", "apostas20_possiveis"])
        for f_, e_ in pares_disjuntos:
            w.writerow([fmt(f_), fmt(e_), 21, comb(21, 13), comb(21, 18)])

    with open(BASE / "combinacoes_20_dezenas_exemplo.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f, delimiter=";")
        w.writerow(["tipo", "dupla_fixa", "dupla_excluida", "combinacao"])
        for j in jogos15:
            w.writerow(["jogo_15", fmt(fixa), fmt(excluida), fmt(j)])
        for j in apostas20:
            w.writerow(["aposta_20", fmt(fixa), fmt(excluida), fmt(j)])

    # ---- Backtest: 20 jogos simples (fixa+excluída) nos 100 concursos ----
    tot_hits = Counter()
    tot_premio15 = 0.0
    conc_com = Counter()
    linhas_bt = []
    for num, data, sorteio in CONCURSOS:
        s = set(sorteio)
        hits_c = Counter()
        premio_c = 0.0
        for j in jogos15:
            h = len(set(j) & s)
            if h >= 11:
                hits_c[h] += 1
                tot_hits[h] += 1
                premio_c += PREMIOS[h]
        tot_premio15 += premio_c
        if hits_c:
            conc_com[">=11"] += 1
        if any(h >= 13 for h in hits_c):
            conc_com[">=13"] += 1
        if any(h >= 14 for h in hits_c):
            conc_com[">=14"] += 1
        if hits_c.get(15):
            conc_com["==15"] += 1
        linhas_bt.append([num, data, hits_c.get(11, 0), hits_c.get(12, 0), hits_c.get(13, 0),
                          hits_c.get(14, 0), hits_c.get(15, 0), f"{premio_c:.2f}".replace(".", ",")])

    with open(BASE / "backtest_duplas_cruzadas.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f, delimiter=";")
        w.writerow(["concurso", "data", "jogos_11", "jogos_12", "jogos_13", "jogos_14", "jogos_15", "premio_R$"])
        w.writerows(linhas_bt)

    # ---- Backtest: 1 aposta de 20 (a 1ª gerada) nos 100 concursos ----
    aposta_ref = apostas20[0]
    tot_premio20 = 0.0
    overlaps = Counter()
    for num, data, sorteio in CONCURSOS:
        t = len(set(aposta_ref) & set(sorteio))
        overlaps[t] += 1
        premio, _ = premio_20bet(t)
        tot_premio20 += premio
    custo20_100 = preco_20 * 100
    custo15_100 = 20 * PRECO_SIMPLES * 100

    # ---- Relatório MD ----
    L = []
    L.append("# Duplas cruzadas pares 1–12: fixa + excluída simultâneas e combinações de 20 dezenas")
    L.append("")
    L.append("**Interpretação adotada (explícita):** duplas cruzadas = 1 par baixa (02,04,06) + 1 par alta (08,10,12) → **9 duplas**. “Simultaneamente” = **o mesmo jogo/aposta** contém a dupla fixa **e** não contém nenhuma dezena da dupla excluída (logo as duas duplas precisam ser **disjuntas**). “Combinações de 20 dezenas” = apostas que marcam **20 números** (= 15.504 jogos simples, R$ 54.264,00). Apresento também a versão equivalente em jogos simples de 15, para comparar custo.")
    L.append("")
    L.append("## 1) As 9 duplas cruzadas e sua presença nos últimos 100 concursos (esperado 35 em 100)")
    L.append("")
    L.append("| # | Dupla cruzada | Ocorrências | % | Último | Atraso |")
    L.append("|---:|---|---:|---:|---:|---:|")
    for i, d in enumerate(rank_duplas, 1):
        L.append(f"| {i} | {fmt(d)} | {contagem[d]} | {contagem[d]}% | {ultimo[d]} | {ULTIMO-ultimo[d]} |")
    L.append("")
    L.append(f"**Exemplo concreto usado abaixo:** dupla **FIXA = {fmt(fixa)}** (a mais frequente) e dupla **EXCLUÍDA = {fmt(excluida)}** (a menos frequente disjunta dela). Restam **21 dezenas** livres (25 − 2 fixas − 2 excluídas).")
    L.append("")
    L.append("## 2) Simultâneo fixa + excluída: o que acontece com o teto de acertos")
    L.append("")
    L.append("Sejam a = quantas da fixa saíram (0,1,2) e b = quantas da excluída saíram (0,1,2). Para um jogo simples de 15 com as duas restrições:")
    L.append("")
    L.append("| a (fixa no sorteio) | b (excluída no sorteio) | Teto do jogo |")
    L.append("|---:|---:|---:|")
    L.append("| 2 | 0 | **15 acertos** (único cenário de jackpot) |")
    L.append("| 2 | 1 | 14 acertos |")
    L.append("| 1 | 0 | 14 acertos |")
    L.append("| 2 | 2 | 13 acertos |")
    L.append("| 1 | 1 | 13 acertos |")
    L.append("| 0 | 0 | 13 acertos |")
    L.append("| 0 | 2 | 11 acertos |")
    L.append("")
    L.append(f"**Jackpot só é possível se a=2 e b=0**, cuja probabilidade é C(21,13)/C(25,15) = **{p_cenario_jackpot*100:.2f}%** por jogo — mas, incondicionalmente, cada jogo continua valendo 1/3.268.760 para 15 pontos (a chance condicional maior é compensada pela raridade do cenário).")
    L.append("")
    L.append(f"**Pares (fixa, excluída) disjuntos possíveis:** {len(pares_disjuntos)} pares ordenados (ver `pares_fixa_excluida_disjuntos.csv`). Pares que compartilham uma dezena são **impossíveis** (0 jogos) — ex.: fixa 06-12 e excluída 06-08 exigem que o 06 esteja e não esteja ao mesmo tempo.")
    L.append("")
    L.append("## 3) Combinações de 20 dezenas: cobertura e custo")
    L.append("")
    L.append(f"- Uma aposta de 20 dezenas cobre **{n_simple_por_20:,} jogos simples** e custa **R$ {preco_20:,.2f}**.")
    L.append(f"- Com fixa+excluída, há **C(21,18) = {comb(21,18):,} apostas de 20** possíveis por par (de C(25,20) = {total_20:,} no total).")
    L.append("- Probabilidades de uma aposta de 20 (sem restrição), pelo nº de dezenas do sorteio dentro da aposta (overlap t):")
    L.append("")
    L.append("| Overlap t | Probabilidade | Leitura |")
    L.append("|---:|---:|---|")
    for t in range(15, 9, -1):
        L.append(f"| {t} | {p_overlap[t]*100:.2f}% | {'jackpot da aposta (sorteio ⊆ aposta)' if t==15 else ''} |")
    L.append("")
    L.append(f"- **Retorno esperado de 1 aposta de 20:** {n_simple_por_20:,} × R$ {ev_simple:.2f} = **~R$ {ev_20:,.2f}** contra R$ {preco_20:,.2f} de custo → **~{ev_20/preco_20*100:.0f}% de retorno, prejuízo esperado ~R$ {preco_20-ev_20:,.2f} por aposta** — exatamente a mesma taxa dos jogos simples.")
    L.append(f"- **Exemplo gerado:** 5 apostas de 20 com fixa {fmt(fixa)} e excluída {fmt(excluida)} custariam **5 × R$ {preco_20:,.2f} = R$ {5*preco_20:,.2f} por concurso**. Os jogos estão em `combinacoes_20_dezenas_exemplo.csv` (junto com 20 jogos simples equivalentes, R$ 70,00).")
    L.append("")
    L.append("## 4) Backtest nos últimos 100 concursos")
    L.append("")
    L.append(f"**Versão simples (20 jogos de 15, fixa+excluída):** custo R$ {custo15_100:,.2f} em 100 concursos · prêmios R$ {tot_premio15:,.2f} · saldo **R$ {tot_premio15-custo15_100:,.2f}** ({tot_premio15/custo15_100*100:.1f}% de retorno). Acertos: 11×{tot_hits.get(11,0)}, 12×{tot_hits.get(12,0)}, 13×{tot_hits.get(13,0)}, 14×{tot_hits.get(14,0)}, 15×{tot_hits.get(15,0)}. Concursos com 13+: {conc_com.get('>=13',0)}/100 · com 14+: {conc_com.get('>=14',0)}/100 · com 15: {conc_com.get('==15',0)}/100.")
    L.append("")
    L.append(f"**Versão 20 dezenas (1 aposta de 20, fixa+excluída, a 1ª gerada):** custo R$ {custo20_100:,.2f} em 100 concursos · prêmios (contando todos os jogos simples dentro da aposta, com 14=R$ 1.500 e 15=R$ 2.000.000 ilustrativos e sem rateio) R$ {tot_premio20:,.2f} · saldo **R$ {tot_premio20-custo20_100:,.2f}** ({tot_premio20/custo20_100*100:.1f}% de retorno). Overlaps observados: " +
             ", ".join(f"t={t}: {overlaps[t]} concursos" for t in sorted(overlaps)) + ".")
    L.append("")
    L.append("⚠️ **Por que o retorno de 70,5% no backtest de 20 dezenas é enganoso:** ele é dominado por **1 único concurso com overlap t=15** (sorteio contido na aposta de 20), que sozinho paga ~R$ 2,26 milhões em prêmios ilustrativos (1 jogo de 15 + 75 de 14 + 1.050 de 13 + … dentro da aposta). Sem esse concurso, o retorno cai para ~29%. Na prática, o prêmio de 15 acertos é **rateado** entre todos os ganhadores do país, então o valor real seria bem menor. O backtest de 20 dezenas tem variância gigantesca — a expectativa de longo prazo continua ~45%.")
    L.append("")
    L.append("## 5) Expectativa de retorno (resumo)")
    L.append("")
    L.append("| Estratégia | Custo/concurso | Retorno esperado/concurso | Prejuízo esperado |")
    L.append("|---|---:|---:|---:|")
    L.append(f"| 20 jogos simples (fixa+excluída) | R$ 70,00 | ~R$ {20*ev_simple:.2f} | ~R$ {70-20*ev_simple:.2f} |")
    L.append(f"| 1 aposta de 20 dezenas (fixa+excluída) | R$ {preco_20:,.2f} | ~R$ {ev_20:,.2f} | ~R$ {preco_20-ev_20:,.2f} |")
    L.append(f"| 5 apostas de 20 dezenas | R$ {5*preco_20:,.2f} | ~R$ {5*ev_20:,.2f} | ~R$ {5*(preco_20-ev_20):,.2f} |")
    L.append("")
    L.append("**Conclusão:** as duplas cruzadas organizam bem a aposta (baixa+alta), e o simultâneo fixa+excluída é uma aposta de cenário (“esta dupla sai e aquela não sai”). Mas **não muda a expectativa de retorno**: ~43–45% do apostado em qualquer formato. A aposta de 20 dezenas só multiplica custo e prêmio esperado na mesma proporção — e, com fixa+excluída ao mesmo tempo, o jackpot fica restrito ao cenário a=2,b=0 (6,22% dos concursos).")
    L.append("")
    L.append("> ⚠️ Nenhuma dupla, fechamento ou frequência passada altera a esperança matemática negativa desenhada pela Caixa (43,35% de prêmio bruto). Aposta de 20 dezenas custa R$ 54 mil por concurso — trate como custo de entretenimento, nunca como investimento.")
    L.append("")
    L.append("## Arquivos")
    L.append("")
    L.append("- `duplas_cruzadas_pares_1a12.csv` — 9 duplas com frequência nos 100 concursos.")
    L.append("- `pares_fixa_excluida_disjuntos.csv` — 36 pares (fixa,excluída) possíveis.")
    L.append("- `combinacoes_20_dezenas_exemplo.csv` — 20 jogos simples + 5 apostas de 20 gerados.")
    L.append("- `backtest_duplas_cruzadas.csv` — backtest dos 20 jogos simples por concurso.")
    L.append("- `relatorio_duplas_cruzadas.html` — versão visual.")
    L.append("- `analise_duplas_cruzadas.py` — script reproduzível.")
    L.append("")
    (BASE / "relatorio_duplas_cruzadas.md").write_text("\n".join(L), encoding="utf-8")

    # ---- HTML visual (resumo) ----
    def barra(v, mx, cor):
        return f'<div class="bar"><span style="width:{v/mx*100:.1f}%;background:{cor}"></span></div>'
    maxd = max(contagem.values())
    linhas_duplas = "\n".join(
        f'<tr><td>{i}</td><td class="mono"><b>{fmt(d)}</b></td><td>{contagem[d]}</td><td>{contagem[d]}%</td>'
        f'<td>{barra(contagem[d], maxd, "#2563eb")}</td></tr>'
        for i, d in enumerate(rank_duplas, 1))
    html_doc = f"""<!DOCTYPE html><html lang="pt-BR"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1"><title>Duplas cruzadas — fixa + excluída + 20 dezenas</title>
<style>body{{font-family:system-ui,sans-serif;max-width:1000px;margin:0 auto;padding:24px;background:#f8fafc;color:#111}}
.card{{background:#fff;border:1px solid #e2e8f0;border-radius:12px;padding:18px;margin:16px 0}}
table{{border-collapse:collapse;width:100%;font-size:14px}}th,td{{border:1px solid #e2e8f0;padding:6px 8px;text-align:left}}th{{background:#eff6ff}}
.mono{{font-family:ui-monospace,monospace}}.bar{{background:#e2e8f0;border-radius:6px;height:14px;min-width:120px;overflow:hidden}}.bar span{{display:block;height:100%}}
.aviso{{background:#fef3c7;border:1px solid #f59e0b;border-radius:8px;padding:12px}}</style></head><body>
<h1>🔀 Duplas cruzadas pares 1–12 — fixa + excluída simultâneas</h1>
<p>Baixas (1–6): 02,04,06 · Altas (7–12): 08,10,12 · <b>9 duplas cruzadas</b> · Exemplo: <b>FIXA {fmt(fixa)}</b> + <b>EXCLUÍDA {fmt(excluida)}</b></p>
<div class="card"><h2>As 9 duplas nos últimos 100 concursos (esperado 35)</h2>
<table><tr><th>#</th><th>Dupla</th><th>Ocorr.</th><th>%</th><th>Frequência</th></tr>{linhas_duplas}</table></div>
<div class="card"><h2>💰 Expectativa de retorno</h2>
<table><tr><th>Estratégia</th><th>Custo/concurso</th><th>Retorno esperado</th><th>Prejuízo esperado</th></tr>
<tr><td>20 jogos simples (fixa+excluída)</td><td>R$ 70,00</td><td>~R$ {20*ev_simple:.2f}</td><td>~R$ {70-20*ev_simple:.2f}</td></tr>
<tr><td>1 aposta de 20 dezenas</td><td>R$ {preco_20:,.2f}</td><td>~R$ {ev_20:,.2f}</td><td>~R$ {preco_20-ev_20:,.2f}</td></tr>
<tr><td>5 apostas de 20 dezenas</td><td>R$ {5*preco_20:,.2f}</td><td>~R$ {5*ev_20:,.2f}</td><td>~R$ {5*(preco_20-ev_20):,.2f}</td></tr></table>
<p>Jackpot simultâneo só no cenário fixa toda no sorteio E excluída toda fora: <b>{p_cenario_jackpot*100:.2f}%</b> dos concursos. Por real apostado, o retorno é sempre ~43–45%.</p></div>
<div class="card"><h2>📈 Backtest (100 concursos)</h2>
<p>20 jogos simples: custo R$ {custo15_100:,.2f} · prêmios R$ {tot_premio15:,.2f} · saldo <b>R$ {tot_premio15-custo15_100:,.2f}</b><br>
1 aposta de 20: custo R$ {custo20_100:,.2f} · prêmios R$ {tot_premio20:,.2f} · saldo <b>R$ {tot_premio20-custo20_100:,.2f}</b></p></div>
<div class="aviso">⚠️ Nenhuma dupla ou frequência passada altera a esperança matemática negativa (43,35% de prêmio bruto). Aposta de 20 dezenas custa R$ 54 mil/concurso.</div>
</body></html>"""
    (BASE / "relatorio_duplas_cruzadas.html").write_text(html_doc, encoding="utf-8")

    print(f"Duplas cruzadas: {DUPLAS}")
    print(f"Rank: {[(fmt(d), contagem[d]) for d in rank_duplas]}")
    print(f"Fixa={fmt(fixa)} Excluida={fmt(excluida)} | pares disjuntos={len(pares_disjuntos)}")
    print(f"P jackpot simultaneo={p_cenario_jackpot*100:.2f}% | EV simples R${ev_simple:.2f} | preco20 R${preco_20:,.2f} EV20 R${ev_20:,.2f}")
    print(f"Backtest simples: custo R${custo15_100:,.2f} premios R${tot_premio15:,.2f} saldo R${tot_premio15-custo15_100:,.2f} hits={dict(tot_hits)}")
    print(f"Backtest 20bet: custo R${custo20_100:,.2f} premios R${tot_premio20:,.2f} saldo R${tot_premio20-custo20_100:,.2f} overlaps={dict(sorted(overlaps.items()))}")


if __name__ == "__main__":
    main()
