import json
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest
from unittest.mock import patch

from scripts import update_research_portal


ROOT = Path(__file__).resolve().parents[1]
TEST_TMP = ROOT / "tmp"


class ResearchPortalDataTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        TEST_TMP.mkdir(exist_ok=True)

    def test_paper_library_separates_indexed_analyzed_and_promoted_counts(self):
        with TemporaryDirectory(dir=TEST_TMP) as temp_dir:
            root = Path(temp_dir)
            parsed = root / "knowledge" / "parsed"
            parsed.mkdir(parents=True)
            records = [
                {
                    "title": "Paper A",
                    "year": 2024,
                    "doi": "10.1/a",
                    "source_group": "Group A",
                    "exported_at": "snapshot-a",
                },
                {
                    "title": "Paper B",
                    "year": 2025,
                    "doi": "",
                    "source_group": "Group B",
                    "exported_at": "snapshot-a",
                },
            ]
            (parsed / "external_paper_index.jsonl").write_text(
                "\n".join(json.dumps(record) for record in records) + "\n",
                encoding="utf-8",
            )
            (parsed / "standardized_paper_analysis.json").write_text(
                json.dumps({"paper_count": 1, "papers": [{"title": "Paper A"}]}),
                encoding="utf-8",
            )

            import_dir = (
                root
                / "knowledge"
                / "imports"
                / "nas_pcsel_paper_library"
                / "20260710-review"
            )
            import_dir.mkdir(parents=True)
            (import_dir / "promotion_dry_run.json").write_text(
                json.dumps({"design_priors_auto_promoted": 0}),
                encoding="utf-8",
            )

            with patch.object(
                update_research_portal, "PORTAL_IMAGE_DIR", root / "public-images"
            ):
                result = update_research_portal.load_paper_library(root)

        self.assertEqual(result["records"], 2)
        self.assertEqual(result["standardized_analyses"], 1)
        self.assertEqual(result["design_priors_auto_promoted"], 0)
        self.assertEqual(result["promotion_status"], "dry-run only")

    def test_cwt_uses_closure_manifest_instead_of_file_volume(self):
        with TemporaryDirectory(dir=TEST_TMP) as temp_dir:
            root = Path(temp_dir)
            report = root / "report" / "oe_20_15945_full_figure_reproduction_20260711"
            figures = report / "current_cwt_figures"
            figures.mkdir(parents=True)
            (figures / "fig2i_et_l70_delta_alpha.png").write_bytes(b"figure-a")
            (figures / "fig5_length_dependence_sweep.png").write_bytes(b"figure-b")
            (report / "figure_reproduction_report.html").write_text(
                "<html></html>", encoding="utf-8"
            )
            (report / "manifest.json").write_text(
                json.dumps(
                    {
                        "item_closure_summary": {
                            "item_count": 8,
                            "pass_count": 1,
                            "diagnostic_count": 6,
                            "blocked_count": 1,
                        },
                        "panel_coverage_summary": {
                            "panel_count": 17,
                            "all_panels_closed": False,
                        },
                    }
                ),
                encoding="utf-8",
            )

            with patch.object(
                update_research_portal, "PORTAL_IMAGE_DIR", root / "public-images"
            ):
                result = update_research_portal.load_cwt(root)

        self.assertEqual(result["item_count"], 8)
        self.assertEqual(result["pass_count"], 1)
        self.assertEqual(result["diagnostic_count"], 6)
        self.assertEqual(result["blocked_count"], 1)
        self.assertEqual(result["panel_count"], 17)
        self.assertFalse(result["all_panels_closed"])
        self.assertEqual(len(result["figures"]), 2)


if __name__ == "__main__":
    unittest.main()
