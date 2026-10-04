---
name: ground-truth-interview
description: Interviews the user to build or update their Personal & Professional Ground Truth (values, energizers and drainers, skills, wins, work style, constraints, goals, compensation, dealbreakers) and saves it as markdown files in the career workspace. Use when the user says "capture my ground truth", "career interview", "who am I professionally", "update my career profile", or starts career planning with no ground truth on file.
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
4. New users: explain the process briefly (7 sections, ~30–45 minutes, can stop and resume anytime), then start.

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
- **Blind spots:** feedback they've heard more than once; where they rely on teammates or systems.

### 3. Professional Capital → `03-professional-capital.md`
- **Domain expertise:** industries and subject matter known deeply.
- **Hard skills:** list, then the user ranks each Expert / Competent / Learning. Never rank for them.
- **Soft skills:** ask for one example for the top two.
- **Trophy case:** top 3 wins, one at a time, as Context / Action / Result. Push for numbers or observable outcomes and their specific role. If `portfolio/evidence-inventory.md` exists, offer evidence items as candidates.
- **Anti-skills:** good at, don't want to do anymore. Flag clearly so downstream agents avoid roles built around them.

### 4. Operating Manual → `04-operating-manual.md`
- Ideal environment (remote/hybrid/office; startup/scale-up/enterprise; pace).
- Culture fit (consensus vs. top-down; analytical vs. bias to action).
- Management preference (ask about best and worst manager and the difference).
- Communication style (async/written, calls, structured meetings).

### 5. The Whole Human → `05-whole-human.md`
- Interests & passions (what they do when nobody pays them). Mention that interest-radar can track specific topics, companies, and people in depth.
- External commitments needing time or boundary protection. Record only the detail they choose to share.
- Geography: location, relocation willingness and conditions, time zones, travel tolerance.

### 6. Trajectory & Non-Negotiables → `06-trajectory-non-negotiables.md`
- **Short-term goal (1–2 yrs):** push for role, scope, company type.
- **Long-term vision (5–10 yrs):** directional is fine; say so.
- **Financials:** minimum base, ideal target, comp basis (base vs. total), currency, risk tolerance (need cash stability / balanced / will trade cash for meaningful equity).
- **Dealbreakers:** separate true dealbreakers from strong preferences.

### 7. Skill Gaps & Development → `07-skill-gaps-development.md`
- **What to learn:** compare the short-term goal with their skills. Offer candidate gaps labeled as suggestions; record only confirmed ones.
- **How they learn best:** trial by fire, courses, mentors, reading, building projects.

### 1B. Executive Summary (synthesis) → `01-executive-summary.md`
- Draft 2 variations of a 2–3 sentence elevator pitch (who they are, superpower, what they're looking for) using only their facts. They pick, edit, or rewrite; save the approved version as a quote.
- **Tensions check:** point out contradictions you noticed (e.g., max earnings vs. a long-hours dealbreaker; an energizer that conflicts with the ideal environment). Ask how they think about each and record their answer. Don't resolve tensions for them.

## File format details

Follow the conventions file, plus:
- One `##` heading per field, named exactly as above.
- Hard skills as a table: `| Skill | Level |`.
- Trophy case as `### Win 1: <title>` with **Context:** / **Action:** / **Result:**.
- Dealbreakers as `### Hard dealbreakers` and `### Strong preferences`.
- Financials as explicit fields: `Minimum base:`, `Ideal target:`, `Comp basis:`, `Currency:`, `Risk tolerance:`.
- Quote the user verbatim (`> `) for value definitions, the elevator pitch, and dealbreakers.

## Wrap up

Update the README status row and open questions, append to the changelog, list any partial sections, and suggest the next skill: usually **portfolio-manifest** (to back the trophy case with evidence) or **title-lab** (if they struggled to name what they do). Suggest a re-run every ~6 months or after a major change.

## Tone

Curious, direct, encouraging. Celebrate specific answers, gently challenge generic ones, never judge preferences. The user should do most of the talking.
