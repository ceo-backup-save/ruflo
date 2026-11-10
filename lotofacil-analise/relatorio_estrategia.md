# Estratégia “excluir trinca × fixar trinca” (3 repetições) — análise de viabilidade e rentabilidade

**Referência:** 10/11/2026 · **Base de backtest:** concursos 3726–3825 (100 concursos) · **Preço do jogo simples:** R$ 3,50 · **Prêmio bruto da Lotofácil:** 43,35% da arrecadação (11 acertos = R$ 7,00; 12 = R$ 14,00; 13 = R$ 35,00; 14 e 15 variáveis/rateados).

## 1) A estratégia, do jeito que foi testada

Repetição = 1 trinca + 2 lotes de 20 jogos. Repetida 3 vezes com 3 trincas diferentes = **6 lotes × 20 = 120 jogos/concurso (R$ 420,00)**.

| Repetição | Trinca (pares 1–12) | Lote 1 — EXCLUÍDAS | Lote 2 — FIXAS |
|---|---|---|---|
| 1 (A) | 06 08 12 (24% nos últimos 100) | 20 jogos de 15 em 22 dezenas (sem 06,08,12) | 20 jogos: 06,08,12 + 12 em 22 |
| 2 (B) | 04 08 12 (23%) | 20 jogos sem 04,08,12 | 20 jogos: 04,08,12 + 12 em 22 |
| 3 (C) | 02 06 12 (22%) | 20 jogos sem 02,06,12 | 20 jogos: 02,06,12 + 12 em 22 |

Os 120 jogos concretos estão em `lotes_estrategia_3_repeticoes.csv` (gerados com semente fixa, todos distintos).

⚠️ **Problema de diversificação já aqui:** as 3 trincas mais frequentes **compartilham a dezena 12** (e A/B compartilham 08; A/C compartilham 06). Se o 12 não sair (36% dos últimos 100 concursos), os 3 lotes de FIXAS ficam todos limitados a no máximo 14 acertos ao mesmo tempo. Trincas disjuntas (ex.: 02-04-06 e 08-10-12) diversificariam melhor — mas, como veremos, isso não muda o valor esperado.

## 2) O ponto matemático central: excluir/fixar NÃO muda a chance de cada jogo

Na Lotofácil há **C(25,15) = 3.268.760** combinações de 15 dezenas, todas igualmente prováveis a cada sorteio. Qualquer jogo simples — com ou sem trinca fixa/excluída — tem exatamente as mesmas probabilidades:

| Acertos | Combinações vencedoras | Probabilidade por jogo |
|---:|---:|---:|
| 11 | 286650 | 8,7694% (1 em 11) |
| 12 | 54600 | 1,6704% (1 em 60) |
| 13 | 4725 | 0,1446% (1 em 692) |
| 14 | 150 | 0,0046% (1 em 21,792) |
| 15 | 1 | 0,0000% (1 em 3,268,760) |

**Prova pela simetria (linearidade da expectativa):** o retorno esperado de N jogos distintos é sempre N × retorno esperado de 1 jogo, **independentemente de quais números foram escolhidos**. Excluir ou fixar uma trinca apenas **redistribui** a cobertura entre cenários — não cria cobertura nova.

### O que a estratégia realmente faz: troca de cenário, não de chance

Seja k = quantas das 3 dezenas da trinca saíram no sorteio. Então:

| k (da trinca no sorteio) | Lote EXCLUÍDAS: máximo possível | Lote FIXAS: máximo possível |
|---:|---:|---:|
| 3 (trinca completa saiu) | 12 acertos | **15 acertos** |
| 2 | 13 acertos | 14 acertos |
| 1 | 14 acertos | 13 acertos |
| 0 (nenhuma saiu) | **15 acertos** | 12 acertos |

Nos últimos 100 concursos, para a trinca 06-08-12: k=3 em **24 concursos**, k=2 em **47**, k=1 em **23**, k=0 em **6**. Ou seja, em **70% dos concursos (k=1 ou 2, cenário parcial) nenhum dos dois lotes pode fazer 15 pontos** — o teto é 14. O prêmio máximo só fica “aberto” em k=0 ou k=3. A chance incondicional de 15 pontos continua a mesma (ver §3), mas fica **concentrada** em poucos concursos: variância maior, não chance maior.

## 3) Previsão média de cobertura (teoria, por concurso)

| Cobertura | 1 lote (20 jogos) | 1 repetição (40 jogos) | 3 repetições (120 jogos) |
|---|---:|---:|---:|
| 15 acertos (jackpot) | 20/3.268.760 = 0,00061% — 1 em 163.438 concursos | 0,00122% — 1 em 81.719 | **0,00367% — 1 em 27.240** |
| 14+ acertos | ~0,0092% — 1 em ~10.900 | ~0,18% — 1 em ~540 | **~0,55% — 1 em ~180** |
| 13+ acertos | ~1,5% — 1 em ~67 | ~5,8% — 1 em ~17 | **~17% — 1 em ~6** |
| 11+ acertos (qualquer prêmio) | ~2,1 jogos premiados em média | ~4,2 jogos premiados em média | **~12,7 jogos premiados em média** |

Leitura prática dos 120 jogos:

- **Jackpot (15):** 1 chance em 27.240 concursos. A ~312 concursos/ano, isso é **1 vez a cada ~87 anos** de jogo contínuo nesse volume. Mesmo jogando 120 jogos **todo concurso por 100 concursos**, a chance de ver um 15 é de apenas ~0,37%.
- **14 acertos:** ~1 em 180 concursos (~1 vez a cada 7 meses jogando todo concurso).
- **13 acertos:** ~1 em 6 concursos — é a faixa “visível” da estratégia, mas paga só R$ 35.
- **11/12 acertos:** você **vai** ganhar quase todo concurso (média de ~12,7 jogos premiados), mas R$ 7/R$ 14 por jogo não chegam perto do custo de R$ 420.

## 4) Rentabilidade: quanto custa, quanto volta, quanto se perde em média

- **Custo:** 120 × R$ 3,50 = **R$ 420.00 por concurso** (R$ 42,000.00 em 100 concursos; ~R$ 131 mil/ano jogando todo concurso).
- **Retorno esperado por jogo:** R$ 0.90 em prêmios fixos (11/12/13) + ~R$ 0.68 em 14/15 (usando 14=R$ 1.500 e 15=R$ 2.000.000 ilustrativos) = **~R$ 1.58 por jogo**, ou seja, **~45% do preço** — compatível com os 43,35% de prêmio bruto da Caixa.
- **Retorno esperado dos 120 jogos:** ~R$ 189.48/concurso contra R$ 420.00 de custo → **prejuízo esperado de ~R$ 230.52 por concurso (~55% do valor apostado)**.
- **Ponto de equilíbrio do jackpot:** para 1 jogo valer R$ 3,50 em expectativa, o prêmio de 15 acertos teria de ser da ordem de **R$ 8 milhões por ganhador** (sem dividir). E, no longo prazo, a regra dos 43,35% impede lucro sistemático: o que acumula num concurso é retirado dos concursos seguintes.

**Conclusão sobre rentabilidade:** não existe escolha de trincas — mais quente, mais fria, excluída ou fixa — que torne a estratégia rentável em expectativa. A estratégia é, matematicamente, equivalente a jogar 120 jogos simples quaisquer. O que muda é apenas **onde** a cobertura fica concentrada (cenários k=0/k=3) e a **variância** (mais “tudo ou nada” no jackpot).

## 5) Backtest: os mesmos 120 jogos nos últimos 100 concursos (3726–3825)

Simulação literal: jogar os 120 jogos de `lotes_estrategia_3_repeticoes.csv` em cada um dos 100 concursos passados. Detalhe por concurso em `backtest_estrategia_100_concursos.csv`.

- **Custo total (100 concursos):** R$ 42,000.00
- **Prêmios totais obtidos:** R$ 12,476.00 (com 14=R$ 1.500 ilustrativo; no período houve 1 jogo(s) de 14 acertos e 0 de 15)
- **Saldo:** R$ -29,524.00 (29.7% de retorno sobre o apostado)
- **Jogos premiados:** 11 acertos: 1071 · 12: 206 · 13: 17 · 14: 1 · 15: 0 (total 1295 em 12.000 jogos = 10.79%, contra 10,59% teóricos)
- **Concursos com pelo menos um prêmio:** 100/100 · com 13+: 16/100 · com 14+: 1/100 · com 15: 0/100
- **Por tipo de lote (60 jogos cada tipo em 100 concursos):** EXCLUÍDAS premiaram 619 jogos (R$ 5,208.00); FIXAS premiaram 676 jogos (R$ 7,268.00) — diferença dentro do ruído, como a teoria prevê.

O backtest confirma a teoria: muitos prêmios pequenos (11/12), poucos 13, nenhum 14/15 em 100 concursos — e prejuízo grande, próximo ao esperado (~55% do apostado). **Atenção:** backtest em 100 concursos não prova nada sobre o futuro; serve só para mostrar que a estratégia se comporta como 120 jogos comuns.

## 6) Veredito

1. **Viável como organização de apostas?** Sim — é uma forma válida de dividir o orçamento entre dois cenários (“a trinca sai” × “a trinca não sai”) e de garantir cobertura de 11–13 acertos em praticamente todo concurso. Se o objetivo é entretenimento com controle de custo, funciona como qualquer outro conjunto de 120 jogos.
2. **Viável como estratégia lucrativa / com chance de ser rentável?** **Não.** Por simetria, nenhuma seleção de dezenas altera o valor esperado: ~43–45% de retorno sobre o apostado no longo prazo. A prevalência passada da trinca (06-08-12 em 24% dos últimos 100) **não** aumenta sua chance no próximo sorteio — continua 19,8% teórica, e escolher a trinca “quente” ou a “fria” é indiferente.
3. **Previsão média de cobertura (120 jogos/concurso):** 15 acertos 1 em 27.240 concursos; 14+ 1 em ~180; 13+ 1 em ~6; 11+ em média ~12,7 jogos premiados por concurso — com custo de R$ 420/concurso e prejuízo esperado de ~R$ 230/concurso.
4. **Se quiser manter a ideia, melhore a diversificação:** use trincas **disjuntas** (ex.: 02-04-06 e 08-10-12) em vez das 3 mais frequentes (que compartilham o 12), e trate o gasto como custo de entretenimento — nunca como investimento. Uma aposta de 16–20 dezenas (fechamento) tem a mesma matemática por real apostado, com menos trabalho de gestão.

> ⚠️ Loteria é um jogo de azar com esperança matemática negativa por desenho (a Caixa retém ~56,65% da arrecadação para prêmios não pagos, operação e destinações sociais). Nenhuma análise de frequência passada muda isso. Jogue apenas com valor que você pode perder.
