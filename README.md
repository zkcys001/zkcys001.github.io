# Kecheng Zheng — Research homepage

A static research homepage for Kecheng Zheng, featuring recent news, six LingBot projects, and selected papers from 2024 onward within the current calendar year and the preceding three years, grouped by year, newest first.

## Local preview

```sh
python3 -m http.server 8765 --bind 127.0.0.1
```

Open http://127.0.0.1:8765/. No application dependencies or build tools are required.

## Editing

- `index.html`: profile, recent news, project videos, and publication records. The hidden archive combines 23 existing records with 35 supplemental records in `recentPublications`. The selection excludes papers before 2024 and includes the six featured projects' papers (`selectedProject: true`) plus papers where Kecheng Zheng is first author, co-first author, corresponding author, or project lead. Roles use author order and the existing `*`, `#`, and `†` markers, which can be combined; bold author names alone do not qualify. Older papers remain available in the full-publications view.
- `stylesheet.css`: responsive layout, typography, colors, and interaction states.
- `images/`: portrait, local video posters, and publication figures.
- `data/`: BibTeX downloads.

Video demos load when visible and respect reduced-motion and data-saving preferences. Every demo also has a manual playback control. Papers are grouped by year in descending order, with every year open by default. Each paper retains its venue label. The default view shows selected papers; the heading button toggles all 58 publications and back, updating year groups and counts. The source archive stays hidden before JavaScript runs.

## Sites packaging

```sh
python3 scripts/prepare_site.py
```

This copies public assets into `dist/`; `.openai/hosting.json` configures the private Sites deployment. Temporary research files in `tmp/` are excluded. The root page remains usable as a standard GitHub Pages site.

Based on the source of Jon Barron's public academic website; see `LICENSE`.
