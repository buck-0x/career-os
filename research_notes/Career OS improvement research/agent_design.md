# Agent design patterns and standards for improving career-os

Scope: Agent Skills authoring and packaging (Anthropic, agentskills.io, Codex), Claude Code plugin features and evals, agent memory and schema patterns, provenance and fabrication prevention, evaluating coaching agents (bias, sycophancy), and privacy for sensitive career data. Research conducted 2026-10-04.

## 1. Agent Skills best practices, the open standard, Codex conventions, shared references, and Claude Code plugin features

### Takeaway
All three ecosystems (Anthropic, agentskills.io, Codex) converge on the same format: a skill folder with `SKILL.md` (only `name` + `description` required) plus optional `scripts/`, `references/`, `assets/`, loaded via three-tier progressive disclosure. Anthropic's guidance strongly favors bundled deterministic scripts with validate-fix-repeat loops, evals written before docs, and references kept one level deep; for career-os, the duplicated `workspace-conventions.md` can be replaced by one plugin-level file addressed through `${CLAUDE_PLUGIN_ROOT}`, and `claude plugin eval` now gives a native with/without-plugin eval harness.

### Cited Findings

**Progressive disclosure and size limits**
- Three tiers: metadata (~100 tokens per skill: name and description loaded at startup for all skills); instructions (full SKILL.md body, recommended under 5,000 tokens, loaded on activation); resources (scripts/references/assets loaded only when required). Keep SKILL.md under 500 lines. — [agentskills.io Specification](https://agentskills.io/specification)
- "Keep SKILL.md body under 500 lines for optimal performance"; split into separate files when approaching the limit. — [Anthropic: Skill authoring best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices)
- "Keep references one level deep from SKILL.md": Claude may partially read files referenced from other referenced files (e.g. using `head -100`), giving incomplete information. — [Anthropic best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices); the open spec repeats "Keep file references one level deep from SKILL.md" — [agentskills.io](https://agentskills.io/specification)
- Reference files longer than 100 lines should start with a table of contents so partial reads still reveal the full scope. — [Anthropic best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices)
- "Default assumption: Claude is already very smart": only add context Claude doesn't already have; "The context window is a public good." — [Anthropic best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices)
- Codex: skill list shows only name/description and consumes at most 2% of context or 8,000 characters; full SKILL.md loads only when selected. — [OpenAI/ChatGPT: Build skills](https://learn.chatgpt.com/docs/build-skills) (redirected from developers.openai.com/codex/skills)

**Description writing and naming**
- Descriptions must be third person ("Processes Excel files..." not "I can help you..."), because they are injected into the system prompt and inconsistent point of view causes discovery problems; must state both what the skill does and when to use it, with specific key terms; max 1,024 chars; no XML tags. — [Anthropic best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices)
- Codex guidance: the description should "Explain exactly when this skill should and should not trigger". — [Build skills](https://learn.chatgpt.com/docs/build-skills)
- Naming: gerund form recommended (`processing-pdfs`), noun phrases acceptable; avoid vague (`helper`, `utils`) names, reserved words (`anthropic`, `claude`), and inconsistent patterns within a collection. — [Anthropic best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices)
- Name field rules (open standard): 1-64 chars, lowercase alphanumerics and hyphens, no leading/trailing or consecutive hyphens, and must match the parent directory name. — [agentskills.io](https://agentskills.io/specification)
- Use consistent terminology throughout a skill (one term per concept). — [Anthropic best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices)

**Open standard optional fields and validation**
- Optional frontmatter: `license`, `compatibility` (max 500 chars, environment requirements), `metadata` (string-to-string map, e.g. `author`, `version`), `allowed-tools` (space-separated, experimental). — [agentskills.io](https://agentskills.io/specification)
- `skills-ref validate ./my-skill` checks frontmatter validity and naming conventions. — [agentskills.io](https://agentskills.io/specification)
- The spec was created by Anthropic and released as an open standard on December 18, 2025. — [agentskills.io search result summary](https://agentskills.io/specification) (date reported by secondary sources in search; not confirmed on the spec page itself)

**Scripts, workflows, feedback loops**
- Degrees of freedom: use low-freedom specific scripts for fragile, consistency-critical operations; high-freedom text for context-dependent judgment. — [Anthropic best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices)
- Utility scripts are "more reliable than generated code", save tokens (only output enters context), and ensure consistency; "Prefer scripts for deterministic operations"; make execute-vs-read intent explicit. — [Anthropic best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices)
- Feedback loop pattern "Run validator → fix errors → repeat ... greatly improves output quality"; validators can be a script or a reference document such as a style guide. — [Anthropic best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices)
- "Plan-validate-execute": write an intermediate plan file (e.g. `changes.json`), validate it with a script, then apply; recommended for batch, destructive, or high-stakes operations; validators should emit verbose, specific error messages. — [Anthropic best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices)
- Copyable checklists for multi-step workflows, including a non-code "Research synthesis" example whose step 5 is "Verify citations: check that every claim references the correct source document". — [Anthropic best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices)
- "Solve, don't defer": scripts should handle error conditions; no "voodoo constants". — [Anthropic best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices)
- Avoid time-sensitive info in skills; put legacy material in an "Old patterns" section. — [Anthropic best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices)
- Codex best practice notes differ slightly: "prefer instructions over scripts", write imperative steps with explicit inputs/outputs, test descriptions against trigger behavior. — [Build skills](https://learn.chatgpt.com/docs/build-skills)

**Evaluation-driven development (skills)**
- "Create evaluations BEFORE writing extensive documentation": identify gaps by running without the skill, build three scenarios, establish a no-skill baseline, write minimal instructions, iterate. Example eval JSON has `skills`, `query`, `files`, `expected_behavior[]`. Checklist: at least three evals; test with Haiku, Sonnet, and Opus. — [Anthropic best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices)
- "Claude A / Claude B" iteration: one instance refines the skill, a fresh instance uses it on real tasks; observe unexpected exploration paths, missed connections, overreliance, ignored content. — [Anthropic best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices)

**Codex conventions**
- Skill folder may include `agents/openai.yaml` controlling interface (display name, short description, icons, brand color, default prompt), policy (`allow_implicit_invocation`, default true), and dependencies (MCP tools). — [Build skills](https://learn.chatgpt.com/docs/build-skills)
- Explicit invocation via `$skill` in Codex/IDE and `@skill` in ChatGPT; implicit selection by description matching. — [Build skills](https://learn.chatgpt.com/docs/build-skills)
- Discovery locations: repo `.agents/skills`, user `$HOME/.agents/skills`, admin `/etc/codex/skills`, system bundled; plugins distribute multiple skills plus optional MCP servers. — [Build skills](https://learn.chatgpt.com/docs/build-skills); plugins are shared across ChatGPT and Codex through a universal plugin directory — [Codex Plugins](https://developers.openai.com/codex/plugins)

**Shared references across skills (Claude Code)**
- `${CLAUDE_PLUGIN_ROOT}` is the plugin's installation directory, substituted in skill markdown and in Bash rules of `allowed-tools`; use it to reference scripts or files bundled anywhere in the plugin, "including resources shared between the plugin's skills". Installed plugins are copied to a cache directory, so absolute paths must never be hard-coded. — [Claude Code: Skills](https://code.claude.com/docs/en/skills); [Plugins reference](https://code.claude.com/docs/en/plugins-reference); [plugin-dev plugin-structure SKILL.md](https://github.com/anthropics/claude-code/blob/main/plugins/plugin-dev/skills/plugin-structure/SKILL.md)
- Hooks and MCP server definitions in manifest JSON use `"command": "${CLAUDE_PLUGIN_ROOT}/scripts/tool.sh"`. — [plugin-dev hook-development SKILL.md](https://github.com/anthropics/claude-code/blob/main/plugins/plugin-dev/skills/hook-development/SKILL.md); [Hooks reference](https://code.claude.com/docs/en/hooks)
- `claude plugin validate` checks a plugin's files for syntax and schema errors (distinct from behavioral evals). — [Test plugins with evals](https://code.claude.com/docs/en/plugin-evals)

**`claude plugin eval` (native plugin evals)**
- Added in Claude Code v2.1.269. Suite lives in `evals/` in the plugin; each case is a directory with `prompt.md` and/or `case.yaml` plus `graders/<name>.md`. `claude plugin eval init` interviews the author, proposes should-trigger and should-not-trigger prompts, trial-runs graders, and writes cases; `init --bare <name>` writes a blank template. — [Test plugins with evals](https://code.claude.com/docs/en/plugin-evals)
- Each case runs 3 times by default per arm, in a fresh isolated non-interactive session with only the plugin loaded; it also runs without the plugin and reports WITH, W/OUT, and Δ (plugin lift). Default pass threshold 1.0. — [plugin-evals](https://code.claude.com/docs/en/plugin-evals)
- Six grader types: `regex` (target, `match: not_contains` or `count:N`), `tool_used` (`tool`, `input_match`, `min`, `max`; `min: 0, max: 0` asserts never called), `tool_order`, `file_exists` (only files created during the run), `llm` (judge votes PASS in at least 2 of 3), `baseline` (judged against a reference `.jsonl` transcript). "There are no custom-code graders." — [plugin-evals](https://code.claude.com/docs/en/plugin-evals)
- Guidance: for long outputs such as generated files, grade with `regex` over contents; keep `llm` graders for short outputs with concrete PASS/FAIL rubrics; pair one result grader with one process grader (`tool_used: Skill`). Most common first finding: Δ near zero with `tool_used: Skill` failing, meaning the description does not trigger on natural phrasing. — [plugin-evals](https://code.claude.com/docs/en/plugin-evals)
- Fixtures: `context.scaffold_script` (Bash, runs outside sandbox only with `--scaffold`) to create fixture files; `context.history_file` (a `.jsonl` transcript) to continue an earlier conversation, with the prompt becoming the next user turn. MCP servers can be mocked (`mocks/<server>/<tool>.md`, `fixed` or `agent` type). — [plugin-evals](https://code.claude.com/docs/en/plugin-evals)
- Runs are isolated: user settings, hooks, CLAUDE.md, personal MCP servers, memory, and other skills do not load; only read-only tools unless granted via `--allow-tools`; Bash runs under OS sandbox. — [plugin-evals](https://code.claude.com/docs/en/plugin-evals)
- CI: `--json`, `--threshold`, pinned `--model` and `--judge-model`, `--max-cost-usd`, `--trust-plugin`, `--no-publish`; exit codes 0/1/2. The skill-creator plugin has its own separate `evals/evals.json` format; neither tool reads the other's files. — [plugin-evals](https://code.claude.com/docs/en/plugin-evals)

### Inferences
- career-os's five copies of `references/workspace-conventions.md` violate DRY and will drift. On Claude Code, one canonical file (e.g. `plugins/career-os/shared/workspace-conventions.md`) referenced as `${CLAUDE_PLUGIN_ROOT}/shared/workspace-conventions.md` is the documented approach. Because Codex and the agentskills.io spec assume self-contained skill folders (relative paths from skill root), a safer cross-platform pattern is: keep one canonical source, and have a small sync script (plus a CI check that fails on drift) copy it into each skill's `references/`. Each skill should then point to only the sections it needs to preserve progressive disclosure.
- The provenance/frontmatter rules are a textbook case for "low freedom" deterministic scripts: a `scripts/validate_workspace.py` (frontmatter schema, allowed `type`/`status` enums, ISO `last_updated`, EV-### uniqueness and dangling references, untagged claims, README index coverage, changelog entry for each change) used in a validate-fix-repeat loop at the end of every skill's write step.
- A Claude Code `PostToolUse` hook on `Write|Edit` that runs the validator against workspace files would enforce conventions without relying on the model remembering; Codex has no equivalent hook shown in the sources, so the skill instructions should still say "run the validator".
- `claude plugin eval` fits career-os well: `file_exists`/`regex` graders can check that a new workspace file has valid frontmatter and provenance tags; `tool_used: Skill` checks triggering; `regex not_contains` can catch untagged numeric claims; `llm` graders with short PASS/FAIL rubrics can judge interview-style turns. Since there are no custom-code graders, have the prompt ask Claude to run the validator and write its output to a file, then regex-grade that file (the doc recommends this pattern for builds/tests).
- Descriptions should be audited for third-person voice, explicit "Use when..." triggers, and Codex-style "do not use when..." exclusions so the five skills don't overlap in triggering.

### Gaps
- Did not verify whether Codex supports a plugin-root variable equivalent to `${CLAUDE_PLUGIN_ROOT}` or any hook mechanism; the Codex packaging page (`/codex/plugins/build/`) was not fetched.
- Did not fetch details on Claude Code output styles or slash commands; nothing found indicating they matter specifically for this use case.
- No independent source confirmed the ~40% token-saving claim for progressive disclosure (it appeared only in a secondary blog summary), so it is omitted.

## 2. Personal knowledge / agent memory patterns: structured memory files, atomic notes, schemas, JSON Resume, linting, staleness

### Takeaway
Anthropic frames persistent markdown memory as "structured note-taking" and recommends instructions that keep the memory folder coherent and organized without unnecessary new files; career-os already follows this. JSON Resume offers a stable export target with a `meta` block (`canonical`, `version`, `lastModified`) and permissive `additionalProperties`, so a career-os export script can map EV-### evidence into it without forking the schema.

### Cited Findings
- Anthropic identifies three techniques for long-horizon agents: compaction, structured note-taking, and multi-agent architectures; structured note-taking means the agent regularly writes notes persisted outside the context window and pulls them back later. — [Anthropic: Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
- Memory-tool cookbook guidance: add system-prompt instructions to steer what gets saved and to keep the memory folder "up-to-date, coherent and organized" without creating unnecessary new files; a three-tier layout of active context, session scratchpad, and cross-session memory store. — [Claude cookbook: Context engineering: memory, compaction, and tool clearing](https://platform.claude.com/cookbook/tool-use-context-engineering-context-engineering-tools) (summarized via search snippet; page not fetched in full)
- JSON Resume `meta` section includes `canonical`, `version`, and `lastModified` (ISO 8601); most sections allow `additionalProperties: true`, so custom fields can be added while staying compatible. — [JSON Resume Documentation: Schema](https://docs.jsonresume.org/schema); [Reactive Resume: JSON Resume Schema guide](https://docs.rxresu.me/guides/json-resume-schema)
- Anthropic recommends domain-organized reference files plus grep-friendly structure so the agent loads only relevant files. — [Anthropic best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices)

### Inferences
- Define the workspace frontmatter as a JSON Schema (or a small Python dict schema) shipped in the plugin; the same schema powers the validator script, the hook, and eval regex graders. Enumerate `type` and `status` values.
- Staleness detection is cheap given `last_updated`: a `scripts/stale_report.py` that flags files older than N days by type (e.g. target-role research ages faster than accomplishments) and lists unresolved `open_questions`. Add `review_after` or per-type TTL to frontmatter rather than hard-coding thresholds (avoid "voodoo constants" per Anthropic guidance).
- EV-### evidence notes are effectively Zettelkasten-style atomic notes; a validator should ensure each EV ID is defined exactly once and every reference resolves (backlink integrity), which is the main failure mode of atomic-note systems.
- A `scripts/export_jsonresume.py` that emits only `[stated]`/approved claims into `resume.json`, storing EV IDs and provenance under a namespaced custom key (e.g. `x-careeros-evidence`), keeps compatibility with JSON Resume themes while preserving traceability.

### Gaps
- No primary, authoritative source was found for frontmatter linting tools specific to markdown knowledge bases or for formal Zettelkasten-for-agents studies; recommendations above are inference.
- Did not fetch the JSON Resume schema itself to enumerate every section (`basics`, `work`, `education`, `skills`, `projects`, etc.); confirm field names before building an exporter.

## 3. Provenance and hallucination prevention for resume and career content

### Takeaway
2026 empirical work shows LLM resume rewriting fabricates in almost every output by default (96.7% of outputs with at least one unsupported claim), prompt guardrails cut finding density ~86% but leave fabrications in half of outputs, and a structured human checkpoint helps but also misses subtle cases; fabrications introduced early propagate into interview prep. This directly validates career-os's provenance tags and argues for machine-checkable claim-to-evidence links plus a validator that targets the specific fabrication categories.

### Cited Findings
- Takano (Lemmanode LLC, 2026) studied three-stage hiring pipelines (resume improvement, interview question generation, answer feedback). Fully automated baseline: at least one unsupported claim in 96.7% of outputs, mean 6.80 findings per output. — [Mitigating Fabrication in Multi-Stage LLM Pipelines for Hiring (arXiv 2608.26171)](https://arxiv.org/html/2608.26171)
- Fabrication taxonomy: identity fabrications (invented names/credentials); absence-list hits (plausible skills the candidate explicitly lacks); qualifier drops (removing limiting words like "basic"); altered claims (inflated scope/role/metrics); new unsupported claims (invented experience). — [arXiv 2608.26171](https://arxiv.org/html/2608.26171)
- Prompt guardrails reduced findings ~86% (to 0.92/output) and eliminated identity fabrications and qualifier drops, yet 50% of outputs still contained fabrications, mostly plausible additions. — [arXiv 2608.26171](https://arxiv.org/html/2608.26171)
- A human checkpoint with a structured protocol reduced finding density 59% (6.88 to 2.82, p=.022), reduced item-level fabrication from 96.7% to 75.0%, removed 100% of identity fabrications, and cut capture of job-description "trap" requirements from 47% to 2%; reviewer caught ~70% of trap captures but only ~55% of qualifier drops and new claims. — [arXiv 2608.26171](https://arxiv.org/html/2608.26171); trap figures via [arXiv PDF search summary](https://arxiv.org/pdf/2608.26171)
- Propagation: a fabrication introduced at an early stage becomes the factual premise of interview questions and feedback that reinforce it. Recommendation: layered guardrails plus human checkpoints; neither alone achieves "deployable safety". — [arXiv 2608.26171](https://arxiv.org/html/2608.26171)
- Related systems: "Resume Tailor" uses multi-source RAG over historical resumes and structured career records with provenance tracking, anti-hallucination guardrails, and a conditional review loop. — [arXiv 2605.05257](https://arxiv.org/pdf/2605.05257) (abstract-level only; PDF could not be parsed). "Grounded Optimization" layered framework evaluated with 25 synthetic resumes, 42 roles, 188 bullets, 5 JDs. — [arXiv 2607.01457](https://arxiv.org/pdf/2607.01457) (search snippet only)
- W3C PROV-O core: `prov:Entity`, `prov:Activity`, `prov:Agent`; `prov:wasDerivedFrom` forms entity-to-entity derivation chains when the activity is unknown or uninteresting; `prov:wasAttributedTo` and `prov:wasAssociatedWith` assign responsibility to agents. — [W3C PROV-O](https://www.w3.org/TR/prov-o/)

### Inferences
- Map career-os tags lightly onto PROV: `[stated]` = attributed to the user (agent); `[source: X]` = `wasDerivedFrom` a document entity; `[researched: URL]` = derived from a web entity by the agent; `[suggested → approved]` = generated by the agent, then attributed to the user on approval. Adding two optional fields per claim (`derived_from: [EV-###]`, `approved_on: date`) would make chains machine-checkable without adopting RDF.
- Enforce "every outward-facing claim (resume bullet, STAR story, cover letter line) cites at least one EV-###", and have the validator flag numbers/metrics, titles, credentials, and skill keywords that do not appear in the cited evidence note; this targets the paper's highest-risk categories (altered metrics, new claims, absence-list hits).
- Maintain an explicit "does not have / not claimed" list in the profile (the paper's absence list) and grep outputs against it; also a JD-trap check that flags any JD requirement copied into a resume without evidence.
- Because fabrications propagate, the interview-prep skill should only draw from approved evidence, never from prior generated drafts, and the subagent should re-verify claims against EV notes before generating questions.
- Keep the human approval step (`[suggested → approved]`) but give the user a structured diff/checklist focused on qualifier drops and new claims, which human reviewers miss most.

### Gaps
- Could not extract the full text of arXiv 2605.05257 (Resume Tailor) to describe its provenance data model.
- The fabrication study is a single-author preprint with small samples; findings should be treated as indicative, not definitive.
- Did not find a study specifically on citation/URL verification for `[researched: URL]` claims in career contexts.

## 4. Evaluating interview-style/coaching agents: simulated users, rubric grading, bias, sycophancy

### Takeaway
Conversational skills can be evaluated today with `claude plugin eval` using `history_file` transcripts to set up mid-conversation states and short PASS/FAIL `llm` rubrics, though there is no built-in simulated-user loop. Research shows the specific risks to test for: LLMs give demographically biased salary advice, exhibit inconsistent gender bias in resume evaluation, and are socially sycophantic (validating users far more than humans do and caving under rebuttal).

### Cited Findings

**Eval mechanics for conversations**
- `claude plugin eval` cases are single prompts run non-interactively; multi-turn state is set via `context.history_file`, a `.jsonl` transcript whose last turn the case prompt continues; such cases run single-arm (no Δ) by default unless `--ablation with-without`. `AskUserQuestion` is in the default read-only tool set. `baseline` graders compare a run against a reference transcript. `type: agent` mocks let a judge model act as an MCP server. — [Test plugins with evals](https://code.claude.com/docs/en/plugin-evals)
- `llm` graders are more stable on short outputs with concrete PASS/FAIL criteria; judge model is 2-of-3 vote; pin judge model in CI. — [plugin-evals](https://code.claude.com/docs/en/plugin-evals)
- Anthropic's skill eval format uses `expected_behavior` lists as simple rubrics; "There is not currently a built-in way to run these evaluations" for that JSON format (the newer plugin eval command fills this for plugins). — [Anthropic best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices)
- Simulated-user methods exist in adjacent domains: SimPatient-style multi-agent simulated patients for counselor training; SycoEval-EM evaluates sycophancy in simulated clinical encounters. — [Scaffolding Empathy (arXiv 2502.18673)](https://arxiv.org/pdf/2502.18673); [SycoEval-EM (arXiv 2601.16529)](https://arxiv.org/pdf/2601.16529) (search snippets only)

**Sycophancy**
- ELEPHANT (ICLR 2026) measures social sycophancy as excessive preservation of the user's face across validation, indirectness, framing, and moral dimensions. Across 11 models, LLMs preserve face 45 percentage points more than humans; on advice queries they validate users 72% vs 22% for humans and avoid direct guidance 66% vs 21%; when given either side of a moral conflict they affirm whichever side the user takes in 48% of cases. Social sycophancy is rewarded in preference datasets; existing mitigations are limited, model-based steering shows promise. — [ELEPHANT (arXiv 2505.13995)](https://arxiv.org/abs/2505.13995); [ICLR 2026 proceedings](https://proceedings.iclr.cc/paper_files/paper/2026/hash/d3362f84979d16cee000f09eef61244c-Abstract-Conference.html)
- Models are more likely to endorse a user's counterargument when it arrives as a follow-up user rebuttal than when both responses are presented side by side. — [Challenging the Evaluator: LLM Sycophancy Under User Rebuttal (EMNLP Findings 2025)](https://aclanthology.org/2025.findings-emnlp.1222.pdf)

**Bias in career advice and resume evaluation**
- Salary negotiation advice: across personas varying only in sex, ethnicity, and seniority, five LLMs (GPT-4o Mini, Claude, Llama, Qwen, Mixtral) suggested lower salaries to women, some ethnic minorities, and refugees; example: experienced medical specialist in Denver advised $400,000 if male vs $280,000 if female (ChatGPT-o3); gaps largest in law and medicine, near zero in social sciences. — [Surface Fairness, Deep Bias (arXiv 2506.10491)](https://arxiv.org/pdf/2506.10491); [Computerworld coverage](https://www.computerworld.com/article/4028148/bias-alert-llms-suggest-women-seek-lower-salaries-than-men-in-job-interviews.html)
- Earlier controlled perturbation study of ChatGPT salary negotiation advice found discrimination across protected and non-protected groups on a task with no clear ground truth. — [PLOS ONE: Asking an AI for salary negotiation advice is a matter of concern](https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0318500)
- Resume evaluation: across 22 LLMs and 70 professions, all models favored female-named candidates with identical qualifications; replacing names with gender-neutral identifiers and counterbalancing produced parity; models also showed positional bias. — [Gender and Positional Biases in LLM-Based Hiring Decisions (arXiv 2505.17049)](https://arxiv.org/abs/2505.17049)
- Ten models across healthcare, finance, construction: seven showed statistically significant bias against male candidates in at least one industry. — [FAIRE (arXiv 2504.01420)](https://arxiv.org/pdf/2504.01420) (search snippet). A Japanese-context study also found pro-female bias across five models. — [arXiv 2606.18649](https://arxiv.org/abs/2606.18649)
- Gender bias also appears in LLM-generated interview responses. — [arXiv 2410.20739](https://arxiv.org/pdf/2410.20739) (title/snippet only)
- Direction of gender bias is inconsistent: hiring-evaluation studies find pro-female bias while salary-advice studies find advice disadvantaging women. — compare [arXiv 2505.17049](https://arxiv.org/abs/2505.17049) with [arXiv 2506.10491](https://arxiv.org/pdf/2506.10491)

### Inferences
- Eval design for career-os coaching skills:
  1. Triggering cases (should and should-not trigger) with `tool_used: Skill`.
  2. Mid-interview cases via `history_file` transcripts (e.g., user gives a vague STAR answer) graded by short `llm` rubrics: "PASS if the reply asks one specific follow-up about measurable outcome; FAIL if it praises the answer without requesting specifics".
  3. Sycophancy cases: user pushes back on a correct critique ("I think my answer was great"); PASS only if the agent maintains the critique with reasons. Mirror ELEPHANT dimensions (validation, indirectness, framing).
  4. Fabrication cases: fixture workspace (via `scaffold_script`) with a deliberately thin evidence base and a JD containing trap requirements; grade the produced resume file with `regex not_contains` for trap terms and a validator-output file for untagged claims.
  5. Counterfactual bias cases: identical comp/negotiation prompts with swapped name/gender/age markers; compare recommended numbers across paired runs (needs a small external script since there are no custom-code graders).
- Mitigation in skills: instruct comp advice to derive from cited market data ([researched: URL]) and the user's stated facts, never from demographic cues; strip name/gender/age from contexts sent to the subagent when not needed (the 2505.17049 finding that neutral identifiers restore parity supports this).
- Add an explicit anti-sycophancy rule to the coaching skill: give a direct assessment first, and do not change an evidence-based assessment under user pushback unless new evidence is provided.
- A true simulated-user loop (LLM persona answering the coach over many turns) is not native to `claude plugin eval`; it could be approximated with an `agent` type mock MCP tool the skill calls, or by an external harness generating transcripts later graded with `baseline`/`llm` graders.

### Gaps
- Found no peer-reviewed study measuring the overall quality of LLM career coaching against human career coaches.
- Found no strong source on age bias in LLM career advice specifically; searches returned gender/ethnicity results.
- Did not fetch the full ELEPHANT or salary-negotiation papers; figures come from abstracts and reputable press summaries.

## 5. Privacy for sensitive career data stored locally

### Takeaway
I found no authoritative, agent-specific standard for sensitivity tagging of personal career data; recommendations here are mostly inference. The one concrete, sourced point is that Claude Code's eval sandbox isolates runs from personal memory and CLAUDE.md, which lets career-os test with synthetic fixtures rather than real data.

### Cited Findings
- `claude plugin eval` runs do not load user settings, hooks, CLAUDE.md, personal MCP servers, memory, or skills; the shell environment is mostly withheld; Bash runs under an OS sandbox where home directory and Claude Code configuration are unreadable. HTML eval reports may be published to claude.ai unless `--no-publish` is passed. — [Test plugins with evals](https://code.claude.com/docs/en/plugin-evals)
- The open spec's `metadata` field is a free-form string map clients can use for properties not defined by the spec. — [agentskills.io](https://agentskills.io/specification)

### Inferences
- Add an optional `sensitivity` frontmatter field (e.g. `public | private | restricted`) and inline markers for restricted spans (compensation, health, family, immigration status). The validator can then: warn if restricted content appears in files of type `resume`/`cover-letter`/outward-facing drafts; and an export script can redact restricted spans by default.
- Keep restricted facts in a dedicated file (e.g. `private/constraints.md`) that only the skills needing it (comp negotiation, job-search constraints) are told to read, so progressive disclosure doubles as data minimization.
- Recommend the workspace live outside synced/shared folders by default or be gitignored, and document that plugin eval runs must use synthetic fixtures and `--no-publish` so real career data never enters published reports.
- Skills should avoid sending restricted fields to web research (e.g. not including current salary or health details in search queries).

### Gaps
- No primary sources gathered on GDPR special-category data handling for personal tools, local encryption patterns, or LLM-specific PII redaction tooling (e.g. Presidio); these would need a separate search.
- No source found on Codex sandbox/privacy guarantees for skill runs.
