from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


class FrontendContractTests(unittest.TestCase):
    def test_modern_stylesheet_is_loaded_after_legacy_styles(self):
        custom_head = read("_includes/head/custom.html")
        stylesheet_link = "/assets/css/wfy-modern.css"
        self.assertIn(stylesheet_link, custom_head)
        self.assertGreater(custom_head.index(stylesheet_link), custom_head.rindex("</style>"))

    def test_modern_stylesheet_defines_visual_and_responsive_contract(self):
        stylesheet = read("assets/css/wfy-modern.scss")
        required_fragments = (
            "--portal-bg",
            "--portal-accent",
            ".masthead",
            ".author__avatar img",
            ".section-index",
            ".portal-module",
            "@media (min-width: 1024px)",
            "@media (max-width: 720px)",
            ":focus-visible",
        )
        for fragment in required_fragments:
            with self.subTest(fragment=fragment):
                self.assertIn(fragment, stylesheet)

    def test_pcsel_page_has_a_complete_section_index(self):
        page = read("_pages/research-pcsel.md") + read(
            "_includes/research-portal-dashboard.html"
        )
        self.assertIn('class="section-index"', page)
        for target in (
            "pcsel-question",
            "pcsel-portal",
            "public-evidence",
            "selected-validation",
            "pcsel-projects",
            "pcsel-agent",
            "device-loop",
            "next-questions",
            "representative-figures",
        ):
            with self.subTest(target=target):
                self.assertIn(f'href="#{target}"', page)
                self.assertIn(f'id="{target}"', page)

    def test_pcsel_stays_inside_research_information_architecture(self):
        navigation = read("_data/navigation.yml")
        research = read("_pages/research.md")
        pcsel = read("_pages/research-pcsel.md")

        self.assertIn('title: "Research"', navigation)
        self.assertNotIn('title: "PCSEL"', navigation)
        self.assertNotIn('title: "Projects"', navigation)
        self.assertIn("permalink: /research/pcsel/", pcsel)
        self.assertIn("'/research/pcsel/'", research)

    def test_home_prioritizes_research_over_dashboard_language(self):
        home = read("_pages/about.md")

        self.assertIn("PCSEL Research", home)
        self.assertNotIn("PCSEL Dashboard", home)
        self.assertNotIn("~300,000-character", home)

    def test_pcsel_page_contains_evidence_bounded_validation_cases(self):
        page = read("_pages/research-pcsel.md")
        required_fragments = (
            'id="selected-validation"',
            'class="validation-case-grid"',
            "Mode-localization gate",
            "Boundary and convergence audit",
            "SCH400 candidate rejection",
            "Fabrication-morphology screen",
            "Literature reproduction ladder",
            "Diagnostic only",
            "Full-wave result",
            "Surrogate screening",
            "No-go",
            "Cross-solver check",
            "screen-reject",
        )
        for fragment in required_fragments:
            with self.subTest(fragment=fragment):
                self.assertIn(fragment, page)

        for image in (
            "apl2018_mode_localization_progression.png",
            "hx1_buffer_convergence.svg",
            "sch400_failure_modes.png",
            "hx1_uniformity_morphology_screen.png",
            "sch_mode_fde_profile.png",
        ):
            with self.subTest(image=image):
                self.assertTrue((ROOT / "images" / "research" / "validation" / image).exists())

    def test_home_has_compact_recognition_and_community_section(self):
        home = read("_pages/about.md")
        for fragment in (
            "Recognition & Community",
            "National Second Prize",
            "50,000+ views",
            "Taishan Seminar",
            "Physics Innovation Alliance",
        ):
            with self.subTest(fragment=fragment):
                self.assertIn(fragment, home)

    def test_portal_uses_evidence_progress_language(self):
        dashboard = read("_includes/research-portal-dashboard.html")
        self.assertIn("Evidence &amp; progress", dashboard)
        self.assertNotIn("research evidence dashboard", dashboard)
        self.assertIn("standardized analyses", dashboard)
        self.assertIn("auto-promoted design priors", dashboard)

    def test_sidebar_uses_confirmed_contact_email(self):
        config = read("_config.yml")
        self.assertIn('email            : "wfy18350221083@163.com"', config)

    def test_internal_build_files_are_excluded_from_public_site(self):
        config = read("_config.yml")
        for path in ("scripts", "tests", "docs/superpowers"):
            with self.subTest(path=path):
                self.assertRegex(config, rf"(?m)^  - {path}$")

    def test_key_research_information_remains_present(self):
        pages = "\n".join(
            read(path)
            for path in (
                "_pages/about.md",
                "_pages/research.md",
                "_pages/research-pcsel.md",
                "_pages/research-memristor.md",
                "_pages/research-waveguide.md",
                "_pages/projects.md",
                "_pages/publications.md",
            )
        )
        required_terms = (
            "GaAs Photonic Crystal Surface-Emitting",
            "pcsel-agent",
            "PCSELBook",
            "codex-for-comsol-lumerical",
            "RLcode",
            "RLcomsol",
            "PCSEL Paper Library",
            "Memristor-Based Reservoir Computing",
            "LN/LT Waveguide Mode Analysis",
            "CN 202610820592.4",
            "Advanced Materials",
            "Materials Futures",
        )
        for term in required_terms:
            with self.subTest(term=term):
                self.assertIn(term, pages)


if __name__ == "__main__":
    unittest.main()
