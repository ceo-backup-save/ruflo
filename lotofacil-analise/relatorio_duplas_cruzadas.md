# Duplas cruzadas pares 1–12: fixa + excluída simultâneas e combinações de 20 dezenas

**Interpretação adotada (explícita):** duplas cruzadas = 1 par baixa (02,04,06) + 1 par alta (08,10,12) → **9 duplas**. “Simultaneamente” = **o mesmo jogo/aposta** contém a dupla fixa **e** não contém nenhuma dezena da dupla excluída (logo as duas duplas precisam ser **disjuntas**). “Combinações de 20 dezenas” = apostas que marcam **20 números** (= 15.504 jogos simples, R$ 54.264,00). Apresento também a versão equivalente em jogos simples de 15, para comparar custo.

## 1) As 9 duplas cruzadas e sua presença nos últimos 100 concursos (esperado 35 em 100)

| # | Dupla cruzada | Ocorrências | % | Último | Atraso |
|---:|---|---:|---:|---:|---:|
| 1 | 06 12 | 43 | 43% | 3822 | 3 |
| 2 | 04 08 | 37 | 37% | 3825 | 0 |
| 3 | 06 08 | 37 | 37% | 3825 | 0 |
| 4 | 04 12 | 35 | 35% | 3818 | 7 |
| 5 | 02 12 | 32 | 32% | 3824 | 1 |
| 6 | 06 10 | 32 | 32% | 3825 | 0 |
| 7 | 02 08 | 28 | 28% | 3817 | 8 |
| 8 | 02 10 | 28 | 28% | 3822 | 3 |
| 9 | 04 10 | 28 | 28% | 3825 | 0 |

**Exemplo concreto usado abaixo:** dupla **FIXA = 06 12** (a mais frequente) e dupla **EXCLUÍDA = 04 10** (a menos frequente disjunta dela). Restam **21 dezenas** livres (25 − 2 fixas − 2 excluídas).

## 2) Simultâneo fixa + excluída: o que acontece com o teto de acertos

Sejam a = quantas da fixa saíram (0,1,2) e b = quantas da excluída saíram (0,1,2). Para um jogo simples de 15 com as duas restrições:

| a (fixa no sorteio) | b (excluída no sorteio) | Teto do jogo |
|---:|---:|---:|
| 2 | 0 | **15 acertos** (único cenário de jackpot) |
| 2 | 1 | 14 acertos |
| 1 | 0 | 14 acertos |
| 2 | 2 | 13 acertos |
| 1 | 1 | 13 acertos |
| 0 | 0 | 13 acertos |
| 0 | 2 | 11 acertos |

**Jackpot só é possível se a=2 e b=0**, cuja probabilidade é C(21,13)/C(25,15) = **6.23%** por jogo — mas, incondicionalmente, cada jogo continua valendo 1/3.268.760 para 15 pontos (a chance condicional maior é compensada pela raridade do cenário).

**Pares (fixa, excluída) disjuntos possíveis:** 36 pares ordenados (ver `pares_fixa_excluida_disjuntos.csv`). Pares que compartilham uma dezena são **impossíveis** (0 jogos) — ex.: fixa 06-12 e excluída 06-08 exigem que o 06 esteja e não esteja ao mesmo tempo.

## 3) Combinações de 20 dezenas: cobertura e custo

- Uma aposta de 20 dezenas cobre **15,504 jogos simples** e custa **R$ 54,264.00**.
- Com fixa+excluída, há **C(21,18) = 1,330 apostas de 20** possíveis por par (de C(25,20) = 53,130 no total).
- Probabilidades de uma aposta de 20 (sem restrição), pelo nº de dezenas do sorteio dentro da aposta (overlap t):

| Overlap t | Probabilidade | Leitura |
|---:|---:|---|
| 15 | 0.47% | jackpot da aposta (sorteio ⊆ aposta) |
| 14 | 5.93% |  |
| 13 | 23.72% |  |
| 12 | 38.54% |  |
| 11 | 25.69% |  |
| 10 | 5.65% |  |

- **Retorno esperado de 1 aposta de 20:** 15,504 × R$ 1.58 = **~R$ 24,480.59** contra R$ 54,264.00 de custo → **~45% de retorno, prejuízo esperado ~R$ 29,783.41 por aposta** — exatamente a mesma taxa dos jogos simples.
- **Exemplo gerado:** 5 apostas de 20 com fixa 06 12 e excluída 04 10 custariam **5 × R$ 54,264.00 = R$ 271,320.00 por concurso**. Os jogos estão em `combinacoes_20_dezenas_exemplo.csv` (junto com 20 jogos simples equivalentes, R$ 70,00).

## 4) Backtest nos últimos 100 concursos

**Versão simples (20 jogos de 15, fixa+excluída):** custo R$ 7,000.00 em 100 concursos · prêmios R$ 1,988.00 · saldo **R$ -5,012.00** (28.4% de retorno). Acertos: 11×195, 12×42, 13×1, 14×0, 15×0. Concursos com 13+: 1/100 · com 14+: 0/100 · com 15: 0/100.

**Versão 20 dezenas (1 aposta de 20, fixa+excluída, a 1ª gerada):** custo R$ 5,426,400.00 em 100 concursos · prêmios (contando todos os jogos simples dentro da aposta, com 14=R$ 1.500 e 15=R$ 2.000.000 ilustrativos e sem rateio) R$ 3,825,674.00 · saldo **R$ -1,600,726.00** (70.5% de retorno). Overlaps observados: t=10: 4 concursos, t=11: 30 concursos, t=12: 36 concursos, t=13: 19 concursos, t=14: 10 concursos, t=15: 1 concursos.

⚠️ **Por que o retorno de 70,5% no backtest de 20 dezenas é enganoso:** ele é dominado por **1 único concurso com overlap t=15** (sorteio contido na aposta de 20), que sozinho paga ~R$ 2,26 milhões em prêmios ilustrativos (1 jogo de 15 + 75 de 14 + 1.050 de 13 + … dentro da aposta). Sem esse concurso, o retorno cai para ~29%. Na prática, o prêmio de 15 acertos é **rateado** entre todos os ganhadores do país, então o valor real seria bem menor. O backtest de 20 dezenas tem variância gigantesca — a expectativa de longo prazo continua ~45%.

## 5) Expectativa de retorno (resumo)

| Estratégia | Custo/concurso | Retorno esperado/concurso | Prejuízo esperado |
|---|---:|---:|---:|
| 20 jogos simples (fixa+excluída) | R$ 70,00 | ~R$ 31.58 | ~R$ 38.42 |
| 1 aposta de 20 dezenas (fixa+excluída) | R$ 54,264.00 | ~R$ 24,480.59 | ~R$ 29,783.41 |
| 5 apostas de 20 dezenas | R$ 271,320.00 | ~R$ 122,402.96 | ~R$ 148,917.04 |

**Conclusão:** as duplas cruzadas organizam bem a aposta (baixa+alta), e o simultâneo fixa+excluída é uma aposta de cenário (“esta dupla sai e aquela não sai”). Mas **não muda a expectativa de retorno**: ~43–45% do apostado em qualquer formato. A aposta de 20 dezenas só multiplica custo e prêmio esperado na mesma proporção — e, com fixa+excluída ao mesmo tempo, o jackpot fica restrito ao cenário a=2,b=0 (6,22% dos concursos).

> ⚠️ Nenhuma dupla, fechamento ou frequência passada altera a esperança matemática negativa desenhada pela Caixa (43,35% de prêmio bruto). Aposta de 20 dezenas custa R$ 54 mil por concurso — trate como custo de entretenimento, nunca como investimento.

## Arquivos

- `duplas_cruzadas_pares_1a12.csv` — 9 duplas com frequência nos 100 concursos.
- `pares_fixa_excluida_disjuntos.csv` — 36 pares (fixa,excluída) possíveis.
- `combinacoes_20_dezenas_exemplo.csv` — 20 jogos simples + 5 apostas de 20 gerados.
- `backtest_duplas_cruzadas.csv` — backtest dos 20 jogos simples por concurso.
- `relatorio_duplas_cruzadas.html` — versão visual.
- `analise_duplas_cruzadas.py` — script reproduzível.
