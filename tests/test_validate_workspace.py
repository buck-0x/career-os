"""Tests for plugins/career-os/shared/validate_workspace.py (stdlib unittest).

Run: python3 -m unittest discover tests
"""

import io
import json
import sys
import tempfile
import textwrap
import unittest
from contextlib import redirect_stderr, redirect_stdout
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "plugins" / "career-os" / "shared"))

import validate_workspace as vw  # noqa: E402

TODAY = "2026-10-04"


def fm(title, type_, status="complete", updated=TODAY, extra=""):
    return (f"---\ntitle: {title}\ntype: {type_}\nstatus: {status}\n"
            f"last_updated: {updated}\nopen_questions: []\n{extra}---\n")


VALID = {
    "README.md": textwrap.dedent("""\
        # Career Workspace: Sam

        ## Status
        | Area | Location | Status | Last updated |
        |---|---|---|---|
        | Ground truth | ground-truth/ | partial | 2026-10-04 |
        | Portfolio | portfolio/ | partial | 2026-10-04 |
        | Positioning | positioning/ | draft | 2026-10-04 |
        """),
    "changelog.md": "- 2026-10-04 [positioning-studio]: created linkedin asset\n",
    "ground-truth/03-professional-capital.md": fm("Professional Capital", "ground-truth") + textwrap.dedent("""\
        # Professional Capital

        ## Hard skills
        | Skill | Level | Evidence |
        |---|---|---|
        | React | Unaided | EV-001 |

        ## Not claimed
        - Kubernetes: never run it in production [stated]
        - People management (anti-skill, never had reports) [stated]
        """),
    "portfolio/evidence-inventory.md": fm("Evidence Inventory", "portfolio", "partial") + textwrap.dedent("""\
        # Evidence Inventory

        ## Items

        ### EV-001: Checkout redesign
        - **Kind:** project
        - **Result:** conversion up 12% in 2024 [source: resume]

        ### EV-002: Design system
        - **Kind:** project
        - **Result:** adopted by 40 engineers [stated]
        """),
    "positioning/assets/linkedin.md": fm("LinkedIn", "positioning", "draft", extra="derived_from: [EV-001, EV-002]\n") + textwrap.dedent("""\
        # LinkedIn

        ## Approved
        Design engineer who lifted checkout conversion 12% and built a design system 40 engineers use.

        ## Proof map
        | Claim | Evidence |
        |---|---|
        | Lifted checkout conversion 12% | EV-001 |
        | Design system used by 40 engineers | EV-002 |

        ## Not for
        People management roles.
        """),
}


class WorkspaceCase(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.ws = Path(self.tmp.name) / "career-workspace"
        for rel, text in VALID.items():
            self.write(rel, text)

    def tearDown(self):
        self.tmp.cleanup()

    def write(self, rel, text):
        p = self.ws / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(text, encoding="utf-8")
        return p

    def codes(self, full=True):
        import datetime as dt
        return [f.code for f in vw.validate(self.ws, dt.date.fromisoformat(TODAY), full=full)
                if f.level == "ERROR"]


class TestValid(WorkspaceCase):
    def test_valid_workspace_has_no_errors(self):
        self.assertEqual(self.codes(), [])

    def test_cli_exit_zero(self):
        with redirect_stdout(io.StringIO()):
            self.assertEqual(vw.main([str(self.ws), "--today", TODAY]), 0)


class TestFrontmatter(WorkspaceCase):
    def test_missing_frontmatter(self):
        self.write("ground-truth/02-core-psychology-values.md", "# Values\n")
        self.assertIn("E-FM", self.codes())

    def test_bad_enum_and_date(self):
        self.write("titles/candidates.md", fm("Candidates", "titles", "done", updated="Oct 4"))
        errs = [f.message for f in vw.validate(self.ws, vw.dt.date.fromisoformat(TODAY))
                if f.code == "E-FM"]
        self.assertTrue(any("type `titles`" in m for m in errs))
        self.assertTrue(any("status `done`" in m for m in errs))
        self.assertTrue(any("YYYY-MM-DD" in m for m in errs))

    def test_future_date(self):
        self.write("titles/candidates.md", fm("Candidates", "title", updated="2027-01-01"))
        self.assertIn("E-FM", self.codes())

    def test_multiline_list_and_sensitivity(self):
        self.write("ground-truth/06-trajectory-non-negotiables.md", textwrap.dedent("""\
            ---
            title: Trajectory
            type: ground-truth
            status: partial
            last_updated: 2026-10-04
            sensitivity: restricted
            open_questions:
              - "Equity vs cash?"
            ---
            # Trajectory
            """))
        self.assertEqual(self.codes(), [])

    def test_bad_sensitivity(self):
        self.write("ground-truth/05-whole-human.md",
                   fm("Whole Human", "ground-truth", extra="sensitivity: secret\n"))
        self.assertIn("E-FM", self.codes())


class TestEvidence(WorkspaceCase):
    def test_duplicate_ev(self):
        p = self.ws / "portfolio/evidence-inventory.md"
        p.write_text(p.read_text() + "\n### EV-002: Again\n- **Kind:** talk\n")
        self.assertIn("E-EV-DUP", self.codes())

    def test_dangling_ev_reference(self):
        self.write("titles/title-stack.md", fm("Title Stack", "title") + "Backed by EV-099.\n")
        self.assertIn("E-EV-REF", self.codes())

    def test_dangling_derived_from(self):
        self.write("titles/candidates.md", fm("Candidates", "title", extra="derived_from: [EV-777]\n"))
        self.assertIn("E-EV-REF", self.codes())


class TestOutward(WorkspaceCase):
    def test_bare_suggested_in_asset(self):
        p = self.ws / "positioning/assets/linkedin.md"
        p.write_text(p.read_text().replace("## Proof map", "Systems thinker [suggested]\n\n## Proof map"))
        self.assertIn("E-UNAPPROVED", self.codes())

    def test_approved_suggestion_ok(self):
        p = self.ws / "positioning/assets/linkedin.md"
        p.write_text(p.read_text().replace("## Proof map", "Systems thinker [suggested → approved]\n\n## Proof map"))
        self.assertNotIn("E-UNAPPROVED", self.codes())

    def test_missing_proof_map(self):
        self.write("positioning/assets/founders.md", fm("Founders", "positioning", "draft") + "# Founders\nHi.\n")
        self.assertIn("E-PROOF-MAP", self.codes())

    def test_proof_row_without_evidence(self):
        p = self.ws / "positioning/assets/linkedin.md"
        p.write_text(p.read_text() + "")
        text = p.read_text().replace("| Design system used by 40 engineers | EV-002 |",
                                     "| Design system used by 40 engineers | trust me |")
        p.write_text(text)
        self.assertIn("E-PROOF-MAP", self.codes())

    def test_invented_number_not_in_proof_map(self):
        p = self.ws / "positioning/assets/linkedin.md"
        p.write_text(p.read_text().replace("lifted checkout conversion 12%", "lifted checkout conversion 35%"))
        self.assertIn("E-NUMBER", self.codes())

    def test_number_in_map_but_not_in_cited_evidence(self):
        p = self.ws / "positioning/assets/linkedin.md"
        text = p.read_text().replace("12%", "35%")
        p.write_text(text)
        msgs = [f.message for f in vw.validate(self.ws, vw.dt.date.fromisoformat(TODAY)) if f.code == "E-NUMBER"]
        self.assertTrue(any("none of the cited evidence" in m for m in msgs))

    def test_tagged_number_accepted(self):
        p = self.ws / "positioning/assets/linkedin.md"
        text = p.read_text().replace("12%", "$2M").replace("| EV-001 |", "| [stated] |")
        p.write_text(text)
        self.assertNotIn("E-NUMBER", self.codes())

    def test_years_and_headings_ignored(self):
        p = self.ws / "positioning/assets/linkedin.md"
        p.write_text(p.read_text().replace("## Approved", "## 150-word bio\nSince 2019, I build things.\n\n## Approved"))
        self.assertNotIn("E-NUMBER", self.codes())

    def test_absence_term_in_asset(self):
        p = self.ws / "positioning/assets/linkedin.md"
        p.write_text(p.read_text().replace("built a design system", "ran Kubernetes and built a design system"))
        self.assertIn("E-ABSENCE", self.codes())

    def test_absence_term_allowed_in_not_for(self):
        p = self.ws / "positioning/assets/linkedin.md"
        p.write_text(p.read_text().replace("People management roles.", "People management roles; Kubernetes ops."))
        self.assertNotIn("E-ABSENCE", self.codes())


class TestSession(WorkspaceCase):
    def test_changelog_required_for_today(self):
        (self.ws / "changelog.md").write_text("- 2026-09-01 [x]: old\n")
        self.assertIn("E-CHANGELOG", self.codes())
        self.assertNotIn("E-CHANGELOG", self.codes(full=False))

    def test_stale_warning(self):
        self.write("interests/topics/old.md", fm("Old", "interest", updated="2024-01-01"))
        import datetime as dt
        warns = [f.code for f in vw.validate(self.ws, dt.date.fromisoformat(TODAY)) if f.level == "WARN"]
        self.assertIn("W-STALE", warns)
        self.assertIn("W-README", warns)  # interests/ has no README row


class TestHook(WorkspaceCase):
    def run_hook(self, rel):
        payload = json.dumps({"tool_name": "Write", "tool_input": {"file_path": str(self.ws / rel)}})
        err = io.StringIO()
        old = sys.stdin
        sys.stdin = io.StringIO(payload)
        try:
            with redirect_stderr(err):
                code = vw.main(["--hook", "--today", TODAY])
        finally:
            sys.stdin = old
        return code, err.getvalue()

    def test_hook_clean(self):
        self.assertEqual(self.run_hook("positioning/assets/linkedin.md"), (0, ""))

    def test_hook_reports_errors_with_exit_2(self):
        p = self.ws / "positioning/assets/linkedin.md"
        p.write_text(p.read_text().replace("12%", "35%"))
        code, err = self.run_hook("positioning/assets/linkedin.md")
        self.assertEqual(code, 2)
        self.assertIn("E-NUMBER", err)

    def test_hook_ignores_other_files(self):
        p = self.ws / "positioning/assets/linkedin.md"
        p.write_text(p.read_text().replace("12%", "35%"))
        self.assertEqual(self.run_hook("interests/index.md")[0], 0)

    def test_hook_outside_workspace(self):
        payload = json.dumps({"tool_input": {"file_path": "/tmp/not-a-workspace/notes.md"}})
        old = sys.stdin
        sys.stdin = io.StringIO(payload)
        try:
            self.assertEqual(vw.main(["--hook"]), 0)
        finally:
            sys.stdin = old

    def test_hook_absence_edit_rechecks_assets(self):
        p = self.ws / "ground-truth/03-professional-capital.md"
        p.write_text(p.read_text() + "- design system: not mine [stated]\n")
        code, err = self.run_hook("ground-truth/03-professional-capital.md")
        self.assertEqual(code, 2)
        self.assertIn("E-ABSENCE", err)


class TestFindWorkspace(WorkspaceCase):
    def test_find_by_readme_title(self):
        other = Path(self.tmp.name) / "my-career"
        self.ws.rename(other)
        found = vw.find_workspace(other / "positioning" / "assets" / "linkedin.md")
        self.assertEqual(found, other.resolve())


if __name__ == "__main__":
    unittest.main()
