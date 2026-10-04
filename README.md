# career-os

Plugin marketplace for **career-os**: a career operating system for technical-creative people whose work doesn't fit a standard title. It captures your ground truth, tracks what interests you, builds a portfolio manifest from evidence, iterates on job titles, and turns it all into positioning you can sell. Works with Codex and Claude Code.

## Install

### Codex

This repository includes a Codex plugin manifest (`plugins/career-os/.codex-plugin/plugin.json`) and marketplace (`.agents/plugins/marketplace.json`).

```bash
codex plugin marketplace add buck-0x/career-os
codex plugin add career-os@career-os-marketplace
```

From a local checkout, use the path instead: `codex plugin marketplace add /path/to/career-os`.

Start a new Codex task, then invoke a skill with `$career-os:<skill>`, for example:

```text
$career-os:ground-truth-interview
```

### Claude Code

```bash
claude plugin marketplace add buck-0x/career-os      # or the repo's git URL
claude plugin install career-os@career-os-marketplace
```

In Claude Code, invoke skills as `/<skill>`.

### Claude app

Add this repo as a plugin marketplace, then install **career-os** from it.

## Repo layout

```
.claude-plugin/marketplace.json   # Claude Code marketplace manifest
.agents/plugins/marketplace.json  # Codex marketplace manifest
plugins/career-os/                # the plugin: 5 skills + 1 agent
  .claude-plugin/plugin.json      # Claude Code plugin manifest
  .codex-plugin/plugin.json       # Codex plugin manifest
  shared/                         # canonical conventions + validator (copied into each skill)
  hooks/hooks.json                # Claude Code hook: validate workspace files after writes
  evals/                          # `claude plugin eval` suite (synthetic fixtures only)
scripts/sync_shared.py            # copies shared/ into every skill; --check fails on drift
tests/                            # validator unit tests
```

Plugin docs: [plugins/career-os/README.md](plugins/career-os/README.md)

## Development

```bash
claude plugin validate ./plugins/career-os
claude plugin validate .
claude --plugin-dir ./plugins/career-os            # try it without installing
```

Shared files: edit `plugins/career-os/shared/` only, then copy them into the skills (CI fails if the copies drift):

```bash
python3 scripts/sync_shared.py
```

Validator tests (Python 3.9+, standard library only):

```bash
python3 -m unittest discover tests
```

Evals run real model sessions and cost credits. Fixtures are synthetic; keep reports local:

```bash
claude plugin eval ./plugins/career-os --no-publish --tag trigger
```

The `fabrication-trap` and `dealbreaker-pushback` cases need their fixture scripts and write access:

```bash
claude plugin eval ./plugins/career-os --no-publish --scaffold --allow-tools Write Edit Bash --case fabrication-trap
```

Bump `version` in both plugin manifests and in `.claude-plugin/marketplace.json` when you release changes so installed copies update.

## License

[MIT](LICENSE)
