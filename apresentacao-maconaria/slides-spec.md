# Especificação de slides — “A maçonaria nos bastidores — ou não?”

**Deck:** 15 slides · 16:9 (1280×720) · pt-BR · tom analítico, editorial, premium
**Design System:** Minimal Editorial Mono
**Arquivo executável:** `index.html` (+ `img/`)

---

## Tokens aplicados

| Token | Valor | Uso |
|---|---|---|
| `background` | `#FFFFFF` | 90–100% de cada slide |
| `ink` | `#111111` | títulos |
| `graphite` | `#1A1A1A` | tab, cards, dots, rules de destaque |
| `graphite-2` | `#2B2B2E` | texto de apoio forte |
| `body` | `#666B73` | corpo e legendas |
| `line` | `#D8DCE3` | divisores |

**Tipografia:** Inter (fallback Helvetica Neue/Arial). Títulos 700, `-0.03em`; corpo 400, 1.45–1.55; labels 500 caixa-alta com `0.14–0.18em`.
**Grid:** 12 colunas, gutter 16 px (1,25%), margens laterais 76 px (5,9%), topo 54 px, base 44 px. Nenhuma linha de grade visível.
**Fotografia:** 8 imagens editoriais geradas, cor natural, luz difusa, sem texto/logos; ocupam no máximo 60% da largura e 70% da altura (exceção intencional: capa e faixas panorâmicas com respiro branco no rodapé).

---

## Slide 01 — Capa

- **Objetivo:** instalar o tema e a hipótese de trabalho em 5 segundos.
- **Layout:** `Minimal_Editorial_Cover` (título grande à esquerda, foto hero à direita, card grafite sobreposto, tab preto no topo).
- **Copy final:**
  - Tab: `RELATÓRIO DE PESQUISA · 2026`
  - Kicker: `APRESENTAÇÃO · 15 SLIDES`
  - Título: **A maçonaria nos bastidores — ou não?**
  - Linha de apoio: “Três eixos, trinta marcos e doze mitos testados contra as fontes.”
  - Card: **Bastidor, sim. Comando, não.** / “A ordem como rede de sociabilidade — não como governo secreto.”
- **Posicionamento:** título em 3 linhas a 74 px, começando a 146 px do topo; filete preto de 56×2 px entre título e apoio; card a 86 px da base, 432 px de largura; foto de 44%×80% encostada no topo/direita.
- **Prompt de imagem:** “Editorial architectural photograph, tight crop of a neoclassical civic building’s marble pediment and columns, soft diffuse late-afternoon daylight, muted warm stone tones, shallow depth of field, no people, no text, no logos, generous empty sky on the left.”
- **Ícones:** nenhum (capa tipográfica).
- **Acessibilidade:** `h1` único; contraste título/fundo 16:1; texto alternativo descreve o frontão e a luz; navegação por teclado disponível desde o slide 1.

## Slide 02 — Tese central

- **Objetivo:** substituir “conspiração” por “rede”.
- **Layout:** `Minimal_Content_Split` 40/60 (texto à esquerda, foto à direita, filete preto curto).
- **Copy final:** kicker `O QUE A DOCUMENTAÇÃO MOSTRA`; título **Bastidor, sim. Comando, não.**; parágrafo “A maçonaria foi uma infraestrutura de sociabilidade, confiança e comunicação das elites liberais. Não um governo secreto com diretriz única.”; três itens: *Canal, não agente* / *Onipresente, não onipotente* / *Dividida entre si*.
- **Posicionamento:** coluna 1–5; foto colunas 7–12 com 78% de altura e legenda de 9,5 px; lista com divisores `#D8DCE3` (sem caixas).
- **Prompt de imagem:** “Editorial photograph of an empty nineteenth-century legislative assembly hall, curved wooden benches, tall windows, soft diffuse daylight, warm wood and cream palette, no people, no text, vertical.”
- **Ícones:** três `arrow` monoline 18 px, traço 1,3.
- **Acessibilidade:** lista semântica `ul/li`; leitura linear título → tese → itens; texto de apoio acima de 4,5:1.

## Slide 03 — Método

- **Objetivo:** dar credibilidade: mostrar como a evidência é classificada.
- **Layout:** `Metric_Case_Study` (métrica + texto à esquerda, foto à direita, divisor cinza).
- **Copy final:** kicker `COMO SEPARAR PROVA DE LENDA`; métrica **A–D**; tabela A documento primário · B historiografia consolidada · C indício forte · D lenda; nota “Regra de ouro: número de maçons em um evento não prova direção maçônica — prova densidade de rede.”
- **Posicionamento:** métrica a 118 px alinhada pela base com a nota; tabela de 4 linhas com divisores de 1 px; foto (72% de altura) na coluna 9–12.
- **Prompt de imagem:** “Editorial still-life of a nineteenth-century leather ledger open on a wooden desk with fountain pen and brass inkwell, soft window light, warm browns and creams, no legible writing, no logos.”
- **Ícones:** nenhum; a tabela é o gráfico.
- **Acessibilidade:** tabela com `<table>` real e `aria-label`; não depende só de cor para diferenciar graus.

## Slide 04 — Eixo político e constitucional

- **Objetivo:** provar que a loja era uma escola de governo.
- **Layout:** `Works_List` (foto grande à esquerda 48–55%, lista de 3 itens com ícones à direita).
- **Copy final:** kicker `EIXO POLÍTICO E CONSTITUCIONAL`; título **A loja como escola de governo**; apoio “Eleição anual, votação por maioria, representação de oficinas e um texto fundante: as *Constituições* de Anderson, de 1723.”; itens: EUA 1776–1787 (8 ou 9 dos 56; 13 dos 39) · Portugal 1820 (Sinédrio) · Brasil 1822 e 1890.
- **Posicionamento:** foto 82% de altura na coluna 1–5; lista ocupa colunas 7–12, começando a 18 px do topo do corpo; cada item com título 14 px e descrição 12 px.
- **Prompt de imagem:** reutiliza `assembleia.jpg` (consistência de acervo).
- **Ícones:** `flag`, `scale`, `column` — monoline, 18 px.
- **Acessibilidade:** ordem de leitura foto → título → lista; descrições curtas (≤ 12 palavras).

## Slide 05 — Eixo social e associativo

- **Objetivo:** mostrar a face menos visível e mais documentável: a associação civil.
- **Layout:** `Minimal_Content_Split` invertido (texto à esquerda, foto à direita).
- **Copy final:** kicker `EIXO SOCIAL E ASSOCIATIVO`; título **Antes de secreta, uma associação civil**; apoio “Socorro mútuo, escolas, hospitais e clubes — numa época em que a sociedade civil ainda não existia como a conhecemos.”; quatro microblocos: Mutualismo · Abolicionismo · Recrutamento · Face conservadora (1964).
- **Posicionamento:** grade 2×2 de microblocos com 18 px de gutter, sem molduras; foto na coluna 8–12 a 74% de altura.
- **Prompt de imagem:** reutiliza `sociabilidade.jpg`.
- **Ícones:** nenhum (o ritmo vem da grade tipográfica).
- **Acessibilidade:** microblocos em ordem de leitura; títulos em negrito funcionam como cabeçalhos visuais.

## Slide 06 — Eixo cultural, simbólico e de imprensa

- **Objetivo:** ligar a ordem à produção de opinião e imaginário.
- **Layout:** `Editorial_Feature` (imagem panorâmica inferior, título + métrica acima, card grafite sobreposto).
- **Copy final:** kicker `EIXO CULTURAL, SIMBÓLICO E DE IMPRENSA`; métrica **1734**; nota “Franklin publica as *Constituições* na Filadélfia: a imprensa entra na ordem.”; card `TRÊS MÁQUINAS DE OPINIÃO` — *Il Risorgimento · A República · A Cidade do Rio* (Cavour 1847, Quintino 1870, Patrocínio 1887); ressalva no topo-direita sobre a “Marselhesa”.
- **Posicionamento:** bloco de título a 112 px; faixa fotográfica de 44% de altura com base a 62 px (rodapé sempre em branco); card a 86 px da base.
- **Prompt de imagem:** “Editorial photograph of a historic letterpress workshop: cast-iron press, trays of metal type, ink rollers, side window light, warm neutral palette, no legible letters, no logos.”
- **Ícones:** nenhum.
- **Acessibilidade:** texto branco sobre `#1A1A1A` (15:1); a ressalva não é essencial à mensagem principal e está em 10,5 px.

## Slide 07 — Cronologia I (1717–1789)

- **Objetivo:** situar a formação da ordem moderna e seu primeiro ciclo revolucionário.
- **Layout:** `Radial_Timeline` (semicírculo, 4 marcos, ícones monoline pretos).
- **Copy final:** kicker `1717 — 1789`; título **A ordem se instala**; marcos 1717 Grande Loja de Londres · 1734 Franklin publica Anderson · 1776 Independência dos EUA · 1789 Revolução Francesa; rodapé “Também no período: 1723 · 1773 · 1782 · 1789 (Inconfidência)”.
- **Posicionamento:** arco elíptico de 900×250 px centralizado; pontos de 9 px sobre a curva; rótulos alinhados à esquerda em 4 colunas de 210 px sob o arco; números de ordem em 9 px sob cada ponto.
- **Prompt de imagem:** não se aplica (slide tipográfico).
- **Ícones:** os pontos funcionam como marcadores; nenhum ícone decorativo.
- **Acessibilidade:** a linha do tempo é reproduzida como quatro blocos de texto em ordem cronológica; não há informação transmitida apenas por posição.

## Slide 08 — Cronologia II (1810–1859)

- **Objetivo:** cobrir independências, constitucionalismo ibérico e o início do Risorgimento.
- **Layout:** `Radial_Timeline` (mesma malha do slide 07 — consistência).
- **Copy final:** `1810 — 1859`; **Independências e nações**; 1810 Carbonária · 1812 Logia Lautaro · 1820 Revolução do Porto · 1822 Independência do Brasil; rodapé com 1821 México, 1835 Farroupilha, 1847, 1848, 1859–70.
- **Posicionamento:** idêntico ao slide 07.
- **Prompt de imagem:** não se aplica.
- **Ícones:** marcadores.
- **Acessibilidade:** idem; datas sempre no início de cada bloco.

## Slide 09 — Cronologia III (1871–1964)

- **Objetivo:** levar a narrativa até o uso conservador da rede no século XX.
- **Layout:** `Radial_Timeline`.
- **Copy final:** `1871 — 1964`; **Cidadania, República, poder**; 1871 Lei do Ventre Livre · 1884 Pedra da Liberdade · 1889 Proclamação da República · 1964 Golpe militar; rodapé com 1890, 1890–1901, 1908–10, 1978.
- **Posicionamento:** idêntico aos slides 07 e 08.
- **Prompt de imagem:** não se aplica.
- **Ícones:** marcadores.
- **Acessibilidade:** idem; o marco de 1964 explicita “estudo recente” para não sugerir unanimidade.

## Slide 10 — Personagens I (EUA · França · América Hispânica)

- **Objetivo:** nomear quem estava no comando e corrigir excessos.
- **Layout:** `Works_List` (foto à esquerda 33%, lista de 3 itens à direita).
- **Copy final:** kicker `QUEM ESTAVA NO COMANDO`; título **Três cenários, uma mesma rede**; EUA — Washington · Franklin · Lafayette; França — Mirabeau · Lafayette (Danton e Robespierre não eram maçons; Marat é disputado); América Hispânica — Bolívar (documentado), San Martín e O’Higgins na Lautaro.
- **Posicionamento:** foto 84% de altura na coluna 1–4; lista nas colunas 6–12.
- **Prompt de imagem:** reutiliza `cover.jpg` em recorte vertical (acervo coerente).
- **Ícones:** `flag`, `book`, `globe`.
- **Acessibilidade:** nomes separados por `·` são lidos como lista; evitar depender de itálico para distinguir ressalvas (usa-se parênteses).

## Slide 11 — Personagens II (Brasil)

- **Objetivo:** dar densidade brasileira em dois ciclos.
- **Layout:** `Minimal_Content_Split` com duas colunas de nomes + card grafite.
- **Copy final:** kicker `BRASIL · DOIS CICLOS`; título **A independência e a República**; coluna 1822: José Bonifácio (1º Grão-Mestre), Gonçalves Ledo, José Clemente Pereira, D. Pedro I (“Guatimozim”); coluna 1871–1889: Rio Branco, José do Patrocínio, Joaquim Nabuco, Quintino Bocaiúva, Benjamin Constant, Deodoro; card `COM RESERVA`: Rui Barbosa, Tiradentes, Caxias e Osório; nota “Densidade de rede não é direção política.”
- **Posicionamento:** colunas 1–7 com dois blocos de nomes; card nas colunas 9–12 alinhado a 34 px do topo; nota em filete na base.
- **Prompt de imagem:** não se aplica (slide de nomes, sem rosto — evita retratos gerados de pessoas reais).
- **Ícones:** nenhum.
- **Acessibilidade:** cada bloco tem rótulo de período em caixa-alta; o card de ressalva tem contraste 15:1.

## Slide 12 — O negativo da prova

- **Objetivo:** transformar verificação em argumento visual.
- **Layout:** tabela editorial + card grafite (variação do `Minimal_Content_Split`).
- **Copy final:** kicker `O NEGATIVO DA PROVA`; título **Onde a lenda é mais forte, a prova é mais fraca**; linhas Jefferson · Danton e Robespierre · Tiradentes · San Martín e O’Higgins · “50 de 56”; card **Presença não prova direção.**
- **Posicionamento:** tabela nas colunas 1–8 com 12 px de respiro por linha; card ancorado na base direita (colunas 9–12).
- **Prompt de imagem:** não se aplica.
- **Ícones:** nenhum; a coluna da direita é a “resposta” visual.
- **Acessibilidade:** `table` com `aria-label`; a mensagem-chave também aparece em texto no card (redundância intencional).

## Slide 13 — Grande Selo e nota de 1 dólar

- **Objetivo:** desmontar o mito mais difundido.
- **Layout:** `Editorial_Feature` (métrica + título acima, imagem panorâmica inferior, card grafite).
- **Copy final:** kicker `GRANDE SELO DOS EUA · NOTA DE 1 DÓLAR`; métrica **1782**; título **O selo não é maçônico**; apoio “O olho da Providência e a pirâmide vêm da iconografia cristã e iluminista.”; card `TRÊS FATOS DOCUMENTADOS`: projetistas não eram maçons; olho sugerido por Du Simitière; nota de 1 dólar só em 1935.
- **Posicionamento:** métrica a 96 px; faixa fotográfica de 44% com base a 62 px; card a 86 px da base, 520 px de largura.
- **Prompt de imagem:** “Extreme macro of an engraved steel intaglio plate and its fine lines on cream paper, raking natural light, warm grey and ivory, no legible letters, no numbers.”
- **Ícones:** nenhum.
- **Acessibilidade:** a numeração 1·2·3 do card é textual; imagem decorativa com alt descritivo.

## Slide 14 — Monumentos e marcos cívicos

- **Objetivo:** distinguir cerimônia, financiamento e símbolo nacional.
- **Layout:** `Project_Modular_Grid` (3 imagens coloridas assimétricas + 2 sínteses).
- **Copy final:** kicker `PEDRA FUNDAMENTAL, RITO E NAÇÃO`; título **Três monumentos, três vínculos**; Monumento a Washington (1848–1885; 22 pedras maçônicas; 250 lojas) · Estátua da Liberdade (1884–1886; Bartholdi, Loja Alsácia-Lorena) · Praça XV e Paço Imperial (Fico, aclamação, Lei Áurea; Lavradio, sede do GOB 1842–1978); sínteses “Cerimônia ≠ código” e “Marco nacional ≠ monumento maçônico”.
- **Posicionamento:** três colunas de 1,05fr / 1fr / 1fr, imagens de 236 px de altura, legendas de 10,5 px; duas sínteses em filete na base.
- **Prompt de imagem:** três fotografias editoriais — obelisco ao entardecer; Estátua da Liberdade em ângulo baixo; fachada colonial carioca com luz de manhã.
- **Ícones:** nenhum; a comparação é feita por colunas.
- **Acessibilidade:** cada figura é `<figure>` com `<figcaption>`; alt descreve o monumento e a luz.

## Slide 15 — Conclusão

- **Objetivo:** fechar com a frase que o público deve repetir.
- **Layout:** variação tipográfica da capa (título grande + card de números).
- **Copy final:** kicker `RESPOSTA FINAL`; título **Bastidor, sim. Comando, não.**; apoio “A ordem foi infraestrutura de confiança e circulação de informação — não arquitetura de poder.”; card `O RELATÓRIO EM NÚMEROS`: 3 eixos · 30 marcos · 12 mitos · 38 fontes; nota de fonte na base.
- **Posicionamento:** título a 70 px em duas linhas; card de 356 px no topo-direita; nota a 640 px de largura na base.
- **Prompt de imagem:** não se aplica (fecho tipográfico).
- **Ícones:** nenhum.
- **Acessibilidade:** números em `font-variant-numeric: tabular-nums`; nota de fonte em 10,5 px com contraste 4,6:1.

---

## Quality checks do deck

- [x] Fundo `#FFFFFF` em 100% dos slides (com faixas fotográficas que preservam o rodapé branco).
- [x] Nenhum azul, amarelo, laranja, rosa, neon ou gradiente em elementos de interface.
- [x] Acentos em `#1A1A1A` restritos a tab, cards, filetes curtos, pontos e marcadores.
- [x] Nenhuma linha de grade visível; o grid de 12 colunas existe apenas na estrutura.
- [x] Hierarquia tipográfica consistente: 74/70 (capa e fecho), 54 (h2), 38–48 (variações), 15 (corpo), 10,5 (legendas), 9–10 (labels).
- [x] Fotografia editorial colorida, natural, realista e sem texto gerado.
- [x] Sem mascotes, emojis, confetti, glassmorphism ou fundos escuros de página inteira.
- [x] Whitespace médio acima de 40% por slide; alinhamento predominantemente à esquerda.
- [x] Navegação por teclado, contador com `aria-live`, contraste mínimo 4,5:1, `prefers-reduced-motion`.

## Como apresentar / exportar

1. Abra `index.html` no navegador (ou use o preview servido).
2. `←` `→` navegam; `Home`/`End` vão ao início/fim; `P` abre a impressão.
3. Na impressão, escolha **Paisagem**, margens **Nenhuma**, ative **Gráficos de fundo** → salvar como PDF gera 15 páginas 16:9.
