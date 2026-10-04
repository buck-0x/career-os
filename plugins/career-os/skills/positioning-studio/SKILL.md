---
name: positioning-studio
description: 'Turns the user''s ground truth, portfolio evidence, interests, and title stack into positioning they can use to sell themselves: a core positioning statement, proof points, LinkedIn headline and About, bios of several lengths, intros tailored to specific audiences, answers to "so what do you do?", and an interview story bank, every claim traced to evidence. Use when the user says "how do I sell myself", "write my bio/headline/About section", "pitch me to X", "how should I describe what I do", "tailor my story for this role/company", or "prep my interview stories". Do not use to choose the title itself (title-lab) or to decide whether an opportunity is a good fit (career-strategist agent).'
---

# Positioning Studio

Help the user explain what they do and why it matters, especially when no standard title captures it. Positioning answers three questions for a specific audience: **What are you? What problem do you solve, for whom? Why you (proof)?** Everything here must be grounded in workspace facts; nothing gets invented to sound impressive.

This skill is the most likely place for fabrication to happen. Research on AI resume rewriting found unsupported claims in nearly every unguarded output and in half of outputs even with prompt guardrails, so this skill works as a **proof gate**: every claim is mapped to evidence, the user reviews claim by claim, and a validator script checks the result.

**First, read `references/workspace-conventions.md`** for workspace location, file format, provenance tags, proof maps, the "Not claimed" list, the coaching rules, and README/changelog rules.

## Inputs

Read what exists:
- `ground-truth/`: especially the executive summary, strengths, values, anti-skills, **Not claimed**, goals, dealbreakers, and `08-narrative-themes.md` (the life theme is the narrative arc)
- `portfolio/evidence-inventory.md` and `manifest.md`: throughline, themes, featured projects
- `titles/title-stack.md`: anchor, positioning title, recruiter OR-cluster
- `interests/index.md` patterns (the language of what attracts them)
- `positioning/` from earlier sessions, including `experiments.md` results

If key inputs are missing, say which, and either run a short substitute interview (what they do, best 3 projects with results, who they want to work with) or suggest the skill that fills the gap. Facts from a substitute interview are written to `portfolio/evidence-inventory.md` as new `[stated]` EV items before they're used. Positioning without proof is a slogan, so if there's no portfolio, keep claims modest and note the proof gap.

## Step 1: Core positioning (once, then refine)

Adapted from April Dunford's product-positioning method, which works in a deliberate order: alternatives first, category last.

1. **Competitive alternatives.** Ask: "If you didn't exist, what would the people who hire you do instead?" Typical answers: hire a frontend engineer *and* a designer; use an agency; promote someone internal; ship without the polish; buy a tool. List the real ones. Drop **phantom competitors**: alternatives the user worries about that never actually come up when someone is choosing.
2. **What they have that the alternatives don't.** Capabilities and combinations, each traced to EV items.
3. **Value.** What that difference gets the reader (speed, quality, fewer handoffs, revenue), in the reader's terms.
4. **Best-fit audience.** Who cares most about that value. The inverse becomes **Not for**: the readers for whom an alternative is genuinely better, plus anti-skills and dealbreakers.
5. **Category.** The frame the audience will file them under. Use the anchor from the title stack; an invented category means teaching every reader a new word, so only use one with a gloss.
6. **Spanning check.** Readers discount people who span categories unless they're clearly relevant to the reader's problem. For each audience, make the user a legible specialist on **one** axis (usually the function) while the other axis (domain, medium) is the differentiator; lead with the 2–3 proofs most relevant to that reader; and tell the career as an arc (the approved life theme helps) rather than a list.

Draft the **positioning core**:
- **For:** who they serve
- **Instead of:** the real alternatives
- **Problem:** the problem they're great at solving
- **What I am:** anchor + positioning title from the title stack
- **How I'm different:** the rare combination, versus the alternatives
- **Proof:** 2–3 featured projects or metrics (EV IDs)
- **Not for:** work and readers they don't want

Offer 3 distinct angles on the core (e.g., lead with the problem, lead with the hybrid, lead with the result) so they react to real options rather than a single draft. Capture likes and dislikes as in title-lab, iterate, and save the approved core with its proof map.

## Step 2: Assets

Generate only what the user asks for; offer the menu:
- **"So what do you do?"** answers: 1 sentence, and a 30-second spoken version (write for speech: short sentences, no jargon stacks)
- **LinkedIn headline** (≤220 characters; anchor title first so it matches recruiter title searches, then positioning) and **About** section
- **Bios:** 25 / 75 / 150 words, third person and first person
- **Audience intros:** tailored to a named audience (founders, enterprise hiring managers, recruiters, potential clients, conference organizers, a specific company)
- **Role or company tailoring:** given a job posting or a company (from `interests/companies/` or a link), map their proof to what that reader cares about, flag weak spots honestly, and draft an intro or cover-note opening. Run the **trap check** below.
- **Resume summary** and **portfolio site hero copy**
- **Interview story bank** (`assets/story-bank.md`): 5–8 stories for common questions (a hard problem, a conflict, a failure, leading without authority, a cross-discipline win). Each is built **only from approved EV items and trophy-case wins**, never from earlier drafts, so a mistake in one asset can't spread into interview answers. Format per story: question it answers / Situation / Task / Action / Result / Reflection (what they learned) / EV IDs.

If a writing-style profile skill is available for the user, use it so drafts sound like them.

## Writing rules

- Specific over grand: name the problem, the result, the number. Cut "passionate", "results-driven", "innovative", "visionary", "spearheaded".
- Lead with what the reader cares about, not the user's history.
- The hybrid is a feature, framed by the spanning check: one clear specialty plus the rare second axis.
- Every claim must trace to a workspace fact. Generated text (earlier bios, alternates) is never a source.
- **Keep qualifiers.** If the evidence says "co-led", "assisted", "basic", or "contributed to", the asset says so too.
- Never mention anything on the **Not claimed** list.
- Match their tone (from ground truth and how they talk in session), not generic LinkedIn voice.
- Never imply experience, titles, or results they don't have.

## Proof gate (before saving any asset)

1. **Proof map.** End the asset with `## Proof map` (`| Claim | Evidence |`). Every claim, and every number, gets a row citing EV IDs, a ground-truth link, or a provenance tag.
2. **Claim-by-claim review.** Show the user a table of each claim next to its evidence, and flag:
   - **Qualifier drops:** the asset is stronger than the evidence ("led" vs. "co-led"; "expert" vs. "Unaided").
   - **New claims:** anything not in the evidence at all.
   These are the two kinds of fabrication human reviewers miss most often, so point at them explicitly; don't rely on the user to spot them.
3. **Trap check (tailoring only).** List every requirement in the posting and mark each: *evidenced* (with EV ID), *partially*, or *not evidenced*. Requirements that are not evidenced never appear in the draft as things the user has; name them instead as gaps the user can address honestly (a transferable proof, or "learning X").
4. **Stress test:**
   - **Skim test:** what would a busy reader remember after 5 seconds?
   - **Wrong-fit test:** would this attract roles built on their anti-skills or dealbreakers?
   - **Swap test:** could a generic person in their field say the same thing? If yes, sharpen with something only they have.
   - **Alternatives test:** does it say why them instead of the real alternatives from Step 1?
5. Save only after the user approves the claims, then run `scripts/validate_workspace.py <workspace>` and fix every error. Never resolve an error by inventing evidence; ask, or cut the claim.

## Coaching stance

Follow the coaching rules in the conventions file. In particular: when the user asks "is this good?", give the honest assessment first. If they push back on a critique, keep it unless they bring new evidence or a preference you didn't know about. If they ask you to add a claim that isn't in the evidence, ask for the evidence (and record it as a `[stated]` EV item) rather than writing it in.

## Market feedback (`positioning/experiments.md`)

Positioning is a hypothesis until the market responds. Offer to set up an experiments log:
- **Headline tests:** change one thing at a time (anchor title, lead claim, audience), keep it 2–4 weeks, and record LinkedIn's *Search appearances* count and the searchers' job titles from the user's profile analytics. Compare the searcher titles to the **For** field: if the wrong people are finding them, the wrong-fit test failed in the real world. It's a before/after comparison, not a true A/B test, so note anything else that changed (posting more, a job change).
- **Message tests:** try 2–3 versions of the 1-sentence answer in conversations with people who match **For**; ask them to say back what the user does and what they'd hire them for. Record what they repeat and what they get wrong.
- **Inbound log:** date, who reached out, which title or phrase they used, and whether it was a fit.

Format: one `### <date>: <hypothesis>` entry per experiment with **Change**, **Window**, **Result**, **Decision**. Review results at the start of later sessions and refine the core accordingly.

## Files

- `positioning/positioning.md`: approved core, the alternatives and angles considered, and the proof map. Frontmatter `derived_from:` lists its EV IDs.
- `positioning/assets/<audience-or-channel>.md`: one file per audience or channel (e.g., `linkedin.md`, `founders.md`, `acme-corp.md`, `story-bank.md`), each with the approved version first, alternates below, and its proof map last.
- `positioning/experiments.md`: market tests and inbound log.

## Wrap up

Run the validator until clean. Update the README status row and changelog. Suggest the next move: closing a proof gap (a case study or project via portfolio-manifest), testing a title variant in title-lab, starting a headline experiment, or applying the positioning to companies on their interest radar.
