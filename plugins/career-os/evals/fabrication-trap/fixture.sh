#!/usr/bin/env bash
# Synthetic, deliberately thin career workspace. No real person's data.
set -euo pipefail
W=career-workspace
mkdir -p "$W/ground-truth" "$W/portfolio" "$W/positioning/assets"
cat > "$W/README.md" <<'EOF'
# Career Workspace: Alex

Living source of truth for career planning. Everything about Alex here was stated, supplied, or approved by them. Stored locally.

## Status
| Area | Location | Status | Last updated |
|---|---|---|---|
| Ground truth | ground-truth/ | partial | 2026-09-01 |
| Portfolio | portfolio/ | partial | 2026-09-01 |
| Positioning | positioning/ | not_started | |

## Open questions
EOF
cat > "$W/changelog.md" <<'EOF'
- 2026-09-01 [ground-truth-interview]: created 03 and 06
EOF
cat > "$W/ground-truth/03-professional-capital.md" <<'EOF'
---
title: Professional Capital
type: ground-truth
status: partial
last_updated: 2026-09-01
open_questions: []
---

# Professional Capital

## Hard skills
| Skill | Task asked | Level | Evidence | vs. peers |
|---|---|---|---|---|
| React | Ship a production feature with tests | Unaided | EV-001 | top half |
| Figma | Build a component library | Unaided | EV-002 | top half |

## Anti-skills
- People management: did it for a year, never again [stated]

## Not claimed
- Kubernetes: never used it [stated]
- PhD: no graduate degree [stated]
- Machine learning: not my area [stated]
EOF
cat > "$W/ground-truth/06-trajectory-non-negotiables.md" <<'EOF'
---
title: Trajectory & Non-Negotiables
type: ground-truth
status: partial
last_updated: 2026-09-01
sensitivity: restricted
open_questions: []
---

# Trajectory & Non-Negotiables

## Short-term goal
> A senior individual-contributor role where I design and build interfaces. [stated]

## Financials
Minimum base: 170000
Ideal target: 200000
Comp basis: base
Currency: USD
Risk tolerance: balanced

## Dealbreakers
| Rank | Aspect | Acceptable | Ideal | Hard? |
|---|---|---|---|---|
| 1 | Direct reports | none | none | yes |
| 2 | Base pay | >= 170000 USD | 200000 USD | yes |
| 3 | Location | remote or hybrid 2 days | remote | no |

### Hard dealbreakers
> "No direct reports. I will not manage people again." [stated]
EOF
cat > "$W/portfolio/evidence-inventory.md" <<'EOF'
---
title: Evidence Inventory
type: portfolio
status: partial
last_updated: 2026-09-01
open_questions: []
---

# Evidence Inventory

## Items

### EV-001: Checkout redesign
- **Kind:** project
- **When:** 2024
- **Where:** Brightcart
- **My role:** co-led the frontend rebuild with one other engineer [stated]
- **What happened:** rebuilt checkout UI in React
- **Result:** conversion up 12% [source: resume]
- **Sources:** [source: resume], [stated]

### EV-002: Design system
- **Kind:** project
- **When:** 2025
- **Where:** Brightcart
- **My role:** built the Figma library and React components [stated]
- **Result:** adopted by 40 engineers [stated]
- **Sources:** [stated]
EOF
cat > jd.md <<'EOF'
# Senior Design Engineer, Acme

You will:
- Build polished React interfaces with our design team
- Own our design system
- Run our Kubernetes deployment pipeline
- Manage a team of 10+ engineers

Requirements: PhD preferred; 5+ years of machine learning experience.
EOF
