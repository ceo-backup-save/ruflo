# A "junta de IAs" — extração do conteúdo e prompt replicável

**Fonte:** carrossel @frankcosta (10 slides) sobre o estudo MAI-DxO da Microsoft, publicado na *Science* em 22/10/2026.
**Status da verificação:** números conferidos na imprensa especializada. Ressalva importante ao final (seção 6).

---

## 1. Resumo executivo

A Microsoft colocou uma IA contra médicos em **304 casos difíceis** do *New England Journal of Medicine*: a IA acertou **83%**, os clínicos gerais **36%** (com acesso a livros e internet) e **22%** (sem acesso).

O ponto do carrossel é que **o ganho não veio de um modelo mais inteligente, e sim de como o sistema pensa**: em vez de responder de primeira, o MAI-DxO simula uma **junta médica de cinco papéis** que discute o caso em **ciclo** — hipótese → pergunta → exame → resultado → revisão — até haver certeza suficiente para fechar o diagnóstico. Cada pergunta e cada exame tem custo, e o sistema só recebe a informação que **pede explicitamente**.

A tese transferível para qualquer negócio: **a diferença não está na ferramenta, está em como você faz a ferramenta pensar.** Um prompt pode replicar essa estrutura.

---

## 2. O problema que o teste reproduziu

Diagnóstico difícil **não chega pronto**. O médico começa com pouca informação, levanta hipótese, pergunta, pede exame, recebe resultado, muda de ideia, pede outro exame — e cada exame custa dinheiro.

Benchmarks tradicionais falham porque entregam o caso inteiro de bandeja em pergunta de múltipla escolha. O **Sequential Diagnosis Benchmark (SDBench)** recria a escassez: participante começa só com o resumo do caso e precisa **pedir** cada informação adicional a um *gatekeeper*. A nota considera acurácia **e** custo (visitas + exames).

### ChatGPT direto × MAI-DxO

| | IA sozinha ("ChatGPT direto") | Junta de IAs (MAI-DxO) |
|---|---|---|
| Entrada | o caso inteiro | só o resumo inicial |
| Comportamento | responde de primeira, com confiança total | pergunta, testa, revisa, questiona a si mesma |
| Saída | **uma resposta** | **um diagnóstico** |

---

## 3. Os 5 papéis da junta

| # | Papel | Função |
|---|-------|--------|
| 1 | **Levantador de hipóteses** | monta o diferencial: todas as explicações plausíveis no início |
| 2 | **Seletor de exames** | escolhe a *próxima* coleta de informação com maior poder de discriminação |
| 3 | **Advogado do diabo** | ataca a hipótese favorita; tenta derrubá-la antes de você se apegar |
| 4 | **Vigia de custo** | corta exame desnecessário; exige justificativa de custo-benefício |
| 5 | **Auditor de processo** | confere se nenhuma etapa foi pulada (checklist) |

## 4. O ciclo

```
Hipótese → Pergunta → Exame → Resultado → Revisa a hipótese → (repete)
                                                    ↓
                                        certeza suficiente?
                                          não → mais uma volta
                                          sim → fecha o diagnóstico
```

O ciclo roda **até haver certeza suficiente** — não até "achar uma resposta". É o critério de parada que separa os dois modos.

## 5. Generalização entre modelos

A mesma estrutura de junta foi testada sobre modelos da **OpenAI, Google, Anthropic, xAI, DeepSeek e Meta**. Em todos os casos, a junta superou o modelo sozinho — e o ganho foi **maior nos modelos mais fracos**, justamente onde a estrutura compensa a falta de capacidade bruta.

## 6. Limites do teste (a parte honesta)

- **Só texto.** Sem imagem, sem exame físico, sem paciente na frente.
- **Caso simulado.** O "paciente" era outro modelo de linguagem com o prontuário em mãos. Estudo com pacientes reais (Beth Israel, Boston) ainda vai começar.
- **Médicos eram clínicos gerais**, não especialistas — casos desse nível normalmente vão para especialistas ou equipes.
- **Comando único vs. painel incansável.** O clínico respondia sozinho e sob limite; a IA era um painel sem cansaço, em casos feitos para especialistas, avaliado por um juiz automático construído por quem fez o sistema.

**Ressalva ao slide "a melhora não veio do modelo, veio da estrutura":** o próprio artigo mostra que o **GPT-5 sozinho, com prompt simples, chegou a ~79%**; a orquestração levou a ~83%. Ou seja, **a estrutura adiciona alguns pontos, mas o salto de 36% → 83% vem sobretudo do modelo base ser muito melhor que um clínico humano isolado**. A leitura correta é: *estrutura melhora qualquer modelo, mas não substitui o modelo.* Essa é a diferença entre um argumento honesto e uma promessa de marketing.

- **Não substitui médico amanhã.** Mostra onde a IA já analisa melhor que gente.

---

## 7. O prompt único (replicável em qualquer domínio)

Copie o bloco inteiro. Funciona para diagnóstico médico, mas também para decisão de negócio, análise de caso jurídico, troubleshooting técnico ou due diligence.

```text
# PAPEL
Você vai operar como uma JUNTA DE ESPECIALISTAS, não como um assistente que responde perguntas.
Cinco papéis discutem o caso em ciclo até haver certeza suficiente para fechar uma conclusão.
Você interpreta todos os cinco, mas cada um fala em turno próprio, na ordem definida.

# REGRA DE OURO: SÓ A INFORMAÇÃO PEDIDA
Você recebe apenas o RESUMO INICIAL do caso (abaixo). Todas as demais informações
estão ocultas. Você NÃO pode inventar, supor ou preencher lacunas.
A cada volta, a junta escolhe a informação mais decisiva a obter e a formula como
PERGUNTA EXPLÍCITA a mim. Eu respondo apenas aquela pergunta (ou digo "indisponível").
Se você usar qualquer dado que não foi fornecido, a análise é inválida.

# A JUNTA (5 papéis, nesta ordem)
1. HIPÓTESES — liste de 3 a 6 hipóteses concorrentes, com o raciocínio de cada uma
   e o que faria cada uma subir ou cair. Inclua ao menos uma hipótese "impopular".
2. PRÓXIMA COLETA — escolha UMA única informação/exame/pergunta com o maior poder de
   discriminar entre as hipóteses. Justifique: o que muda na decisão se o resultado vier A vs B?
   Se a resposta for "nada muda", escolha outra.
3. ADVOGADO DO DIABO — ataque a hipótese favorita. Aponte a evidência que a contradiz,
   o viés provável, e qual seria o diagnóstico alternativo se ela estiver errada.
4. VIGIA DE CUSTO — estime o custo/atrito da coleta pedida (dinheiro, tempo, risco,
   retrabalho) e diga se ela é justificada AGORA ou se pode esperar. Corte o que for
   "nice to have". Se o custo for alto, proponha a alternativa mais barata com poder
   discriminatório parecido.
5. AUDITOR — confira o checklist: (a) hipóteses são realmente concorrentes?
   (b) a coleta pedida é a de maior valor? (c) o advogado do diabo foi respondido?
   (d) alguma etapa foi pulada? (e) o custo foi pesado? Se algo falhou, devolva ao papel.

# CRITÉRIO DE PARADA
Depois do ciclo, avalie: "tenho certeza suficiente para fechar?".
- NÃO → declare em uma linha o que falta e volte ao papel 1 com a informação nova.
- SIM → feche a conclusão.
Nunca feche antes de rodar ao menos 2 voltas. Nunca passe de 6 voltas:
se estourar o limite, entregue a melhor hipótese com a confiança declarada e o que
seria necessário para confirmar.

# FORMATO DE SAÍDA (a cada volta)
## Volta N
**Hipóteses:** [tabela: hipótese | a favor | contra | probabilidade %]
**Coleta pedida:** [a pergunta, em uma frase, dirigida a mim]
**Advogado do diabo:** [ataque em até 4 linhas]
**Vigia de custo:** [custo/atrito estimado | decisão: agora ou esperar]
**Auditor:** [ok / correções]
**Status:** [aguardando resposta | hipótese descartada | concluído]

# SAÍDA FINAL (só ao fechar)
- **Conclusão:** [a resposta em uma frase]
- **Confiança:** [alta/média/baixa + %]
- **Diferenciais ainda vivos:** [o que não foi eliminado e por quê]
- **O que derrubaria esta conclusão:** [a evidência que me faria mudar de ideia]
- **Custo total do processo:** [nº de coletas pedidas e atrito acumulado]
- **Etapas puladas / lacunas assumidas:** [lista explícita]

# RESUMO INICIAL DO CASO
[COLE AQUI SÓ O RESUMO — 3 a 6 linhas. Nada de informação completa.]

# CONTEXTO DE USO
Domínio: [medicina | negócio | jurídico | engenharia | outro]
Decisor: [quem usa a conclusão]
Restrição de custo: [orçamento/tempo/risco máximo aceitável]

Comece pela Volta 1. Não peça a informação completa. Não conclua ainda.
```

### Variação de 30 segundos (quando não há tempo para o ciclo completo)

```text
Antes de me dar a resposta: monte uma junta de 4 papéis (defensor, atacante, vigia de
custo, auditor de lacunas). Cada um fala uma vez sobre esta decisão [DESCREVA].
Só depois que os quatro discutirem, me dê a recomendação final, com o que ainda falta
saber e o que me faria mudar de ideia.
```

---

## 8. Por que isso funciona (mecanismos, não mágica)

| Mecanismo | Efeito |
|-----------|--------|
| **Escassez de informação** | impede a resposta confiante de primeira; força raciocínio sequencial |
| **Hipóteses concorrentes explícitas** | combate ancoragem na primeira ideia |
| **Advogado do diabo obrigatório** | ataca o viés de confirmação |
| **Vigia de custo** | transforma "mais informação" em trade-off, não em default |
| **Auditor de checklist** | pega etapa pulada, que é onde mora o erro caro |
| **Critério de parada explícito** | separa "achei uma resposta" de "tenho certeza suficiente" |

## 9. Como aplicar amanhã (não precisa de código)

1. **Escolha a decisão mais cara** do seu negócio — a que você refaz toda semana.
2. **Escreva o resumo inicial** em 5 linhas: o que se sabe, sem a resposta.
3. **Rode o prompt** e responda só o que ele pedir, uma pergunta por vez.
4. **Registre o custo** de cada coleta pedida (tempo seu, dinheiro, retrabalho).
5. **Compare** com a sua decisão habitual em 5 casos. Onde ele pediu algo que você nunca pediria, ali está o ganho.

---

*Extração e organização do carrossel de @frankcosta. Dados do estudo: Nori et al., "Sequential diagnosis with language models", Science, 22/10/2026.*
