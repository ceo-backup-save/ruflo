# 🏆 GitHub é uma mina de ouro — 10 repositórios para criar produtos de IA

Curadoria dos 10 projetos open source apresentados no carrossel **@fabianocarvalhojr** (08–10/10), organizados por **o que o repo faz**, **licença** e **ideia de negócio** para transformar código em produto que as pessoas pagam.

> Regra de ouro do carrossel: **não crie para todo mundo. Crie para um cliente específico.**

## 📋 Índice rápido

| # | Projeto | Repositório | Linguagem | Licença | Produto possível |
|---|---------|-------------|-----------|---------|------------------|
| 01 | morphic | [miurla/morphic](https://github.com/miurla/morphic) | TypeScript | Apache-2.0 | Buscador com IA para um nicho |
| 02 | moonshine | [moonshine-ai/moonshine](https://github.com/moonshine-ai/moonshine) | C++ | Custom (NOASSERTION) | App de voz / transcrição |
| 03 | Unstract + DocETL | [Zipstack/unstract](https://github.com/Zipstack/unstract) · [ucbepic/docetl](https://github.com/ucbepic/docetl) | Python | AGPL-3.0 · MIT | Documentos → dados úteis |
| 04 | pdfme | [pdfme/pdfme](https://github.com/pdfme/pdfme) | TypeScript | MIT | Gerador de PDFs |
| 05 | assistant-ui | [assistant-ui/assistant-ui](https://github.com/assistant-ui/assistant-ui) | TypeScript | MIT | Interface de chat com IA |
| 06 | OpnForm | [OpnForm/OpnForm](https://github.com/OpnForm/OpnForm) | PHP | Custom (NOASSERTION) | Criador de formulários |
| 07 | LitServe | [Lightning-AI/LitServe](https://github.com/Lightning-AI/LitServe) | Python | Apache-2.0 | Modelos de IA como API |
| 08 | next-forge | [vercel/next-forge](https://github.com/vercel/next-forge) | TypeScript | MIT | Micro-SaaS completo |
| 09 | puck | [puckeditor/puck](https://github.com/puckeditor/puck) | TypeScript | MIT | Criador de sites |

---

## 01 · Buscador com IA — morphic
🔗 https://github.com/miurla/morphic — ⭐ ~9,2k · Apache-2.0

Motor de busca com respostas citadas e suporte a múltiplos provedores de modelo (OpenAI, Anthropic, Gemini, Perplexity).

- **O que dá para fazer:** busca com IA, respostas com fontes, troca de provider
- **Ideia de negócio:** assistente de pesquisa para **advogados, marketing ou analistas financeiros** — um setor, um problema real
- **Clientes:** advocacia · agências de marketing · finanças

## 02 · App de voz com IA — moonshine
🔗 https://github.com/moonshine-ai/moonshine — ⭐ ~11,3k · licença customizada (verificar antes de uso comercial)

Reconhecimento de fala **on-device** para desktop, mobile e browser (Rust + bindings React).

- **O que dá para fazer:** fala → texto, multiplataforma, processamento local (sem depender da nuvem)
- **Ideia de negócio:** app privado de produtividade por voz (ditado, transcrição de aulas, fluxos por comando de voz)
- **Atenção:** a licença não é SPDX padrão — leia o LICENSE do repo antes de vender

## 03 · Documentos → dados úteis — Unstract + DocETL
🔗 https://github.com/Zipstack/unstract (AGPL-3.0) — ⭐ ~7,4k
🔗 https://github.com/ucbepic/docetl (MIT) — ⭐ ~4,2k

**Unstract** transforma PDFs, scans e imagens em JSON estruturado via API. **DocETL** extrai e analisa dados não estruturados em escala (pipelines declarativos).

- **Ideia de negócio 1:** ferramenta de IA para nota fiscal — sobe o PDF, sai `invoice_number`, `date`, `vendor`, `total`, `items`, `status`
- **Ideia de negócio 2:** analisador de feedback de cliente — avaliações e tickets viram sentimento + top topics
- **Clientes:** pequenas empresas · contabilidade · e-commerce · SaaS
- **Atenção:** Unstract é **AGPL-3.0** — se você oferecer como serviço na rede, precisa abrir o código derivado (ou usar o DocETL, MIT, como base)

## 04 · Gerador de PDF — pdfme
🔗 https://github.com/pdfme/pdfme — ⭐ ~5k · MIT

Gerador de PDF com **designer visual de templates** (texto, tabelas, imagens, código de barras, QR), em JS/TS.

- **Ideia de negócio:** plataforma de documentos com a marca do cliente — notas, propostas, certificados e relatórios em segundos
- **Clientes:** freelancers · escolas/cursos · pequenas empresas · times grandes

## 05 · Interface de chat com IA — assistant-ui
🔗 https://github.com/assistant-ui/assistant-ui — ⭐ ~12,9k · MIT

Toolkit React para chats de IA elegantes: streaming, anexo de arquivos, componentes prontos.

- **Ideia de negócio:** assistente de IA **de um setor** (não mais um chatbot genérico): e-commerce, ensino, suporte ao cliente
- **Clientes:** e-commerce · plataformas de ensino · SaaS · suporte

## 06 · Criador de formulários — OpnForm
🔗 https://github.com/OpnForm/OpnForm — ⭐ ~4k · licença customizada (verificar)

Construtor de formulários open source com lógica condicional, upload de arquivos e webhooks.

- **Ideia de negócio:** portal de entrada de clientes — coleta dados, documentos e o pedido por formulários personalizados
- **Clientes:** agências · freelancers · consultores · empresas de serviço
- **Atenção:** projeto em PHP (Laravel); confirme a licença para uso comercial

## 07 · Modelos de IA como API — LitServe
🔗 https://github.com/Lightning-AI/LitServe — ⭐ ~4k · Apache-2.0

Serve qualquer modelo (ou pipeline) como API em poucas linhas, com batching e escala.

```python
from litserve import LitAPI, LitServer

class MyAPI(LitAPI):
    ...

server = LitServer(MyAPI())
server.run(port=8000)
```

- **Ideia de negócio:** API de processamento com IA (classificação de imagens, áudio, OCR) vendida por requisição
- **Clientes:** devs de SaaS · startups · agências de apps · empresas que usam IA

## 08 · Micro-SaaS pronto — next-forge
🔗 https://github.com/vercel/next-forge — ⭐ ~7,7k · MIT

Starter kit SaaS completo para Next.js: autenticação, Stripe, banco de dados, e-mail e analytics já configurados.

- **Ideia de negócio:** SaaS de nicho com conta de usuário, assinatura paga e estrutura essencial no dia 1
- **Clientes:** pequenas empresas · fundadores de startup · freelancers · empreendedores de SaaS

## 09 · Criador de sites — puck
🔗 https://github.com/puckeditor/puck — ⭐ ~13,6k · MIT

Editor visual drag-and-drop para React (block-based, headless).

- **Ideia de negócio:** editor de sites de nicho — restaurantes, corretores de imóveis, negócios locais
- **Clientes:** restaurantes · imobiliárias · negócios locais · pequenas agências

---

## ⚖️ Licenças — leia antes de monetizar

| Licença | O que significa para o seu produto |
|---------|-----------------------------------|
| **MIT / Apache-2.0** | Uso comercial livre; mantenha o aviso de copyright |
| **AGPL-3.0** (Unstract) | Se rodar como serviço de rede, precisa liberar o código derivado |
| **Custom / NOASSERTION** (moonshine, OpnForm) | Leia o LICENSE no repo — pode haver restrição comercial |

## 🚀 Roteiro sugerido (7 dias)

1. **Escolha o nicho**, não o repo — quem vai pagar e por qual dor?
2. **Clone e rode local** o projeto escolhido
3. **Troque a demo pelo caso real** do cliente (o dado dele, o documento dele)
4. **Embrulhe a entrega** em um fluxo simples: upload → processamento → resultado
5. **Cobre por resultado**, não por token: R$ por documento, por usuário, por mês

---

*Curadoria feita a partir do carrossel de @fabianocarvalhojr. Todos os créditos aos mantenedores dos projetos originais.*
