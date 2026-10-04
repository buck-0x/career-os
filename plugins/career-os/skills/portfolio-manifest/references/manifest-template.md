# Portfolio Formats

## evidence-inventory.md

```markdown
---
title: Evidence Inventory
type: portfolio
status: partial
last_updated: YYYY-MM-DD
open_questions: []
---

# Evidence Inventory

## Summary
- Items: <n> (projects <n>, metrics <n>, praise <n>, awards <n>, artifacts <n>)
- Unresolved conflicts: <n>

## Items

### EV-001: <short name>
- **Kind:** project | metric | launch | artifact | praise | praise-from-others | award | talk | writing | skill-demo
- **When:** <dates or year>
- **Where:** <company / context / self-initiated>
- **My role:** <role and specific contribution, or _Not in source_>
- **What happened:** <1–3 lines, keeping the source's qualifiers ("assisted", "co-led", "basic")>
- **Result:** <outcome, metric, or _Not in source_>
- **Skills shown:** [skill, skill]
- **Disciplines:** [engineering, design, writing, strategy, ...]
- **Link/artifact:** <URL or file>
- **Visibility:** public | NDA | describe-only | unknown
- **Sources:** [source: resume], [stated]
- **Conflicts:** <e.g., resume says 2021, LinkedIn says 2022>

### EV-002: <giver's role> on <situation>
- **Kind:** praise-from-others
- **When:** <date received>
- **From:** <role and relationship, e.g., "former manager at Acme"; name only if the user wants it>
- **Quote:** > <their words, verbatim>
- **Themes:** [<strengths the quote shows>]
- **Sources:** [source: best-self reply, YYYY-MM-DD]
```

## manifest.md

```markdown
---
title: Portfolio Manifest
type: portfolio
status: draft | complete
last_updated: YYYY-MM-DD
open_questions: []
---

# Portfolio Manifest: <Name>

## Throughline
> <one or two sentences, approved by the user, describing what connects their work>

## Themes
| Theme | What it means | Evidence |
|---|---|---|
| <name> | <user-approved definition> | EV-003, EV-011, EV-020 |

## Featured projects

### 1. <Project name>
- **One-liner:** <what it is, in plain words>
- **When / where:** <dates, org or self-initiated>
- **Role:** <their role and specific contribution>
- **Challenge:** <the problem or constraint>
- **What I did:** <the key moves; emphasize where disciplines combined>
- **Result:** <outcome, metric, or qualitative result>
- **Skills:** [..]  **Themes:** [..]
- **Artifacts:** <links, files, or "available on request (NDA)">
- **Visibility:** public | NDA | describe-only
- **Evidence:** EV-…
- **Best for audiences:** [hiring managers in X, founders, clients, ...]

(5–8 projects, in the user's chosen order)

## Skills matrix
| Skill | Level (from ground truth) | Proven by |
|---|---|---|
| <skill> | Expert | EV-002, Project 1 |

## Proof gaps
- <skill or claim with no evidence yet>: suggested way to close it (project, case study, writeup) [suggested]

## Also available (not featured)
- <project> (EV-…): why it's not featured (older, off-goal, anti-skill)
```

## sources.md

```markdown
| Source | Type | Location | Ingested | Extracted | Notes |
|---|---|---|---|---|---|
| Resume 2026 | resume | resume.pdf | YYYY-MM-DD | EV-001–EV-014 | |
```
