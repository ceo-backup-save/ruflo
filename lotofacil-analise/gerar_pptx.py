# -*- coding: utf-8 -*-
"""Gera a apresentação 'Tema Luck' (.pptx) sobre o conjunto recomendado."""
import json
from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE
from pptx.chart.data import CategoryChartData
from pptx.enum.chart import XL_CHART_TYPE, XL_LEGEND_POSITION, XL_LABEL_POSITION

d = json.load(open("dados_recomendado.json"))

VERDE = RGBColor(0x00, 0x5C, 0x38)   # verde trevo
VERDE2 = RGBColor(0x00, 0x8C, 0x4F)
OURO = RGBColor(0xF2, 0xB7, 0x05)
CREME = RGBColor(0xFF, 0xFB, 0xEB)
CINZA = RGBColor(0x33, 0x33, 0x33)
BRANCO = RGBColor(0xFF, 0xFF, 0xFF)
VERM = RGBColor(0xC0, 0x2A, 0x2A)

prs = Presentation()
prs.slide_width = Inches(13.333)
prs.slide_height = Inches(7.5)
W, H = prs.slide_width, prs.slide_height
BLANK = prs.slide_layouts[6]


def bg(slide, color=CREME):
    r = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, W, H)
    r.fill.solid(); r.fill.fore_color.rgb = color
    r.line.fill.background(); r.shadow.inherit = False
    return r


def txt(slide, s, left, top, width, height, size=18, bold=False, color=CINZA,
        align=PP_ALIGN.LEFT, font="Trebuchet MS", anchor=MSO_ANCHOR.TOP, spacing=1.0):
    tb = slide.shapes.add_textbox(left, top, width, height)
    tf = tb.text_frame
    tf.word_wrap = True
    tf.vertical_anchor = anchor
    tf.margin_left = tf.margin_right = Emu(0)
    lines = s.split("\n")
    for i, line in enumerate(lines):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.alignment = align
        p.line_spacing = spacing
        run = p.add_run(); run.text = line
        f = run.font
        f.size = Pt(size); f.bold = bold; f.color.rgb = color; f.name = font
    return tb


def bar(slide, left, top, width, height, color):
    s = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
    s.fill.solid(); s.fill.fore_color.rgb = color
    s.line.fill.background(); s.shadow.inherit = False
    try:
        s.adjustments[0] = 0.15
    except Exception:
        pass
    return s


def header(slide, kicker, title, sub=None):
    bar(slide, Inches(0.7), Inches(0.55), Inches(0.11), Inches(1.05), OURO)
    txt(slide, kicker.upper(), Inches(0.95), Inches(0.5), Inches(11.5), Inches(0.3),
        size=12, bold=True, color=VERDE2)
    txt(slide, title, Inches(0.95), Inches(0.75), Inches(11.6), Inches(0.8),
        size=30, bold=True, color=VERDE)
    if sub:
        txt(slide, sub, Inches(0.95), Inches(1.5), Inches(11.6), Inches(0.5),
            size=14, color=CINZA)


def bullets(slide, items, left, top, width, size=17, gap=Inches(0.62)):
    for i, (icone, texto, cor) in enumerate(items):
        y = top + gap * i
        txt(slide, icone, left, y, Inches(0.4), Inches(0.4), size=size, bold=True,
            color=cor or VERDE2, align=PP_ALIGN.LEFT)
        txt(slide, texto, left + Inches(0.42), y, width - Inches(0.42), Inches(0.55),
            size=size, color=CINZA)


def tabela(slide, dados, left, top, width, altura_linha=Inches(0.36), size=12,
           cabecalho=VERDE, larguras=None):
    linhas, cols = len(dados), len(dados[0])
    shp = slide.shapes.add_table(linhas, cols, left, top, width, altura_linha * linhas).table
    if larguras:
        total = sum(larguras)
        for i, lw in enumerate(larguras):
            shp.columns[i].width = int(width * lw / total)
    for r in range(linhas):
        shp.rows[r].height = altura_linha
        for c in range(cols):
            cell = shp.cell(r, c)
            cell.text = str(dados[r][c])
            cell.margin_left = cell.margin_right = Inches(0.06)
            cell.margin_top = cell.margin_bottom = Inches(0.02)
            cell.vertical_anchor = MSO_ANCHOR.MIDDLE
            p = cell.text_frame.paragraphs[0]
            p.alignment = PP_ALIGN.CENTER if c else PP_ALIGN.LEFT
            f = p.runs[0].font
            f.size = Pt(size); f.name = "Trebuchet MS"
            if r == 0:
                f.bold = True; f.color.rgb = BRANCO
                cell.fill.solid(); cell.fill.fore_color.rgb = cabecalho
            else:
                f.color.rgb = CINZA
                cell.fill.solid()
                cell.fill.fore_color.rgb = BRANCO if r % 2 else RGBColor(0xF3, 0xF7, 0xF2)
    return shp


def cartao(slide, left, top, width, height, titulo, valor, cor=VERDE, sub=None):
    c = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
    c.fill.solid(); c.fill.fore_color.rgb = BRANCO
    c.line.color.rgb = RGBColor(0xDD, 0xE5, 0xDA); c.line.width = Pt(1)
    c.shadow.inherit = False
    txt(slide, titulo, left + Inches(0.25), top + Inches(0.18), width - Inches(0.5), Inches(0.3),
        size=12, bold=True, color=RGBColor(0x77, 0x88, 0x7C))
    txt(slide, valor, left + Inches(0.25), top + Inches(0.48), width - Inches(0.5), Inches(0.55),
        size=25, bold=True, color=cor)
    if sub:
        txt(slide, sub, left + Inches(0.25), top + Inches(1.06), width - Inches(0.5),
            Inches(0.3), size=10.5, color=CINZA)
    return c


# ============ 1. CAPA ============
s = prs.slides.add_slide(BLANK)
bg(s, VERDE)
# trevos decorativos
for (l, t, sz, cor) in [(Inches(10.6), Inches(0.5), Inches(2.2), VERDE2),
                        (Inches(11.9), Inches(4.3), Inches(1.3), VERDE2),
                        (Inches(-0.4), Inches(5.6), Inches(1.9), VERDE2)]:
    sh = s.shapes.add_shape(MSO_SHAPE.TEAR, l, t, sz, sz)
    sh.rotation = 225
    sh.fill.solid(); sh.fill.fore_color.rgb = cor
    sh.line.fill.background(); sh.shadow.inherit = False
bar(s, Inches(0.9), Inches(2.05), Inches(0.16), Inches(1.5), OURO)
txt(s, "TEMA  LUCK", Inches(1.25), Inches(1.95), Inches(8), Inches(0.4),
    size=15, bold=True, color=OURO)
txt(s, "Conjunto\nRecomendado", Inches(1.25), Inches(2.35), Inches(9), Inches(2.0),
    size=54, bold=True, color=BRANCO, spacing=0.95)
txt(s, "Paridade 7/8  +  faixa natural 9–10", Inches(1.28), Inches(4.35), Inches(9), Inches(0.5),
    size=22, color=RGBColor(0xC8, 0xE6, 0xD3))
bar(s, Inches(1.28), Inches(5.15), Inches(3.4), Inches(0.06), OURO)
txt(s, "20 jogos · fixa 06-12 · excluída 04-10\nBase: 100 últimos concursos (3726–3825) · Lotofácil",
    Inches(1.28), Inches(5.45), Inches(9), Inches(0.9), size=14,
    color=RGBColor(0x9F, 0xC7, 0xB2))
txt(s, "Novembro de 2026", Inches(1.28), Inches(6.6), Inches(5), Inches(0.35),
    size=12, color=RGBColor(0x7F, 0xA8, 0x92))

# ============ 2. O QUE É ============
s = prs.slides.add_slide(BLANK); bg(s)
header(s, "Ponto de partida", "O que é o conjunto recomendado",
       "Cinco regras simples — e nenhuma delas é obrigatória para ganhar.")
regras = [
    ("1", "Sempre contém a dupla fixa   06 - 12"),
    ("2", "Nunca contém a dupla excluída   04 - 10"),
    ("3", "7 pares ou 8 pares  (8 ou 7 ímpares)"),
    ("4", "9 ou 10 dezenas entre 1 e 16"),
    ("5", "As 13 restantes vêm das dezenas mais frequentes"),
]
for i, (n, t) in enumerate(regras):
    y = Inches(2.15) + Inches(0.82) * i
    c = s.shapes.add_shape(MSO_SHAPE.OVAL, Inches(1.0), y, Inches(0.55), Inches(0.55))
    c.fill.solid(); c.fill.fore_color.rgb = VERDE if i < 2 else OURO
    c.line.fill.background(); c.shadow.inherit = False
    txt(s, n, Inches(1.0), y + Inches(0.09), Inches(0.55), Inches(0.4), size=17, bold=True,
        color=BRANCO, align=PP_ALIGN.CENTER)
    txt(s, t, Inches(1.75), y + Inches(0.08), Inches(9.4), Inches(0.5), size=19, color=CINZA)
txt(s, "Resultado: 20 jogos de 15 dezenas, R$ 70,00 por concurso.",
    Inches(1.0), Inches(6.45), Inches(11), Inches(0.4), size=15, bold=True, color=VERDE)

# ============ 3. POR QUE 7/8 e 9/10 ============
s = prs.slides.add_slide(BLANK); bg(s)
header(s, "A justificativa", "Por que 7/8 de paridade e 9/10 de faixa",
       "Tudo sai da estrutura do jogo: 13 ímpares, 12 pares, 16 dezenas até 16 e 9 acima.")
tabela(s, [
    ["Critério", "Esperado pela estrutura", "Ocorreu em 100 concursos", "Veredito"],
    ["7 ou 8 pares", "7,2 pares", f"{d['p7ou8_pares']} concursos", "✅ padrão real"],
    ["9 ou 10 dezenas em 1–16", "9,6 dezenas", f"{d['p9ou10_faixa']} concursos", "✅ padrão real"],
    ["7 ou 8 dezenas em 1–16", "9,6 dezenas", f"{d['p78_faixa']} concursos", "⚠️ atípico"],
], Inches(0.95), Inches(2.2), Inches(11.4), altura_linha=Inches(0.5), size=13,
   larguras=[3.2, 2.8, 3.0, 2.2])
txt(s, "Contas que explicam os números",
    Inches(0.95), Inches(4.55), Inches(6), Inches(0.35), size=15, bold=True, color=VERDE)
for i, t in enumerate([
    "Pares esperados = 15 × 12/25 = 7,2  →  7 ou 8 pares é o centro da distribuição",
    "Dezenas em 1–16 esperadas = 15 × 16/25 = 9,6  →  9 ou 10 é o centro",
    "Pedir 7/8 em 1–16 é pedir o contrário da estrutura: só 16% dos concursos",
]):
    txt(s, "•  " + t, Inches(0.95), Inches(5.0) + Inches(0.5) * i, Inches(11.4), Inches(0.45),
        size=14, color=CINZA)

# ============ 3b. DISTRIBUIÇÕES (gráficos) ============
s = prs.slides.add_slide(BLANK); bg(s)
header(s, "Os dados por trás da regra", "Como os sorteios realmente se distribuem",
       "100 concursos (3726–3825): paridade e faixa de dezenas em 1–16")

cd = CategoryChartData()
cd.categories = [f"{k} pares" for k in sorted(d["dist_pares"], key=int)]
cd.add_series("Concursos", [d["dist_pares"][k] for k in sorted(d["dist_pares"], key=int)])
gf = s.shapes.add_chart(XL_CHART_TYPE.COLUMN_CLUSTERED, Inches(0.9), Inches(2.05),
                        Inches(5.7), Inches(4.1), cd)
ch = gf.chart
ch.has_legend = False
ch.has_title = True
ch.chart_title.text_frame.text = "Quantos pares saíram em cada concurso"
ch.chart_title.text_frame.paragraphs[0].runs[0].font.size = Pt(13)
ch.chart_title.text_frame.paragraphs[0].runs[0].font.bold = True
ch.chart_title.text_frame.paragraphs[0].runs[0].font.color.rgb = VERDE
pl = ch.plots[0]
pl.gap_width = 40
pl.has_data_labels = True
pl.data_labels.font.size = Pt(11)
pl.data_labels.position = XL_LABEL_POSITION.OUTSIDE_END
ser = pl.series[0]
for i, k in enumerate(sorted(d["dist_pares"], key=int)):
    pt = ser.points[i]
    pt.format.fill.solid()
    pt.format.fill.fore_color.rgb = OURO if k in (7, 8) else RGBColor(0xA8, 0xC8, 0xB4)
ch.value_axis.has_major_gridlines = False
ch.value_axis.visible = False
ch.category_axis.tick_labels.font.size = Pt(10)

cd2 = CategoryChartData()
cd2.categories = [f"{k}" for k in sorted(d["dist_faixa"], key=int)]
cd2.add_series("Concursos", [d["dist_faixa"][k] for k in sorted(d["dist_faixa"], key=int)])
gf2 = s.shapes.add_chart(XL_CHART_TYPE.COLUMN_CLUSTERED, Inches(6.8), Inches(2.05),
                         Inches(5.6), Inches(4.1), cd2)
ch2 = gf2.chart
ch2.has_legend = False
ch2.has_title = True
ch2.chart_title.text_frame.text = "Quantas dezenas de 1 a 16 saíram"
ch2.chart_title.text_frame.paragraphs[0].runs[0].font.size = Pt(13)
ch2.chart_title.text_frame.paragraphs[0].runs[0].font.bold = True
ch2.chart_title.text_frame.paragraphs[0].runs[0].font.color.rgb = VERDE
pl2 = ch2.plots[0]
pl2.gap_width = 40
pl2.has_data_labels = True
pl2.data_labels.font.size = Pt(11)
pl2.data_labels.position = XL_LABEL_POSITION.OUTSIDE_END
ser2 = pl2.series[0]
for i, k in enumerate(sorted(d["dist_faixa"], key=int)):
    pt = ser2.points[i]
    pt.format.fill.solid()
    pt.format.fill.fore_color.rgb = OURO if k in (9, 10) else RGBColor(0xA8, 0xC8, 0xB4)
ch2.value_axis.has_major_gridlines = False
ch2.value_axis.visible = False
ch2.category_axis.tick_labels.font.size = Pt(10)

txt(s, "Em dourado, as faixas escolhidas pelo conjunto recomendado: 7–8 pares e 9–10 dezenas em 1–16.",
    Inches(0.95), Inches(6.35), Inches(11.4), Inches(0.4), size=12.5, color=CINZA)

# ============ 4. A VERDADE ============
s = prs.slides.add_slide(BLANK); bg(s, RGBColor(0xFF, 0xF6, 0xDA))
header(s, "Transparência", "O equilíbrio não aumenta a chance",
       "Qualquer jogo de 15 dezenas tem exatamente as mesmas probabilidades.")
tabela(s, [
    ["Acertos", "Chance por jogo", "1 em…"],
    ["11", "8,7694%", "11,4"],
    ["12", "1,6704%", "59,9"],
    ["13", "0,1446%", "691,5"],
    ["14", "0,0046%", "21.792"],
    ["15", "0,000031%", "3.268.760"],
], Inches(0.95), Inches(2.05), Inches(5.5), altura_linha=Inches(0.42), size=13)
bar(s, Inches(7.0), Inches(2.05), Inches(5.35), Inches(2.55), BRANCO)
txt(s, "Prova em 200.000 sorteios simulados", Inches(7.3), Inches(2.25), Inches(4.8), Inches(0.35),
    size=14, bold=True, color=VERDE)
for i, (rot, a, b) in enumerate([("11 acertos", "8,862%", "8,857%"),
                                ("12 acertos", "1,644%", "1,720%"),
                                ("13 acertos", "0,142%", "0,163%")]):
    y = Inches(2.75) + Inches(0.55) * i
    txt(s, rot, Inches(7.3), y, Inches(1.5), Inches(0.35), size=13, color=CINZA)
    txt(s, a, Inches(8.9), y, Inches(1.1), Inches(0.35), size=13, bold=True, color=VERDE,
        align=PP_ALIGN.CENTER)
    txt(s, b, Inches(10.1), y, Inches(1.1), Inches(0.35), size=13, bold=True, color=VERM,
        align=PP_ALIGN.CENTER)
txt(s, "equilibrado     livre", Inches(8.85), Inches(4.15), Inches(2.4), Inches(0.3),
    size=10, color=RGBColor(0x88, 0x88, 0x88), align=PP_ALIGN.CENTER)
txt(s, "O equilíbrio apenas CONCENTRA a aposta num tipo de sorteio.\nComo o prêmio é o mesmo em qualquer tipo, a conta final não muda.",
    Inches(0.95), Inches(5.05), Inches(11.4), Inches(0.9), size=16, color=RGBColor(0x7A, 0x4A, 0x00))

# ============ 5. COMO AS 13 SÃO ESCOLHIDAS ============
s = prs.slides.add_slide(BLANK); bg(s)
header(s, "Seleção", "De onde vêm as 13 dezenas restantes",
       "Fixa (06, 12) dentro · excluída (04, 10) fora · 21 dezenas disponíveis · 13 escolhidas")
tabela(s, [["Dezena", "Frequência em 100"]] + [[f"{dz:02d}", str(f)] for dz, f in d["freq"][:8]],
       Inches(0.95), Inches(2.15), Inches(4.6), altura_linha=Inches(0.4), size=12,
       larguras=[1, 1.6])
txt(s, "+ as demais 10 dezenas disponíveis, com peso menor",
    Inches(0.95), Inches(5.65), Inches(4.8), Inches(0.6), size=11, color=CINZA)
for i, (t, sub) in enumerate([
    ("Sorteio ponderado", "Cada dezena entra com peso = sua frequência nos 100 concursos."),
    ("Rejeição", "Se o jogo não cumprir 7/8 pares e 9/10 na faixa, o sorteio é repetido."),
    ("Aviso", "Frequência é passado, não previsão: no próximo concurso toda dezena tem 60%."),
]):
    y = Inches(2.15) + Inches(1.45) * i
    cor = VERM if t == "Aviso" else VERDE2
    txt(s, t, Inches(6.2), y, Inches(6.1), Inches(0.4), size=17, bold=True, color=cor)
    txt(s, sub, Inches(6.2), y + Inches(0.42), Inches(6.1), Inches(0.8), size=14, color=CINZA)

# ============ 6. OS 20 JOGOS (parte 1) ============
for parte, ini, fim in [("1 de 2", 0, 10), ("2 de 2", 10, 20)]:
    s = prs.slides.add_slide(BLANK); bg(s)
    header(s, f"Os jogos · parte {parte}", "20 jogos prontos para apostar",
           "Todos contêm 06 e 12 · nenhum contém 04 ou 10 · paridade 7/8 · faixa 9/10")
    linhas = [["#", "Jogo (15 dezenas)", "Pares/Ímpares", "1–16 / 17–25"]]
    for i in range(ini, fim):
        p, im, f1, f2 = d["stats"][i]
        linhas.append([str(i + 1), d["jogos"][i], f"{p}/{im}", f"{f1}/{f2}"])
    tabela(s, linhas, Inches(0.95), Inches(2.1), Inches(11.4), altura_linha=Inches(0.4), size=12,
           larguras=[0.5, 7.2, 1.6, 1.8])

# ============ 7. CUSTO E RETORNO ============
s = prs.slides.add_slide(BLANK); bg(s)
header(s, "Dinheiro", "Quanto custa e quanto volta",
       "20 jogos × R$ 3,50 = R$ 70,00 por concurso")
cartao(s, Inches(0.95), Inches(2.1), Inches(3.6), Inches(1.5), "CUSTO POR CONCURSO",
       "R$ 70,00", VERM, "R$ 210,00 por semana (3 sorteios)")
cartao(s, Inches(4.85), Inches(2.1), Inches(3.6), Inches(1.5), "RETORNO ESPERADO (realista)",
       "≈ R$ 21,91", VERDE, "31,3% do custo")
cartao(s, Inches(8.75), Inches(2.1), Inches(3.6), Inches(1.5), "PREJUÍZO ESPERADO",
       "≈ –R$ 48,09", VERM, "por concurso, no longo prazo")
tabela(s, [
    ["Cenário de prêmios", "Retorno por jogo", "20 jogos", "Retorno", "Prejuízo"],
    ["Ilustrativo (14 = R$ 1.500 · 15 = R$ 2 mi)", "R$ 1,579", "R$ 31,58", "45,1%", "–R$ 38,42"],
    ["Rateio realista (14 = R$ 1.300 · 15 = R$ 450 mil)", "R$ 1,096", "R$ 21,91", "31,3%", "–R$ 48,09"],
    ["Sem 14/15 (só prêmios fixos)", "R$ 0,898", "R$ 17,96", "25,7%", "–R$ 52,04"],
], Inches(0.95), Inches(4.0), Inches(11.4), altura_linha=Inches(0.55), size=12,
   larguras=[5.2, 2.0, 1.6, 1.2, 1.6])
txt(s, "A Caixa devolve 43,35% da arrecadação em prêmios. Prêmios de 14 e 15 acertos são rateados — por isso o número realista é 30%, não 45%.",
    Inches(0.95), Inches(6.5), Inches(11.4), Inches(0.6), size=12, color=RGBColor(0x77, 0x77, 0x77))

# ============ 8. SIMULAÇÃO ============
s = prs.slides.add_slide(BLANK); bg(s)
header(s, "O que esperar na prática", "20.000 concursos simulados",
       "O conjunto de 20 jogos, jogado repetidamente, com prêmios realistas de rateio")
cartao(s, Inches(0.95), Inches(2.15), Inches(2.7), Inches(1.45), "SALDO MÉDIO",
       f"–R$ {abs(d['mc']['media']):.0f}", VERM)
cartao(s, Inches(3.82), Inches(2.15), Inches(2.7), Inches(1.45), "SALDO MEDIANO",
       f"–R$ {abs(d['mc']['mediana']):.0f}", VERM)
cartao(s, Inches(6.69), Inches(2.15), Inches(2.7), Inches(1.45), "5% MELHORES",
       f"–R$ {abs(d['mc']['p95']):.0f}", VERDE)
cartao(s, Inches(9.56), Inches(2.15), Inches(2.7), Inches(1.45), "CHANCE DE LUCRO",
       f"{d['mc']['lucro_pct']:.1f}%", VERM, "em um concurso")
txt(s, "Como ler", Inches(0.95), Inches(3.85), Inches(5), Inches(0.35), size=15, bold=True, color=VERDE)
for i, t in enumerate([
    f"Em ~{100 - d['mc']['lucro_pct']:.1f}% dos concursos o conjunto devolve menos do que custou.",
    "O lucro, quando aparece (~2,3%), vem quase sempre de um único acerto de 14.",
    "O maior saldo positivo observado foi de +R$ 1.307 — e não se repete.",
    "Pior caso: perder os R$ 70 inteiros. Acontece com frequência.",
]):
    txt(s, "•  " + t, Inches(0.95), Inches(4.3) + Inches(0.5) * i, Inches(11.4), Inches(0.45),
        size=14, color=CINZA)
txt(s, "Conclusão: entretenimento com custo conhecido — não investimento.",
    Inches(0.95), Inches(6.55), Inches(11.4), Inches(0.4), size=15, bold=True, color=VERM)

# ============ 9. COMO USAR ============
s = prs.slides.add_slide(BLANK); bg(s)
header(s, "Roteiro", "Como usar o conjunto na prática", "Seis passos, na ordem")
passos = [
    ("Defina o orçamento do mês", "Trate como lazer. Nunca aumente após perder — isso é perseguir prejuízo."),
    ("Escolha fixa e excluída antes do sorteio", "Aqui: 06-12 fixa, 04-10 fora. Não mude no meio do caminho."),
    ("Confira cada jogo", "7/8 pares e 9/10 em 1–16. Se um jogo fugir, troque uma dezena."),
    ("Não complete com a excluída", "04 e 10 ficam fora de todos os 20 jogos, sem exceção."),
    ("Revise a cada 25 concursos", "Recalcule a prevalência e regenere as 13 dezenas."),
    ("Registre custo e prêmio", "Comparar com o custo é o único jeito de não se enganar com um 13 isolado."),
]
for i, (t, sub) in enumerate(passos):
    col = i % 2
    lin = i // 2
    x = Inches(0.95) + Inches(6.05) * col
    y = Inches(2.1) + Inches(1.55) * lin
    bar(s, x, y + Inches(0.05), Inches(0.07), Inches(1.15), OURO)
    txt(s, f"{i+1}.  {t}", x + Inches(0.25), y, Inches(5.6), Inches(0.4), size=15, bold=True,
        color=VERDE)
    txt(s, sub, x + Inches(0.25), y + Inches(0.42), Inches(5.5), Inches(0.8), size=12.5,
        color=CINZA)

# ============ 10. RESUMO ============
s = prs.slides.add_slide(BLANK); bg(s, VERDE)
txt(s, "RESUMO", Inches(0.95), Inches(0.65), Inches(6), Inches(0.4), size=14, bold=True, color=OURO)
txt(s, "O conjunto em 8 linhas", Inches(0.95), Inches(1.0), Inches(11), Inches(0.7), size=32,
    bold=True, color=BRANCO)
itens = [
    ("Fixa", "06-12 — dupla cruzada mais frequente (43%)"),
    ("Excluída", "04-10 — 28%, disjunta da fixa"),
    ("Jogos", "20 de 15 dezenas · R$ 70,00 por concurso"),
    ("Paridade", "7/8 pares — 56% dos concursos reais"),
    ("Faixa", "9/10 em 1–16 — 54% dos concursos reais"),
    ("Retorno esperado", "≈ 30% (realista) · prejuízo ≈ R$ 48/concurso"),
    ("Chance de lucro", "≈ 2,3% em um concurso"),
    ("Chance de 15 acertos", "1 em 3.268.760 — em qualquer jogo"),
]
for i, (k, v) in enumerate(itens):
    y = Inches(2.05) + Inches(0.58) * i
    txt(s, k, Inches(0.95), y, Inches(3.0), Inches(0.4), size=14, bold=True,
        color=RGBColor(0x9F, 0xC7, 0xB2))
    txt(s, v, Inches(4.0), y, Inches(8.4), Inches(0.4), size=15, color=BRANCO)
bar(s, Inches(0.95), Inches(6.85), Inches(11.4), Inches(0.05), OURO)

# ============ 11. FECHAMENTO ============
s = prs.slides.add_slide(BLANK); bg(s, RGBColor(0xFF, 0xF6, 0xDA))
sh = s.shapes.add_shape(MSO_SHAPE.TEAR, Inches(0.9), Inches(0.85), Inches(0.9), Inches(0.9))
sh.rotation = 225
sh.fill.solid(); sh.fill.fore_color.rgb = VERDE
sh.line.fill.background(); sh.shadow.inherit = False
txt(s, "Boa sorte — com os pés no chão", Inches(2.0), Inches(0.95), Inches(10), Inches(0.7),
    size=30, bold=True, color=VERDE)
txt(s, "Este material é educativo e usa dados públicos dos 100 últimos concursos da Lotofácil\n(3726 a 3825, julho a novembro de 2026). Não é recomendação de investimento.",
    Inches(1.0), Inches(2.4), Inches(11.3), Inches(0.9), size=16, color=CINZA)
tabela(s, [
    ["O que a técnica faz", "O que ela NÃO faz"],
    ["Organiza os jogos com critério claro", "Não aumenta a chance de acertar"],
    ["Evita buracos na aposta (fixa/excluída)", "Não prevê dezenas futuras"],
    ["Garante jogos no padrão típico de paridade", "Não vira retorno positivo: 43,35% volta"],
    ["Dá um roteiro de disciplina e orçamento", "Não substitui a sorte — nem a matemática"],
], Inches(1.0), Inches(3.55), Inches(11.3), altura_linha=Inches(0.55), size=13,
   larguras=[1, 1])
txt(s, "Jogue só o que pode perder. O resto é conversa de sorte.",
    Inches(1.0), Inches(6.5), Inches(11.3), Inches(0.5), size=17, bold=True, color=VERM)

NOTAS = [
 "Capa. Apresente o tema: um jeito organizado de montar 20 jogos, com critério estatístico explícito — e honestidade sobre o que isso NÃO faz.",
 "As cinco regras. Reforce: nenhuma delas é condição para ganhar; são filtros de organização. A fixa 06-12 é a dupla cruzada mais frequente (43%).",
 "A justificativa matemática. 13 ímpares e 12 pares → 7,2 pares esperados. 16 dezenas até 16 e 9 acima → 9,6 esperadas em 1–16.",
 "Gráficos. Mostre que a distribuição tem um centro: 7–8 pares (56 concursos) e 9–10 em 1–16 (54 concursos). As faixas douradas são o centro, não a cauda.",
 "Ponto de honestidade: qualquer jogo de 15 tem a MESMA chance. Simulação de 200 mil sorteios confirma 8,86% para 11 acertos nos dois casos.",
 "De onde vêm as 13 restantes: sorteio ponderado pela frequência, com rejeição até cumprir paridade e faixa. Aviso: frequência é passado, não previsão.",
 "Primeira metade dos 20 jogos. Convide a conferir: todos têm 06 e 12, nenhum tem 04 ou 10, todos com 7/8 pares e 9/10 na faixa.",
 "Segunda metade dos jogos. Custo total: R$ 70,00 por concurso.",
 "Economia: R$ 70,00 por concurso, retorno realista ~31%, prejuízo esperado ~R$ 48. Explique o rateio dos prêmios de 14 e 15.",
 "Simulação de 20 mil concursos: saldo médio negativo, lucro em apenas 2,3% dos concursos, quase sempre por um único 14.",
 "Roteiro prático. O item mais importante é o primeiro: orçamento fechado antes de apostar.",
 "Resumo em oito linhas — bom slide para foto.",
 "Fechamento. Deixe claro: o que a técnica faz e o que ela não faz. Jogue só o que pode perder.",
]
for sl, nota in zip(prs.slides, NOTAS):
    sl.notes_slide.notes_text_frame.text = nota

prs.save("Apresentacao_Luck_Conjunto_Recomendado.pptx")
print("slides:", len(prs.slides))
