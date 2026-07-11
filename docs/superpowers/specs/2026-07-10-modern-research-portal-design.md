# Modern Research Portal Design

## Objective

Refresh the existing Jekyll site as a modern, minimal academic research portal while preserving every substantive claim, project, publication, patent record, research direction, evidence boundary, figure, and contact route already present.

## Visual Direction

- Use an off-white page background, white content surfaces, graphite text, muted teal for actions, and amber only for evidence/status labels.
- Keep corners at 6px or less, shadows very subtle, and motion limited to focus and hover feedback.
- Use a system sans-serif stack with restrained heading sizes and generous line-height. No external font or JavaScript dependency is added.
- Treat major page sections as unframed content bands. Cards remain only for repeated evidence items, projects, metrics, publications, and figures.

## Information Architecture

- Use a five-item global navigation: Home, Research, Publications, Notes, and CV.
- Keep PCSEL as the primary program inside Research rather than a separate global-navigation item.
- Keep `/projects/` as a linked Research Software page, not a top-level destination.
- Use the desktop sidebar as a compact identity rail with a consistently centered portrait, institution, location, email, GitHub, and Zhihu links.
- Preserve the homepage sequence: research thesis, evidence snapshot, trajectory, current PCSEL workflow, research highlights, education, publications, useful links, and contact.
- Add a compact in-page index to the long PCSEL page so visitors can jump to the scientific question, validation cases, evidence and progress, evidence map, project stack, pcsel-agent, device loop, open questions, and figures. Explicit section IDs avoid collisions with Kramdown's generated heading IDs.

## Component Rules

- The homepage hero is typographic and unframed. Its primary action is PCSEL Research; supporting destinations read as secondary actions.
- Validation cases use real computed figures and pair each finding with an evidence-status label and an explicit interpretation boundary.
- Evidence and project grids use consistent padding, metadata labels, title scales, and borders.
- Outer PCSEL portal modules and major research sections remain unframed; their inner repeated data items may use cards.
- Tables retain all columns and become horizontally scrollable on narrow screens.
- Images use stable aspect ratios where appropriate, `object-fit`, and existing alt text. The author portrait uses a 4:5 crop centered on the face and body.

## Responsive Behavior

- At desktop widths, the page uses a two-column identity-rail/content layout with a maximum readable content width.
- At tablet and mobile widths, content becomes one column, cards collapse to one column, action rows wrap, and the PCSEL section index becomes horizontally scrollable.
- No text may overlap, clip, or force page-width overflow. Buttons and links keep visible keyboard focus states.

## Data and Content Boundaries

- Do not inflate research claims, publication metadata, patent status, or public/private evidence boundaries.
- Keep indexed literature records, standardized analyses, and promoted design priors as separate metrics.
- Keep PCSEL, memristor, and LN/LT waveguide research visible as separate directions.
- Keep pcsel-agent, PCSELBook, codex-for-comsol-lumerical, RLcode, RLcomsol, and the PCSEL paper library visible.
- Use `wfy18350221083@163.com` as the sidebar contact email. The homepage may continue to show the existing Gmail address as an additional route.

## Verification

- Static tests assert that the new stylesheet is loaded, responsive rules and design tokens exist, the PCSEL index is present, the sidebar email is correct, and key research content remains present.
- A Jekyll build is attempted with the available local toolchain. If unavailable, report that explicitly and rely on static checks plus browser rendering of the live or locally served output when possible.
- Desktop and mobile screenshots are checked for navigation, portrait crop, section hierarchy, overflow, and image rendering.
