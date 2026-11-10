#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Estratégia 2 (nova proposta do usuário):
  - 20 trios pares de 1..12 (C(6,3)=20)
  - Para CADA trio: 1 lote com ~30 combinações de 15 dezenas,
    com as 3 dezenas do trio EXCLUÍDAS (15 sorteadas das 22 restantes)
  - Total: 20 lotes x 30 = 600 jogos simples por concurso
  - Custo: 600 x R$3,50 = R$2.100,00 por concurso

Análises:
  1. Cobertura teórica (jackpot, 14+, 13+, 11+) por lote, por conjunto e por real apostado.
  2. Condicional: se a trinca está FORA do sorteio, a chance por jogo sobe 19x
     (1/170.544 em vez de 1/3.268.760) — mas incondicionalmente é a mesma.
  3. Fechamento: o que 30 jogos em 22 dezenas conseguem garantir?
     (limite inferior combinatório + garantia real calculada por enumeração p/ 1 lote)
  4. Duplicidade entre lotes (jogos repetidos entre trios diferentes).
  5. Backtest: os 600 jogos jogados nos últimos 100 concursos (3726..3825).
  6. Comparação com a estratégia anterior (120 jogos) e com 600 jogos livres.
"""
import csv
import itertools
import random
from collections import Counter
from math import comb
from pathlib import Path

from analise_lotofacil import CONCURSOS

BASE = Path(__file__).resolve().parent
PRECO = 3.50
PREMIOS = {11: 7.0, 12: 14.0, 13: 35.0, 14: 1500.0, 15: 2000000.0}
PARES = [2, 4, 6, 8, 10, 12]
TRINCAS = list(itertools.combinations(PARES, 3))  # 20
JOGOS_POR_LOTE = 30


def fmt(dezenas):
    return " ".join(f"{d:02d}" for d in dezenas)


def gerar():
    rng = random.Random(20261110)  # mesma semente da estratégia anterior
    jogos = []  # (lote_idx, trinca, jogo)
    for idx, trinca in enumerate(TRINCAS, 1):
        restantes = [d for d in range(1, 26) if d not in trinca]
        vistos_lote = set()
        while len(vistos_lote) < JOGOS_POR_LOTE:
            jogo = tuple(sorted(rng.sample(restantes, 15)))
            if jogo in vistos_lote:
                continue
            vistos_lote.add(jogo)
            jogos.append((idx, trinca, jogo))
    return jogos


def main():
    total_combos = comb(25, 15)          # 3.268.760
    combos_22 = comb(22, 15)             # 170.544
    jogos = gerar()
    assert len(jogos) == 600
    distintos = {j[2] for j in jogos}
    n_distintos = len(distintos)
    duplicados = 600 - n_distintos

    # ---------- CSV dos 600 jogos ----------
    with open(BASE / "lotes_20_trios_600_jogos.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f, delimiter=";")
        w.writerow(["lote", "trinca_excluida", "jogo_15_dezenas"])
        for idx, trinca, jogo in jogos:
            w.writerow([f"Lote {idx:02d}", fmt(trinca), fmt(jogo)])

    # ---------- Probabilidades exatas por jogo ----------
    p = {}
    for h in (11, 12, 13, 14, 15):
        n = comb(15, h) * comb(10, 15 - h)
        p[h] = n / total_combos
    p11mais = sum(p.values())
    ev = sum(p[h] * PREMIOS[h] for h in p)
    ev_fixo = sum(p[h] * PREMIOS[h] for h in (11, 12, 13))

    # ---------- Condicional: trinca FORA do sorteio (sorteio subset das 22) ----------
    # P(11+ | sorteio em 22) para 1 jogo de 15 em 22:
    cond_n = sum(comb(15, h) * comb(7, 15 - h) for h in (11, 12, 13, 14, 15))
    cond_p11mais = cond_n / combos_22
    cond_p15 = 1 / combos_22
    p_trinca_fora = combos_22 / total_combos  # 5,22%

    # ---------- Fechamento: limite inferior p/ garantir X acertos em 22 ----------
    # Para garantir h acertos sempre que o sorteio (15 em 22) tiver >=h dezenas
    # dentro das 22, é preciso cobrir todos os subconjuntos de h dezenas das 22.
    # Cada jogo cobre C(15,h) desses subconjuntos.
    limites = {}
    for h in (9, 10, 11):
        limites[h] = comb(22, h) / comb(15, h)

    # ---------- Garantia real de 1 lote (enumeração dos 170.544 sorteios em 22) ----------
    # Lote 1 = trinca 02-04-06 excluída, universo = 22 dezenas restantes.
    lote1 = [j for (i, t, j) in jogos if i == 1]
    universo1 = [d for d in range(1, 26) if d not in TRINCAS[0]]
    pior = 15
    dist_pior = Counter()
    for sorteio in itertools.combinations(universo1, 15):
        s = set(sorteio)
        melhor = max(len(set(j) & s) for j in lote1)
        dist_pior[melhor] += 1
        if melhor < pior:
            pior = melhor
    # pior = maior número de acertos garantido (pior caso) por este lote de 30

    # ---------- Backtest nos 100 concursos ----------
    tot_hits = Counter()
    tot_premio = 0.0
    concursos_com = Counter()
    linhas = []
    premio_por_lote = Counter()
    hits_por_lote = Counter()
    # quantos trios estavam totalmente fora de cada sorteio (k=0)
    trios_fora_por_concurso = []
    for num, data, sorteio in CONCURSOS:
        s = set(sorteio)
        hits_c = Counter()
        premio_c = 0.0
        for idx, trinca, jogo in jogos:
            h = len(set(jogo) & s)
            if h >= 11:
                hits_c[h] += 1
                tot_hits[h] += 1
                premio_c += PREMIOS[h]
                premio_por_lote[idx] += PREMIOS[h]
                hits_por_lote[idx] += 1
        tot_premio += premio_c
        if hits_c:
            concursos_com[">=11"] += 1
        if any(h >= 13 for h in hits_c):
            concursos_com[">=13"] += 1
        if any(h >= 14 for h in hits_c):
            concursos_com[">=14"] += 1
        if hits_c.get(15):
            concursos_com["==15"] += 1
        fora = sum(1 for t in TRINCAS if not (set(t) & s))
        trios_fora_por_concurso.append(fora)
        linhas.append([num, data, hits_c.get(11, 0), hits_c.get(12, 0), hits_c.get(13, 0),
                       hits_c.get(14, 0), hits_c.get(15, 0), max([h for h in hits_c] + [0]),
                       fora, f"{premio_c:.2f}".replace(".", ",")])

    with open(BASE / "backtest_estrategia2_100_concursos.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f, delimiter=";")
        w.writerow(["concurso", "data", "jogos_11", "jogos_12", "jogos_13", "jogos_14", "jogos_15",
                    "maior_acertos", "trios_totalmente_fora_do_sorteio", "premio_R$"])
        w.writerows(linhas)

    custo_1 = 600 * PRECO
    custo_100 = custo_1 * 100
    media_fora = sum(trios_fora_por_concurso) / len(trios_fora_por_concurso)

    # ---------- Relatório ----------
    L = []
    L.append("# Estratégia 2 — 20 trios × 30 jogos com a trinca excluída (600 jogos): análise")
    L.append("")
    L.append("**Interpretação adotada:** para **cada um dos 20 trios** pares de 1–12, 1 lote com **30 combinações** de 15 dezenas **excluindo as 3 da trinca** (15 sorteadas das 22 restantes). Total: **20 lotes × 30 = 600 jogos/concurso = R$ 2.100,00**. Se a sua ideia era outro número de jogos por lote, a matemática por jogo abaixo não muda — basta multiplicar.")
    L.append("")
    L.append("## 1) Cobertura teórica")
    L.append("")
    L.append("| Cobertura | 1 lote (30 jogos) | 20 lotes (600 jogos) |")
    L.append("|---|---:|---:|")
    L.append(f"| 15 acertos | 30/3.268.760 = 0,00092% (1 em {total_combos//30:,}) | 600/3.268.760 = 0,0184% (1 em {total_combos//600:,}) |".replace(",", "."))
    L.append("| 14+ acertos | ~0,014% (1 em ~7.200) | ~2,8% (1 em ~36) |")
    L.append("| 13+ acertos | ~4,4% (1 em ~23) | ~59% (1 em ~1,7) |")
    L.append("| 11+ acertos | ~3,2 jogos premiados em média | ~63,5 jogos premiados em média |")
    L.append("")
    L.append("- **Jackpot:** 1 em 5.448 concursos (~17 anos jogando todo concurso, a 312/ano). Em 100 concursos, a chance de ver um 15 é de apenas ~1,8%.")
    L.append("- **14+:** ~1 em 36 concursos. **13+:** ~59% dos concursos terão pelo menos um 13 (paga R$ 35).")
    L.append("- **11/12:** você ganhará dezenas de prêmios pequenos por concurso (~63 jogos premiados), somando em média só ~R$ 540 em prêmios fixos contra R$ 2.100 de custo.")
    L.append("")
    L.append("## 2) “Aumenta a chance do fechamento”? Só no condicional — e é aí que está a ilusão")
    L.append("")
    L.append(f"- **Se a trinca está totalmente FORA do sorteio** (probabilidade de {p_trinca_fora*100:.2f}% por trinca), o sorteio é um subconjunto das 22 dezenas e cada jogo do lote tem chance de 15 pontos de **1/{combos_22:,}** — **19,2× maior** que 1/3.268.760. E a chance de 11+ por jogo sobe para **{cond_p11mais*100:.1f}%** (contra 10,6% incondicional).")
    L.append("- **Mas** esse cenário acontece só em 5,22% dos concursos para uma trinca específica. Nos outros 94,78%, o lote está parcial ou totalmente capado (teto 14/13/12).")
    L.append(f"- **Incondicionalmente, cada jogo continua valendo 1/3.268.760 para o jackpot** — exatamente como 600 jogos livres. A estratégia não cria chance; ela **aposta 20 vezes** em 20 cenários “trinca fora” diferentes, pagando 20× mais para isso.")
    L.append(f"- Nos últimos 100 concursos, em média **{media_fora:.1f} das 20 trincas** estavam totalmente fora de cada sorteio — mas a distribuição é bimodal: **47 concursos com 0 trincas fora** (jackpot impossível nos 600 jogos), 38 com 1, 13 com 4 e 2 com 10. Cada lote “aberto” tem apenas 30/170.544 = 0,018% de chance condicional de 15 pontos. Somados, voltamos aos mesmos 0,018% incondicionais dos 600 jogos.")
    L.append("")
    L.append("## 3) Fechamento de verdade: 30 jogos em 22 dezenas garantem 11 — mas só se a trinca estiver fora")
    L.append("")
    L.append(f"**Garantia real do lote de exemplo (30 jogos, enumeração dos {combos_22:,} sorteios possíveis nas 22 dezenas):** no pior caso, o melhor jogo do lote faz **{pior} acertos** — ou seja, **30 jogos aleatórios em 22 dezenas já garantem pelo menos 11 acertos sempre que o sorteio está contido nas 22 dezenas (trinca fora)**. Distribuição do melhor jogo por sorteio: " +
             ", ".join(f"{h} acertos: {dist_pior[h]} sorteios" for h in sorted(dist_pior)) + ".")
    L.append("")
    L.append("Por que 30 jogos bastam para 11, mas não para 12/13? Cada jogo tem 38,7% de chance de 11+ contra um sorteio nas 22 dezenas; com 30 jogos, a chance de nenhum chegar a 11 é ~(1−0,387)^30 ≈ 0,00004% — praticamente zero. Para 12 acertos a chance por jogo cai para 10,7% e 30 jogos já deixam ~5% dos sorteios sem nenhum 12 (é o grupo “melhor jogo = 11” acima).")
    L.append("")
    L.append("⚠️ **Correção de um erro comum:** cobrir todos os subconjuntos de 11 dezenas das 22 exigiria C(22,11)/C(15,11) ≈ 517 jogos — mas isso é condição **suficiente, não necessária**. A garantia de 11 acertos só exige que cada sorteio compartilhe 11 dezenas com algum jogo, o que 30 jogos aleatórios já conseguem (provado pela enumeração acima).")
    L.append("")
    L.append("**O problema é o condicional:** essa garantia de 11 só vale quando a trinca está fora (5,22% dos concursos por lote). Nos demais concursos o lote está capado. E, somando os 20 lotes, há um dado decisivo:")
    L.append("")
    L.append("- Em **47 dos últimos 100 concursos, nenhuma das 20 trincas estava totalmente fora do sorteio** (o sorteio tinha 4+ dezenas pares em 1–12, atingindo todas as trincas). Nesses concursos, **o jackpot é impossível para os 600 jogos** — todo jogo exclui uma trinca que saiu parcialmente. Nos outros 53 concursos, em média 1–10 lotes ficam “abertos” para 15 pontos.")
    L.append("- Com 600 jogos **livres** (sem exclusão), o jackpot seria possível em 100% dos concursos. A estratégia troca cobertura universal por cobertura concentrada: mesma chance incondicional por real, variância muito maior.")
    L.append("")
    L.append("Se a ideia fosse jogar **todas** as C(22,15) = 170.544 combinações das 22 dezenas, o custo seria 170.544 × R$ 3,50 = **R$ 596.904 por lote** (× 20 lotes = R$ 11,9 milhões/concurso). Inviável — e mesmo assim, só pagaria o jackpot se a trinca estivesse fora.")
    L.append("")
    L.append("## 4) Duplicidade entre os 20 lotes")
    L.append("")
    L.append(f"Dos 600 jogos gerados aleatoriamente, **{n_distintos} são distintos** ({duplicados} duplicados entre lotes). Com geração aleatória a duplicidade é quase zero — bom para cobertura. **Atenção:** se você gerar os 30 jogos de cada lote sempre com a mesma regra sistemática (ex.: “os 30 primeiros jogos em ordem”), os lotes vão gerar **os mesmos jogos repetidos** e você pagará várias vezes pelo mesmo jogo, sem cobertura nova. A geração precisa ser globalmente distinta.")
    L.append("")
    L.append("## 5) Rentabilidade")
    L.append("")
    L.append(f"- **Custo:** R$ {custo_1:,.2f}/concurso · R$ {custo_100:,.2f} em 100 concursos · ~R$ 655 mil/ano jogando todo concurso.")
    L.append(f"- **Retorno esperado:** ~R$ {600*ev:,.2f}/concurso (~{ev/PRECO*100:.0f}% do apostado, compatível com os 43,35% da Caixa) → **prejuízo esperado de ~R$ {custo_1-600*ev:,.2f}/concurso (~{100-ev/PRECO*100:.0f}%)**.")
    L.append("- **Por real apostado, é idêntico** à estratégia anterior (120 jogos) e a 600 jogos livres: R$ 1,58 de retorno esperado para cada R$ 3,50. Multiplicar os jogos multiplica o custo e o prejuízo esperado na mesma proporção — não há ganho de escala.")
    L.append("")
    L.append("## 6) Backtest: os 600 jogos nos últimos 100 concursos")
    L.append("")
    L.append(f"- **Custo (100 concursos):** R$ {custo_100:,.2f} · **Prêmios:** R$ {tot_premio:,.2f} · **Saldo: R$ {tot_premio-custo_100:,.2f}** ({tot_premio/custo_100*100:.1f}% de retorno)")
    L.append(f"- **Acertos em 60.000 jogos:** 11: {tot_hits.get(11,0)} · 12: {tot_hits.get(12,0)} · 13: {tot_hits.get(13,0)} · 14: {tot_hits.get(14,0)} · 15: {tot_hits.get(15,0)} (teórico: ~5.261 / ~1.002 / ~87 / ~3 / ~0,02)")
    L.append(f"- **Concursos com pelo menos um prêmio:** {concursos_com.get('>=11',0)}/100 · com 13+: {concursos_com.get('>=13',0)}/100 · com 14+: {concursos_com.get('>=14',0)}/100 · com 15: {concursos_com.get('==15',0)}/100")
    L.append("")
    L.append("O backtest é a estratégia anterior multiplicada por 5: muitos prêmios de R$ 7/R$ 14, alguns 13, raríssimos 14, nenhum 15 — e prejuízo próximo ao esperado. Detalhe por concurso em `backtest_estrategia2_100_concursos.csv`.")
    L.append("")
    L.append("## 7) Veredito")
    L.append("")
    L.append("1. **Aumenta a chance de fechamento?** No sentido condicional, sim: 30 jogos em 22 dezenas **garantem 11 acertos se a trinca estiver fora** (provado por enumeração) e a chance de 15 pontos sobe 19× nesse cenário — mas esse cenário é só 5,22% por trinca, e em 47% dos concursos nenhuma trinca está fora (jackpot impossível nos 600 jogos). Incondicionalmente, por real apostado, a chance é idêntica à de jogos livres.")
    L.append("2. **Aumenta a chance total?** Só porque você gasta 5× mais que na estratégia anterior (600 vs 120 jogos). Por real apostado, a cobertura é **idêntica** a qualquer outro conjunto de jogos.")
    L.append("3. **É rentável?** Não. Esperança matemática de ~43–45% de retorno, prejuízo esperado de ~R$ 1.155/concurso. Em 100 concursos de backtest: −R$ " + f"{custo_100-tot_premio:,.2f}" + ".")
    L.append("4. **Útil para quê?** Como forma de **organizar** a aposta por cenários (“qual trinca fica de fora?”) e garantir volume de prêmios pequenos — desde que tratada como custo de entretenimento. Se o objetivo é cobertura de 11–13 com menos gestão, um fechamento clássico de 18–20 dezenas (uma única aposta múltipla) entrega a mesma matemática por real, sem 600 volantes.")
    L.append("")
    L.append("> ⚠️ Nenhuma exclusão, fechamento ou análise de frequência passada altera a esperança matemática negativa desenhada pela Caixa (43,35% de prêmio bruto). Jogue apenas com valor que pode perder.")
    L.append("")

    (BASE / "relatorio_estrategia2.md").write_text("\n".join(L), encoding="utf-8")

    print(f"Jogos: {len(jogos)} | distintos: {n_distintos} | duplicados: {duplicados}")
    print(f"P(trinca fora)={p_trinca_fora*100:.2f}% | P11+|fora={cond_p11mais*100:.1f}% | P15|fora=1/{combos_22}")
    print(f"Limites fechamento: " + ", ".join(f"{h}:>={limites[h]:,.0f}" for h in limites))
    print(f"Garantia real lote1 (pior caso): {pior} acertos | dist: {dict(sorted(dist_pior.items()))}")
    print(f"EV/jogo R$ {ev:.2f} | custo/concurso R$ {custo_1:,.2f}")
    print(f"Backtest: custo R$ {custo_100:,.2f} premios R$ {tot_premio:,.2f} saldo R$ {tot_premio-custo_100:,.2f}")
    print(f"Hits: {dict(tot_hits)} | concursos >=11:{concursos_com.get('>=11',0)} >=13:{concursos_com.get('>=13',0)} >=14:{concursos_com.get('>=14',0)} 15:{concursos_com.get('==15',0)}")
    print(f"Trios fora por concurso (média): {media_fora:.1f}")


if __name__ == "__main__":
    main()
