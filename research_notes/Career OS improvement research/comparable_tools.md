# Comparable AI and open-source career tools (state as of Oct 2026)

## Which open-source repos offer LLM/agent career tooling (Claude Code skills/plugins, tailoring agents, career-ops style systems, JSON Resume, tracking agents)?

### Takeaway
The open-source space is dominated by one breakout project, santifer/career-ops (launched Apr 4 2026; about 73K stars and 13.8K forks by mid-2026), which is a full job-search pipeline (scan, evaluate/score, tailor CV PDF, track, interview prep, negotiation) running inside Claude Code/Codex and other CLIs. Around it sits a long tail of smaller Claude Code skill packs focused on resume tailoring with explicit anti-fabrication/provenance rules; one of them (r-hedayati/claude-resume-skills) uses a provenance marker scheme very close to career-os's tags. Almost none of them address career exploration or identity (who am I, what title fits), which is career-os's center of gravity.

### Cited Findings

**santifer/career-ops (flagship comparable)**
- Built by Santiago Fernandez de Valderrama in March 2026 while job hunting; public launch April 4 2026; 35K stars in one week; 73.2K+ stars and 13.8K+ forks by July 2026; 4,900+ Discord users; author evaluated 740 offers, sent 68 applications, landed a Head of Applied AI role, later went full-time on the project — [santifer.io](https://santifer.io/career-ops-system)
- README (fetched Oct 2026): 73.4K stars, 13.8K forks, MIT, 2,615 commits; runs on Claude Code, Codex, OpenCode, Gemini/Antigravity CLI, Copilot, and others "via open Agent Skill Standard" — [GitHub santifer/career-ops](https://github.com/santifer/career-ops)
- Modes include: evaluation (`/career-ops {JD}`, `pipeline`, `oferta(s)`), documents (`pdf`, `latex`, `cover`, `email`), research (`deep`, `contacto`, `discover`, `company:funded`), interview (`interview-prep`, `interview/plan`, `interview/practice`, `interview/debrief`, `interview-redflag`), tracking (`tracker`, `patterns`, `outcome`, `calibrate`, `followup`, `reply-watch`), skill development (`training`, `project`, `upskill`, `titles`), and `offer-prep` (contract review) — [GitHub santifer/career-ops](https://github.com/santifer/career-ops)
- Evaluates each job into an A-H structured report with a 1-5 global score (CV match, level strategy, comp research, legitimacy checks such as repost detection) — [GitHub santifer/career-ops](https://github.com/santifer/career-ops)
- Scans 45+ company career portals via Playwright; batch mode processes many URLs in parallel; also added a Hacker News "Who is hiring?" provider via Algolia — [career-ops search summary / santifer.io](https://santifer.io/career-ops-system); [trendshift](https://trendshift.io/repositories/25195)
- Data model: `cv.md`, optional `article-digest.md` for proof points, `config/profile.yml`, `data/applications.md` tracker, `reports/`, `output/` PDFs; data dir overridable via env vars — [GitHub santifer/career-ops](https://github.com/santifer/career-ops)
- Anti-hallucination: blocks a PDF whose numbers or facts appear in neither the CV nor the article digest unless overridden; "reformulate, never fabricate"; open issues track title and faithfulness validation — [GitHub santifer/career-ops](https://github.com/santifer/career-ops)
- STAR+Reflection story bank accumulates across evaluations; contact discovery drafts LinkedIn messages to hiring managers; "the script never POSTs" (draft-only, human submits) — [GitHub santifer/career-ops](https://github.com/santifer/career-ops)
- Uses six fixed role "archetypes" (AI Platform/LLMOps, Agentic Workflows, Technical AI PM, Solutions Architect, Field Developer, Transformation Lead) to frame CVs; design lessons: "automate analysis, not decisions", dedup beats scoring tweaks, parallel batch beats sequential — [santifer.io](https://santifer.io/career-ops-system)
- Many forks repackage it (e.g., JeremyBanta/career-ops, ymys/career-ops-claude, LAR3labs/reqmancer "Private career-ops setup") — [GitHub JeremyBanta](https://github.com/JeremyBanta/career-ops); [GitHub LAR3labs/reqmancer](https://github.com/LAR3labs/reqmancer)
- Project's own blog argues mass auto-apply "burns your reputation" and positions career-ops as human-in-the-loop — [career-ops.org blog](https://career-ops.org/blog/can-an-ai-agent-run-your-job-search)

**r-hedayati/claude-resume-skills** (closest to career-os provenance model)
- 19 Claude Code skills: pipeline (`/apply`, `/job-description-analyzer`, `/resume-gap-analyzer`, `/resume-tailor`, `/resume-ats-optimizer`, `/master-resume-updater`, `/cover-letter-generator`) and supporting (`/writing-style`, `/experience-discovery`, `/resume-bullet-writer`, `/resume-quantifier`, `/resume-version-manager`, `/interview-prep-generator`, `/linkedin-profile-optimizer`, `/application-form-filler`, `/cold-email-writer`, `/salary-negotiation-prep`, etc.); outputs compiled LaTeX — [GitHub r-hedayati/claude-resume-skills](https://github.com/r-hedayati/claude-resume-skills)
- Every claim carries a marker: [V] verified (documented source), [S] self-reported, [?] unsourced (rejected); also blocks hidden text / prompt injection, verifies PDF text extraction, max two pages; argues ATS-beating is "largely fictional" and optimizes for semantic match and verifiable specificity — [GitHub r-hedayati/claude-resume-skills](https://github.com/r-hedayati/claude-resume-skills)

**proficientlyjobs/proficiently-claude-skills**
- 407 stars, 71 forks (Oct 2026); MIT; skills: setup (resume, preferences, LinkedIn contacts, work-history interview), job-search, tailor-resume, cover-letter, network-scan (scans contacts' companies for matching openings), apply (autofills Greenhouse/Lever/Workday via Claude in Chrome), and a Telegram headless loop; data in `~/.proficiently/` with one folder per application — [GitHub proficiently](https://github.com/proficientlyjobs/proficiently-claude-skills)

**Other Claude Code skill repos**
- varunr89/resume-tailoring-skill: "truth-preserving optimization", conversational experience-discovery interview to surface undocumented work, multi-job batch (3-5 similar roles, claims 11-27% time saved), outputs MD/DOCX/PDF + interview prep; expects a library of 10+ prior resumes — [GitHub varunr89](https://github.com/varunr89/resume-tailoring-skill)
- javiera-vasquez/claude-code-job-tailor: write experience once in YAML; agents rank JD requirements and select relevant achievements; tailored PDF in under 60s — [GitHub javiera-vasquez](https://github.com/javiera-vasquez/claude-code-job-tailor)
- Paramchoudhary/ResumeSkills: ATS optimization, bullet writing, JD analysis, tailoring, cover letters, LinkedIn optimization, interview prep, salary negotiation — [GitHub Paramchoudhary](https://github.com/Paramchoudhary/ResumeSkills)
- StephanieKoehl/resume-best-practices: resume guide + Claude Code skill (XYZ bullet formula, print-to-PDF specs) — [GitHub StephanieKoehl](https://github.com/StephanieKoehl/resume-best-practices)
- GitHub topic page aggregates more — [github.com/topics/resume-tailoring](https://github.com/topics/resume-tailoring)

**JSON Resume ecosystem**
- Official `@jsonresume/mcp` server lets Cursor/Windsurf agents analyze a codebase and update a JSON Resume stored in a GitHub Gist (uses GITHUB_TOKEN + OPENAI_API_KEY; Zod validation); updated June 15 2025 — [PulseMCP](https://www.pulsemcp.com/servers/jsonresume-enhancer); [Glama](https://glama.ai/mcp/servers/jsonresume/mcp)

**Open/dev-oriented brag tooling**
- BragDoc: CLI analyzes git commits locally with AI, extracts achievements, auto-groups into workstreams with 1-5 impact ratings, exports PDF/Markdown for reviews; free tier + paid AI — [bragdoc.ai](https://www.bragdoc.ai/)
- Brag AI turns GitHub activity into human-readable achievements — [ruancomelli.com/brag-ai](https://www.ruancomelli.com/brag-ai/)

### Inferences
- career-ops is the de facto reference point; anyone evaluating career-os will compare it. Its scope is "job search ops" (downstream), whereas career-os is "career identity and evidence" (upstream). This is complementary rather than overlapping; career-os could position as the upstream layer that produces the `cv.md` / `article-digest.md` / profile that career-ops consumes.
- career-ops has a `titles` mode and fixed archetypes; career-os's title-lab (iterative, reaction-driven, for people who fit no archetype) is a sharper differentiator against that.
- Provenance tagging is becoming an expected norm in this niche ([V]/[S]/[?] in claude-resume-skills; fact-gating in career-os competitors). career-os's tags are richer (source vs researched vs suggested-then-approved), but competitors enforce them at output time (blocking PDFs); career-os may want an equivalent "proof gate" check.
- Cross-CLI portability via the Agent Skill standard is table stakes (career-ops supports ~9 CLIs).

### Gaps
- Star counts and last-commit dates for claude-resume-skills, varunr89, javiera-vasquez, Paramchoudhary repos were not shown on fetched pages; not verified.
- Did not find a specific Hacker News thread with substantive criticism of career-ops; only a claim that star spikes correlate with HN/Reddit posts.
- No open-source project found that targets career exploration/identity for non-standard profiles (values, energizers, title discovery); absence is a finding but search was not exhaustive.

## Which commercial products do career exploration, positioning, or evidence/achievement capture, and what stands out?

### Takeaway
Commercial tools split into (a) job-search suites (Teal, Huntr, Careerflow, Simplify) centered on tracking, tailoring, autofill, and LinkedIn optimization; (b) interview tools (Final Round AI, Yoodli); (c) a growing "brag doc" category (BragDoc, BragBook, BragJournal, BragLog, TrackToBrag) for continuous win logging; and (d) a few exploration tools (Kickresume Career Map, Google Career Dreamer) that map background to career paths and generate a "career identity statement". None combine deep self-discovery, evidence provenance, and title iteration as career-os does.

### Cited Findings
- Teal: resume builder with JD keyword analysis, match score, Chrome-extension job tracker (bookmark from any board), CRM-style dashboard linking saved jobs to tailored resumes with follow-up dates and recruiter names, AI cover letters, AI interview practice — [Rezi review of Teal](https://www.rezi.ai/posts/teal-review); [resumehog](https://resumehog.com/blog/posts/teal-hq-review-april-2026-is-the-job-tracker-worth-your-time.html)
- Huntr: Kanban tracker with CRM layer (cards hold notes, tasks, contacts, interaction timeline), Chrome extension covering 50+ sites; pricing reported variously as $40/mo or free-to-40-jobs then $10/mo (sources conflict) — [applyarc](https://applyarc.com/compare/careerflow-vs-huntr); [bestjobsearchapps](https://bestjobsearchapps.com/articles/en/7-best-aiassisted-job-search-sites-for-2026-huntr-simplify-careerflow-more)
- Careerflow: tracker + LinkedIn profile review (headline suggestions, About rewrites), networking tracker, recruiter/hiring-manager search, autofill; Pro $12-19/mo, Premium $25/mo adds mock interviews and networking tools — [applyarc](https://applyarc.com/compare/careerflow-vs-huntr)
- Simplify: Copilot autofills applications on 100+ portals (Workday, Greenhouse, iCIMS) and auto-logs them in its tracker with docs, notes, recruiter contacts; premium about $40/mo — [bestjobsearchapps](https://bestjobsearchapps.com/articles/en/7-best-aiassisted-job-search-sites-for-2026-huntr-simplify-careerflow-more)
- LinkedIn Premium Career ($29.99/mo): AI chatbot that assesses fit for a posting from your profile, names skills gaps, researches companies, helps shape profile and prep interviews; plus InMails, salary insights, applicant badges — [Geeky Gadgets](https://www.geeky-gadgets.com/linkedin-premium-career-review/); [Quartz](https://qz.com/linkedin-has-built-an-ai-coach-for-your-next-job-search-1850977187)
- Kickresume Career Map: upload resume/LinkedIn + questionnaire on lifestyle, salary, aspirations; outputs personalized career paths with average salaries, skills you have vs need, linked job openings; updatable as experience grows; free basic, premium full — [Kickresume](https://www.kickresume.com/en/ai-career-map/)
- Google Career Dreamer (US-only "early-stage experiment"): identifies transferable skills from life experience, drafts a "Career Identity Statement" for resumes/profiles, suggests careers and local jobs using Lightcast and BLS data; hands off to Gemini for resumes/cover letters — [Grow with Google](https://grow.google/career-dreamer)
- Resumly markets skills-based (not title-based) matching against 1M+ listings with sub-scores for skills, depth, industry, education, pitched at career changers — [Resumly](https://www.resumly.ai/best/best-ai-job-search-tools-for-career-changers)
- Brag doc category: BragLog (on-device AI via Apple FoundationModels, daily log to review doc, iOS/Mac) — [braglog.app](https://braglog.app/); BragBook (log wins, generate impact statements, review prep, case studies) — [bragbook.io](https://bragbook.io/); BragJournal (from $6/mo, for reviews/promotions/manager updates) — [bragjournal.ai](https://bragjournal.ai/); TrackToBrag (dated entries with metrics, AI turns into resume bullets and review statements) — [tracktobrag.app](https://www.tracktobrag.app/); BragDoc (git-commit extraction) — [bragdoc.ai](https://www.bragdoc.ai/)
- Final Round AI: live interview copilot + mock interviews; Yoodli is practice-only communication coaching, not live assistance — [mocky.pro](https://mocky.pro/en/blog/ai-mock-interview-tools-compared); [Final Round AI blog on Yoodli](https://www.finalroundai.com/blog/yoodli-review-pros-cons)

### Inferences
- "Career identity statement" (Google) and LinkedIn headline/About rewrites (Careerflow) are the commercial analogs of positioning-studio; none stress-test claims against evidence.
- Brag-doc apps validate demand for ongoing win capture with low friction (daily entry, git/commit ingestion, on-device privacy). career-os's portfolio-manifest is a one-time ingest; a lightweight recurring "log a win" path would close this gap.
- Exploration tools (Career Map, Career Dreamer) return fixed taxonomy career paths with salary data; career-os's title-lab could borrow the salary/skill-gap overlay per title while keeping its iterative reaction loop.

### Gaps
- Did not verify Teal's or Placement's career-exploration features (e.g., any work-styles assessment); Placement, Jobscan, Rezi, Kickresume resume features were not individually researched within budget.
- No first-hand data on how well Career Map or Career Dreamer handle hybrid/non-standard profiles.

## What features recur across tools that career-os lacks?

### Takeaway
The recurring features career-os lacks are almost all downstream of positioning: job-pipeline tracking, per-job tailoring and resume rendering (PDF/LaTeX/DOCX), opportunity scanning, networking/contact tracking and outreach drafts, interview prep with a story bank, negotiation prep, and continuous win logging. A smaller set are cross-cutting: output-time fact gates and voice/writing-style capture.

### Cited Findings
- Job pipeline/tracker with statuses, follow-ups, outcomes and pattern analysis: career-ops (`tracker`, `followup`, `outcome`, `patterns`, `calibrate`) — [GitHub santifer/career-ops](https://github.com/santifer/career-ops); Teal, Huntr, Simplify — [applyarc](https://applyarc.com/compare/careerflow-vs-huntr)
- Per-job tailoring and rendering: career-ops PDF/LaTeX; claude-resume-skills compiled LaTeX with gap analyzer and version manager; job-tailor YAML-to-PDF — [career-ops](https://github.com/santifer/career-ops); [claude-resume-skills](https://github.com/r-hedayati/claude-resume-skills); [claude-code-job-tailor](https://github.com/javiera-vasquez/claude-code-job-tailor)
- Structured opportunity scoring against a profile (career-ops A-H report, 1-5 score; LinkedIn fit assessment) — [career-ops](https://github.com/santifer/career-ops); [Quartz](https://qz.com/linkedin-has-built-an-ai-coach-for-your-next-job-search-1850977187). (career-os's career-strategist agent overlaps conceptually.)
- Job discovery/scanning: career-ops portal scan + HN Who's Hiring; proficiently job-search and network-scan (contacts' companies) — [career-ops](https://github.com/santifer/career-ops); [proficiently](https://github.com/proficientlyjobs/proficiently-claude-skills)
- Networking/outreach: career-ops `contacto` drafts LinkedIn messages; claude-resume-skills `/cold-email-writer`; Careerflow networking tracker; Huntr per-company contacts — sources above
- Interview prep with accumulating STAR story bank, practice, debrief — [career-ops](https://github.com/santifer/career-ops); `/interview-prep-generator` — [claude-resume-skills](https://github.com/r-hedayati/claude-resume-skills)
- Salary negotiation and offer/contract review — [career-ops](https://github.com/santifer/career-ops); [ResumeSkills](https://github.com/Paramchoudhary/ResumeSkills)
- Continuous win logging / brag doc generation — [BragDoc](https://www.bragdoc.ai/); [BragLog](https://braglog.app/)
- Writing-style/voice capture skill — `/writing-style` in [claude-resume-skills](https://github.com/r-hedayati/claude-resume-skills)
- Output-time fact gate (block PDF if numbers absent from sources) — [career-ops](https://github.com/santifer/career-ops); [?]-claim rejection — [claude-resume-skills](https://github.com/r-hedayati/claude-resume-skills)
- Application autofill (Greenhouse/Lever/Workday) — [proficiently](https://github.com/proficientlyjobs/proficiently-claude-skills); [Simplify](https://bestjobsearchapps.com/articles/en/7-best-aiassisted-job-search-sites-for-2026-huntr-simplify-careerflow-more)
- Skill-gap / upskill planning per target role — career-ops `upskill`, `training` — [career-ops](https://github.com/santifer/career-ops); Kickresume Career Map — [Kickresume](https://www.kickresume.com/en/ai-career-map/)
- Experience-discovery interview to surface undocumented work (career-os's ground-truth-interview analog exists in varunr89 and proficiently setup) — [varunr89](https://github.com/varunr89/resume-tailoring-skill); [proficiently](https://github.com/proficientlyjobs/proficiently-claude-skills)

### Inferences
- Highest-leverage additions consistent with career-os's identity: (1) an evidence-to-resume renderer that only uses approved EV items; (2) a provenance gate/lint over generated artifacts; (3) a recurring win-log skill feeding EV-###; (4) a story bank derived from EV items for interviews; (5) a light opportunity/contact tracker. Full scanning and autofill are better left to career-ops/Simplify, possibly via an export/interop format (e.g., emitting `cv.md` + `article-digest.md` or JSON Resume).
- Voice capture is a cheap differentiator against the "generic AI voice" complaint.

### Gaps
- No quantitative data on which features users actually use most (e.g., tracker vs tailoring) in these tools.

## What do users complain about (generic AI voice, hallucinated experience, privacy, etc.)?

### Takeaway
The dominant complaints are generic AI-sounding text, fabricated metrics/skills that later embarrass candidates in interviews, mass auto-apply spam that hurts reputation, billing/credit traps, and privacy concerns (data used for AI training). Users want AI as an assistant on their own material, not a ghostwriter.

### Cited Findings
- AI resumes sound generic, exaggerated, repetitive; overused verbs like "spearheaded", "leveraged"; phrases like "results-driven professional" — [VisualCV on Reddit](https://www.visualcv.com/blog/best-ai-resume-builders-reddit/); [VisualCV SWE](https://www.visualcv.com/blog/ai-generated-resumes-software-engineers-reddit/)
- With vague input, builders invent accomplishments, metrics or technologies, causing trouble when interviewers ask about them; Reddit preference is AI as "resume assistant, not a resume ghostwriter" — [VisualCV](https://www.visualcv.com/blog/best-ai-resume-builders-reddit/)
- Teal: AI output needs heavy editing, match scores shallow, generic bullets, can feel overwhelming; 10 AI credits used in a single tailoring session, then paywall — [Rezi review](https://www.rezi.ai/posts/teal-review); [remotejobassistant](https://www.remotejobassistant.com/blog/teal-resume-review)
- Final Round AI: Trustpilot 2.9 avg across 277 reviews (Sept 18 2026); copilot freezes mid-interview; billing surprises (yearly upfront, $150 monthly, auto-renew); generic or hallucinated answers on scenario questions; unresponsive support — [mockinterviewpro](https://www.mockinterviewpro.com/reviews/final-round-ai); [rainaiservices](https://rainaiservices.com/reviews/final-round-ai/)
- Auto-apply: JobCopilot reportedly submitted one user's application 4 times per role; 62% of hiring professionals more likely to reject a non-personalized AI resume (stat as cited by career-ops blog, primary source not verified) — [career-ops.org blog](https://career-ops.org/blog/can-an-ai-agent-run-your-job-search)
- Privacy: LinkedIn began using profiles, posts, resumes and activity to train generative AI by default from Nov 3 2025 in EU/EEA/UK/Switzerland/Canada/HK (opt-out not retroactive; private messages and salary/application data excluded) — [TechRadar](https://www.techradar.com/pro/linkedin-set-to-expand-ai-training-on-user-profiles-heres-how-to-stop-it-using-your-personal-data); [Windows Latest](https://www.windowslatest.com/2025/09/23/microsofts-linkedin-warns-it-will-auto-train-ai-models-on-your-data-but-you-can-opt-out/)
- Local-first is a marketed differentiator: career-ops ("your resume and personal data never leave your computer" except to the chosen AI provider), BragLog (on-device), BragDoc (local commit analysis) — [career-ops](https://github.com/santifer/career-ops); [braglog.app](https://braglog.app/); [bragdoc.ai](https://www.bragdoc.ai/)
- claude-resume-skills explicitly defends against hidden text/prompt-injection tricks in resumes — [GitHub](https://github.com/r-hedayati/claude-resume-skills)

### Inferences
- career-os's provenance tags and "[suggested → approved]" flow directly address the top two complaints (generic voice, hallucinated experience); this should be marketed prominently, and ideally enforced at output time.
- Local markdown workspace is a privacy selling point given LinkedIn's 2025 policy change; stating it explicitly in the README would align with how competitors pitch.
- Avoiding auto-apply is a defensible stance shared by career-ops.

### Gaps
- Several complaint summaries come from competitor-authored or SEO review sites (Rezi reviewing Teal, Final Round AI reviewing Yoodli, VisualCV summarizing Reddit); direct Reddit threads were not fetched. Treat as indicative.
- No user complaint data found specifically about career-ops (issues tracker not reviewed).
