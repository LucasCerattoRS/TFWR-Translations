import sys
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "tools"))
import check_translations as ct  # noqa: E402

FIX = HERE / "fixtures"


class CheckTranslations(unittest.TestCase):
    def test_good_fixture_passes(self):
        self.assertEqual(ct.check(FIX / "good"), [])

    def test_lost_key_fails(self):
        errs = ct.check(FIX / "bad_key")
        self.assertEqual(errs, ["XX/Strings/a.txt: missing key @bye"])

    def test_lost_placeholder_fails(self):
        errs = ct.check(FIX / "bad_placeholder")
        self.assertEqual(len(errs), 1)
        self.assertIn("@hello: placeholder missing {1}", errs[0])

    def test_lost_double_brace_in_docs_fails(self):
        errs = ct.check(FIX / "bad_docs")
        self.assertEqual(len(errs), 1)
        self.assertIn("XX/docs/p.md: placeholder missing {{itemblock}}", errs[0])

    def test_unbalanced_backtick_fails(self):
        errs = ct.check(FIX / "bad_backtick")
        self.assertEqual(len(errs), 1)
        self.assertIn("unbalanced backticks", errs[0])

    def test_cli_exit_codes(self):
        self.assertEqual(ct.main([str(FIX / "good")]), 0)
        self.assertEqual(ct.main([str(FIX / "bad_key")]), 1)

    def test_repo_has_no_new_problems(self):
        root = HERE.parent
        known = set((root / "tools/known_issues.txt").read_text(encoding="utf-8").splitlines())
        self.assertEqual([e for e in ct.check(root) if e not in known], [])


if __name__ == "__main__":
    unittest.main()
