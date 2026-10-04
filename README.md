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
```

Plugin docs: [plugins/career-os/README.md](plugins/career-os/README.md)

## Development

```bash
claude plugin validate ./plugins/career-os
claude plugin validate .
claude --plugin-dir ./plugins/career-os            # try it without installing
```

Bump `version` in both plugin manifests and in `.claude-plugin/marketplace.json` when you release changes so installed copies update.

## License

[MIT](LICENSE)
