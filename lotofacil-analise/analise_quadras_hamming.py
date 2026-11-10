#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Lista 1 (mantida): últimos 100 concursos 3726..3825.
Lista 2 (nova): quadras (4 dezenas) formadas APENAS por dezenas pares de 1 a 25,
  com análise de distância de Hamming.

Definições adotadas (explícitas e didáticas):
  - Dezenas pares em 1..25: 02,04,06,08,10,12,14,16,18,20,22,24 (12 dezenas)
  - Quadras: todas as combinações de 4 em 4 dessas 12 -> C(12,4) = 495 quadras
  - Cada quadra é um vetor binário de 12 posições (1 = dezena par presente na quadra)
  - Distância de Hamming entre duas quadras = nº de posições em que os vetores diferem
      = 2 * (4 - |interseção|)
    Logo:
      distância 2  <=> compartilham exatamente 3 dezenas (trocam 1 dezena)
      distância 4  <=> compartilham exatamente 2 dezenas
      distância 6  <=> compartilham exatamente 1 dezena
      distância 8  <=> não compartilham nenhuma dezena
  - "Quadras com Hamming distância 2" = vizinhas da quadra de referência:
    4 escolhas de qual dezena sai x 8 escolhas de qual dezena entra = 32 vizinhas.
  - Presença de uma quadra em um concurso da Lista 1 = as 4 dezenas pares estão
    TODAS entre as 15 sorteadas. Esperado teórico: (15/25)*(14/24)*(13/23)*(12/22)
    = 10,79% -> ~10,8 concursos em 100.
"""
import csv
import html
import itertools
from collections import Counter
from math import comb
from pathlib import Path

from analise_lotofacil import CONCURSOS

BASE = Path(__file__).resolve().parent
ULTIMO = CONCURSOS[-1][0]
N = len(CONCURSOS)
PARES = list(range(2, 26, 2))  # 12 evens
QUADRAS = list(itertools.combinations(PARES, 4))  # 495


def fmt(t):
    return " ".join(f"{d:02d}" for d in t)


def hamming(a, b):
    return 2 * (4 - len(set(a) & set(b)))


def main():
    assert len(PARES) == 12 and len(QUADRAS) == 495

    # ---- presença das quadras na Lista 1 ----
    contagem = Counter()
    ultimo = {}
    for num, data, sorteio in CONCURSOS:
        s = set(sorteio)
        for q in QUADRAS:
            if set(q) <= s:
                contagem[q] += 1
                ultimo[q] = num

    linhas = []
    for q in QUADRAS:
        cnt = contagem.get(q, 0)
        ult = ultimo.get(q)
        linhas.append({
            "quadra": q, "ocorrencias": cnt, "percentual": cnt / N * 100,
            "ultimo": ult, "atraso": (ULTIMO - ult) if ult is not None else None,
        })
    linhas.sort(key=lambda x: (-x["ocorrencias"], x["quadra"]))
    referencia = linhas[0]["quadra"]

    for r in linhas:
        r["dist_ref"] = hamming(r["quadra"], referencia)
        r["inter_ref"] = len(set(r["quadra"]) & set(referencia))

    vizinhas_d2 = [r for r in linhas if r["dist_ref"] == 2]
    vizinhas_d2.sort(key=lambda x: (-x["ocorrencias"], x["quadra"]))
    assert len(vizinhas_d2) == 32, len(vizinhas_d2)

    # ---- por concurso: pares presentes e quadras cobertas ----
    por_concurso = []
    total_presencas = 0
    dist_m = Counter()
    for num, data, sorteio in CONCURSOS:
        pares_no = sorted(d for d in sorteio if d in PARES)
        m = len(pares_no)
        dist_m[m] += 1
        cobertas = comb(m, 4) if m >= 4 else 0
        total_presencas += cobertas
        por_concurso.append((num, data, sorteio, pares_no, cobertas))
    media_cobertas = total_presencas / N

    # ---- co-ocorrência de pares de evens (para heatmap 12x12) ----
    cooc = Counter()
    for num, data, sorteio in CONCURSOS:
        pares_no = [d for d in sorteio if d in PARES]
        for a, b in itertools.combinations(sorted(pares_no), 2):
            cooc[(a, b)] += 1

    # ---- CSV ----
    with open(BASE / "ranking_quadras_pares.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f, delimiter=";")
        w.writerow(["quadra", "ocorrencias_em_100", "percentual_%", "ultimo_concurso", "atraso_concursos",
                    "distancia_hamming_da_referencia", "intersecao_com_referencia"])
        for r in linhas:
            w.writerow([fmt(r["quadra"]), r["ocorrencias"], f"{r['percentual']:.1f}".replace(".", ","),
                        r["ultimo"] or "", r["atraso"] if r["atraso"] is not None else "",
                        r["dist_ref"], r["inter_ref"]])

    top20 = linhas[:20]
    bottom20 = sorted(linhas, key=lambda x: (x["ocorrencias"], x["quadra"]))[:20]
    esperado = (15/25) * (14/24) * (13/23) * (12/22) * 100

    # ================= MD didático =================
    L = []
    L.append("# Lista 1 × Lista 2 — Quadras pares (1–25) e distância de Hamming 2")
    L.append("")
    L.append("**Lista 1 (mantida):** últimos 100 concursos **3726–3825** (número + 15 dezenas) — ver `lista1_ultimos_100_concursos.csv` e `relatorio.md`.")
    L.append("**Lista 2 (nova):** quadras (4 dezenas) formadas **apenas por dezenas pares de 1 a 25**: 02, 04, 06, 08, 10, 12, 14, 16, 18, 20, 22, 24 → **C(12,4) = 495 quadras**.")
    L.append("")
    L.append("## Passo a passo (didático)")
    L.append("")
    L.append("**Passo 1 — O que é uma quadra par?** Uma quadra é só um grupo de 4 dezenas pares, ex.: `02 04 06 08`. Há 495 grupos possíveis com as 12 pares.")
    L.append("")
    L.append("**Passo 2 — O que é distância de Hamming?** Escreva cada quadra como 12 posições (uma por dezena par, na ordem 02,04,…,24), com 1 onde a dezena está na quadra e 0 onde não está. A distância de Hamming entre duas quadras é **em quantas posições elas diferem**.")
    L.append("")
    L.append("Exemplo com a quadra de referência (a mais frequente nos 100 concursos):")
    L.append("")
    L.append(f"- Referência: **{fmt(referencia)}**")
    L.append("- Vetor binário (02,04,06,08,10,12,14,16,18,20,22,24): " +
             " ".join("1" if d in referencia else "0" for d in PARES))
    # exemplo de vizinha distância 2
    viz_ex = vizinhas_d2[0]["quadra"]
    L.append(f"- Vizinhança distância 2 (ex.): **{fmt(viz_ex)}** — compartilha 3 dezenas com a referência, troca 1 (sai uma, entra outra) → vetor difere em **2 posições** → Hamming = 2.")
    L.append("- Distância 4 = compartilha 2 dezenas (troca 2). Distância 6 = compartilha 1. Distância 8 = compartilha 0.")
    L.append("")
    L.append("**Passo 3 — Quantas quadras estão a distância 2 da referência?** 4 escolhas de qual dezena sai × 8 escolhas de qual entra = **32 vizinhas**. São elas que a Lista 2 destaca como “quadras com Hamming distância 2”.")
    L.append("")
    L.append("**Passo 4 — Comparação Lista 1 × Lista 2:** uma quadra “aparece” em um concurso quando suas 4 dezenas pares estão todas nas 15 sorteadas. Cada concurso cobre C(m,4) quadras, onde m = nº de pares sorteados naquele concurso (média ~7,2 pares; como C(m,4) cresce rápido, a média real é 43,7 quadras por concurso — ver cobertura abaixo).")
    L.append("")
    L.append("---")
    L.append("")
    L.append(f"## Resultado — quadras mais presentes (esperado ~{esperado:.1f} em 100)")
    L.append("")
    L.append(f"Quadra de referência (mais frequente): **{fmt(referencia)}** — {linhas[0]['ocorrencias']} concursos ({linhas[0]['percentual']:.0f}%).")
    L.append("")
    L.append("| # | Quadra | Ocorrências | % | Dist. Hamming da ref. |")
    L.append("|---:|---|---:|---:|---:|")
    for i, r in enumerate(top20, 1):
        L.append(f"| {i} | {fmt(r['quadra'])} | {r['ocorrencias']} | {r['percentual']:.0f}% | {r['dist_ref']} |")
    L.append("")
    L.append("## Quadras menos presentes")
    L.append("")
    L.append("| # | Quadra | Ocorrências | % | Dist. Hamming da ref. |")
    L.append("|---:|---|---:|---:|---:|")
    for i, r in enumerate(bottom20, 1):
        L.append(f"| {i} | {fmt(r['quadra'])} | {r['ocorrencias']} | {r['percentual']:.0f}% | {r['dist_ref']} |")
    L.append("")
    L.append("## As 32 vizinhas a distância 2 da referência")
    L.append("")
    L.append("| # | Quadra vizinha (dist. 2) | Ocorrências | % |")
    L.append("|---:|---|---:|---:|")
    for i, r in enumerate(vizinhas_d2, 1):
        L.append(f"| {i} | {fmt(r['quadra'])} | {r['ocorrencias']} | {r['percentual']:.0f}% |")
    L.append("")
    L.append(f"**Cobertura por concurso:** total de presenças de quadras na Lista 1 = {total_presencas} (média de {media_cobertas:.1f} quadras cobertas por concurso). Distribuição de m (pares por concurso): " +
             ", ".join(f"m={m}: {dist_m[m]} concursos" for m in sorted(dist_m)) + ".")
    L.append("")
    L.append("> ⚠️ Como nas trincas: a quadra mais frequente no passado não tem mais chance no próximo concurso (continua ~10,8% teórica para qualquer quadra específica). Distância de Hamming organiza a similaridade entre quadras — não aumenta a chance de acerto.")
    L.append("")
    L.append("## Arquivos")
    L.append("")
    L.append("- `ranking_quadras_pares.csv` — 495 quadras com ocorrências, %, último concurso, atraso e distância de Hamming da referência.")
    L.append("- `relatorio_quadras_hamming.html` — versão visual e didática (gráficos, heatmap, Lista 1 com pares destacados).")
    L.append("- `analise_quadras_hamming.py` — script reproduzível.")
    L.append("")
    (BASE / "relatorio_quadras_hamming.md").write_text("\n".join(L), encoding="utf-8")

    # ================= HTML visual =================
    def barra(valor, maxv, cor):
        pct = (valor / maxv * 100) if maxv else 0
        return f'<div class="bar"><span class="barfill" style="width:{pct:.1f}%;background:{cor}"></span></div>'

    max_top = top20[0]["ocorrencias"]
    max_bot = bottom20[-1]["ocorrencias"] if bottom20 else 1

    def linhas_tabela_top():
        out = []
        for i, r in enumerate(top20, 1):
            out.append(f'<tr><td>{i}</td><td class="mono"><b>{fmt(r["quadra"])}</b></td>'
                       f'<td>{r["ocorrencias"]}</td><td>{r["percentual"]:.0f}%</td>'
                       f'<td>{barra(r["ocorrencias"], max_top, "#2563eb")}</td>'
                       f'<td>{r["dist_ref"]}</td></tr>')
        return "\n".join(out)

    def linhas_tabela_bottom():
        out = []
        for i, r in enumerate(bottom20, 1):
            out.append(f'<tr><td>{i}</td><td class="mono"><b>{fmt(r["quadra"])}</b></td>'
                       f'<td>{r["ocorrencias"]}</td><td>{r["percentual"]:.0f}%</td>'
                       f'<td>{barra(r["ocorrencias"], max_bot, "#dc2626")}</td>'
                       f'<td>{r["dist_ref"]}</td></tr>')
        return "\n".join(out)

    def linhas_vizinhas():
        out = []
        for i, r in enumerate(vizinhas_d2, 1):
            sai = [d for d in referencia if d not in r["quadra"]]
            entra = [d for d in r["quadra"] if d not in referencia]
            out.append(f'<tr><td>{i}</td><td class="mono"><b>{fmt(r["quadra"])}</b></td>'
                       f'<td>sai {sai[0]:02d} → entra {entra[0]:02d}</td>'
                       f'<td>{r["ocorrencias"]}</td><td>{r["percentual"]:.0f}%</td></tr>')
        return "\n".join(out)

    def linhas_lista1():
        out = []
        for num, data, sorteio, pares_no, cobertas in por_concurso:
            cels = []
            for d in sorteio:
                if d in PARES:
                    cels.append(f'<span class="par">{d:02d}</span>')
                else:
                    cels.append(f'<span class="impar">{d:02d}</span>')
            out.append(f'<tr><td>{num}</td><td class="mono">{" ".join(cels)}</td>'
                       f'<td>{len(pares_no)} pares</td><td>{cobertas} quadras</td></tr>')
        return "\n".join(out)

    # heatmap 12x12 co-ocorrência de evens
    max_cooc = max(cooc.values()) if cooc else 1
    heat_rows = []
    heat_rows.append('<tr><th></th>' + "".join(f'<th>{d:02d}</th>' for d in PARES) + '</tr>')
    for a in PARES:
        cells = [f'<th>{a:02d}</th>']
        for b in PARES:
            if a == b:
                cells.append('<td class="diag">—</td>')
            else:
                v = cooc.get((min(a, b), max(a, b)), 0)
                alpha = v / max_cooc
                # cor azul com intensidade alpha (fundo claro -> azul forte)
                cells.append(f'<td style="background:rgba(37,99,235,{0.08+0.85*alpha:.2f});color:{"#fff" if alpha>0.6 else "#111"}">{v}</td>')
        heat_rows.append("<tr>" + "".join(cells) + "</tr>")
    heatmap = "\n".join(heat_rows)

    vetor_ref = " ".join("1" if d in referencia else "0" for d in PARES)
    vetor_viz = " ".join("1" if d in viz_ex else "0" for d in PARES)

    html_doc = f"""<!DOCTYPE html>
<html lang="pt-BR"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Lista 1 × Lista 2 — Quadras pares e Hamming distância 2</title>
<style>
body{{font-family:system-ui,-apple-system,Segoe UI,Roboto,sans-serif;max-width:1100px;margin:0 auto;padding:24px;color:#111;background:#f8fafc}}
h1{{font-size:26px}} h2{{margin-top:36px;border-bottom:2px solid #2563eb;padding-bottom:6px}}
.card{{background:#fff;border:1px solid #e2e8f0;border-radius:12px;padding:18px;margin:16px 0}}
.mono{{font-family:ui-monospace,Menlo,Consolas,monospace}}
table{{border-collapse:collapse;width:100%;font-size:14px}}
th,td{{border:1px solid #e2e8f0;padding:6px 8px;text-align:left}}
th{{background:#eff6ff}}
.bar{{background:#e2e8f0;border-radius:6px;height:14px;min-width:120px;overflow:hidden}}
.barfill{{display:block;height:100%}}
.par{{background:#dbeafe;border-radius:4px;padding:1px 4px;font-weight:700;color:#1e40af}}
.impar{{color:#64748b}}
.passo{{display:flex;gap:12px;margin:12px 0}}
.numero{{flex:0 0 36px;height:36px;border-radius:50%;background:#2563eb;color:#fff;display:flex;align-items:center;justify-content:center;font-weight:800}}
.aviso{{background:#fef3c7;border:1px solid #f59e0b;border-radius:8px;padding:12px}}
.scroll{{max-height:420px;overflow:auto}}
td.diag{{text-align:center;color:#94a3b8}}
.small{{font-size:13px;color:#475569}}
</style></head><body>
<h1>📋 Lista 1 × Lista 2 — Quadras pares (1–25) e distância de Hamming 2</h1>
<p class="small">Lista 1: últimos 100 concursos 3726–3825 · Lista 2: 495 quadras só com pares 02–24 · Referência: 10/11/2026</p>

<div class="card">
<h2>🧭 Passo a passo (didático)</h2>
<div class="passo"><div class="numero">1</div><div><b>O que é uma quadra par?</b> Um grupo de 4 dezenas pares, ex.: <span class="mono">02 04 06 08</span>. Com as 12 pares (02,04,…,24) há C(12,4) = <b>495 quadras</b>.</div></div>
<div class="passo"><div class="numero">2</div><div><b>O que é distância de Hamming?</b> Escreva cada quadra como 12 posições (1 = par na quadra, 0 = fora). A distância é <b>em quantas posições os vetores diferem</b>.</div></div>
<div class="passo"><div class="numero">3</div><div><b>Distância 2 = trocar 1 dezena.</b> Duas quadras a distância 2 compartilham 3 dezenas (uma sai, outra entra) → vetores diferem em 2 posições. Distância 4 = compartilham 2; 6 = compartilham 1; 8 = compartilham 0.</div></div>
<div class="passo"><div class="numero">4</div><div><b>Comparação:</b> uma quadra “aparece” num concurso quando suas 4 pares estão todas nas 15 sorteadas. Cada concurso cobre C(m,4) quadras (m = pares sorteados).</div></div>
<p class="mono">Referência (mais frequente): <b>{fmt(referencia)}</b><br>Vetor: {vetor_ref} &nbsp;(ordem 02,04,06,08,10,12,14,16,18,20,22,24)</p>
<p class="mono">Vizinha distância 2 (ex.): <b>{fmt(viz_ex)}</b><br>Vetor: {vetor_viz} &nbsp;→ difere em 2 posições ✓</p>
</div>

<div class="card">
<h2>📊 Lista 2 — Quadras mais presentes (esperado ~{esperado:.1f} em 100)</h2>
<table><tr><th>#</th><th>Quadra</th><th>Ocorr.</th><th>%</th><th>Frequência</th><th>Dist. da ref.</th></tr>
{linhas_tabela_top()}
</table>
<h3>Quadras menos presentes</h3>
<table><tr><th>#</th><th>Quadra</th><th>Ocorr.</th><th>%</th><th>Frequência</th><th>Dist. da ref.</th></tr>
{linhas_tabela_bottom()}
</table>
</div>

<div class="card">
<h2>🔗 As 32 vizinhas a distância 2 da referência</h2>
<p class="small">4 escolhas de qual dezena sai × 8 de qual entra = 32. Ordenadas por frequência nos 100 concursos.</p>
<table><tr><th>#</th><th>Quadra vizinha</th><th>Troca</th><th>Ocorr.</th><th>%</th></tr>
{linhas_vizinhas()}
</table>
</div>

<div class="card">
<h2>🌡️ Heatmap — co-ocorrência de pares de dezenas pares</h2>
<p class="small">Cada célula = em quantos dos 100 concursos as duas dezenas pares saíram juntas. Mais escuro = mais frequente.</p>
<table>{heatmap}</table>
</div>

<div class="card">
<h2>📋 Lista 1 — 100 concursos (pares em <span class="par">azul</span>)</h2>
<p class="small">“Quadras cobertas” = quantas das 495 quadras estão contidas neste concurso. Média: {media_cobertas:.1f} por concurso · Total de presenças: {total_presencas}.</p>
<div class="scroll"><table><tr><th>Concurso</th><th>15 dezenas</th><th>Pares</th><th>Quadras cobertas</th></tr>
{linhas_lista1()}
</table></div>
</div>

<div class="aviso">⚠️ A quadra mais frequente no passado <b>não</b> tem mais chance no próximo concurso (qualquer quadra específica: ~10,8% teórica). A distância de Hamming organiza a <b>similaridade</b> entre quadras — não aumenta a chance de acerto. Estatística descritiva, não previsão.</div>
<p class="small">Arquivos: ranking_quadras_pares.csv (495 quadras) · relatorio_quadras_hamming.md · analise_quadras_hamming.py</p>
</body></html>"""
    (BASE / "relatorio_quadras_hamming.html").write_text(html_doc, encoding="utf-8")

    print(f"Quadras: {len(QUADRAS)} | referencia: {fmt(referencia)} {linhas[0]['ocorrencias']} ({linhas[0]['percentual']:.0f}%)")
    print(f"Top5: {[(fmt(r['quadra']), r['ocorrencias']) for r in linhas[:5]]}")
    print(f"Bottom5: {[(fmt(r['quadra']), r['ocorrencias']) for r in bottom20[:5]]}")
    print(f"Vizinhas dist2: {len(vizinhas_d2)} | ex: {fmt(viz_ex)}")
    print(f"Presencas totais: {total_presencas} | media/concurso: {media_cobertas:.1f} | dist m: {dict(sorted(dist_m.items()))}")


if __name__ == "__main__":
    main()
