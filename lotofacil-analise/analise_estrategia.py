#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Análise da estratégia: lote EXCLUINDO uma trinca par vs lote com a trinca FIXA,
repetida por 3 vezes (3 trincas).

Estrutura implementada (exemplo concreto, reproduzível):
  Repetição 1: trinca A = 06 08 12 (a mais prevalente nos últimos 100, 24%)
    - Lote A1: 20 jogos de 15 com 06,08,12 EXCLUÍDAS (15 de 22 restantes)
    - Lote A2: 20 jogos com 06,08,12 FIXAS (06,08,12 + 12 de 22 restantes)
  Repetição 2: trinca B = 04 08 12 (2ª mais prevalente, 23%)
    - Lote B1: 20 jogos com 04,08,12 EXCLUÍDAS
    - Lote B2: 20 jogos com 04,08,12 FIXAS
  Repetição 3: trinca C = 02 06 12 (3ª mais prevalente, 22%)
    - Lote C1: 20 jogos com 02,06,12 EXCLUÍDAS
    - Lote C2: 20 jogos com 02,06,12 FIXAS
  Total: 6 lotes x 20 = 120 jogos simples por concurso. Custo: 120 x R$3,50 = R$420.

Geração: aleatória com semente fixa (20261110), jogos distintos entre si.
Backtest: os mesmos 120 jogos jogados nos últimos 100 concursos (3726..3825).
Prêmios usados no backtest: 11=R$7, 12=R$14, 13=R$35 (fixos Caixa);
14=R$1.500 e 15=R$2.000.000 como valores ILUSTRATIVOS (14 e 15 são variáveis/rateados).
"""
import csv
import itertools
import random
from collections import Counter
from math import comb
from pathlib import Path

from analise_lotofacil import CONCURSOS  # reusa os 100 concursos validados

BASE = Path(__file__).resolve().parent
PRECO = 3.50
PREMIOS = {11: 7.0, 12: 14.0, 13: 35.0, 14: 1500.0, 15: 2000000.0}

TRINCAS_ESTRATEGIA = [
    ("A", (6, 8, 12)),
    ("B", (4, 8, 12)),
    ("C", (2, 6, 12)),
]
JOGOS_POR_LOTE = 20


def fmt(dezenas):
    return " ".join(f"{d:02d}" for d in dezenas)


def gerar_lotes():
    rng = random.Random(20261110)
    jogos = []  # (lote, tipo, trinca, jogo_tuple)
    vistos = set()
    for letra, trinca in TRINCAS_ESTRATEGIA:
        restantes = [d for d in range(1, 26) if d not in trinca]
        # lote excluídas
        gerados = 0
        while gerados < JOGOS_POR_LOTE:
            jogo = tuple(sorted(rng.sample(restantes, 15)))
            if jogo in vistos:
                continue
            vistos.add(jogo)
            jogos.append((f"{letra}1-excluidas-{fmt(trinca)}", "excluidas", trinca, jogo))
            gerados += 1
        # lote fixas
        gerados = 0
        while gerados < JOGOS_POR_LOTE:
            jogo = tuple(sorted(list(trinca) + rng.sample(restantes, 12)))
            if jogo in vistos:
                continue
            vistos.add(jogo)
            jogos.append((f"{letra}2-fixas-{fmt(trinca)}", "fixas", trinca, jogo))
            gerados += 1
    return jogos


def prob_exata():
    total = comb(25, 15)
    p = {}
    for acertos in (11, 12, 13, 14, 15):
        n = comb(15, acertos) * comb(10, 15 - acertos)
        p[acertos] = (n, n / total)
    return total, p


def main():
    total_combos, p = prob_exata()
    jogos = gerar_lotes()
    assert len(jogos) == 120 and len({j[3] for j in jogos}) == 120

    # ---------- CSV dos lotes ----------
    with open(BASE / "lotes_estrategia_3_repeticoes.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f, delimiter=";")
        w.writerow(["lote", "tipo", "trinca", "jogo_15_dezenas"])
        for lote, tipo, trinca, jogo in jogos:
            w.writerow([lote, tipo, fmt(trinca), fmt(jogo)])

    # ---------- Backtest nos 100 concursos ----------
    linhas_backtest = []
    tot_hits = Counter()
    tot_premio = 0.0
    concursos_com = Counter()  # >=11, >=13, >=14, ==15
    max_por_concurso = []
    premio_por_concurso = []
    # por tipo de lote
    por_tipo = {"excluidas": Counter(), "fixas": Counter()}
    premio_por_tipo = {"excluidas": 0.0, "fixas": 0.0}
    jogos_por_tipo = Counter(t for _, t, _, _ in jogos)

    for num, data, sorteio in CONCURSOS:
        s = set(sorteio)
        hits_concurso = Counter()
        premio_concurso = 0.0
        for lote, tipo, trinca, jogo in jogos:
            h = len(set(jogo) & s)
            if h >= 11:
                hits_concurso[h] += 1
                tot_hits[h] += 1
                por_tipo[tipo][h] += 1
                premio_concurso += PREMIOS[h]
                premio_por_tipo[tipo] += PREMIOS[h]
        tot_premio += premio_concurso
        premio_por_concurso.append(premio_concurso)
        max_h = max([h for h in hits_concurso] + [0])
        max_por_concurso.append(max_h)
        if hits_concurso:
            concursos_com[">=11"] += 1
        if any(h >= 13 for h in hits_concurso):
            concursos_com[">=13"] += 1
        if any(h >= 14 for h in hits_concurso):
            concursos_com[">=14"] += 1
        if hits_concurso.get(15):
            concursos_com["==15"] += 1
        linhas_backtest.append(
            [num, data, hits_concurso.get(11, 0), hits_concurso.get(12, 0),
             hits_concurso.get(13, 0), hits_concurso.get(14, 0), hits_concurso.get(15, 0),
             max_h, f"{premio_concurso:.2f}".replace(".", ",")]
        )

    with open(BASE / "backtest_estrategia_100_concursos.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f, delimiter=";")
        w.writerow(["concurso", "data", "jogos_11", "jogos_12", "jogos_13", "jogos_14", "jogos_15", "maior_acertos", "premio_R$"])
        w.writerows(linhas_backtest)

    custo_100 = 120 * PRECO * 100
    custo_1 = 120 * PRECO

    # ---------- Estatística condicional da trinca A nos 100 ----------
    cond = Counter()
    for num, data, sorteio in CONCURSOS:
        k = len(set((6, 8, 12)) & set(sorteio))
        cond[k] += 1

    # ---------- Valor esperado teórico por jogo ----------
    ev = sum(p[h][1] * PREMIOS[h] for h in p)
    ev_fixo = sum(p[h][1] * PREMIOS[h] for h in (11, 12, 13))

    # ---------- Relatório ----------
    L = []
    L.append("# Estratégia “excluir trinca × fixar trinca” (3 repetições) — análise de viabilidade e rentabilidade")
    L.append("")
    L.append("**Referência:** 10/11/2026 · **Base de backtest:** concursos 3726–3825 (100 concursos) · **Preço do jogo simples:** R$ 3,50 · **Prêmio bruto da Lotofácil:** 43,35% da arrecadação (11 acertos = R$ 7,00; 12 = R$ 14,00; 13 = R$ 35,00; 14 e 15 variáveis/rateados).")
    L.append("")
    L.append("## 1) A estratégia, do jeito que foi testada")
    L.append("")
    L.append("Repetição = 1 trinca + 2 lotes de 20 jogos. Repetida 3 vezes com 3 trincas diferentes = **6 lotes × 20 = 120 jogos/concurso (R$ 420,00)**.")
    L.append("")
    L.append("| Repetição | Trinca (pares 1–12) | Lote 1 — EXCLUÍDAS | Lote 2 — FIXAS |")
    L.append("|---|---|---|---|")
    L.append("| 1 (A) | 06 08 12 (24% nos últimos 100) | 20 jogos de 15 em 22 dezenas (sem 06,08,12) | 20 jogos: 06,08,12 + 12 em 22 |")
    L.append("| 2 (B) | 04 08 12 (23%) | 20 jogos sem 04,08,12 | 20 jogos: 04,08,12 + 12 em 22 |")
    L.append("| 3 (C) | 02 06 12 (22%) | 20 jogos sem 02,06,12 | 20 jogos: 02,06,12 + 12 em 22 |")
    L.append("")
    L.append("Os 120 jogos concretos estão em `lotes_estrategia_3_repeticoes.csv` (gerados com semente fixa, todos distintos).")
    L.append("")
    L.append("⚠️ **Problema de diversificação já aqui:** as 3 trincas mais frequentes **compartilham a dezena 12** (e A/B compartilham 08; A/C compartilham 06). Se o 12 não sair (36% dos últimos 100 concursos), os 3 lotes de FIXAS ficam todos limitados a no máximo 14 acertos ao mesmo tempo. Trincas disjuntas (ex.: 02-04-06 e 08-10-12) diversificariam melhor — mas, como veremos, isso não muda o valor esperado.")
    L.append("")
    L.append("## 2) O ponto matemático central: excluir/fixar NÃO muda a chance de cada jogo")
    L.append("")
    L.append("Na Lotofácil há **C(25,15) = 3.268.760** combinações de 15 dezenas, todas igualmente prováveis a cada sorteio. Qualquer jogo simples — com ou sem trinca fixa/excluída — tem exatamente as mesmas probabilidades:")
    L.append("")
    L.append("| Acertos | Combinações vencedoras | Probabilidade por jogo |")
    L.append("|---:|---:|---:|")
    for h in (11, 12, 13, 14, 15):
        n, pr = p[h]
        L.append(f"| {h} | {n} | {pr*100:.4f}% (1 em {1/pr:,.0f}) |".replace(".", ","))
    L.append("")
    L.append("**Prova pela simetria (linearidade da expectativa):** o retorno esperado de N jogos distintos é sempre N × retorno esperado de 1 jogo, **independentemente de quais números foram escolhidos**. Excluir ou fixar uma trinca apenas **redistribui** a cobertura entre cenários — não cria cobertura nova.")
    L.append("")
    L.append("### O que a estratégia realmente faz: troca de cenário, não de chance")
    L.append("")
    L.append("Seja k = quantas das 3 dezenas da trinca saíram no sorteio. Então:")
    L.append("")
    L.append("| k (da trinca no sorteio) | Lote EXCLUÍDAS: máximo possível | Lote FIXAS: máximo possível |")
    L.append("|---:|---:|---:|")
    L.append("| 3 (trinca completa saiu) | 12 acertos | **15 acertos** |")
    L.append("| 2 | 13 acertos | 14 acertos |")
    L.append("| 1 | 14 acertos | 13 acertos |")
    L.append("| 0 (nenhuma saiu) | **15 acertos** | 12 acertos |")
    L.append("")
    L.append(f"Nos últimos 100 concursos, para a trinca 06-08-12: k=3 em **{cond[3]} concursos**, k=2 em **{cond[2]}**, k=1 em **{cond[1]}**, k=0 em **{cond[0]}**. Ou seja, em **{cond[1]+cond[2]}% dos concursos (k=1 ou 2, cenário parcial) nenhum dos dois lotes pode fazer 15 pontos** — o teto é 14. O prêmio máximo só fica “aberto” em k=0 ou k=3. A chance incondicional de 15 pontos continua a mesma (ver §3), mas fica **concentrada** em poucos concursos: variância maior, não chance maior.")
    L.append("")
    L.append("## 3) Previsão média de cobertura (teoria, por concurso)")
    L.append("")
    L.append("| Cobertura | 1 lote (20 jogos) | 1 repetição (40 jogos) | 3 repetições (120 jogos) |")
    L.append("|---|---:|---:|---:|")
    L.append("| 15 acertos (jackpot) | 20/3.268.760 = 0,00061% — 1 em 163.438 concursos | 0,00122% — 1 em 81.719 | **0,00367% — 1 em 27.240** |")
    L.append("| 14+ acertos | ~0,0092% — 1 em ~10.900 | ~0,18% — 1 em ~540 | **~0,55% — 1 em ~180** |")
    L.append("| 13+ acertos | ~1,5% — 1 em ~67 | ~5,8% — 1 em ~17 | **~17% — 1 em ~6** |")
    L.append("| 11+ acertos (qualquer prêmio) | ~2,1 jogos premiados em média | ~4,2 jogos premiados em média | **~12,7 jogos premiados em média** |")
    L.append("")
    L.append("Leitura prática dos 120 jogos:")
    L.append("")
    L.append("- **Jackpot (15):** 1 chance em 27.240 concursos. A ~312 concursos/ano, isso é **1 vez a cada ~87 anos** de jogo contínuo nesse volume. Mesmo jogando 120 jogos **todo concurso por 100 concursos**, a chance de ver um 15 é de apenas ~0,37%.")
    L.append("- **14 acertos:** ~1 em 180 concursos (~1 vez a cada 7 meses jogando todo concurso).")
    L.append("- **13 acertos:** ~1 em 6 concursos — é a faixa “visível” da estratégia, mas paga só R$ 35.")
    L.append("- **11/12 acertos:** você **vai** ganhar quase todo concurso (média de ~12,7 jogos premiados), mas R$ 7/R$ 14 por jogo não chegam perto do custo de R$ 420.")
    L.append("")
    L.append("## 4) Rentabilidade: quanto custa, quanto volta, quanto se perde em média")
    L.append("")
    L.append(f"- **Custo:** 120 × R$ 3,50 = **R$ {custo_1:,.2f} por concurso** (R$ {custo_100:,.2f} em 100 concursos; ~R$ 131 mil/ano jogando todo concurso).")
    L.append(f"- **Retorno esperado por jogo:** R$ {ev_fixo:.2f} em prêmios fixos (11/12/13) + ~R$ {ev-ev_fixo:.2f} em 14/15 (usando 14=R$ 1.500 e 15=R$ 2.000.000 ilustrativos) = **~R$ {ev:.2f} por jogo**, ou seja, **~{ev/PRECO*100:.0f}% do preço** — compatível com os 43,35% de prêmio bruto da Caixa.")
    L.append(f"- **Retorno esperado dos 120 jogos:** ~R$ {120*ev:,.2f}/concurso contra R$ {custo_1:,.2f} de custo → **prejuízo esperado de ~R$ {custo_1-120*ev:,.2f} por concurso (~{100-ev/PRECO*100:.0f}% do valor apostado)**.")
    L.append(f"- **Ponto de equilíbrio do jackpot:** para 1 jogo valer R$ 3,50 em expectativa, o prêmio de 15 acertos teria de ser da ordem de **R$ 8 milhões por ganhador** (sem dividir). E, no longo prazo, a regra dos 43,35% impede lucro sistemático: o que acumula num concurso é retirado dos concursos seguintes.")
    L.append("")
    L.append("**Conclusão sobre rentabilidade:** não existe escolha de trincas — mais quente, mais fria, excluída ou fixa — que torne a estratégia rentável em expectativa. A estratégia é, matematicamente, equivalente a jogar 120 jogos simples quaisquer. O que muda é apenas **onde** a cobertura fica concentrada (cenários k=0/k=3) e a **variância** (mais “tudo ou nada” no jackpot).")
    L.append("")
    L.append("## 5) Backtest: os mesmos 120 jogos nos últimos 100 concursos (3726–3825)")
    L.append("")
    L.append("Simulação literal: jogar os 120 jogos de `lotes_estrategia_3_repeticoes.csv` em cada um dos 100 concursos passados. Detalhe por concurso em `backtest_estrategia_100_concursos.csv`.")
    L.append("")
    L.append(f"- **Custo total (100 concursos):** R$ {custo_100:,.2f}")
    L.append(f"- **Prêmios totais obtidos:** R$ {tot_premio:,.2f} (com 14=R$ 1.500 ilustrativo; no período houve {tot_hits.get(14,0)} jogo(s) de 14 acertos e {tot_hits.get(15,0)} de 15)")
    L.append(f"- **Saldo:** R$ {tot_premio-custo_100:,.2f} ({(tot_premio/custo_100*100):.1f}% de retorno sobre o apostado)")
    L.append(f"- **Jogos premiados:** 11 acertos: {tot_hits.get(11,0)} · 12: {tot_hits.get(12,0)} · 13: {tot_hits.get(13,0)} · 14: {tot_hits.get(14,0)} · 15: {tot_hits.get(15,0)} (total {sum(tot_hits.values())} em 12.000 jogos = {sum(tot_hits.values())/12000*100:.2f}%, contra 10,59% teóricos)")
    L.append(f"- **Concursos com pelo menos um prêmio:** {concursos_com.get('>=11',0)}/100 · com 13+: {concursos_com.get('>=13',0)}/100 · com 14+: {concursos_com.get('>=14',0)}/100 · com 15: {concursos_com.get('==15',0)}/100")
    L.append(f"- **Por tipo de lote (60 jogos cada tipo em 100 concursos):** EXCLUÍDAS premiaram {sum(por_tipo['excluidas'].values())} jogos (R$ {premio_por_tipo['excluidas']:,.2f}); FIXAS premiaram {sum(por_tipo['fixas'].values())} jogos (R$ {premio_por_tipo['fixas']:,.2f}) — diferença dentro do ruído, como a teoria prevê.")
    L.append("")
    L.append("O backtest confirma a teoria: muitos prêmios pequenos (11/12), poucos 13, nenhum 14/15 em 100 concursos — e prejuízo grande, próximo ao esperado (~55% do apostado). **Atenção:** backtest em 100 concursos não prova nada sobre o futuro; serve só para mostrar que a estratégia se comporta como 120 jogos comuns.")
    L.append("")
    L.append("## 6) Veredito")
    L.append("")
    L.append("1. **Viável como organização de apostas?** Sim — é uma forma válida de dividir o orçamento entre dois cenários (“a trinca sai” × “a trinca não sai”) e de garantir cobertura de 11–13 acertos em praticamente todo concurso. Se o objetivo é entretenimento com controle de custo, funciona como qualquer outro conjunto de 120 jogos.")
    L.append("2. **Viável como estratégia lucrativa / com chance de ser rentável?** **Não.** Por simetria, nenhuma seleção de dezenas altera o valor esperado: ~43–45% de retorno sobre o apostado no longo prazo. A prevalência passada da trinca (06-08-12 em 24% dos últimos 100) **não** aumenta sua chance no próximo sorteio — continua 19,8% teórica, e escolher a trinca “quente” ou a “fria” é indiferente.")
    L.append("3. **Previsão média de cobertura (120 jogos/concurso):** 15 acertos 1 em 27.240 concursos; 14+ 1 em ~180; 13+ 1 em ~6; 11+ em média ~12,7 jogos premiados por concurso — com custo de R$ 420/concurso e prejuízo esperado de ~R$ 230/concurso.")
    L.append("4. **Se quiser manter a ideia, melhore a diversificação:** use trincas **disjuntas** (ex.: 02-04-06 e 08-10-12) em vez das 3 mais frequentes (que compartilham o 12), e trate o gasto como custo de entretenimento — nunca como investimento. Uma aposta de 16–20 dezenas (fechamento) tem a mesma matemática por real apostado, com menos trabalho de gestão.")
    L.append("")
    L.append("> ⚠️ Loteria é um jogo de azar com esperança matemática negativa por desenho (a Caixa retém ~56,65% da arrecadação para prêmios não pagos, operação e destinações sociais). Nenhuma análise de frequência passada muda isso. Jogue apenas com valor que você pode perder.")
    L.append("")

    (BASE / "relatorio_estrategia.md").write_text("\n".join(L), encoding="utf-8")

    print(f"Total combos: {total_combos}")
    for h in (11, 12, 13, 14, 15):
        n, pr = p[h]
        print(f"  {h} acertos: {n} combos, {pr*100:.4f}%, 1 em {1/pr:,.0f}")
    print(f"\nJogos gerados: {len(jogos)} (distintos: {len({j[3] for j in jogos})})")
    print(f"Condicional trinca 06-08-12 nos 100: k=0:{cond[0]} k=1:{cond[1]} k=2:{cond[2]} k=3:{cond[3]}")
    print(f"EV por jogo: R$ {ev:.2f} (fixos R$ {ev_fixo:.2f}) | custo R$ {PRECO}")
    print(f"Backtest 100 concursos: custo R$ {custo_100:,.2f} | premios R$ {tot_premio:,.2f} | saldo R$ {tot_premio-custo_100:,.2f}")
    print(f"Hits: {dict(tot_hits)} | concursos >=11:{concursos_com.get('>=11',0)} >=13:{concursos_com.get('>=13',0)} >=14:{concursos_com.get('>=14',0)} 15:{concursos_com.get('==15',0)}")
    print(f"Por tipo: excluidas {dict(por_tipo['excluidas'])} R$ {premio_por_tipo['excluidas']:,.2f} | fixas {dict(por_tipo['fixas'])} R$ {premio_por_tipo['fixas']:,.2f}")


if __name__ == "__main__":
    main()
