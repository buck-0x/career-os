# career-os

A career operating system for technical-creative people whose work doesn't fit a standard title. It builds a shared **career workspace** of markdown files that capture who you are, what pulls you, what you've proven, what to call yourself, and how to say it, so any career-planning agent can work from the same ground truth.

## Install

This plugin is distributed from the `career-os` repo, whose root is a plugin marketplace.

**Claude Code**

```bash
claude plugin marketplace add <owner>/career-os      # or the repo's git URL
claude plugin install career-os@career-os-marketplace
```

Inside a session, `/plugin marketplace add <owner>/career-os` and then `/plugin install career-os@career-os-marketplace` does the same.

**Claude app:** add the repo as a plugin marketplace, then install **career-os** from it.

Skills run as `/career-os:ground-truth-interview`, `/career-os:interest-radar`, `/career-os:portfolio-manifest`, `/career-os:title-lab`, and `/career-os:positioning-studio`, and also trigger on their own when you ask for that kind of help.

## Skills

| Skill | What it does | Writes to |
|---|---|---|
| **ground-truth-interview** | Interactive interview: values, energizers/drainers, skills, wins, work style, life context, goals, comp, dealbreakers, skill gaps | `ground-truth/` |
| **interest-radar** | Drop links or names of topics, companies, people, titles, and projects; it researches each, asks why it pulls you, and surfaces patterns | `interests/` |
| **portfolio-manifest** | Ingests your resume, LinkedIn, site, GitHub, case studies, reviews, etc. into an evidence inventory, fills gaps by interview, and curates a portfolio manifest with themes, featured projects, a skills matrix, and proof gaps | `portfolio/` |
| **title-lab** | Iterates on job titles: market research per title, what you like and dislike, new candidates generated from your reactions, weighted scoring, and a final title stack | `titles/` |
| **positioning-studio** | Turns all of the above into a positioning core plus headlines, bios, "what do you do" answers, and audience- or role-specific intros, each stress-tested for proof | `positioning/` |

## Agent

**career-strategist** reads the whole workspace to evaluate opportunities, compare paths, and build plans. It applies your dealbreakers and comp floor as filters and looks for where interest (pull) overlaps with evidence (proof).

## Suggested order

1. `ground-truth-interview`
2. `portfolio-manifest` (bring your resume and links)
3. `interest-radar` (anytime; keep feeding it)
4. `title-lab`
5. `positioning-studio`

Every skill works on its own and gets sharper as the other areas fill in.

## The workspace

All skills share one folder, `career-workspace/`, created on first use (you choose where). The layout, file format, and provenance rules (`[stated]`, `[source: …]`, `[researched: …]`, `[suggested → approved]`) are in `skills/*/references/workspace-conventions.md`. Facts about you are only ever written from what you said, what you supplied, or what you approved.
