---
name: portfolio-manifest
description: Ingests information about the user (resume, LinkedIn export, portfolio site, GitHub, case studies, decks, writing, performance reviews, project links) into an evidence inventory, then interviews them to curate a portfolio manifest of their strongest work mapped to skills, themes, and target roles. Use when the user says "build my portfolio", "portfolio manifest", "here's my resume/site/GitHub", "what proof do I have", or wants to turn scattered work into a story. Also use for quick win logging: "log a win", "add this to my brag doc", "I just shipped X". Do not use to write bios or headlines from the manifest (positioning-studio) or to tailor a resume to a posting (positioning-studio).
---

# Portfolio Manifest

Turn scattered evidence of the user's work into two things:
1. **Evidence inventory:** every atomic proof point found in their materials, with sources.
2. **Portfolio manifest:** a curated, structured catalog of their best projects that recruiters, collaborators, and other agents can use to understand what they've actually done, and that can later be rendered as a portfolio site, deck, or resume.

Modern technical-creative people often have work spread across code, design, writing, talks, and side projects, and no single title covers it. The manifest's job is to make the throughline visible.

**First, read `references/workspace-conventions.md`** for workspace location, file format, provenance tags, and README/changelog rules. **Then read `references/manifest-template.md`** for the evidence and manifest formats.

## Quick mode: log a win

When the user just wants to record something that happened ("log a win", "I just shipped X", "add this to my brag doc"), skip the phases:
1. Ask 2–3 questions: what happened, *their* part in it, and the result or reaction (a number, a quote, a before/after). Accept "too early to tell".
2. If they're in a git repo and ask for it, read recent commits (`git log --author=<them> --since=<date>`) to draft the item; show the draft and record only what they confirm, tagged `[stated]`.
3. Append one `EV-###` item (next free number, never renumber), log it in `sources.md` as source "win log", then run the validator.
4. Ask whether it should displace anything in the featured projects; if yes, run Phase 4 for that project only.

Suggest they log wins within a week of them happening; detail fades fast, and a steady log makes the next review, promotion case, or job search much easier.

## Phase 1: Gather sources

1. Read `portfolio/sources.md` if it exists so you don't re-ingest.
2. Ask what they have, offering a checklist (multi-select when available): resume/CV, LinkedIn profile or export, personal/portfolio site, GitHub or other code hosts, Dribbble/Behance/Figma community, case studies, slide decks, writing (blog, Substack, papers), talks/videos, performance reviews or peer feedback, awards/press, product launches, side projects, and anything else.
3. Accept files, links, and pasted text. Use whatever is available to read them: attached files, connected folders on their computer, connected apps (e.g., Drive) when the user points there, and WebFetch for public URLs. For sites with many pages (portfolio site, GitHub profile), read the index first, then the pages that describe actual work. For GitHub, focus on repos they own or significantly contributed to, READMEs, stars, and what the code does; ignore forks with no changes.
4. Don't fetch pages behind sign-in walls through workarounds. Ask the user to export or paste the content.
5. Log each source in `sources.md` (name, type, URL or file, date ingested, what was extracted, anything skipped).
6. **Evidence from others.** Self-descriptions are weaker evidence than what others observed. Ask for pasted performance reviews, LinkedIn recommendations, peer feedback, or client testimonials. If they have little, offer to draft a short **best-self stories** request they can send to 5–10 colleagues, managers, or clients (method from Roberts et al., 2005, "Composing the reflected best-self portrait"):

   > "I'm working on understanding my strengths. Could you tell me about one specific time you saw me at my best: what was happening, what I did, and why it mattered? A few sentences is plenty."

   They send it themselves; never send it for them. When replies come back, each becomes a `praise-from-others` evidence item quoting the reply, with the giver's role (name only if the user wants). Look for themes across replies and offer them to ground-truth-interview as strengths and blind-spot gaps.

For large batches, extract in parallel with subagents when available, each returning evidence items in the inventory format.

## Phase 2: Extract evidence

Break every source into atomic evidence items (`EV-001`, `EV-002`, …) in `evidence-inventory.md`. One item = one claimable thing: a project, a launch, a metric, a skill demonstrated, a piece of praise, an award.

- Extract only what the source says. Tag each with `[source: <name>]`.
- Note **gaps** rather than filling them: a project with no outcome gets `Result: _Not in source_`.
- Flag **inconsistencies** between sources (different dates, titles, or numbers) for the user to resolve.
- De-duplicate items that appear in several sources; list all sources on the item.

Show the user a summary: counts by type, the 10 most substantial items, and gaps/conflicts.

Also note **qualifiers** exactly as the source states them ("assisted with", "basic", "co-led", "contributed to"). Dropping a qualifier is one of the most common ways AI-written career material inflates a claim, so qualifiers stay attached to the item and travel with it into every downstream asset.

## Phase 3: Fill gaps by interview

Work through the highest-value items with gaps, 2–4 questions per turn:
- "What was your specific role versus the team's?"
- "What changed because of this? Any number, before/after, or quote?"
- "What was hard about it, and what did you do that someone else wouldn't have?"
- "Which disciplines did this combine?" (e.g., engineering + design + storytelling)
- "Can this be shown publicly, shown under NDA, or only described?"

Tag answers `[stated]`. Never inflate. If they don't know a metric, record a qualitative result instead.

## Phase 4: Curate the manifest

1. **Find the throughlines.** Cluster evidence into 3–5 themes (recurring problems, disciplines, or kinds of impact). Present them as hypotheses with supporting EV IDs and have the user name, merge, or reject them. These themes are the raw material for title-lab and positioning-studio.
2. **Pick featured projects.** Propose 5–8 candidates balancing strength of evidence, recency, relevance to their short-term goal (`ground-truth/06`), and coverage of themes. Avoid featuring work built around **anti-skills** (`ground-truth/03`) unless the user insists. The user picks the final set and order.
3. **Write project entries** (template in references) and a **skills matrix** linking each skill to the evidence that proves it. Flag skills they claim in ground truth that have no evidence yet: these are "proof gaps," worth building a project or writing a case study for.
4. Show the full manifest for review before saving as `manifest.md`. Set `derived_from:` in its frontmatter to the EV IDs it relies on.

If `ground-truth/` doesn't exist, the manifest still works; note that featured-project selection would be sharper with goals and anti-skills captured, and suggest ground-truth-interview.

## Updating

On later runs, ingest only new sources, append new EV items (never renumber), and ask whether new work should replace anything featured. Record changes in the changelog.

## Wrap up

Run `scripts/validate_workspace.py <workspace>` and fix every error until clean. Update the README status row and changelog. Offer next steps:
- **title-lab**, using the themes to explore titles that describe the throughline;
- **positioning-studio**, to turn themes + featured projects into a pitch;
- rendering the manifest as a portfolio page, resume, or deck (use the matching output format available in the session).
