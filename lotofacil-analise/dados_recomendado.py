import json, random, statistics
from collections import Counter
from math import comb
from analise_lotofacil import CONCURSOS
from analise_fixa_excluida_equilibrio import gerar, stats_jogo, FIXA, EXCLUIDA, RESTANTES, FREQ, cumpre_equilibrio

PARES=set(range(2,26,2))
jogos = gerar(20, True, 20261112, faixa_alvo=((9,6),(10,5)))
assert all(cumpre_equilibrio(j, ((9,6),(10,5))) for j in jogos)

# distribuicoes observadas
dp=Counter(); df=Counter()
for _,_,s in CONCURSOS:
    dp[sum(1 for d in s if d in PARES)]+=1
    df[sum(1 for d in s if d<=16)]+=1

P={h: comb(15,h)*comb(10,15-h)/comb(25,15) for h in (11,12,13,14,15)}
EV_FIXO = P[11]*7 + P[12]*14 + P[13]*35

# Monte Carlo futuro: 20 jogos, 20.000 concursos simulados (blocos de 1 concurso)
rng=random.Random(2026)
PREMIOS={11:7.0,12:14.0,13:35.0,14:1300.0,15:450000.0}
saldo=[]
for _ in range(20000):
    s=set(rng.sample(range(1,26),15))
    prem=0.0
    for j in jogos:
        h=len(set(j)&s)
        if h>=11: prem+=PREMIOS[h]
    saldo.append(prem-70.0)
saldo.sort()
def pct(v): return saldo[int(v*len(saldo))]
res = {
 "jogos":[" ".join(f"{d:02d}" for d in j) for j in jogos],
 "stats":[stats_jogo(j) for j in jogos],
 "dist_pares":dict(sorted(dp.items())),
 "dist_faixa":dict(sorted(df.items())),
 "p7ou8_pares": dp[7]+dp[8],
 "p9ou10_faixa": df[9]+df[10],
 "p78_faixa": df[7]+df[8],
 "P":{str(k):v for k,v in P.items()},
 "EV_FIXO":EV_FIXO,
 "freq":[ (d, FREQ[d]) for d in sorted(RESTANTES, key=lambda x:(-FREQ[x],x)) ],
 "mc":{"media":statistics.mean(saldo),"mediana":statistics.median(saldo),
       "p05":pct(0.05),"p25":pct(0.25),"p75":pct(0.75),"p95":pct(0.95),
       "lucro_pct":sum(1 for v in saldo if v>0)/len(saldo)*100,
       "max":saldo[-1],"min":saldo[0]},
}
json.dump(res, open("dados_recomendado.json","w"), ensure_ascii=False, indent=1)
print("jogos", len(jogos))
print("dist pares", res["dist_pares"])
print("dist faixa", res["dist_faixa"])
print("7/8 pares:", res["p7ou8_pares"], "9/10 em 1-16:", res["p9ou10_faixa"], "7/8 faixa:", res["p78_faixa"])
print("EV fixo R$", round(EV_FIXO,3))
print("MC", {k:(round(v,1) if isinstance(v,float) else v) for k,v in res["mc"].items()})
