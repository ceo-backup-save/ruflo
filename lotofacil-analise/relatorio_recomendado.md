# O Conjunto Recomendado — paridade 7/8 + faixa natural 9–10

*Explicação didática completa do conjunto “Recomendado: paridade 7/8 + faixa natural 9–10”, com os 20 jogos, os porquês, os números e o que esperar de retorno.*

---

## 1. O que é o “Recomendado” em uma frase

É o conjunto de **20 jogos de 15 dezenas** que: (a) contém sempre a **dupla fixa 06-12**; (b) nunca contém a **dupla excluída 04-10**; (c) têm **7 pares ou 8 pares** (e portanto 8 ou 7 ímpares); (d) têm **9 ou 10 dezenas entre 1 e 16** (e 6 ou 5 entre 17 e 25); (e) completam as 13 dezenas restantes com as **mais frequentes** dos últimos 100 concursos.

É a versão “arrumada” da sua técnica: mantém o que é real (paridade) e abandona o que é artificial (faixa 7/8), trocando por uma faixa que a Lotofácil **realmente** sorteia.

## 2. Por que “paridade 7/8” entrou e “faixa 7/8” saiu

A Lotofácil tem **25 dezenas: 13 ímpares e 12 pares**. Você sorteia 15. O valor esperado de pares é 15 × 12/25 = **7,2**.

| Faixa | Esperado (teoria) | Observado em 100 concursos | Veredito |
|---|---|---|---|
| **7 ou 8 pares** | 7,2 pares | **56 concursos** | ✅ é o padrão real |
| 7 ou 8 dezenas em 1–16 | 9,6 dezenas | 16 concursos | ⚠️ atípico |
| **9 ou 10 dezenas em 1–16** | 9,6 dezenas | **54 concursos** | ✅ é o padrão real |

**Explicação da faixa:** há 16 dezenas de 01 a 16 e apenas 9 de 17 a 25. Num sorteio de 15, o esperado é 15 × 16/25 = **9,6** na primeira metade e **5,4** na segunda. Pedir 7 ou 8 em 1–16 (e portanto 8 ou 7 em 17–25) é pedir o **contrário** do que a estrutura do jogo produz — só aconteceu em 16% dos concursos. Já 9 ou 10 em 1–16 aconteceu em **54%**.

**Distribuição completa observada (100 concursos):**

| Pares no sorteio | Concursos |
|---:|---:|
| 5 | 11 |
| 6 | 25 |
| 7 | 33 |
| 8 | 23 |
| 9 | 6 |
| 10 | 2 |

| Dezenas 1–16 | Concursos |
|---:|---:|
| 7 | 5 |
| 8 | 11 |
| 9 | 29 |
| 10 | 25 |
| 11 | 25 |
| 12 | 4 |
| 13 | 1 |

## 3. A parte que quase ninguém diz: isso NÃO aumenta a chance

Um jogo de 15 dezenas tem **sempre** a mesma distribuição de acertos, seja qual for a combinação:

| Acertos | Probabilidade por jogo | 1 em… |
|---|---:|---:|
| 11 | 8.7694% | 11,4 |
| 12 | 1.6704% | 59,9 |
| 13 | 0.1446% | 691,5 |
| 14 | 0.0046% | 21.791,7 |
| 15 | 0.000031% | 3.268.760 |

Isso vale para o jogo equilibrado, para o desequilibrado, para o com dezenas quentes e para o aleatório. **É simetria:** qualquer conjunto de 15 tem o mesmo número de sorteios favoráveis. O que o equilíbrio faz é **concentrar** a aposta num tipo de sorteio (os equilibrados) e reduzir a exposição nos outros. Como o prêmio não muda conforme o tipo de sorteio, a conta final é a mesma.

Em 200.000 sorteios simulados, o jogo com paridade 7/8 + faixa 7/8 acertou 11 em 8,862% das vezes, e o jogo livre em 8,857% — **a mesma coisa**.

## 4. Como as 13 dezenas restantes são escolhidas (prevalência)

Com a fixa (06, 12) dentro e a excluída (04, 10) fora, sobram 21 dezenas. As 13 são sorteadas com **peso proporcional à frequência nos últimos 100 concursos**, e o sorteio é repetido (com rejeição) até o jogo cumprir a paridade 7/8 e a faixa 9/10.

**Ranking de frequência das 21 dezenas disponíveis (100 concursos; esperado 60 cada):**

| # | Dezena | Frequência |
|---:|---:|---:|
| 1 | 05 | 67 |
| 2 | 03 | 66 |
| 3 | 11 | 66 |
| 4 | 15 | 64 |
| 5 | 23 | 64 |
| 6 | 24 | 64 |
| 7 | 13 | 63 |
| 8 | 19 | 63 |
| 9 | 08 | 62 |
| 10 | 16 | 62 |
| 11 | 25 | 62 |
| 12 | 14 | 60 |
| … | … | … |
| 18 | 20 | 54 |
| 19 | 22 | 54 |
| 20 | 02 | 51 |
| 21 | 18 | 51 |

⚠️ **Aviso honesto:** essa prevalência é **passado, não previsão**. A dezena 05 saiu em 67 dos 100 concursos, mas no próximo concurso cada dezena tem 60% de chance — igualzinho. Usar frequência para escolher é uma forma de **organizar** o jogo; não é uma vantagem matemática. Como a prevalência foi medida nos mesmos 100 concursos usados no backtest, os resultados do backtest ficam **otimistas** (viés de sobreajuste).

## 5. Os 20 jogos do conjunto recomendado

Todos: contêm 06 e 12 · não contêm 04 nem 10 · 7 ou 8 pares · 9 ou 10 dezenas em 1–16.

| # | Jogo | Pares/Ímpares | 1–16 / 17–25 |
|---:|---|---|---|
| 1 | 01 02 03 06 07 08 09 12 14 15 21 22 23 24 25 | 7/8 | 10/5 |
| 2 | 01 02 03 06 07 08 12 13 14 16 17 18 22 23 25 | 8/7 | 10/5 |
| 3 | 01 02 03 06 08 09 11 12 13 16 19 20 23 24 25 | 7/8 | 10/5 |
| 4 | 01 02 05 06 08 11 12 13 16 17 18 19 20 22 23 | 8/7 | 9/6 |
| 5 | 01 02 05 06 09 11 12 13 14 17 18 19 20 22 25 | 7/8 | 9/6 |
| 6 | 01 02 05 06 09 12 13 14 15 16 17 21 22 23 24 | 7/8 | 10/5 |
| 7 | 01 02 06 07 08 11 12 13 14 18 19 20 23 24 25 | 8/7 | 9/6 |
| 8 | 01 02 06 07 09 11 12 13 15 18 20 21 22 24 25 | 7/8 | 9/6 |
| 9 | 01 02 06 07 12 13 14 15 16 17 18 19 22 23 24 | 8/7 | 9/6 |
| 10 | 01 03 05 06 07 08 12 13 15 17 18 20 22 23 24 | 7/8 | 9/6 |
| 11 | 01 03 05 06 07 08 12 14 15 16 18 19 20 21 23 | 7/8 | 10/5 |
| 12 | 01 03 05 06 08 11 12 14 15 16 17 18 20 22 25 | 8/7 | 10/5 |
| 13 | 01 03 05 06 08 11 12 15 16 19 20 22 23 24 25 | 7/8 | 9/6 |
| 14 | 01 05 06 07 08 09 12 15 16 18 19 20 21 22 24 | 8/7 | 9/6 |
| 15 | 02 03 05 06 07 08 09 11 12 17 18 20 21 23 24 | 7/8 | 9/6 |
| 16 | 02 03 05 06 07 08 12 15 16 18 19 20 21 22 23 | 8/7 | 9/6 |
| 17 | 02 03 05 06 08 11 12 13 15 16 17 21 22 23 24 | 7/8 | 10/5 |
| 18 | 02 03 06 07 09 12 14 15 16 17 18 19 21 22 25 | 7/8 | 9/6 |
| 19 | 03 05 06 07 08 11 12 13 14 16 18 19 21 22 23 | 7/8 | 10/5 |
| 20 | 03 05 06 08 11 12 13 15 16 17 18 20 23 24 25 | 7/8 | 9/6 |

**Custo:** 20 × R$ 3,50 = **R$ 70,00 por concurso** (R$ 210,00 por semana com 3 sorteios).

## 6. Expectativa de retorno — com números, sem ilusão

A Caixa devolve **43,35%** da arrecadação em prêmios. Por isso, todo jogo da Lotofácil tem, em média, retorno negativo. Para o nosso conjunto:

| Cenário | Prêmio de 14 | Prêmio de 15 | Retorno esperado por jogo | 20 jogos | Retorno | Prejuízo esperado |
|---|---:|---:|---:|---:|---:|---:|
| Ilustrativo (padrão dos relatórios) | R$ 1.500 | R$ 2.000.000 | R$ 1,579 | R$ 31,58 | 45,1% | R$ 38,42 |
| Rateio realista | R$ 1.300 | R$ 450.000 | R$ 1,096 | R$ 21,91 | 31,3% | R$ 48,09 |
| Sem 14/15 (só prêmios fixos) | — | — | R$ 0,898 | R$ 17,96 | 25,7% | R$ 52,04 |

**Leitura:** o “prêmio” de 15 acertos é **rateado** entre todos os ganhadores do país (e a Caixa ainda retém parte para o fundo de reserva). Por isso o número realista de retorno fica na casa de **30%**, e não 45%.

### Simulação de 20.000 concursos futuros (20 jogos por concurso)

| Métrica | Valor |
|---|---:|
| Saldo médio por concurso | **−R$ 51.08** |
| Saldo mediano | −R$ 56.00 |
| 5% piores casos | −R$ 70.00 ou pior |
| 5% melhores casos | −R$ 14.00 ou melhor |
| Chance de terminar o concurso no lucro | **2.3%** |
| Melhor caso observado | +R$ 1,307.00 |
| Pior caso | −R$ 70.00 (perde os R$ 70) |

Ou seja: em cerca de **97,7% dos concursos** o conjunto devolve menos do que custou. O lucro aparece em ~2,3% das vezes, quase sempre por causa de um único acerto de 14 — e some no concurso seguinte. **É entretenimento com custo conhecido, não investimento.**

## 7. Como usar na prática (passo a passo)

1. **Decida o orçamento do mês** e trate como gasto de lazer. Não aumente o valor depois de uma perda (isso é “perseguir o prejuízo”).
2. **Jogue o conjunto pronto** (seção 5) ou gere o seu com o script, sempre com a fixa e a excluída decididas **antes** do sorteio.
3. **Confira a paridade e a faixa** de cada jogo antes de apostar: 7/8 pares e 9/10 em 1–16. Se um jogo não cumprir, troque uma dezena.
4. **Não “complete” a aposta** com as dezenas da excluída. A regra é: 04 e 10 ficam fora de todos os jogos.
5. **Revise a cada 25 concursos:** recalcule a prevalência e regenere os 13 restantes. (Sabendo que isso reorganiza, não melhora a expectativa.)
6. **Registre o custo real.** Comparar prêmio com custo é o único jeito de não se enganar com um acerto isolado de 13.

## 8. Resumo em uma tabela

| Item | Valor |
|---|---|
| Fixa | 06-12 (dupla cruzada mais frequente: 43%) |
| Excluída | 04-10 (28%, disjunta da fixa) |
| Jogos | 20 de 15 dezenas |
| Paridade | 7/8 pares — 56% dos concursos reais |
| Faixa | 9/10 em 1–16 — 54% dos concursos reais |
| Custo | R$ 70,00 por concurso |
| Retorno esperado | ~30% (realista) a 45% (ilustrativo) |
| Prejuízo esperado | R$ 38 a R$ 52 por concurso |
| Chance de lucro em um concurso | ~2,3% |
| Chance de 15 acertos (qualquer jogo) | 1 em 3.268.760 |

*Fonte dos dados: 100 últimos concursos da Lotofácil (3726 a 3825, julho a novembro de 2026). Scripts e CSVs no repositório.*