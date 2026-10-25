Hi!

This is my personal website: Wu Feiyang.

Website: [https://wfy-op.github.io](https://wfy-op.github.io)

## Deployment

This site is built with Jekyll and deployed to GitHub Pages through GitHub Actions.

The public structure is `Home · Research · Publications · Software · Notes · CV`. This is a personal introduction and project record. PCSEL remains the primary program inside Research; Software gives a concise overview of computing, data, and learning tools.

- Push changes to `main` to trigger a production deployment.
- Use the Actions tab to run `Deploy Jekyll site to GitHub Pages` manually when needed.
- The build command is `bundle exec jekyll build`, and the published artifact is `_site`.

## Local Preview

Install Ruby and Bundler, then run:

```bash
bundle install
bundle exec jekyll serve
```

Static content and data checks can run without Ruby:

```bash
python -m unittest discover -s tests -v
```

## Updating profile content

- `_data/software.yml` supplies the project list and selected homepage entries; use public descriptions and links only.
- Project screenshots use the same data source. Only flattened, reviewed captures belong in `images/software/`; see [capture and privacy notes](docs/screenshot-showcase.md). Never commit unmasked originals or private capture scripts.
- Keep the two arXiv preprints separate from journal articles in Publications and both CV languages.
- CV source lives in the adjacent `CODE_Latex/wfy-cv` project. Compile both languages and sync the two small final PDFs into `files/Feiyang-Wu-CV-EN.pdf` and `files/Feiyang-Wu-CV-ZH.pdf`.
- Local provenance notes in `docs/local-project-sources.md` stay out of Git and the public build. Existing research evidence snapshots retain their own dates.

Update: Oct. 2026
