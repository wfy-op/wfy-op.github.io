# Modern Research Portal Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Restyle the existing Jekyll personal site as a modern, minimal research portal and foreground evidence-bounded PCSEL validation cases without removing substantive information.

**Architecture:** Add one late-loaded Jekyll SCSS entry point that overrides the legacy Academic Pages theme and existing component styles. Keep PCSEL nested under Research, add real-result validation cards, and generate literature/CWT status from local aggregate artifacts.

**Tech Stack:** Jekyll, Liquid, Markdown, SCSS/CSS, Python standard-library `unittest`.

## Global Constraints

- Preserve all research claims, metrics, dates, publications, patent status, figures, and public/private evidence boundaries.
- Add no external font, JavaScript framework, or runtime dependency.
- Keep cards at 6px radius or less and major page sections unframed.
- Keep PCSEL, memristor, and LN/LT waveguide research visible.
- Keep PCSEL inside the Research information architecture rather than global navigation.
- Distinguish indexed papers, standardized analyses, and auto-promoted design priors.
- Support desktop, tablet, and mobile layouts without text clipping or horizontal page overflow.

---

### Task 1: Static Frontend Contract

**Files:**
- Create: `tests/test_site_frontend.py`

**Interfaces:**
- Consumes: repository Markdown, YAML, HTML include, and SCSS files.
- Produces: `python -m unittest tests.test_site_frontend -v` as the repeatable acceptance command.

- [ ] **Step 1: Write tests for the late-loaded stylesheet, design tokens, responsive rules, PCSEL index, correct email, and content invariants.**
- [ ] **Step 2: Run the test module and confirm it fails because the new stylesheet and section index do not exist.**

### Task 2: Modern Visual System

**Files:**
- Create: `assets/css/wfy-modern.scss`
- Modify: `_includes/head/custom.html`
- Modify: `_config.yml`

**Interfaces:**
- Consumes: existing Minimal Mistakes classes and the site's custom component classes.
- Produces: `/assets/css/wfy-modern.css`, loaded after legacy styles.

- [ ] **Step 1: Add the Jekyll SCSS entry point with color, spacing, typography, focus, navigation, sidebar, content, component, portal, and responsive rules.**
- [ ] **Step 2: Link the compiled stylesheet after the existing custom style block.**
- [ ] **Step 3: Update the sidebar email to `wfy18350221083@163.com`.**
- [ ] **Step 4: Run the static tests and confirm only the PCSEL index assertion remains failing.**

### Task 3: PCSEL Long-Page Navigation

**Files:**
- Modify: `_pages/research-pcsel.md`

**Interfaces:**
- Consumes: existing section headings and IDs from the PCSEL page and dashboard include.
- Produces: `.section-index` with valid fragment links and explicit section IDs.

- [ ] **Step 1: Add the index links near the top of the page.**
- [ ] **Step 2: Add stable IDs to the scientific question, evidence map, project stack, pcsel-agent, device loop, future questions, research threads, related artifacts, and figure sections.**
- [ ] **Step 3: Run the static tests and confirm the complete module passes.**

### Task 4: Build and Visual Acceptance

**Files:**
- Verify only; no planned production edits.

**Interfaces:**
- Consumes: generated Jekyll output or live/local browser rendering.
- Produces: build logs, desktop screenshot, and mobile screenshot.

- [ ] **Step 1: Run `bundle exec jekyll build` when Bundler is available; otherwise record the missing local dependency.**
- [ ] **Step 2: Render desktop and mobile views and inspect navigation, portrait crop, grids, tables, images, and overflow.**
- [ ] **Step 3: Run `git diff --check`, image-reference checks, and the static test suite.**
- [ ] **Step 4: Review the final diff to ensure unrelated dirty files were not modified.**
