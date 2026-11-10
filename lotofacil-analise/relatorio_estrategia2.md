# Estratégia 2 — 20 trios × 30 jogos com a trinca excluída (600 jogos): análise

**Interpretação adotada:** para **cada um dos 20 trios** pares de 1–12, 1 lote com **30 combinações** de 15 dezenas **excluindo as 3 da trinca** (15 sorteadas das 22 restantes). Total: **20 lotes × 30 = 600 jogos/concurso = R$ 2.100,00**. Se a sua ideia era outro número de jogos por lote, a matemática por jogo abaixo não muda — basta multiplicar.

## 1) Cobertura teórica

| Cobertura | 1 lote (30 jogos) | 20 lotes (600 jogos) |
|---|---:|---:|
| 15 acertos | 30/3.268.760 = 0.00092% (1 em 108.958) | 600/3.268.760 = 0.0184% (1 em 5.447) |
| 14+ acertos | ~0,014% (1 em ~7.200) | ~2,8% (1 em ~36) |
| 13+ acertos | ~4,4% (1 em ~23) | ~59% (1 em ~1,7) |
| 11+ acertos | ~3,2 jogos premiados em média | ~63,5 jogos premiados em média |

- **Jackpot:** 1 em 5.448 concursos (~17 anos jogando todo concurso, a 312/ano). Em 100 concursos, a chance de ver um 15 é de apenas ~1,8%.
- **14+:** ~1 em 36 concursos. **13+:** ~59% dos concursos terão pelo menos um 13 (paga R$ 35).
- **11/12:** você ganhará dezenas de prêmios pequenos por concurso (~63 jogos premiados), somando em média só ~R$ 540 em prêmios fixos contra R$ 2.100 de custo.

## 2) “Aumenta a chance do fechamento”? Só no condicional — e é aí que está a ilusão

- **Se a trinca está totalmente FORA do sorteio** (probabilidade de 5.22% por trinca), o sorteio é um subconjunto das 22 dezenas e cada jogo do lote tem chance de 15 pontos de **1/170,544** — **19,2× maior** que 1/3.268.760. E a chance de 11+ por jogo sobe para **38.7%** (contra 10,6% incondicional).
- **Mas** esse cenário acontece só em 5,22% dos concursos para uma trinca específica. Nos outros 94,78%, o lote está parcial ou totalmente capado (teto 14/13/12).
- **Incondicionalmente, cada jogo continua valendo 1/3.268.760 para o jackpot** — exatamente como 600 jogos livres. A estratégia não cria chance; ela **aposta 20 vezes** em 20 cenários “trinca fora” diferentes, pagando 20× mais para isso.
- Nos últimos 100 concursos, em média **1.1 das 20 trincas** estavam totalmente fora de cada sorteio — mas a distribuição é bimodal: **47 concursos com 0 trincas fora** (jackpot impossível nos 600 jogos), 38 com 1, 13 com 4 e 2 com 10. Cada lote “aberto” tem apenas 30/170.544 = 0,018% de chance condicional de 15 pontos. Somados, voltamos aos mesmos 0,018% incondicionais dos 600 jogos.

## 3) Fechamento de verdade: 30 jogos em 22 dezenas garantem 11 — mas só se a trinca estiver fora

**Garantia real do lote de exemplo (30 jogos, enumeração dos 170,544 sorteios possíveis nas 22 dezenas):** no pior caso, o melhor jogo do lote faz **11 acertos** — ou seja, **30 jogos aleatórios em 22 dezenas já garantem pelo menos 11 acertos sempre que o sorteio está contido nas 22 dezenas (trinca fora)**. Distribuição do melhor jogo por sorteio: 11 acertos: 8755 sorteios, 12 acertos: 107008 sorteios, 13 acertos: 51666 sorteios, 14 acertos: 3085 sorteios, 15 acertos: 30 sorteios.

Por que 30 jogos bastam para 11, mas não para 12/13? Cada jogo tem 38,7% de chance de 11+ contra um sorteio nas 22 dezenas; com 30 jogos, a chance de nenhum chegar a 11 é ~(1−0,387)^30 ≈ 0,00004% — praticamente zero. Para 12 acertos a chance por jogo cai para 10,7% e 30 jogos já deixam ~5% dos sorteios sem nenhum 12 (é o grupo “melhor jogo = 11” acima).

⚠️ **Correção de um erro comum:** cobrir todos os subconjuntos de 11 dezenas das 22 exigiria C(22,11)/C(15,11) ≈ 517 jogos — mas isso é condição **suficiente, não necessária**. A garantia de 11 acertos só exige que cada sorteio compartilhe 11 dezenas com algum jogo, o que 30 jogos aleatórios já conseguem (provado pela enumeração acima).

**O problema é o condicional:** essa garantia de 11 só vale quando a trinca está fora (5,22% dos concursos por lote). Nos demais concursos o lote está capado. E, somando os 20 lotes, há um dado decisivo:

- Em **47 dos últimos 100 concursos, nenhuma das 20 trincas estava totalmente fora do sorteio** (o sorteio tinha 4+ dezenas pares em 1–12, atingindo todas as trincas). Nesses concursos, **o jackpot é impossível para os 600 jogos** — todo jogo exclui uma trinca que saiu parcialmente. Nos outros 53 concursos, em média 1–10 lotes ficam “abertos” para 15 pontos.
- Com 600 jogos **livres** (sem exclusão), o jackpot seria possível em 100% dos concursos. A estratégia troca cobertura universal por cobertura concentrada: mesma chance incondicional por real, variância muito maior.

Se a ideia fosse jogar **todas** as C(22,15) = 170.544 combinações das 22 dezenas, o custo seria 170.544 × R$ 3,50 = **R$ 596.904 por lote** (× 20 lotes = R$ 11,9 milhões/concurso). Inviável — e mesmo assim, só pagaria o jackpot se a trinca estivesse fora.

## 4) Duplicidade entre os 20 lotes

Dos 600 jogos gerados aleatoriamente, **600 são distintos** (0 duplicados entre lotes). Com geração aleatória a duplicidade é quase zero — bom para cobertura. **Atenção:** se você gerar os 30 jogos de cada lote sempre com a mesma regra sistemática (ex.: “os 30 primeiros jogos em ordem”), os lotes vão gerar **os mesmos jogos repetidos** e você pagará várias vezes pelo mesmo jogo, sem cobertura nova. A geração precisa ser globalmente distinta.

## 5) Rentabilidade

- **Custo:** R$ 2,100.00/concurso · R$ 210,000.00 em 100 concursos · ~R$ 655 mil/ano jogando todo concurso.
- **Retorno esperado:** ~R$ 947.39/concurso (~45% do apostado, compatível com os 43,35% da Caixa) → **prejuízo esperado de ~R$ 1,152.61/concurso (~55%)**.
- **Por real apostado, é idêntico** à estratégia anterior (120 jogos) e a 600 jogos livres: R$ 1,58 de retorno esperado para cada R$ 3,50. Multiplicar os jogos multiplica o custo e o prejuízo esperado na mesma proporção — não há ganho de escala.

## 6) Backtest: os 600 jogos nos últimos 100 concursos

- **Custo (100 concursos):** R$ 210,000.00 · **Prêmios:** R$ 61,090.00 · **Saldo: R$ -148,910.00** (29.1% de retorno)
- **Acertos em 60.000 jogos:** 11: 5399 · 12: 1023 · 13: 85 · 14: 4 · 15: 0 (teórico: ~5.261 / ~1.002 / ~87 / ~3 / ~0,02)
- **Concursos com pelo menos um prêmio:** 100/100 · com 13+: 48/100 · com 14+: 4/100 · com 15: 0/100

O backtest é a estratégia anterior multiplicada por 5: muitos prêmios de R$ 7/R$ 14, alguns 13, raríssimos 14, nenhum 15 — e prejuízo próximo ao esperado. Detalhe por concurso em `backtest_estrategia2_100_concursos.csv`.

## 7) Veredito

1. **Aumenta a chance de fechamento?** No sentido condicional, sim: 30 jogos em 22 dezenas **garantem 11 acertos se a trinca estiver fora** (provado por enumeração) e a chance de 15 pontos sobe 19× nesse cenário — mas esse cenário é só 5,22% por trinca, e em 47% dos concursos nenhuma trinca está fora (jackpot impossível nos 600 jogos). Incondicionalmente, por real apostado, a chance é idêntica à de jogos livres.
2. **Aumenta a chance total?** Só porque você gasta 5× mais que na estratégia anterior (600 vs 120 jogos). Por real apostado, a cobertura é **idêntica** a qualquer outro conjunto de jogos.
3. **É rentável?** Não. Esperança matemática de ~43–45% de retorno, prejuízo esperado de ~R$ 1.155/concurso. Em 100 concursos de backtest: −R$ 148,910.00.
4. **Útil para quê?** Como forma de **organizar** a aposta por cenários (“qual trinca fica de fora?”) e garantir volume de prêmios pequenos — desde que tratada como custo de entretenimento. Se o objetivo é cobertura de 11–13 com menos gestão, um fechamento clássico de 18–20 dezenas (uma única aposta múltipla) entrega a mesma matemática por real, sem 600 volantes.

> ⚠️ Nenhuma exclusão, fechamento ou análise de frequência passada altera a esperança matemática negativa desenhada pela Caixa (43,35% de prêmio bruto). Jogue apenas com valor que pode perder.
