# Research Portal Content Hierarchy Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Make the personal site easier to scan by placing current PCSEL research first, using real research figures for the three research directions, and moving supporting PCSEL evidence into clearly labeled secondary disclosures without removing important claims.

**Architecture:** Keep the existing Jekyll/Minimal Mistakes structure and URLs. Recompose the home page from a compact facts strip, image-led research programs, and a single PCSEL workflow feature; simplify the PCSEL anchor map; retain generated portal data while presenting secondary modules through native HTML disclosures. Add only CSS selectors needed by the new hierarchy.

**Tech Stack:** Jekyll, Liquid, Markdown/HTML, SCSS, Python `unittest`, GitHub Pages.

## Global Constraints

- PCSEL remains nested at `/research/pcsel/`; it is not added to the global navigation.
- Preserve PCSEL, memristor, LN/LT waveguide, Prof. Lei Wang collaboration, publications, patent, PCSELBook, RLcode, RLcomsol, paper library, and solver-skill content.
- Use only existing real simulation, experiment, or project figures; do not fabricate paper reproductions.
- Keep private paths, chats, raw reports, and unreleased artifacts out of public output.
- Preserve desktop and mobile readability with no horizontal overflow.

---

### Task 1: Encode the hierarchy contract

**Files:**
- Modify: `tests/test_site_frontend.py`

**Interfaces:**
- Consumes: static Jekyll source files.
- Produces: tests asserting home-page hierarchy, PCSEL section hierarchy, secondary disclosures, and required image coverage.

- [x] **Step 1: Write failing tests** for `home-research-grid`, three linked image-led directions, the six-link PCSEL index, `pcsel-system`, and `evidence-disclosure` markup.
- [x] **Step 2: Run** `C:\ProgramData\anaconda3\envs\AI_group\python.exe -m unittest discover -s tests -p test_site_frontend.py -v` and confirm failures mention the missing hierarchy selectors.
- [x] **Step 3: Do not modify production files until the expected failures are observed.**

### Task 2: Recompose the home page

**Files:**
- Modify: `_pages/about.md`
- Modify: `assets/css/wfy-modern.scss`

**Interfaces:**
- Consumes: `/images/research/pcsel_device_concept.png`, `/images/research/memristor_reservoir_framework.png`, and `/images/research/waveguide_phase_matching_ln_lt.png`.
- Produces: `home-facts`, `home-research-grid`, `home-research-card`, and one `home-feature` workflow section.

- [x] **Step 1: Replace** the six-card Evidence Snapshot with four compact facts: current role, current PCSEL focus, two papers, and accepted patent application.
- [x] **Step 2: Replace** duplicate workflow/highlight blocks with three linked image-led research cards, making PCSEL the primary card.
- [x] **Step 3: Keep** one concise PCSEL workflow feature with three evidence-gate bullets.
- [x] **Step 4: Add** stable image aspect ratios, primary-card desktop span, and single-column mobile styles.
- [x] **Step 5: Run** `C:\ProgramData\anaconda3\envs\AI_group\python.exe -m unittest discover -s tests -p test_site_frontend.py -v` and confirm the home hierarchy tests pass.

### Task 3: Simplify the PCSEL narrative

**Files:**
- Modify: `_pages/research-pcsel.md`
- Modify: `_includes/research-portal-dashboard.html`
- Modify: `assets/css/wfy-modern.scss`

**Interfaces:**
- Consumes: `site.data.research_portal`, existing validation figures, existing workstream figures, and the existing agent architecture figure.
- Produces: six top-level anchors: `pcsel-overview`, `selected-validation`, `research-threads`, `pcsel-portal`, `pcsel-system`, and `next-questions`.

- [x] **Step 1: Replace** the ten-link section index with six decision-oriented links.
- [x] **Step 2: Present** the scientific question as an image-led program overview with explicit Question, Method, and Decision rule.
- [x] **Step 3: Move** pcsel-agent workstreams immediately after validation cases and retain their real figures.
- [x] **Step 4: Consolidate** Project Stack, public boundaries, architecture, report corpus, and device loop into `pcsel-system`; place the long report corpus inside a native disclosure.
- [x] **Step 5: Keep** HX1/COMSOL-FDTD evidence visible; place literature detail, RLcomsol, CWT, and DailyBrief modules in labeled `evidence-disclosure` elements whose summaries expose their current key metric.
- [x] **Step 6: Remove** duplicate Public Evidence Map, Related Project Artifacts, and Representative PCSEL Figures sections after their unique information has been retained in the consolidated system and visible workstreams.
- [x] **Step 7: Style** disclosures with accessible focus states, clear summary labels, responsive media, and no nested-card treatment.
- [x] **Step 8: Run** the frontend test module and then the full unittest suite.

### Task 4: Verify and publish

**Files:**
- Inspect: generated GitHub Pages deployment and live pages.

**Interfaces:**
- Consumes: committed source on `main`.
- Produces: a successful GitHub Pages build and visually verified live home, Research, and PCSEL pages.

- [ ] **Step 1: Run** `C:\ProgramData\anaconda3\envs\AI_group\python.exe -m unittest discover -s tests -v` and require zero failures.
- [ ] **Step 2: Review** `git diff --check` and `git diff --stat`; stage only intended files.
- [ ] **Step 3: Commit and push** the hierarchy update to `main` without staging unrelated `.DS_Store` or `.claude/settings.local.json` changes.
- [ ] **Step 4: Confirm** both the final workflow and GitHub Pages deployment succeed for the pushed SHA.
- [ ] **Step 5: Inspect** the live home and PCSEL pages at desktop and 390 px mobile widths; verify images load, disclosures work, and `scrollWidth <= clientWidth`.
