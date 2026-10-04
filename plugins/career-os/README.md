# career-os

A career operating system for technical-creative people whose work doesn't fit a standard title. It builds a shared **career workspace** of markdown files that capture who you are, what pulls you, what you've proven, what to call yourself, and how to say it, so any career-planning agent can work from the same ground truth.

career-os works upstream of job-search tools: it doesn't scan job boards or auto-apply. It produces verified material (evidence, titles, positioning) that you, or a tailoring tool, can use with confidence, because every claim about you traces to something you said, supplied, or approved, and a validator script checks that.

## Install

This plugin is distributed from the `career-os` repo, whose root is a plugin marketplace.

**Codex**

```bash
codex plugin marketplace add buck-0x/career-os
codex plugin add career-os@career-os-marketplace
```

**Claude Code**

```bash
claude plugin marketplace add buck-0x/career-os      # or the repo's git URL
claude plugin install career-os@career-os-marketplace
```

Inside a session, `/plugin marketplace add buck-0x/career-os` and then `/plugin install career-os@career-os-marketplace` does the same.

**Claude app:** add the repo as a plugin marketplace, then install **career-os** from it.

Skills run as `/career-os:ground-truth-interview`, `/career-os:interest-radar`, `/career-os:portfolio-manifest`, `/career-os:title-lab`, and `/career-os:positioning-studio` in Claude Code, or `$career-os:<skill>` in Codex. They also trigger on their own when you ask for that kind of help.

## Skills

| Skill | What it does | Writes to |
|---|---|---|
| **ground-truth-interview** | Interactive interview: values, energizers/drainers, evidence-anchored skills, wins and a hard lesson, a "Not claimed" list, work style, life context, goals, comp, ranked dealbreakers, skill gaps, and optional narrative themes | `ground-truth/` |
| **interest-radar** | Drop links or names of topics, companies, people, titles, and projects; it researches each, asks why it pulls you and who you know near it, maps people's career paths, and surfaces patterns | `interests/` |
| **portfolio-manifest** | Ingests your resume, LinkedIn, site, GitHub, case studies, reviews, and colleagues' "best-self" stories into an evidence inventory, fills gaps by interview, and curates a portfolio manifest with themes, featured projects, a skills matrix, and proof gaps. Also logs single wins as they happen | `portfolio/` |
| **title-lab** | Iterates on job titles: market research per title (O*NET, wage data, live postings), what you like and dislike, new candidates from your reactions, weighted scoring, and a title stack with the recruiter search string and a skim test | `titles/` |
| **positioning-studio** | Turns all of the above into a positioning core (alternatives first) plus headlines, bios, intros, role tailoring, and an interview story bank, each passed through a proof gate, plus a log for testing positioning in the market | `positioning/` |

## Agent

**career-strategist** reads the whole workspace to evaluate opportunities, compare paths, and build plans. It eliminates options by your ranked dealbreakers (naming what ruled each one out), looks for where interest (pull) overlaps with evidence (proof), proposes cheap experiments instead of verdicts, and drafts a decision-journal entry. It's built to give honest assessments and to hold them under pushback.

## Suggested order

1. `ground-truth-interview`
2. `portfolio-manifest` (bring your resume and links)
3. `interest-radar` (anytime; keep feeding it)
4. `title-lab`
5. `positioning-studio`

Every skill works on its own and gets sharper as the other areas fill in.

## The workspace

All skills share one folder, `career-workspace/`, created on first use (you choose where). The layout, file format, and provenance rules (`[stated]`, `[source: …]`, `[researched: …]`, `[suggested → approved]`) are in `shared/workspace-conventions.md` (copied into each skill's `references/`). Facts about you are only ever written from what you said, what you supplied, or what you approved.

## Proof checks

Every outward-facing asset (bio, headline, intro, story bank) carries a proof map tracing each claim to evidence. `validate_workspace.py` (bundled in each skill's `scripts/`; Python 3.9+, no dependencies) checks frontmatter, evidence IDs, proof maps, numbers that don't trace to evidence, mentions of anything on your "Not claimed" list, unapproved suggestions, the changelog, and stale files. Skills run it at the end of each session; in Claude Code a plugin hook also runs it after every write to a workspace file. You can run it yourself:

```bash
python3 <plugin>/shared/validate_workspace.py path/to/career-workspace --stale
```

## Privacy

Your workspace is plain markdown on your own machine; career-os has no server and stores nothing elsewhere. Ground-truth files with life context and compensation are marked `sensitivity: restricted`, and skills keep restricted details out of web searches and outward-facing text. Keep the workspace out of public repositories.
