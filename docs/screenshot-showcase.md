# Project interface screenshots

Capture date: 2026-10-25.

The homepage shows one preview per illustrated project. The Software page uses the same data in `_data/software.yml` and provides two full-size PNG links per project. Images live under `images/software/`; screenshots are actual application renders, not generated mockups.

| Project | Captures | Privacy treatment |
| --- | --- | --- |
| Experimental data system | Homepage; multi-batch analysis | Opaque masks cover record identifiers, laboratory statistics, measurement images/results, source locations, and status details. |
| PCSEL Research Studio | Homepage; batch comparison | Opaque masks cover private conversations, source records, batch identifiers, research values, progress, and internal connection details. |
| PCSEL Paper Library | Search; paper-detail reading card | At the user's request, literature metadata, parameters, reading cards, filters, and library statistics remain visible. Only local file paths and private AI history are hidden. No full-text PDF page is reproduced. |
| PCSEL process records | Standard run-sheet page; process overview | Opaque masks cover identity, sample and recipe-specific details, process parameters, actual progress, metrics, and connection information. |
| PCSELBook knowledge site | Homepage; teaching chapter | Publicly available teaching content only. |
| Optical Lab | Homepage; interactive workbench | Public interface and a teaching example only. |

Masks were applied in the browser before each capture. There is no hidden original beneath a mask in the PNG, and no unmasked screenshot is supplied with the site. Capture scripts and private route/selector audits stay under ignored `tmp/`; do not add them to Git or the public build.

When updating captures, inspect the final image itself for text, charts, axes, identifiers, local paths, connection details, accounts, and recipe information. Keep the interface layout and function names; never replace private values with invented results. Capture at 1440 × 1000 for consistent previews, and update alternative text and captions if the selected page changes.
