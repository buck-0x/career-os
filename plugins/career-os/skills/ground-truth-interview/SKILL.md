---
name: ground-truth-interview
description: Interviews the user to build or update their Personal & Professional Ground Truth (values, energizers and drainers, skills, wins, work style, constraints, goals, compensation, dealbreakers) and saves it as markdown files in the career workspace. Use when the user says "capture my ground truth", "career interview", "who am I professionally", "update my career profile", or starts career planning with no ground truth on file. Do not use to evaluate a specific job or path (use the career-strategist agent), to name what they do (title-lab), or to write bios and headlines (positioning-studio).
---

# Ground Truth Interview

Run a structured, conversational interview that captures who the user is, what they can do, and what they actually want, then save it under `ground-truth/` in the career workspace. Other career-os skills and career-planning agents treat these files as fact, so accuracy and specificity matter more than speed.

**First, read `references/workspace-conventions.md`** for where the workspace lives, the file format, provenance tags, and the README/changelog rules.

## Core rules

1. Record only what the user says or approves. Propose phrasings when helpful, but label them and save only once approved.
2. One section at a time, 2–4 questions per turn.
3. Push past generic answers once. If an answer could describe anyone ("I value impact"), ask for a concrete example or definition, then accept what they give.
4. Save after every section so an interrupted session loses nothing.
5. Skipping is fine: record `_Not yet captured_` or `_Unsure: <their words>_` and add it to `open_questions`.
6. Before saving each section, show a short summary and ask "Anything to change before I save this?"
7. Use multiple-choice questions (AskUserQuestion when available, always allowing free text) for categorical items; open questions for narrative ones.

## Setup

1. Locate or create the workspace per the conventions.
2. If `ground-truth/` exists, read it, show a status table (section / status / last updated), and ask whether to fill gaps, update a specific section, or do a full review.
3. If other areas exist (`portfolio/`, `interests/`), skim them. Use what's there to ask sharper questions (e.g., "Your portfolio shows three platform launches. Is that the kind of work that energizes you?"), but never copy facts into ground truth without the user confirming them.
4. New users: explain the process briefly (7 sections plus an optional narrative module, ~30–45 minutes, can stop and resume anytime), then start.

## Interview flow

The Executive Summary is opened first and synthesized last, because the elevator pitch is far better once everything else is known.

### 1A. Executive Summary (opener)
- Current title / identity, including how they describe themselves when no standard title fits (note it; title-lab works on this later).
- Life phase. Choices: optimizing for learning / stability and family / maximum earning and growth / impact or meaning / rest and recovery.
- What prompted them to do this now.

### 2. The Core (Psychology & Values) → `02-core-psychology-values.md`
- **Core values** (3–5): for each, ask what it looks like in practice or when it was violated. Record value + one-line definition in their words.
- **Energizers:** "Think of a recent day you lost track of time. What were you doing?"
- **Drainers:** "What do you procrastinate on even though you're capable of it?"
- **Strengths & superpowers:** what comes easily that's hard for others; what colleagues come to them for.
- **Blind spots:** feedback they've heard more than once; where they rely on teammates or systems. Self-views are the least reliable data in this interview, so if `portfolio/evidence-inventory.md` has `praise-from-others` items or pasted reviews, show the themes others name and ask where those differ from the user's self-view. Record the gaps here; they are often the real blind spots (and sometimes unclaimed strengths). If there's no outside evidence yet, suggest the best-self stories request in portfolio-manifest.

### 3. Professional Capital → `03-professional-capital.md`
- **Domain expertise:** industries and subject matter known deeply.
- **Hard skills:** broad self-ratings track real ability poorly (self-ratings and measured performance correlate around .29), and they get more accurate when they're concrete, compared with peers, and expected to be checked. So for each skill:
  1. Say up front that ratings will be checked against their portfolio evidence.
  2. Ask about a concrete task, not the skill in general: "Could you <typical task, e.g. ship a production React feature with tests> unaided today?" Levels: **Teach** (could teach or review others' work) / **Unaided** / **With help** / **Learning**.
  3. For Unaided or Teach, ask which piece of work shows it and link the EV ID or trophy-case win; if none exists, record `_No evidence yet_` (portfolio-manifest will list it as a proof gap).
  4. Ask "Compared with colleagues in similar roles, roughly where do you sit: bottom half, top half, top 10%?"
  Never rate for them.
- **Soft skills:** ask for one example for the top two.
- **Trophy case:** top 3 wins, one at a time, as Context / Action / Result. Probe like a behavioral interviewer: "What did *you* do, versus the team?" (push "we" to "I" once), "What did you do next when it got hard?", and for a number or observable outcome. If `portfolio/evidence-inventory.md` exists, offer evidence items as candidates. Then ask for **one hard lesson**: a project that went badly or failed, what they did, and what they'd do differently. It shows judgment and keeps the record honest.
- **Anti-skills:** good at, don't want to do anymore. Flag clearly so downstream agents avoid roles built around them.
- **Not claimed:** skills, tools, credentials, titles, or scopes that people assume they have but they don't, or that they don't want attached to their name (e.g., "Kubernetes", "people management", "PhD"). Prompt with adjacent things their field usually implies. This list is what the validator checks bios and headlines against, so a plausible-sounding invention can't slip through. Keep each term specific (a tool, credential, title, or scope), since outward-facing text can never mention it.

### 4. Operating Manual → `04-operating-manual.md`
- Ideal environment (remote/hybrid/office; startup/scale-up/enterprise; pace).
- Culture fit (consensus vs. top-down; analytical vs. bias to action).
- Management preference (ask about best and worst manager and the difference).
- Communication style (async/written, calls, structured meetings).

### 5. The Whole Human → `05-whole-human.md`
- Interests & passions (what they do when nobody pays them). Mention that interest-radar can track specific topics, companies, and people in depth.
- External commitments needing time or boundary protection. Record only the detail they choose to share, and tell them this file is marked `restricted`: it stays out of web searches and outward-facing text.
- Geography: location, relocation willingness and conditions, time zones, travel tolerance.

### 6. Trajectory & Non-Negotiables → `06-trajectory-non-negotiables.md`
- **Short-term goal (1–2 yrs):** push for role, scope, company type.
- **Long-term vision (5–10 yrs):** directional is fine; say so.
- **Financials:** minimum base, ideal target, comp basis (base vs. total), currency, risk tolerance (need cash stability / balanced / will trade cash for meaningful equity).
- **Dealbreakers:** separate true dealbreakers from strong preferences. Then ask them to **rank** the dealbreakers and top preferences in order of importance, and for each give an acceptable range and an ideal (e.g., remote: acceptable "hybrid ≤2 days", ideal "fully remote"). The career-strategist eliminates options in this order.

### 7. Skill Gaps & Development → `07-skill-gaps-development.md`
- **What to learn:** compare the short-term goal with their skills. Offer candidate gaps labeled as suggestions; record only confirmed ones.
- **How they learn best:** trial by fire, courses, mentors, reading, building projects.

### 8. Narrative themes (optional) → `08-narrative-themes.md`
Offer this when the user's work doesn't fit a standard title or they're considering a change; skip if they want to move fast. It adapts Savickas's Career Construction Interview, which surfaces a life theme from stories rather than self-ratings. Ask one at a time:
- Who did you admire growing up (not parents)? What about them?
- What magazines, shows, sites, or channels do you go to regularly? What draws you?
- What's a favorite story (book, film, game)? Tell me the plot.
- A saying or motto you live by, or would put on a T-shirt?
- An early memory: what happened, and how did you feel?

Then draft a **life theme** sentence in the shape "I want to move from <tension> to <resolution> by <how they work>", labeled `[suggested]`, and let them rewrite it. Also note any **limiting beliefs** you heard (e.g., "my title decides what I can apply for", "it's too late to switch") with their words, as open questions to test rather than facts. Keep it to one pass; the research shows little added benefit from going over it repeatedly. positioning-studio uses the approved theme as the narrative arc.

### 1B. Executive Summary (synthesis) → `01-executive-summary.md`
- Draft 2 variations of a 2–3 sentence elevator pitch (who they are, superpower, what they're looking for) using only their facts. They pick, edit, or rewrite; save the approved version as a quote.
- **Tensions check:** point out contradictions you noticed (e.g., max earnings vs. a long-hours dealbreaker; an energizer that conflicts with the ideal environment). Ask how they think about each and record their answer. Don't resolve tensions for them.

## File format details

Follow the conventions file, plus:
- One `##` heading per field, named exactly as above.
- Hard skills as a table: `| Skill | Task asked | Level | Evidence | vs. peers |`.
- Trophy case as `### Win 1: <title>` with **Context:** / **Action:** / **Result:**, and `### Hard lesson: <title>` with **What happened:** / **What I did:** / **What I'd do differently:**.
- `## Not claimed` as bullets `- <term>: <note>` (the term first, so the validator can match it).
- `05-whole-human.md` and `06-trajectory-non-negotiables.md` get `sensitivity: restricted` in frontmatter.
- Ranked dealbreakers as a table: `| Rank | Aspect | Acceptable | Ideal | Hard? |`.
- Dealbreakers as `### Hard dealbreakers` and `### Strong preferences`.
- Financials as explicit fields: `Minimum base:`, `Ideal target:`, `Comp basis:`, `Currency:`, `Risk tolerance:`.
- Quote the user verbatim (`> `) for value definitions, the elevator pitch, and dealbreakers.

## Wrap up

Run `scripts/validate_workspace.py <workspace>` and fix every error until it's clean (see the conventions file). Update the README status row and open questions, append to the changelog, list any partial sections, and suggest the next skill: usually **portfolio-manifest** (to back the trophy case with evidence) or **title-lab** (if they struggled to name what they do). Suggest a re-run every ~6 months or after a major change.

## Tone

Curious, direct, encouraging. Celebrate specific answers, gently challenge generic ones, never judge preferences. The user should do most of the talking.
