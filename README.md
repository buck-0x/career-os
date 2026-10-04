# career-os

Plugin marketplace for **career-os**: a career operating system for technical-creative people whose work doesn't fit a standard title. It captures your ground truth, tracks what interests you, builds a portfolio manifest from evidence, iterates on job titles, and turns it all into positioning you can sell.

## Install

**Claude Code**

```bash
claude plugin marketplace add <owner>/career-os      # or the repo's git URL
claude plugin install career-os@career-os-marketplace
```

**Claude app:** add this repo as a plugin marketplace, then install **career-os** from it.

## Repo layout

```
.claude-plugin/marketplace.json   # marketplace manifest (lists the plugin)
plugins/career-os/                # the plugin: 5 skills + 1 agent
```

Plugin docs: [plugins/career-os/README.md](plugins/career-os/README.md)

## Development

```bash
claude plugin validate ./plugins/career-os
claude plugin validate .
claude --plugin-dir ./plugins/career-os            # try it without installing
```

Bump `version` in `plugins/career-os/.claude-plugin/plugin.json` when you release changes so installed copies update.
