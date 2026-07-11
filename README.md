Hi!

This is my personal website: Wu Feiyang.

Website: [https://wfy-op.github.io](https://wfy-op.github.io)

## Deployment

This site is built with Jekyll and deployed to GitHub Pages through GitHub Actions.

The public structure is `Home · Research · Publications · Notes · CV`. PCSEL remains the primary program inside Research, with selected validation cases, research software, and reproducible evidence/progress metrics kept on the PCSEL page.

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

Update: Jul. 2026
