# Fixa + excluída aprimorada: equilíbrio (7/8) + prevalência

**Fixa = 06 12** · **Excluída = 04 10** · Jogo de 15 dezenas com as demais 13 escolhidas por prevalência (frequência nos últimos 100) e, no conjunto “com equilíbrio”, com paridade 7/8 e faixa 7/8.

## 1) O equilíbrio é prevalente nos sorteios? (últimos 100 concursos)

**Pares por concurso** (esperado 7,2): 5 pares: 11 concursos, 6 pares: 25 concursos, 7 pares: 33 concursos, 8 pares: 23 concursos, 9 pares: 6 concursos, 10 pares: 2 concursos.

**Dezenas em 1–16 por concurso** (esperado 9,6): 7 em 1–16: 5 concursos, 8 em 1–16: 11 concursos, 9 em 1–16: 29 concursos, 10 em 1–16: 25 concursos, 11 em 1–16: 25 concursos, 12 em 1–16: 4 concursos, 13 em 1–16: 1 concursos.

**Conjunta:** paridade 7/8 **e** faixa 7/8 ao mesmo tempo em apenas **10 dos 100 concursos**. Paridade 7/8 sozinha: 56 concursos. Faixa 7/8 sozinha: 16 concursos.

⚠️ **Ponto didático 1 — a paridade 7/8 é prevalente.** Esperado 7,2 pares por sorteio; 7 ou 8 pares ocorreram em 56 dos 100 concursos. Exigir 7/8 aqui é seguir o padrão real.

⚠️ **Ponto didático 2 — a faixa 7/8 NÃO é prevalente.** Com 16 dezenas em 1–16 e 9 em 17–25, o esperado é 9,6 em 1–16 e 5,4 em 17–25. Exigir 7 ou 8 em 17–25 é um equilíbrio **artificial**: só aconteceu em 16 dos 100 concursos, e o par completo (paridade 7/8 **e** faixa 7/8) em 10 dos 100.

⚠️ **Ponto didático 3 — mas isso NÃO muda a chance por jogo.** Por simetria, qualquer jogo de 15 dezenas tem exatamente a mesma distribuição de acertos: P(k acertos) = C(15,k)·C(10,15−k)/C(25,15), e 15 acertos é 1 em 3.268.760 para **qualquer** combinação. Um jogo com só 7 dezenas em 1–16 tem, sim, teto de 12 acertos nos sorteios “típicos” de 10 em 1–16 — mas nos sorteios com 8 em 1–16 ele passa a ser favorecido, e no total as probabilidades se igualam. A restrição **redistribui** o risco entre tipos de sorteio, não o reduz. Como o prêmio não depende do tipo de sorteio, a expectativa de retorno é idêntica.

## 2) Os 20 jogos com equilíbrio (fixa + excluída + prevalência + 7/8 + 7/8)

| # | Jogo (15 dezenas) | Pares/Ímpares | 1–16 / 17–25 |
|---:|---|---|---|
| 1 | 01 02 03 05 06 07 12 13 17 18 19 20 22 23 24 | 7/8 | 8/7 |
| 2 | 01 02 03 05 06 08 12 15 18 19 20 21 22 24 25 | 8/7 | 8/7 |
| 3 | 01 02 03 06 07 08 12 13 18 19 20 21 22 24 25 | 8/7 | 8/7 |
| 4 | 01 02 03 06 08 09 11 12 17 18 19 22 23 24 25 | 7/8 | 8/7 |
| 5 | 01 02 05 06 09 12 14 16 17 18 19 20 23 24 25 | 8/7 | 8/7 |
| 6 | 01 03 06 07 08 09 12 14 17 18 20 21 22 23 24 | 8/7 | 8/7 |
| 7 | 01 03 06 07 08 11 12 16 18 19 21 22 23 24 25 | 7/8 | 8/7 |
| 8 | 01 03 06 07 09 12 14 16 17 18 19 20 22 23 24 | 8/7 | 8/7 |
| 9 | 01 03 06 08 11 12 14 15 17 19 20 21 22 24 25 | 7/8 | 8/7 |
| 10 | 01 05 06 08 12 13 14 16 18 19 20 21 22 23 25 | 8/7 | 8/7 |
| 11 | 01 05 06 09 12 14 15 16 17 18 19 20 23 24 25 | 7/8 | 8/7 |
| 12 | 02 03 06 07 08 09 12 17 18 19 20 21 23 24 25 | 7/8 | 7/8 |
| 13 | 02 03 06 11 12 13 16 17 19 20 21 22 23 24 25 | 7/8 | 7/8 |
| 14 | 02 05 06 07 08 12 13 17 18 19 20 21 23 24 25 | 7/8 | 7/8 |
| 15 | 02 06 07 08 09 12 14 17 19 20 21 22 23 24 25 | 8/7 | 7/8 |
| 16 | 02 06 07 09 12 13 15 16 17 18 19 21 22 24 25 | 7/8 | 8/7 |
| 17 | 03 05 06 07 08 09 12 16 18 19 20 21 22 23 25 | 7/8 | 8/7 |
| 18 | 03 05 06 08 12 13 14 16 17 18 19 20 23 24 25 | 8/7 | 8/7 |
| 19 | 03 06 12 13 14 15 16 17 18 19 20 21 22 24 25 | 8/7 | 7/8 |
| 20 | 06 08 11 12 13 14 15 16 17 18 19 20 21 22 25 | 8/7 | 8/7 |

Método: amostragem ponderada pela frequência de cada dezena nos últimos 100 (05, 03, 11, 15, 23, 24… pesam mais), com rejeição até cumprir paridade e faixa. Todos contêm 06-12 e nenhum contém 04-10.

### 2b) Conjunto recomendado: paridade 7/8 + faixa NATURAL (9–10 em 1–16)

| # | Jogo (15 dezenas) | Pares/Ímpares | 1–16 / 17–25 |
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

## 3) Backtest comparativo (mesmos 100 concursos)

- **Com equilíbrio (20 jogos):** custo R$ 7,000.00 · prêmios R$ 1,953.00 · saldo **R$ -5,047.00** (27.9% de retorno). Acertos: 11×201, 12×39, 13×0, 14×0, 15×0. Concursos com 13+: 0/100 · 14+: 0/100.
- **Sem equilíbrio (20 jogos, mesma fixa/excluída e prevalência):** custo R$ 7,000.00 · prêmios R$ 3,551.00 · saldo **R$ -3,449.00** (50.7% de retorno). Acertos: 11×198, 12×45, 13×1, 14×1, 15×0. Concursos com 13+: 2/100 · 14+: 1/100.
- **Recomendado — paridade 7/8 + faixa natural 9–10 (20 jogos):** custo R$ 7,000.00 · prêmios R$ 2,205.00 · saldo **R$ -4,795.00** (31.5% de retorno). Acertos: 11×236, 12×32, 13×3, 14×0, 15×0. Concursos com 13+: 3/100 · 14+: 0/100.

⚠️ **Viés de sobreajuste:** a prevalência foi calculada nos **mesmos** 100 concursos do backtest. Os jogos “com prevalência” parecem melhores no backtest do que seriam no futuro, porque foram escolhidos com as dezenas que **aconteceram** de sair muito nesses 100 concursos. No próximo concurso, cada dezena volta a ter a mesma chance (60% para qualquer dezena). O backtest serve para comparar os dois conjuntos entre si, não para prometer retorno futuro.

## 3b) Quantos jogos existem sob cada restrição e a diferença é ruído?

Universo com a fixa 06-12 e a excluída 04-10 fora (21 dezenas livres, 13 escolhidas):

| Restrição | Jogos possíveis | % do total |
|---|---:|---:|
| Nenhuma (C(21.13)) | 203.490 | 100.0% |
| Só paridade 7/8 | 120.120 | 59.0% |
| Só faixa 7/8 (dentro de 13 restantes) | 40.392 | 19.8% |
| Paridade 7/8 + faixa 7/8 (técnica do pedido) | 25.704 | 12.6% |
| Paridade 7/8 + faixa natural 9/10 | 75.144 | 36.9% |

**Monte Carlo (40 conjuntos de 20 jogos por técnica, mesmos 100 concursos):**

| Técnica | Prêmios médios | Desvio-padrão | Mínimo | Máximo | Retorno médio |
|---|---:|---:|---:|---:|---:|
| Paridade 7/8 + faixa 7/8 | R$ 1.996,97 | R$ 248,63 | R$ 1.708,00 | R$ 3.334,00 | 28,5% |
| Sem restrição (prevalência) | R$ 2.531,60 | R$ 628,09 | R$ 1.862,00 | R$ 3.922,00 | 36,2% |
| Paridade 7/8 + faixa natural 9/10 | R$ 2.332,82 | R$ 529,25 | R$ 1.876,00 | R$ 3.754,00 | 33,3% |

**Como ler esta tabela (importante):** por simetria, as três técnicas têm a **mesma probabilidade por jogo** — a expectativa teórica é idêntica (~45%, ~R$ 3.160 para 2.000 jogos). As médias observadas (28–36%) ficam **abaixo** de 45% porque o prêmio de 15 acertos quase nunca aparece em 2.000 jogos: ~0,06% de chance, ou 1 em 1.635 conjuntos. O que sobra é a cauda de 13 e 14 acertos, que oscila muito de conjunto para conjunto (desvio-padrão de R$ 250 a R$ 630).

A diferença entre “sem restrição” (R$ 2.531,60) e “paridade + faixa 7/8” (R$ 1.996,97) **não** é mérito da restrição: é o **viés de sobreajuste** da prevalência, que atua com mais força quando o conjunto não é obrigado a se espalhar por paridade e faixa. Nos dois casos, a conclusão prática é a mesma: retorno realizado muito abaixo do custo.

### 3c) Validação por simulação (200.000 sorteios)

Para tirar a dúvida “o jogo restrito acerta mais ou menos?”, comparei um jogo com paridade 7/8 + faixa 7/8 contra um jogo qualquer, ambos com a mesma fixa/excluída, contra 200.000 sorteios aleatórios:

| Acertos | Jogo restrito | Jogo irrestrito | Teórico |
|---|---:|---:|---:|
| 11 | 8,862% | 8,857% | 8,769% |
| 12 | 1,644% | 1,720% | 1,670% |
| 13 | 0,142% | 0,163% | 0,145% |
| 14 | 0,006% | 0,004% | 0,0046% |
| 15 | 0,000% | 0,000% | 1/3.268.760 |

As diferenças estão dentro do ruído amostral. **Confirmado: a restrição não muda a probabilidade de acertar.**

## 4) Expectativa de retorno (teoria)

- Por jogo simples, com ou sem equilíbrio e com ou sem prevalência: **~R$ 1,58 de retorno esperado contra R$ 3,50 de custo (~45%)**. Para 20 jogos: ~R$ 31,58 de retorno contra R$ 70,00 → **prejuízo esperado ~R$ 38,42/concurso**.
- O equilíbrio **não aumenta** a chance por jogo (simetria: qualquer jogo de 15 tem as mesmas probabilidades). Ele apenas concentra a cobertura em sorteios equilibrados — que, na faixa, são **menos** frequentes que os sorteios típicos (9–10 em 1–16).
- A prevalência **não aumenta** a chance futura: a dezena 05 saiu 67% nos últimos 100, mas sua chance no próximo concurso continua 60%, igual às demais.

**Veredito:** a técnica aprimorada é uma forma organizada e didática de montar jogos (fixa/excluída + equilíbrio + dezenas frequentes) e garante jogos “típicos” na paridade, que é o eixo onde o equilíbrio realmente existe (7/8 em 56% dos concursos). Mas **não é mais rentável** que jogos simples comuns: a expectativa é ~45% em qualquer formato, e a simulação confirma que a restrição não altera a probabilidade por jogo.

**Recomendação prática, se quiser manter o pedido:** use paridade 7/8 (aderente à realidade) e **relaxe a faixa para a prevalência real (~9–10 em 1–16 / ~5–6 em 17–25)** — o conjunto “recomendado” acima. Ele mantém o espírito do equilíbrio sem forçar um padrão que só ocorre em 10% dos sorteios, e concentra as dezenas mais prevalentes. É a versão que eu apostaria entre as três, não por ter mais chance, mas por ser mais coerente com o que a Lotofácil realmente sorteia.

> ⚠️ Esperança matemática negativa por desenho (43,35% de prêmio bruto). Frequência passada não prevê o futuro.

## Arquivos

- `jogos_fixa_excluida_equilibrio.csv` — 20 jogos com equilíbrio + 20 sem, com paridade/faixa de cada um.
- `backtest_equilibrio.csv` — backtest dos dois conjuntos por concurso.
- `relatorio_fixa_excluida_equilibrio.html` — versão visual.
- `analise_fixa_excluida_equilibrio.py` — script reproduzível.
