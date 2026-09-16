# Power BI Skills

> **3 skills do Claude pra documentar, auditar e criar DAX no Power BI. Grátis, open source, funciona no Claude.ai. 2 minutos pra instalar.**

[![Xperiun](https://img.shields.io/badge/by-Xperiun-7099FF?style=flat-square)](https://xperiun.com)
[![Free](https://img.shields.io/badge/Claude-Free%20OK-3FD1B8?style=flat-square)](https://claude.ai)
[![License](https://img.shields.io/badge/license-MIT-E8C9A0?style=flat-square)](LICENSE)

---

## O problema

Você herda um `.pbix` de 400 medidas sem documentação. Gasta 3 semanas só pra entender o modelo. Aí precisa criar uma medida e digita DAX no editor pequenininho do Power BI Desktop. E quando termina, ninguém sabe se o modelo tá bem feito.

**3 tarefas chatas, repetitivas, que rodam toda semana:**

1. **Documentar** o modelo
2. **Auditar** se tá bem feito
3. **Criar** medidas DAX

Esse repo automatiza as 3, e roda **direto no Claude.ai grátis**.

---

## As 3 skills

### 🩺 `pbi-modelo-review`

**Audita o modelo Power BI e devolve scorecard 0-100 + lista priorizada de issues.**

- 23 checks em 6 famílias (modelagem, relacionamentos, performance, naming, DAX, documentação)
- Output: relatório HTML visual (estilo Lighthouse) + markdown
- Detecta: bi-direcional desnecessário, Auto Date/Time, FAT FACT, DAX antipatterns, paths pessoais hardcoded
- Roda em ~3-5 min em modelo médio

### 📚 `pbi-doc`

**Gera mini-site de documentação navegável + 5 markdowns Git-friendly.**

- Sidebar fixa com navegação, busca client-side e scroll spy
- Documenta: tabelas + colunas tipadas + medidas DAX explicadas em PT + relacionamentos (SVG visual) + dependências
- Cada medida vira card expansível com DAX + "O que faz" + "Como funciona" + "É usada por"
- Output: 1 HTML standalone + 5 .md (Git diff entre versões mostra evolução do modelo)

### ⚡ `pbi-dax-create`

**Cria medida DAX a partir de descrição em PT, respeitando o modelo existente.**

- Lê tabelas/colunas/medidas reais do modelo
- Detecta padrão de naming (Title Case, prefixos, sufixos)
- Aplica boas práticas DAX automaticamente (DIVIDE em vez de /, SUMX vs SUM, time intelligence)
- Avisa se medida similar já existe (não duplica)
- Pergunta sempre antes de aplicar (modo seguro)

---

## Downloads

| Skill | `.zip` |
|---|---|
| 🩺 Auditar modelo | [`pbi-modelo-review.zip`](claude-web/pbi-modelo-review.zip) |
| 📚 Documentar modelo | [`pbi-doc.zip`](claude-web/pbi-doc.zip) |
| ⚡ Criar medida DAX | [`pbi-dax-create.zip`](claude-web/pbi-dax-create.zip) |

**Setup em 2 minutos, 3 caminhos (Web, Desktop, Code):** ver [INSTALL.md](INSTALL.md).

**Pré-requisito:** seu projeto Power BI salvo como **PBIP** (não `.pbix`). [Como converter em 30s](INSTALL.md#antes-de-começar--pré-requisitos).

---

## Por que esse caminho (e não MCP)

A maioria dos tutoriais de IA + Power BI ensina via **MCP server**: server rodando ao vivo, dados indo pra API, "Sempre permitir" clicado no susto. **Em cliente corporativo isso não passa.**

Esse repo segue **PBIP + Claude Skills**:

| MCP | Claude Skills (este repo) |
|---|---|
| Server rodando ao vivo | Anexa só os arquivos .tmdl que você quer |
| "Sempre permitir" clicado | Você controla o que sobe a cada conversa |
| Dados indo pra API sem filtro | Você escolhe arquivo a arquivo |
| Barrado em cliente corporativo | Auditável e compatível com LGPD |
| Precisa Power BI Premium / Pro+ | Claude Free funciona |

---

## Onde rodar

| Ambiente | Pra quem | Plano | Anexar arquivos? | Output |
|---|---|---|---|---|
| **Claude.ai (web)** ⭐ | Quem não tem nada instalado | Free serve | A cada conversa (drag-drop) | Artifact HTML inline + download |
| **Claude Desktop** | Quem já usa o app nativo | Free serve, Pro recomendado | A cada conversa (drag-drop) | Igual ao web |
| **Claude Code** | Dev/analista com Git e uso intenso | Pro ou superior | **Lê sozinha** do disco | Salva direto em `_review/`, `_docs/` no projeto e edita `.tmdl` (com aprovação) |

⭐ = recomendado se você não tem certeza.

**Passo a passo de cada um:** [INSTALL.md](INSTALL.md).

---

## Como usar

### Documentar um modelo

```
> Quero documentar meu modelo Power BI
> [a skill pede os .tmdl da pasta SemanticModel/]
> [anexa um ZIP com os .tmdl]
> [recebe mini-site HTML completo + 5 markdowns]
```

### Auditar um modelo

```
> audita esse modelo
> [anexa .tmdl]
> [recebe scorecard 0-100 + issues priorizados]
```

### Criar uma medida DAX

```
> cria uma medida pra ticket médio
> [se preciso, a skill pede o Medidas.tmdl pra entender o naming]
> [recebe sugestões de nome + DAX completo + explicação + onde colar]
```

---

## Estrutura

```
claude-code/          ← as 3 skills em pasta, pra copiar no Claude Code
  pbi-modelo-review/
  ├── SKILL.md        ← instruções da skill
  ├── references/     ← checks e tokens visuais
  └── templates/      ← relatório HTML e markdown
claude-web/           ← as mesmas 3 skills em .zip, pra upload no Claude.ai
```

Cada skill é **independente**: pode instalar só uma. Pro Claude Code:

```bash
cp -r claude-code/* ~/.claude/skills/
```

---

## Contribuindo

Issues e PRs bem-vindos. Mexeu em alguma skill de `claude-code/`? Rode `python scripts/build-zips.py` pra regenerar os `.zip` de `claude-web/`. Sugestões de novas skills via [GitHub Discussions](https://github.com/xperiun/skills-xperiun-free/discussions).

---

## Sobre a Xperiun

[Xperiun](https://xperiun.com) é a escola de Power BI + Dados + IA pra analistas e líderes brasileiros que querem virar **incomparáveis**.

Esse repo é parte do compromisso de manter conhecimento de ponta acessível e gratuito. Quem quiser ir mais fundo (curso completo, mentoria, comunidade) conhece o programa em [xperiun.com](https://xperiun.com).

**Siga:** [@leokarpa](https://instagram.com/leokarpa) · [@xperiun](https://instagram.com/xperiun)

---

## Licença

MIT. Use, modifique, distribua. Se ajudou, deixa uma estrela ⭐ no repo.

---

*Construído pela equipe Xperiun. v0.1.1 · 2026-09*
