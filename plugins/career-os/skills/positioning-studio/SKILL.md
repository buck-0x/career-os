---
name: positioning-studio
description: Turns the user's ground truth, portfolio evidence, interests, and title stack into positioning they can use to sell themselves: a core positioning statement, proof points, LinkedIn headline and About, bios of several lengths, intros tailored to specific audiences, and answers to "so what do you do?". Use when the user says "how do I sell myself", "write my bio/headline/About section", "pitch me to X", "how should I describe what I do", or "tailor my story for this role/company".
---

# Positioning Studio

Help the user explain what they do and why it matters, especially when no standard title captures it. Positioning answers three questions for a specific audience: **What are you? What problem do you solve, for whom? Why you (proof)?** Everything here must be grounded in workspace facts; nothing gets invented to sound impressive.

**First, read `references/workspace-conventions.md`** for workspace location, file format, provenance tags, and README/changelog rules.

## Inputs

Read what exists:
- `ground-truth/` especially the executive summary, strengths, values, anti-skills, goals, dealbreakers
- `portfolio/manifest.md` throughline, themes, featured projects
- `titles/title-stack.md`
- `interests/index.md` patterns (the language of what attracts them)
- `positioning/` from earlier sessions

If key inputs are missing, say which, and either run a short substitute interview (what they do, best 3 projects with results, who they want to work with) or suggest the skill that fills the gap. Positioning without proof is a slogan, so if there's no portfolio, keep claims modest and note the proof gap.

## Step 1: Core positioning (once, then refine)

1. Draft the **positioning core** in this structure:
   - **For:** who they serve (audience/company type/problem owner)
   - **Problem:** the problem they're great at solving
   - **What I am:** anchor + positioning title from the title stack
   - **How I'm different:** the combination of disciplines or experiences that's rare (the hybrid is the asset)
   - **Proof:** 2–3 featured projects or metrics (cite EV IDs or projects)
   - **Not for:** work they don't want (anti-skills, dealbreakers). This keeps outbound language from attracting the wrong roles.
2. Offer 3 distinct angles on the core (e.g., lead with the problem, lead with the hybrid, lead with the result) so they react to real options rather than a single draft.
3. Capture likes and dislikes as in title-lab, iterate, and save the approved core.

## Step 2: Assets

Generate only what the user asks for; offer the menu:
- **"So what do you do?"** answers: 1 sentence, and a 30-second spoken version (write for speech: short sentences, no jargon stacks)
- **LinkedIn headline** (≤220 characters; anchor title + positioning, scannable) and **About** section
- **Bios:** 25 / 75 / 150 words, third person and first person
- **Audience intros:** tailored to a named audience (founders, enterprise hiring managers, recruiters, potential clients, conference organizers, a specific company)
- **Role or company tailoring:** given a job posting or a company (from `interests/companies/` or a link), map their proof to what that reader cares about, flag weak spots honestly, and draft an intro or cover-note opening
- **Resume summary** and **portfolio site hero copy**

If a writing-style profile skill is available for the user, use it so drafts sound like them.

## Writing rules

- Specific over grand: name the problem, the result, the number. Cut "passionate", "results-driven", "innovative", "visionary".
- Lead with what the reader cares about, not the user's history.
- The hybrid is a feature: say plainly what combination they bring and why that combination matters for the reader's problem.
- Every claim must trace to a workspace fact; mark anything that doesn't with `[needs proof]` and ask.
- Match their tone (from ground truth and how they talk in session), not generic LinkedIn voice.
- Never imply experience, titles, or results they don't have.

## Stress test

Before saving any asset, run a quick check and share the result:
- **Skim test:** what would a busy reader remember after 5 seconds?
- **Wrong-fit test:** would this attract roles built on their anti-skills or dealbreakers?
- **Proof test:** list each claim and its source.
- **Swap test:** could a generic person in their field say the same thing? If yes, sharpen with something only they have.

## Files

- `positioning/positioning.md`: approved core, the angles considered, and the proof map (claim → evidence).
- `positioning/assets/<audience-or-channel>.md`: one file per audience or channel (e.g., `linkedin.md`, `founders.md`, `acme-corp.md`), each with the approved version first and alternates below.

## Wrap up

Update the README status row and changelog. Suggest the next move: closing a proof gap (a case study or project via portfolio-manifest), testing a title variant in title-lab, or applying the positioning to companies on their interest radar.
