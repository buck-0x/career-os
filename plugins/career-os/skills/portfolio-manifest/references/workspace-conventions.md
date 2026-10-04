# Career Workspace Conventions

Every skill in the career-os plugin reads and writes one shared folder, the **career workspace**. These conventions keep the files consistent so any skill or career-planning agent can rely on them.

## Locating the workspace

1. If the user names a folder, use it.
2. Otherwise look for an existing folder named `career-workspace/` (in the working directory or any connected folder on the user's computer). It is identified by `career-workspace/README.md`.
3. If none exists, ask once where to create it; default to `career-workspace/` in the working directory, or in a connected folder on their computer when one is available.
4. Create only the subfolders the current skill needs. Never delete or rename other skills' files.

## Layout

```
career-workspace/
  README.md                 # index: status of every area, open questions, guidance for agents
  changelog.md              # one dated line per session, across all skills
  ground-truth/             # ground-truth-interview
    01-executive-summary.md
    02-core-psychology-values.md
    03-professional-capital.md
    04-operating-manual.md
    05-whole-human.md
    06-trajectory-non-negotiables.md
    07-skill-gaps-development.md
  interests/                # interest-radar
    index.md                # table of every item + emerging patterns
    topics/<slug>.md
    companies/<slug>.md
    people/<slug>.md
    titles/<slug>.md
    projects/<slug>.md
  portfolio/                # portfolio-manifest
    sources.md              # every source ingested, when, and what was taken from it
    evidence-inventory.md   # atomic evidence items (EV-###)
    manifest.md             # the curated portfolio manifest
  titles/                   # title-lab
    candidates.md           # scoreboard of every title explored
    <slug>.md               # deep dive per title
    title-stack.md          # chosen title(s) + rationale
  positioning/              # positioning-studio
    positioning.md          # core positioning statement, proof, and variants
    assets/<audience>.md    # bios, headlines, intros per audience/channel
```

## File rules

- **Frontmatter on every file:**
  ```yaml
  ---
  title: <human title>
  type: ground-truth | interest | portfolio | title | positioning | index
  status: complete | partial | draft | not_started
  last_updated: YYYY-MM-DD
  open_questions: []
  ---
  ```
- **Slugs:** kebab-case, e.g. `companies/anthropic.md`, `titles/design-engineer.md`.
- **Provenance tags** on facts that matter:
  - `[stated]` the user said it in conversation
  - `[source: <name or URL>]` extracted from a document or page the user supplied
  - `[researched: <URL>]` found by Claude via web research (market facts only, never facts about the user)
  - `[suggested → approved]` Claude proposed it and the user approved it
- **Never write unapproved claims about the user.** Facts about the user come only from the user or from sources they supplied. Claude's suggestions are labeled as suggestions until approved.
- **Missing values:** `_Not yet captured_`. Never leave a heading empty.
- **Cross-links:** refer to other workspace files with relative links, e.g. `[Win 2](../ground-truth/03-professional-capital.md#win-2)` or evidence IDs like `EV-014`.
- **Changes over time:** when a value changes (salary floor, target title, goal), note the old value in `changelog.md` rather than keeping history inside the file.

## README.md (workspace index)

Each skill updates its own row and adds to the open questions. Create it if missing:

```markdown
# Career Workspace: <Name>

Living source of truth for career planning. Everything about <Name> here was stated, supplied, or approved by them.

## How agents should use this
- Treat `ground-truth/` as authoritative. Hard dealbreakers and financial minimums are filters.
- Anti-skills mean "capable but unwilling": never recommend roles built around them.
- `interests/` shows pull (what attracts them); `portfolio/` shows proof (what they've done). Recommendations should sit where pull and proof overlap.
- `titles/title-stack.md` and `positioning/positioning.md` are the approved way to describe them. Reuse that language.
- `_Not yet captured_` and open questions are unknowns: ask, don't guess.
- Flag anything with `last_updated` older than ~6 months as possibly stale.

## Status
| Area | Location | Status | Last updated |
|---|---|---|---|
| Ground truth | ground-truth/ | not_started | |
| Interests | interests/ | not_started | |
| Portfolio | portfolio/ | not_started | |
| Titles | titles/ | not_started | |
| Positioning | positioning/ | not_started | |

## Open questions
```

## changelog.md

Append one line per session: `- YYYY-MM-DD [skill-name]: <what was created/updated>; <notable changes, including old → new values>`.

## Session etiquette (all skills)

- Read `README.md` first and any files the skill depends on, so you never ask for something already captured.
- Keep your own turns short; ask 2–4 questions at a time.
- Save as you go, not only at the end.
- Close by updating the README status row and the changelog, then suggest the most useful next skill based on what's still missing.
