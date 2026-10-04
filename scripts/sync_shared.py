#!/usr/bin/env python3
"""Copy plugins/career-os/shared/ files into every skill folder.

Codex and the Agent Skills standard expect each skill folder to be
self-contained, so each skill carries its own copy of the shared conventions
and validator. Edit the canonical files in plugins/career-os/shared/ and run:

  python3 scripts/sync_shared.py          # write copies
  python3 scripts/sync_shared.py --check  # exit 1 if any copy is missing or differs (CI)
"""

import argparse
import sys
from pathlib import Path

PLUGIN = Path(__file__).resolve().parents[1] / "plugins" / "career-os"
SHARED = PLUGIN / "shared"
# canonical file -> destination inside each skill folder
FILES = {
    "workspace-conventions.md": "references/workspace-conventions.md",
    "validate_workspace.py": "scripts/validate_workspace.py",
}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args()

    skills = sorted(p for p in (PLUGIN / "skills").iterdir() if (p / "SKILL.md").is_file())
    drift = []
    for skill in skills:
        for src_name, dest_rel in FILES.items():
            src = (SHARED / src_name).read_bytes()
            dest = skill / dest_rel
            if dest.is_file() and dest.read_bytes() == src:
                continue
            if args.check:
                drift.append(dest.relative_to(PLUGIN.parents[1]))
            else:
                dest.parent.mkdir(parents=True, exist_ok=True)
                dest.write_bytes(src)
                if dest.suffix == ".py":
                    dest.chmod(0o755)
                print(f"wrote {dest.relative_to(PLUGIN.parents[1])}")
    if drift:
        print("Out of sync with plugins/career-os/shared/ (run python3 scripts/sync_shared.py):")
        for d in drift:
            print(f"  {d}")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
