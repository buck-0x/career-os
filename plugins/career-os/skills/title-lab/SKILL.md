---
name: title-lab
description: Iterates with the user on job titles for people whose work doesn't fit a standard title. Researches what each candidate title means in the market, captures what the user likes and dislikes about it, generates new variations from those reactions, scores fit, and converges on a title stack for different contexts. Use when the user says "what should my title be", "I don't know what to call myself", "compare these titles", "is X the right title for me", "explore title Y", or reacts to a title they saw.
---

# Title Lab

Help the user find language for what they do. Most technical-creative people don't fit one standard title, so the goal is usually not a single perfect title but a **title stack**: a searchable anchor title that recruiters and algorithms recognize, plus modifiers and context-specific variants that carry the nuance.

The method is iterative: put titles in front of the user, capture precise reactions (what they like and what they don't), and use those reactions to generate better candidates. The likes and dislikes are as valuable as the final pick, because they reveal how the user wants to be seen.

**First, read `references/workspace-conventions.md`** for workspace location, file format, provenance tags, and README/changelog rules. **Read `references/title-patterns.md`** before generating candidates.

## Inputs to read first

Read whatever exists, and don't re-ask what's there:
- `ground-truth/01` (current identity), `02` (energizers, strengths), `03` (skills, wins, **anti-skills**), `06` (short-term goal, comp floor)
- `interests/titles/` and patterns in `interests/index.md`
- `portfolio/manifest.md` themes and throughline
- `titles/candidates.md` from previous sessions

If none exist, run a short warm-up: what they do day to day, the 2–3 things they're best at, what they want more and less of, and titles they've used or been called.

## Loop

### 1. Seed candidates
Assemble 6–10 starting titles from: titles they've held, titles others have called them, titles saved in their interest radar, titles from people they admire, and titles generated from their portfolio themes using the patterns reference. Include at least one conventional, highly searchable title and at least one bold or invented one, so reactions span the range.

### 2. Research each candidate (market reality)
For each title, use WebSearch (and job-posting pages via WebFetch where available) to find:
- what it typically means: core responsibilities, the disciplines it implies
- seniority signals and typical reporting lines
- demand: roughly how common it is in current postings, and which kinds of companies use it
- a rough compensation range if sources exist, clearly labeled with source and date
- adjacent and synonym titles
- 2–3 real example postings or people using the title

Tag findings `[researched: <URL>]`. Keep this brief per title; the user's reaction matters more. For many titles at once, research in parallel with subagents when available.

### 3. Capture reactions
Show titles in small groups (3–4). For each, ask:
- Gut reaction 1–5.
- What do you **like** about it? (the words, what it signals, the work it implies, the audience it attracts, the seniority, how it sounds when you say it out loud)
- What do you **dislike**? (too narrow, too generic, wrong seniority, implies an anti-skill, sounds like hype, attracts the wrong roles)
- Would you say it out loud at a dinner party? Would you put it on LinkedIn?

Record reactions verbatim `[stated]`. Point out when a reaction conflicts with ground truth (e.g., they love "Head of" but listed people management as an anti-skill) and ask, without judging.

### 4. Generate the next round
Distill reactions into **design constraints**, e.g. "keep 'systems', avoid 'manager', must signal builder not advisor, must be searchable." Show the constraints and let the user edit them. Then generate 4–6 new candidates that satisfy them, using the patterns reference (anchor + modifier, compound, function-over-form, domain-qualified, invented-but-explained). Explain in one line what each new title keeps and drops from earlier rounds.

Repeat steps 2–4 until reactions converge (usually 2–4 rounds). Stop sooner if the user is clearly happy.

### 5. Score finalists
Score the top 3–5 on a 1–5 scale, using the user's own data:

| Criterion | Question |
|---|---|
| Accuracy | Does the portfolio evidence back it up? |
| Energy fit | Does it imply work that energizes, not drains, and avoid anti-skills? |
| Direction | Does it point toward the short-term goal and long-term vision? |
| Findability | Will recruiters and job search actually match it? |
| Distinctiveness | Does it make them memorable rather than interchangeable? |
| Comp signal | Does it map to roles that meet the comp floor? |
| Say-it-out-loud | Does the user feel good saying it? |

Ask the user to weight the criteria (e.g., findability matters more if actively job hunting, distinctiveness more if consulting). Show weighted totals, but let the user overrule the math.

### 6. Build the title stack → `titles/title-stack.md`
Converge on:
- **Anchor title:** searchable, used for job boards and applications.
- **Positioning title:** the expressive version (headline, site, intros).
- **Context variants:** resume, LinkedIn headline, conference bio, intro to founders, intro to enterprise hiring managers, consulting/freelance.
- **Search terms:** titles to search when job hunting (the anchor plus adjacent titles that matched in research).
- **Retired titles:** ones they've moved away from and why.
- **Rationale:** the constraints and reactions that led here, in their words.

Everything in the stack must be user-approved.

## Files

- `titles/candidates.md`: scoreboard of every title explored (title | round | gut score | likes | dislikes | status: active / finalist / chosen / rejected), plus the current design constraints.
- `titles/<slug>.md`: per-title deep dive: researched meaning, example postings, comp notes, reactions, and score.
- `titles/title-stack.md`: the decision.

## Wrap up

Update the README status row and changelog (record old → new anchor title when it changes). Suggest **positioning-studio** to turn the title stack into headlines, bios, and pitches; if research found postings that fit, suggest saving promising companies with **interest-radar**.
