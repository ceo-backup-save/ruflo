# Lista 1 × Lista 2 — Quadras pares (1–25) e distância de Hamming 2

**Lista 1 (mantida):** últimos 100 concursos **3726–3825** (número + 15 dezenas) — ver `lista1_ultimos_100_concursos.csv` e `relatorio.md`.
**Lista 2 (nova):** quadras (4 dezenas) formadas **apenas por dezenas pares de 1 a 25**: 02, 04, 06, 08, 10, 12, 14, 16, 18, 20, 22, 24 → **C(12,4) = 495 quadras**.

## Passo a passo (didático)

**Passo 1 — O que é uma quadra par?** Uma quadra é só um grupo de 4 dezenas pares, ex.: `02 04 06 08`. Há 495 grupos possíveis com as 12 pares.

**Passo 2 — O que é distância de Hamming?** Escreva cada quadra como 12 posições (uma por dezena par, na ordem 02,04,…,24), com 1 onde a dezena está na quadra e 0 onde não está. A distância de Hamming entre duas quadras é **em quantas posições elas diferem**.

Exemplo com a quadra de referência (a mais frequente nos 100 concursos):

- Referência: **04 08 12 24**
- Vetor binário (02,04,06,08,10,12,14,16,18,20,22,24): 0 1 0 1 0 1 0 0 0 0 0 1
- Vizinhança distância 2 (ex.): **04 06 12 24** — compartilha 3 dezenas com a referência, troca 1 (sai uma, entra outra) → vetor difere em **2 posições** → Hamming = 2.
- Distância 4 = compartilha 2 dezenas (troca 2). Distância 6 = compartilha 1. Distância 8 = compartilha 0.

**Passo 3 — Quantas quadras estão a distância 2 da referência?** 4 escolhas de qual dezena sai × 8 escolhas de qual entra = **32 vizinhas**. São elas que a Lista 2 destaca como “quadras com Hamming distância 2”.

**Passo 4 — Comparação Lista 1 × Lista 2:** uma quadra “aparece” em um concurso quando suas 4 dezenas pares estão todas nas 15 sorteadas. Cada concurso cobre C(m,4) quadras, onde m = nº de pares sorteados naquele concurso (média ~7,2 pares; como C(m,4) cresce rápido, a média real é 43,7 quadras por concurso — ver cobertura abaixo).

---

## Resultado — quadras mais presentes (esperado ~10.8 em 100)

Quadra de referência (mais frequente): **04 08 12 24** — 17 concursos (17%).

| # | Quadra | Ocorrências | % | Dist. Hamming da ref. |
|---:|---|---:|---:|---:|
| 1 | 04 08 12 24 | 17 | 17% | 0 |
| 2 | 06 12 14 16 | 17 | 17% | 6 |
| 3 | 06 12 16 24 | 17 | 17% | 4 |
| 4 | 02 06 12 24 | 16 | 16% | 4 |
| 5 | 06 12 14 24 | 16 | 16% | 4 |
| 6 | 04 06 12 24 | 15 | 15% | 2 |
| 7 | 06 08 12 24 | 15 | 15% | 2 |
| 8 | 06 14 16 24 | 15 | 15% | 6 |
| 9 | 08 12 18 24 | 15 | 15% | 2 |
| 10 | 02 06 14 16 | 14 | 14% | 8 |
| 11 | 02 06 16 22 | 14 | 14% | 8 |
| 12 | 02 14 16 22 | 14 | 14% | 8 |
| 13 | 04 08 12 18 | 14 | 14% | 2 |
| 14 | 04 08 18 24 | 14 | 14% | 2 |
| 15 | 06 08 12 22 | 14 | 14% | 4 |
| 16 | 06 10 14 20 | 14 | 14% | 8 |
| 17 | 06 12 16 22 | 14 | 14% | 6 |
| 18 | 08 12 16 24 | 14 | 14% | 2 |
| 19 | 02 06 14 20 | 13 | 13% | 8 |
| 20 | 02 06 14 24 | 13 | 13% | 6 |

## Quadras menos presentes

| # | Quadra | Ocorrências | % | Dist. Hamming da ref. |
|---:|---|---:|---:|---:|
| 1 | 04 10 16 18 | 3 | 3% | 6 |
| 2 | 10 12 14 18 | 3 | 3% | 6 |
| 3 | 02 10 12 18 | 4 | 4% | 6 |
| 4 | 02 12 14 18 | 4 | 4% | 6 |
| 5 | 04 06 18 20 | 4 | 4% | 6 |
| 6 | 04 08 10 16 | 4 | 4% | 4 |
| 7 | 04 14 16 18 | 4 | 4% | 6 |
| 8 | 10 12 16 18 | 4 | 4% | 6 |
| 9 | 02 04 06 18 | 5 | 5% | 6 |
| 10 | 02 04 12 20 | 5 | 5% | 4 |
| 11 | 02 04 14 18 | 5 | 5% | 6 |
| 12 | 02 04 16 20 | 5 | 5% | 6 |
| 13 | 02 04 18 20 | 5 | 5% | 6 |
| 14 | 02 04 18 22 | 5 | 5% | 6 |
| 15 | 02 04 18 24 | 5 | 5% | 4 |
| 16 | 02 08 12 20 | 5 | 5% | 4 |
| 17 | 02 10 12 20 | 5 | 5% | 6 |
| 18 | 02 12 18 20 | 5 | 5% | 6 |
| 19 | 04 06 16 18 | 5 | 5% | 6 |
| 20 | 04 10 18 20 | 5 | 5% | 6 |

## As 32 vizinhas a distância 2 da referência

| # | Quadra vizinha (dist. 2) | Ocorrências | % |
|---:|---|---:|---:|
| 1 | 04 06 12 24 | 15 | 15% |
| 2 | 06 08 12 24 | 15 | 15% |
| 3 | 08 12 18 24 | 15 | 15% |
| 4 | 04 08 12 18 | 14 | 14% |
| 5 | 04 08 18 24 | 14 | 14% |
| 6 | 08 12 16 24 | 14 | 14% |
| 7 | 04 06 08 12 | 13 | 13% |
| 8 | 04 06 08 24 | 13 | 13% |
| 9 | 04 08 16 24 | 13 | 13% |
| 10 | 04 08 20 24 | 13 | 13% |
| 11 | 04 08 22 24 | 13 | 13% |
| 12 | 04 12 18 24 | 13 | 13% |
| 13 | 08 12 22 24 | 13 | 13% |
| 14 | 02 04 08 24 | 12 | 12% |
| 15 | 02 08 12 24 | 12 | 12% |
| 16 | 04 08 14 24 | 12 | 12% |
| 17 | 04 12 20 24 | 12 | 12% |
| 18 | 04 08 12 22 | 11 | 11% |
| 19 | 04 12 14 24 | 11 | 11% |
| 20 | 04 12 16 24 | 11 | 11% |
| 21 | 04 12 22 24 | 11 | 11% |
| 22 | 08 12 20 24 | 11 | 11% |
| 23 | 02 04 12 24 | 10 | 10% |
| 24 | 04 08 10 24 | 10 | 10% |
| 25 | 04 08 12 20 | 10 | 10% |
| 26 | 04 10 12 24 | 10 | 10% |
| 27 | 08 12 14 24 | 10 | 10% |
| 28 | 02 04 08 12 | 9 | 9% |
| 29 | 04 08 10 12 | 9 | 9% |
| 30 | 04 08 12 14 | 9 | 9% |
| 31 | 04 08 12 16 | 9 | 9% |
| 32 | 08 10 12 24 | 9 | 9% |

**Cobertura por concurso:** total de presenças de quadras na Lista 1 = 4371 (média de 43.7 quadras cobertas por concurso). Distribuição de m (pares por concurso): m=5: 11 concursos, m=6: 25 concursos, m=7: 33 concursos, m=8: 23 concursos, m=9: 6 concursos, m=10: 2 concursos.

> ⚠️ Como nas trincas: a quadra mais frequente no passado não tem mais chance no próximo concurso (continua ~10,8% teórica para qualquer quadra específica). Distância de Hamming organiza a similaridade entre quadras — não aumenta a chance de acerto.

## Arquivos

- `ranking_quadras_pares.csv` — 495 quadras com ocorrências, %, último concurso, atraso e distância de Hamming da referência.
- `relatorio_quadras_hamming.html` — versão visual e didática (gráficos, heatmap, Lista 1 com pares destacados).
- `analise_quadras_hamming.py` — script reproduzível.
