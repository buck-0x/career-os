---
name: interest-radar
description: Ingests links or names of topics, companies, people, job titles, and projects the user finds interesting, researches each one, captures why it appeals to them, and saves it to the career workspace with emerging patterns. Use when the user shares a link and says "this is interesting", "add this to my radar", "save this company/person/project", "track this topic", or asks what their interests say about their direction. Do not use to build their own portfolio from their work (portfolio-manifest) or to evaluate whether to apply somewhere (career-strategist agent).
---

# Interest Radar

Capture what pulls the user's attention: topics, companies, people, titles, and projects. Each item gets a short factual profile plus, most importantly, **why it appeals to them in their own words**. Over time the radar reveals patterns that point toward roles, companies, and positioning the user may not have named yet.

**First, read `references/workspace-conventions.md`** for workspace location, file format, provenance tags, and README/changelog rules.

## Item types

| Type | Folder | Examples |
|---|---|---|
| topic | `interests/topics/` | spatial computing, AI agents in ops, regenerative ag |
| company | `interests/companies/` | a startup, a studio, a lab, a nonprofit |
| person | `interests/people/` | someone whose career, work, or path they admire |
| title | `interests/titles/` | a job title spotted in the wild ("Creative Technologist") |
| project | `interests/projects/` | a product, open-source repo, art piece, essay, case study |

Infer the type from the input and confirm only if it's ambiguous (a founder's personal site could be a person or a company).

## Ingest flow

Users may drop one link or a batch. Handle batches by processing all items, then running one combined "why" round.

1. **Capture input.** Accept URLs, names, pasted text, or screenshots. If several, list them back in a numbered table with inferred type.
2. **Research each item.** Fetch the URL (WebFetch) or search (WebSearch) for a name. For a batch of more than ~5 items, research in parallel with subagents when available. Gather only what helps career decisions:
   - topic: what it is, where it's heading, who's hiring in it, adjacent roles
   - company: what they do, stage/size, funding or business model, location/remote policy if public, notable roles they hire for, culture signals
   - person: current role, career path (prior roles), what they're known for, public work. **Public professional information only**: no personal details, contact info, or home location. Pay special attention to the **path**: where they started, the moves that got them here, and how long each took. Seeing someone make a similar move ("modeling") is one of the ingredients that makes career interventions work, and it's most useful when their starting point resembles the user's.
   - title: what it typically means, typical responsibilities, adjacent/synonym titles, where it shows up
   - project: what it is, who made it, the skills and disciplines it combines
   Tag researched facts `[researched: <URL>]`. If a page can't be fetched, say so and ask the user to paste the relevant text.
3. **Ask why (the important part).** For each item, ask 1–2 questions, e.g.:
   - "What caught your eye here: the problem, the craft, the people, the business, or the lifestyle?"
   - person: "Is it their work, their path, or the way they talk about what they do?"
   - company: "Would you want to work *there*, work *on something like this*, or just learn from them?"
   - title: "What does this title promise that your current one doesn't?"
   Offer multiple choice (AskUserQuestion when available) with free text. Allow "just bookmark it" to skip; mark the reason `_Not yet captured_`.
4. **Capture pull strength and intent:** strength 1–5, and intent: `explore` / `learn-from` / `work-with` / `work-at` / `become-like` / `build-something-like`.
5. **Ask who's near it.** "Do you know anyone who works at, on, or near this?" Record names or roles they choose to share (or "no one yet"). Career changes mostly happen through people, so this turns the radar into a list of conversations to have. Contact details are optional and stay in the workspace.
6. **Save** one file per item, then update `interests/index.md`.

## Item file template

```markdown
---
title: <Name>
type: interest
interest_type: topic | company | person | title | project
status: complete | partial
last_updated: YYYY-MM-DD
added: YYYY-MM-DD
url: <primary URL or empty>
pull_strength: 1-5
intent: [explore, work-at, ...]
tags: [ai, design, climate, ...]
riasec: []          # optional Holland codes, e.g. [I, A]
open_questions: []
---

# <Name>

## Why it pulls me
> <user's words> [stated]

## What it is
<3–6 lines of researched facts, each tagged>

## Career relevance
- Roles / titles connected to it: ...
- Skills it rewards: ...
- Connections to my ground truth: <links to values, energizers, wins; only connections the user confirmed>

## Path (people items)
<how they got here: starting point → key moves → current role, with rough timing, tagged [researched: URL]; then, in the user's words, which part of the path they'd want to borrow>

## Who I know near this
<people or roles the user named, or _No one yet_; first conversation to have>

## Notes & follow-ups
- <user's own next steps, if any>
```

## index.md

Maintain a table and a patterns section:

```markdown
| Item | Type | Pull | Intent | Tags | Added | File |
|---|---|---|---|---|---|---|

## Emerging patterns
- <pattern> (evidence: items A, B, C) [suggested → approved]

## Pattern candidates (not yet confirmed)
- <pattern> (evidence: ...) [suggested]
```

## Pattern synthesis

After every ingest of 3+ items, and whenever the user asks "what does my radar say?":

1. Look across all items for recurring tags, problem spaces, disciplines, company stages, business models, and the *reasons* given (often more revealing than the items themselves).
2. Compare against `ground-truth/` if present: interests that match energizers and values, and interests that clash with dealbreakers or anti-skills.
   Optionally code each item with up to two Holland (RIASEC) letters: Realistic, Investigative, Artistic, Social, Enterprising, Conventional. A recurring code pair points to O*NET occupations with the same interest profile (O*NET Interest Profiler; see title-lab's data sources). Present codes as `[suggested]`.
3. Present 2–5 patterns as hypotheses, each with its evidence, e.g. "You keep saving people who moved from engineering into design leadership (A, B, C). Is that a path you're considering?"
4. Record confirmed patterns under **Emerging patterns**; keep unconfirmed ones under **Pattern candidates**.
5. Point out handoffs: title items worth exploring in **title-lab**; recurring language worth using in **positioning-studio**; people whose path is worth a prototype conversation (see the "Who I know near this" sections), which the career-strategist can turn into experiments.

## Updating items

When a user re-shares an existing item, update it instead of duplicating it: add new reasons, adjust pull strength, and note the change in the changelog. Items whose pull drops to 1 or that the user says no longer interest them get `status: archived` (keep the file; patterns use it as negative signal).

## Wrap up

Run `scripts/validate_workspace.py <workspace>` and fix every error until clean. Update the README status row and changelog. Suggest the next step based on what you saw: a title to explore in title-lab, a person whose path is worth mapping against their own portfolio, or a ground-truth section that the radar contradicts.
