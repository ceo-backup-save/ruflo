# A Ordem e o Palco — nova apresentação

**Título sugerido:** *A Ordem e o Palco*
**Subtítulo:** *A maçonaria entre a rede e o poder — 1717 a 1964*
**Alternativas de título:** *Rede, não arquitetura* (mais tese, menos narrativa) · *O compasso e a urna* (mais editorial, mais arriscado)
**Slides:** 16, em 4 atos · **Idioma:** pt-BR · **Tom:** analítico, editorial, premium
**Arquivo:** `index.html` + `img/` · **A antiga apresentação (`../apresentacao-maconaria/`) não foi alterada.**

---

## 1. Escala sugerida

A nova peça foi construída em **1920 × 1080 px (Full HD, 16:9)** — e não em 1280 × 720. A tipografia foi ampliada em **1,5×** e as margens em 1,5×, mantendo as mesmas proporções. O resultado é o mesmo desenho, visto de mais longe.

| Parâmetro | Versão anterior | **Nova versão** | Ganho |
|---|---|---|---|
| Canvas | 1280 × 720 | **1920 × 1080** | nitidez em telão e em PDF |
| Margem lateral | 76 px (5,9%) | **114 px (5,9%)** | mesma proporção |
| Topo / base | 54 / 44 px | **96 / 92 px** | respiro editorial |
| Título | 74 px | **132 px** | leitura a 10–12 m |
| Título de seção | 54 px | **86 px** | hierarquia mais clara |
| Corpo | 15 px | **28 px** | 1,5× |
| Legendas | 10,5 px | **16–19 px** | 1,5× |
| Grid | 12 col · gutter 16 | **12 col · gutter 24** | 1,25% |
| Foto (máx.) | 60% × 70% | **60% × 70%** | regra mantida |

**Por que essa escala:** um deck de pesquisa é lido em três situações — projeção, tela de laptop e PDF impresso. 1920×1080 cobre as três: é a resolução nativa da maioria dos projetores e permite exportar 15–16 páginas em 16:9 sem reflow. A escala 1,5× mantém o *whitespace* entre 40% e 48% mesmo com menos texto por slide.

---

## 2. Tokens (idênticos ao design system)

`#FFFFFF` fundo · `#111111` títulos · `#1A1A1A` tab, cards, filetes, números de folio · `#2B2B2E` apoio forte · `#666B73` corpo · `#D8DCE3` divisores e numerais de folio.
Inter 700 nos títulos (`-0.03em`), 400 no corpo (1.5), 500 caixa-alta nos labels (`0.14–0.18em`).
Fotografia editorial colorida, luz difusa, sem texto gerado; ocupa no máximo 60% da largura e 70% da altura.

---

## 3. Estrutura em quatro atos

| Ato | Slides | Função |
|---|---|---|
| **I — A pergunta** | 01–03 | instalar o problema e dar a escala do fenômeno |
| **II — Os eixos** | 04–06 | político, social, cultural/imprensa |
| **III — A prova** | 07–13 | método, cronologia, personagens, negativo, monumentos |
| **IV — A resposta** | 14–16 | mecanismos, limites, conclusão |

---

## 4. Especificação slide a slide

### Slide 01 — Capa
- **Objetivo:** instalar título e tese num único gesto.
- **Layout:** capa editorial assimétrica; foto a 40%×92% encostada no topo/direita; tab preto; card grafite na base.
- **Copy:** `ESTUDO · 2026` · `ATO I · A PERGUNTA` · **A Ordem e o Palco** · “A maçonaria entre a rede e o poder — 1717 a 1964.” · card **Bastidor, sim. Comando, não.**
- **Posicionamento:** bloco de texto a 258 px do topo; título em 132 px, duas linhas; filete preto 96×3 px; card a 150 px da base, 620 px de largura.
- **Prompt de imagem:** “Editorial wide-angle photograph of a historic archive reading room, long wooden table, tall shelves, tall windows, soft diffuse morning light, warm wood and cream, no people, no text, no logos.”
- **Ícones:** nenhum.
- **Acessibilidade:** `h1` único; `alt` descritivo; contraste 16:1.

### Slide 02 — A pergunta
- **Objetivo:** transformar a dúvida do público em método.
- **Layout:** split 7/4 com três definições em coluna.
- **Copy:** pergunta em quatro linhas (“Uma sociedade discreta explica três séculos de política?”) + **Rede** / **Presença** / **Rito**, cada uma com uma frase.
- **Posicionamento:** pergunta a 86 px ocupando 7 colunas; definições nas colunas 9–12, separadas por filetes de 1 px, alinhadas à esquerda.
- **Imagem:** não se aplica.
- **Ícones:** nenhum.
- **Acessibilidade:** definições em blocos com título e corpo; leitura linear.

### Slide 03 — A escala do fenômeno
- **Objetivo:** dar dimensão por números e introduzir o “zero” como argumento.
- **Layout:** quatro métricas em linha + numeral de folio `03` em cinza.
- **Copy:** **8–9** signatários maçons (de 56) · **13** de 39 constituintes · **250** lojas no Monumento a Washington · **0** documentos de comando central. Nota: “O quarto número é o mais importante — e o menos citado.”
- **Posicionamento:** métricas a 208 px alinhadas pela base, 4 colunas de 393 px; legendas de 19 px com largura máxima de 250 px.
- **Imagem:** não se aplica.
- **Ícones:** nenhum; o “0” é o elemento gráfico.
- **Acessibilidade:** números em `tabular-nums`; o zero também é explicado em texto.

### Slide 04 — Eixo político e constitucional
- **Objetivo:** mostrar a loja como tecnologia de governo.
- **Layout:** três colunas com ano em 72 px e filete preto de 2 px no topo.
- **Copy:** **1776 EUA** (constituição em ambiente de loja; 13 dos 39) · **1820 Portugal** (Sinédrio; maioria maçônica) · **1822 Brasil** (Grande Oriente Brasílico; D. Pedro Grão-Mestre). Nota de limite ao pé.
- **Posicionamento:** colunas de 1/3, gutter 48 px; texto de 23 px; microlegendas de 16 px.
- **Imagem:** não se aplica.
- **Ícones:** nenhum.
- **Acessibilidade:** três blocos equivalentes, cada um começando pelo ano.

### Slide 05 — Eixo social e associativo
- **Objetivo:** revelar a face associativa e sua ambiguidade política.
- **Layout:** foto à esquerda (6 colunas), lista numerada de 4 itens à direita.
- **Copy:** **01 Mutualismo** · **02 Abolicionismo** (1871, 1885, 1888) · **03 Recrutamento** · **04 Conservadorismo** (1964).
- **Posicionamento:** foto a 84% de altura; lista com divisores; títulos 28 px, descrições 21 px.
- **Prompt de imagem:** reutiliza `sociabilidade.jpg` (livro de socorros mútuos).
- **Ícones:** números em vez de ícones (mais editorial).
- **Acessibilidade:** `ul/li` com ordem explícita.

### Slide 06 — Eixo cultural e de imprensa
- **Objetivo:** provar que a ordem produziu opinião, não só ritual.
- **Layout:** quatro linhas tipográficas com ano em 44 px + foto estreita à direita.
- **Copy:** **1734** Filadélfia, Franklin · **1847** Turim, *Il Risorgimento* · **1870** Rio, *A República* · **1887** Rio, *A Cidade do Rio*.
- **Posicionamento:** anos em coluna fixa de 150 px; filetes entre linhas; foto de 420 px na coluna 10–12.
- **Prompt de imagem:** reutiliza `imprensa.jpg`.
- **Ícones:** nenhum.
- **Acessibilidade:** cada linha é um par ano→fato, legível em sequência.

### Slide 07 — Método
- **Objetivo:** dar régua ao espectador antes das conclusões.
- **Layout:** quatro graus em colunas, letra em 96 px.
- **Copy:** **A** documento primário · **B** historiografia · **C** indício · **D** lenda + regra de ouro.
- **Posicionamento:** filetes de 2 px apenas em A e B (hierarquia visual do peso da prova).
- **Imagem:** não se aplica.
- **Ícones:** nenhum.
- **Acessibilidade:** a distinção A/B × C/D também aparece por espessura do filete e por texto.

### Slide 08 — Cronologia em três atos
- **Objetivo:** condensar doze marcos em uma única página legível.
- **Layout:** três faixas horizontais; rótulo de ato à esquerda e quatro marcos por faixa.
- **Copy:** **Ato 1 (1717–1789)**: 1717 · 1734 · 1776 · 1789. **Ato 2 (1810–1859)**: 1810 · 1812 · 1820 · 1822. **Ato 3 (1871–1964)**: 1871 · 1884 · 1889 · 1964. Rodapé com marcos fora do recorte.
- **Posicionamento:** coluna de rótulo de 250 px; quatro colunas iguais; filetes entre faixas.
- **Imagem:** não se aplica.
- **Ícones:** nenhum.
- **Acessibilidade:** ordem cronológica garantida no DOM; anos em negrito.

### Slide 09 — Quem era, quem não era
- **Objetivo:** nomear sem inflar.
- **Layout:** duas colunas separadas por filete vertical.
- **Copy:** **Filiação documentada** — Washington, Franklin, Lafayette, John Paul Jones, Bolívar, José Bonifácio, Gonçalves Ledo, D. Pedro I, Rio Branco, Deodoro, Garibaldi. **Sem prova ou negada** — Jefferson, Danton e Robespierre, Tiradentes, San Martín e O’Higgins (Lautaro), Rui Barbosa (contestado).
- **Posicionamento:** nomes em 26 px com 1,75 de entrelinha; coluna direita recuada por 56 px de padding.
- **Imagem:** não se aplica (evita retratos gerados de pessoas reais).
- **Ícones:** nenhum.
- **Acessibilidade:** listas curtas; a ressalva de Lautaro está em texto, não apenas em cor.

### Slide 10 — O negativo da prova
- **Objetivo:** transformar verificação em argumento.
- **Layout:** tabela de duas colunas + card grafite.
- **Copy:** cinco pares “o que se diz → o que se sabe”; card **Presença não prova direção.**
- **Posicionamento:** tabela nas colunas 1–8; card na base direita, 3 colunas.
- **Imagem:** não se aplica.
- **Ícones:** nenhum.
- **Acessibilidade:** `<table>` com `aria-label`; a mensagem do card repete a tese.

### Slide 11 — O Grande Selo e a nota de 1 dólar
- **Objetivo:** desmontar o mito mais popular com uma data inesperada.
- **Layout:** feature editorial — métrica e título no topo, três fatos alinhados, faixa fotográfica na base.
- **Copy:** métrica **1935**; título **O selo entra no dólar**; fatos **1782** projetistas não maçons · **1776** olho de Du Simitière · **1935** Roosevelt e Wallace, de 32º.
- **Posicionamento:** métrica a 180 px; fatos a 470 px da base; foto com 29% de altura e base a 96 px (rodapé branco preservado).
- **Prompt de imagem:** reutiliza `selo.jpg` (macro de placa gravada, sem letras).
- **Ícones:** nenhum.
- **Acessibilidade:** os três fatos são numerados por ano, não por posição.

### Slide 12 — Pedra fundamental não é código
- **Objetivo:** explicar a fama maçônica dos monumentos sem misticismo.
- **Layout:** duas figuras lado a lado com legendas analíticas.
- **Copy:** **1848 Monumento a Washington** (rito, 22 pedras, 250 lojas) · **1884 Estátua da Liberdade** (Bartholdi, Loja Alsácia-Lorena, Grão-Mestre de Nova York).
- **Posicionamento:** imagens de 300 px de altura; legendas com título de 19 px e corpo de 16 px.
- **Prompt de imagem:** reutiliza `washington.jpg` e `liberdade.jpg`.
- **Ícones:** nenhum.
- **Acessibilidade:** `<figure>/<figcaption>`; alt descreve monumento e luz.

### Slide 13 — Praça XV e Paço Imperial
- **Objetivo:** ancorar a tese no Brasil e no presente urbano.
- **Layout:** foto panorâmica à esquerda (7 colunas), lista de três datas e card do Lavradio à direita.
- **Copy:** **1822** Dia do Fico · **1822** Aclamação · **1888** Lei Áurea · card **Fora da praça:** Palácio do Lavradio, sede do GOB de 1842 a 1978.
- **Posicionamento:** foto a 82% de altura com legenda de 16 px; datas em 36 px; card de 30 px de padding.
- **Prompt de imagem:** “Editorial wide-angle photograph of a historic colonial plaza in Rio de Janeiro, white stone palace, stone fountain, palm trees, soft morning light, no people, no text.”
- **Ícones:** nenhum.
- **Acessibilidade:** a foto é contextual; nenhuma informação depende dela.

### Slide 14 — Sete mecanismos de bastidor
- **Objetivo:** explicar *como* a rede funcionava.
- **Layout:** grade 4 + 3 com numerais 01–07 e folio `07` ao fundo.
- **Copy:** correspondência · neutralidade interna · sigilo e juramento · mobilidade · mutualismo · imprensa · liturgia cívica.
- **Posicionamento:** gutter 32 px; títulos de 28 px; descrições de 18 px.
- **Imagem:** não se aplica.
- **Ícones:** nenhum — o numeral é o ícone.
- **Acessibilidade:** a numeração é textual e sequencial.

### Slide 15 — Cinco limites
- **Objetivo:** impedir a leitura conspiracionista e a leitura apologética.
- **Layout:** cinco colunas com numeral, título e uma linha.
- **Copy:** sem comando único · maçons contra maçons · perseguição · captura pelo Estado · o palco decidia.
- **Posicionamento:** filetes de 2 px nos dois primeiros, 1 px nos demais; nota final em 16 px.
- **Imagem:** não se aplica.
- **Ícones:** nenhum.
- **Acessibilidade:** cada limite é um bloco autônomo.

### Slide 16 — Conclusão
- **Objetivo:** fixar a frase final.
- **Layout:** título em 132 px + card de números + nota de fonte.
- **Copy:** **Rede, não arquitetura.** · “A ordem produziu confiança, circulação de informação e repertório simbólico — não uma engenharia de poder.” · **4 atos · 12 marcos · 12 mitos · 38 fontes.**
- **Posicionamento:** título a 240 px do topo; card de 480 px à direita; nota de fonte a 120 px da base.
- **Imagem:** não se aplica.
- **Ícones:** nenhum.
- **Acessibilidade:** números tabulares; nota de fonte com contraste 4,6:1.

---

## 5. Quality checks

- [x] Fundo `#FFFFFF` em 16/16 slides; faixas fotográficas nunca invadem o rodapé.
- [x] Nenhuma cor de UI fora de `#111`, `#1A1A1A`, `#2B2B2E`, `#666B73`, `#D8DCE3`.
- [x] Numerais de folio em `#D8DCE3` usados como grafismo, nunca como texto informativo.
- [x] Nenhuma linha de grade visível; grid 12 colunas só na estrutura.
- [x] Escala 1,5× consistente entre canvas, margens e tipografia.
- [x] Fotografia sem texto, sem logos, sem filtros; máximo 60% × 70%.
- [x] Sem emojis, mascotes, confetti, glassmorphism, dark full-slide.
- [x] Navegação por teclado, `aria-live`, contraste ≥ 4,5:1, `prefers-reduced-motion`.

## 6. Exportar

`P` → Paisagem 16:9, margens “Nenhuma”, “Gráficos de fundo” ativado → PDF com 16 páginas em 1920×1080.
