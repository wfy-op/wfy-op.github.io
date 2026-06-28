"""Refresh the public research portal snapshot from local research artifacts.

The script is intentionally conservative: it publishes aggregate metrics,
selected figures, and sanitized status notes only. Raw chat logs, local paths,
PDF files, and private run artifacts are not copied into the website.
"""

from __future__ import annotations

import csv
import html
import json
import os
import re
import shutil
from collections import Counter
from datetime import datetime
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
PORTAL_IMAGE_DIR = ROOT / "images" / "research" / "portal"
DATA_FILE = ROOT / "_data" / "research_portal.yml"


def env_path(name: str) -> Path | None:
    value = os.environ.get(name)
    if not value:
        return None
    path = Path(value)
    return path if path.exists() else None


def maybe_float(value: str | None) -> float | None:
    if value is None or str(value).strip() == "":
        return None
    return float(value)


def copy_asset(src: Path, dest_name: str) -> str | None:
    if not src.exists():
        return None
    PORTAL_IMAGE_DIR.mkdir(parents=True, exist_ok=True)
    dest = PORTAL_IMAGE_DIR / dest_name
    shutil.copy2(src, dest)
    return f"/images/research/portal/{dest_name}"


def write_bar_svg(path: Path, title: str, rows: list[tuple[str, int]], x_label: str) -> str:
    PORTAL_IMAGE_DIR.mkdir(parents=True, exist_ok=True)
    width, height = 820, 420
    margin_l, margin_r, margin_t, margin_b = 76, 28, 62, 78
    plot_w = width - margin_l - margin_r
    plot_h = height - margin_t - margin_b
    max_value = max((value for _, value in rows), default=1)
    bar_gap = 8
    bar_w = (plot_w - bar_gap * (len(rows) - 1)) / max(len(rows), 1)

    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" role="img" aria-label="{html.escape(title)}">',
        '<rect width="100%" height="100%" fill="#ffffff"/>',
        f'<text x="{margin_l}" y="34" font-family="Arial, sans-serif" font-size="22" font-weight="700" fill="#263238">{html.escape(title)}</text>',
        f'<line x1="{margin_l}" y1="{height - margin_b}" x2="{width - margin_r}" y2="{height - margin_b}" stroke="#d8dee4" stroke-width="1"/>',
        f'<line x1="{margin_l}" y1="{margin_t}" x2="{margin_l}" y2="{height - margin_b}" stroke="#d8dee4" stroke-width="1"/>',
    ]

    for i in range(5):
        value = round(max_value * i / 4)
        y = height - margin_b - plot_h * i / 4
        parts.append(f'<line x1="{margin_l}" y1="{y:.1f}" x2="{width - margin_r}" y2="{y:.1f}" stroke="#eef1f3" stroke-width="1"/>')
        parts.append(f'<text x="{margin_l - 10}" y="{y + 4:.1f}" text-anchor="end" font-family="Arial, sans-serif" font-size="12" fill="#65737e">{value}</text>')

    for index, (label, value) in enumerate(rows):
        x = margin_l + index * (bar_w + bar_gap)
        bar_h = 0 if max_value == 0 else plot_h * value / max_value
        y = height - margin_b - bar_h
        fill = "#286a6b" if index % 2 == 0 else "#8a5a16"
        parts.append(f'<rect x="{x:.1f}" y="{y:.1f}" width="{bar_w:.1f}" height="{bar_h:.1f}" rx="3" fill="{fill}"/>')
        parts.append(f'<text x="{x + bar_w / 2:.1f}" y="{y - 7:.1f}" text-anchor="middle" font-family="Arial, sans-serif" font-size="12" fill="#263238">{value}</text>')
        parts.append(
            f'<text x="{x + bar_w / 2:.1f}" y="{height - margin_b + 20}" text-anchor="middle" '
            f'font-family="Arial, sans-serif" font-size="11" fill="#4c5963" transform="rotate(35 {x + bar_w / 2:.1f} {height - margin_b + 20})">{html.escape(label)}</text>'
        )

    parts.append(f'<text x="{width / 2}" y="{height - 12}" text-anchor="middle" font-family="Arial, sans-serif" font-size="12" fill="#65737e">{html.escape(x_label)}</text>')
    parts.append("</svg>")
    path.write_text("\n".join(parts), encoding="utf-8")
    return f"/images/research/portal/{path.name}"


def load_paper_library(pcsel_dir: Path | None) -> dict[str, Any]:
    fallback = {
        "records": 0,
        "doi_count": 0,
        "recent_2020_plus": 0,
        "year_range": "not available",
        "top_years": [],
        "top_groups": [],
        "exported_at": "not available",
        "redistribution_allowed": False,
    }
    if not pcsel_dir:
        return fallback
    index_path = pcsel_dir / "knowledge" / "parsed" / "external_paper_index.jsonl"
    if not index_path.exists():
        return fallback

    records = []
    for line in index_path.read_text(encoding="utf-8", errors="replace").splitlines():
        if line.strip():
            records.append(json.loads(line))

    years = [int(item["year"]) for item in records if str(item.get("year", "")).isdigit()]
    top_years = Counter(years).most_common(8)
    top_groups = Counter(item.get("source_group") or "Unspecified" for item in records).most_common(8)
    exported = Counter(item.get("exported_at") or "not available" for item in records).most_common(1)

    year_chart = write_bar_svg(
        PORTAL_IMAGE_DIR / "pcsel_library_year_distribution.svg",
        "PCSEL library year distribution",
        [(str(year), count) for year, count in top_years],
        "Top publication years by local index count",
    )

    return {
        "records": len(records),
        "doi_count": sum(1 for item in records if item.get("doi")),
        "recent_2020_plus": sum(1 for year in years if year >= 2020),
        "year_range": f"{min(years)}-{max(years)}" if years else "not available",
        "top_years": [{"label": str(year), "count": count} for year, count in top_years],
        "top_groups": [{"label": label, "count": count} for label, count in top_groups],
        "exported_at": exported[0][0] if exported else "not available",
        "redistribution_allowed": any(bool(item.get("redistribution_allowed")) for item in records),
        "year_chart": year_chart,
    }


def load_hx1(pcsel_dir: Path | None) -> dict[str, Any]:
    fallback = {
        "fdtd_rows": 0,
        "comsol_rows": 0,
        "depths_nm": [],
        "mesh_labels": [],
        "fdtd_q_minmax": "not available",
        "fdtd_detuning_minmax_nm": "not available",
        "comsol_q_minmax": "not available",
        "created_at": "not available",
        "figures": [],
    }
    if not pcsel_dir:
        return fallback

    base = pcsel_dir / "assets" / "20260626_hx1_940_hole_depth_q_wavelength_fdtd"
    artifacts = base / "artifacts"
    figures = base / "figures"
    mesh_csv = artifacts / "hx1_940_fdtd_mesh3_mesh5_hole_depth_results.csv"
    comsol_csv = artifacts / "hx1_940_comsol_depth_rows_for_report.csv"
    summary_json = artifacts / "hx1_940_fdtd_vs_comsol_hole_depth_summary.json"
    if not mesh_csv.exists() or not comsol_csv.exists():
        return fallback

    with mesh_csv.open(encoding="utf-8", errors="replace", newline="") as handle:
        fdtd_rows = list(csv.DictReader(handle))
    with comsol_csv.open(encoding="utf-8", errors="replace", newline="") as handle:
        comsol_rows = list(csv.DictReader(handle))

    depths = sorted({maybe_float(row.get("h_nm")) for row in fdtd_rows if maybe_float(row.get("h_nm")) is not None})
    mesh_labels = sorted({(row.get("comparison_label") or row.get("run_label") or "").strip() for row in fdtd_rows})
    fdtd_q = [maybe_float(row.get("fdtd_closest_q")) for row in fdtd_rows]
    fdtd_q = [value for value in fdtd_q if value is not None]
    detuning = [maybe_float(row.get("fdtd_closest_detuning_nm")) for row in fdtd_rows]
    detuning = [value for value in detuning if value is not None]
    comsol_q = [maybe_float(row.get("best_pm1_q")) for row in comsol_rows]
    comsol_q = [value for value in comsol_q if value is not None]

    created_at = "not available"
    if summary_json.exists():
        try:
            created_at = json.loads(summary_json.read_text(encoding="utf-8", errors="replace")).get("created_at", "not available")
        except json.JSONDecodeError:
            created_at = "not available"

    copied = [
        {
            "src": copy_asset(figures / "hx1_940_hole_depth_structure_schematic.svg", "hx1_940_hole_depth_structure_schematic.svg"),
            "alt": "HX1-940 hole-depth structure schematic",
            "caption": "Structure schematic used for the HX1-940 hole-depth sweep; quantum-well clearance remains part of the risk gate.",
        },
        {
            "src": copy_asset(figures / "hx1_940_fdtd_vs_comsol_q_by_depth.png", "hx1_940_fdtd_vs_comsol_q_by_depth.png"),
            "alt": "HX1-940 Q-factor comparison by hole depth",
            "caption": "FDTD closest-mode Q and COMSOL target-window Q compared across the 100-600 nm hole-depth sweep.",
        },
        {
            "src": copy_asset(figures / "hx1_940_fdtd_vs_comsol_wavelength_by_depth.png", "hx1_940_fdtd_vs_comsol_wavelength_by_depth.png"),
            "alt": "HX1-940 wavelength comparison by hole depth",
            "caption": "FDTD and COMSOL wavelength trends expose solver-model differences rather than a final accepted device prediction.",
        },
    ]

    return {
        "fdtd_rows": len(fdtd_rows),
        "comsol_rows": len(comsol_rows),
        "depths_nm": [int(value) for value in depths],
        "mesh_labels": [label for label in mesh_labels if label],
        "fdtd_q_minmax": f"{min(fdtd_q):.1f}-{max(fdtd_q):.1f}" if fdtd_q else "not available",
        "fdtd_detuning_minmax_nm": f"{min(detuning):.2f}-{max(detuning):.2f}" if detuning else "not available",
        "comsol_q_minmax": f"{min(comsol_q):.1f}-{max(comsol_q):.1f}" if comsol_q else "not available",
        "created_at": created_at,
        "figures": [item for item in copied if item["src"]],
    }


def load_cwt(cwt_dir: Path | None) -> dict[str, Any]:
    fallback = {
        "provenance_count": 0,
        "report_figures": 0,
        "scripts_count": 0,
        "report_exists": False,
        "figures": [],
        "focus": [],
    }
    if not cwt_dir:
        return fallback

    provenance = list(cwt_dir.glob("results/*/provenance.json"))
    assets = cwt_dir / "reports" / "assets"
    scripts = cwt_dir / "scripts"

    copied = [
        {
            "src": copy_asset(assets / "fig3_7_c2d_r2_order_pair_audit.png", "cwt_fig3_7_c2d_r2_order_pair_audit.png"),
            "alt": "CWT Fig. 3.7 R2 order-pair audit",
            "caption": "Computed CWT audit figure for the Fig. 3.7 C2D R2 order-pair reproduction check.",
        },
        {
            "src": copy_asset(assets / "fig4_5_table42_method_ranking_audit.png", "cwt_fig4_5_table42_method_ranking_audit.png"),
            "alt": "CWT Fig. 4.5 Table 4.2 method-ranking audit",
            "caption": "Computed CWT audit figure linking method-ranking checks to the reproduction report.",
        },
    ]

    return {
        "provenance_count": len(provenance),
        "report_figures": len(list(assets.glob("*.png"))) if assets.exists() else 0,
        "scripts_count": len(list(scripts.glob("reproduce_*.py"))) if scripts.exists() else 0,
        "report_exists": (cwt_dir / "reports" / "cwt_reproduction_report.html").exists(),
        "figures": [item for item in copied if item["src"]],
        "focus": [
            "Fig. 3.5 truncation-order convergence",
            "Fig. 3.6 radiation constant versus filling factor",
            "Fig. 3.7 frequency versus filling factor",
            "Fig. 4.5 / Table 4.2 method-ranking checks",
        ],
    }


def load_rlcomsol(rlcomsol_dir: Path | None) -> dict[str, Any]:
    fallback = {
        "reports_count": 0,
        "scripts_count": 0,
        "tests_count": 0,
        "completed_runs": "not available",
        "verdict": "not available",
        "best_seed": "not available",
        "best_step": "not available",
        "best_score": "not available",
        "best_q": "not available",
        "latest_report": "not available",
        "figures": [],
        "public_boundary": "Private COMSOL/RL project; the website exposes aggregate status and selected sanitized figures only.",
    }
    if not rlcomsol_dir:
        return fallback

    reports_dir = rlcomsol_dir / "reports"
    scripts_dir = rlcomsol_dir / "scripts"
    tests_dir = rlcomsol_dir / "tests"
    latest_report = reports_dir / "20260625_comsol_goal_three_seed_radius_guard_perm_a_20pt_panel.md"
    panel_dir = rlcomsol_dir / "runs" / "comsol_goal_three_seed_radius_guard_perm_a_20pt_panel_20260625"

    parsed = {}
    if latest_report.exists():
        text = latest_report.read_text(encoding="utf-8", errors="replace")
        patterns = {
            "completed_runs": r"Completed runs: `([^`]+)`",
            "verdict": r"Verdict: `([^`]+)`",
            "best": r"Best cross-seed accepted point: `([^`]+)` step `([^`]+)` with score `([^`]+)` and Q `([^`]+)`",
        }
        for key, pattern in patterns.items():
            match = re.search(pattern, text)
            if match:
                parsed[key] = match.groups() if len(match.groups()) > 1 else match.group(1)

    best = parsed.get("best", ("not available", "not available", "not available", "not available"))
    copied = [
        {
            "src": copy_asset(
                panel_dir / "three_seed_radius_guard_perm_a_20pt_curves.png",
                "rlcomsol_three_seed_radius_guard_perm_a_20pt_curves.png",
            ),
            "alt": "RLcomsol three-seed COMSOL optimization curves",
            "caption": "Three-seed 20-step COMSOL smoke panel: best-so-far and accepted-score curves under a fixed radius-guard protocol.",
        },
        {
            "src": copy_asset(
                panel_dir / "three_seed_radius_guard_perm_a_20pt_actions.png",
                "rlcomsol_three_seed_radius_guard_perm_a_20pt_actions.png",
            ),
            "alt": "RLcomsol action trajectory panel",
            "caption": "Action trajectory panel showing warmup, restart, and incumbent-refinement actions separately from final design claims.",
        },
    ]

    return {
        "reports_count": len(list(reports_dir.glob("*.md"))) if reports_dir.exists() else 0,
        "scripts_count": len(list(scripts_dir.glob("*.py"))) if scripts_dir.exists() else 0,
        "tests_count": len(list(tests_dir.glob("test_*.py"))) if tests_dir.exists() else 0,
        "completed_runs": parsed.get("completed_runs", "not available"),
        "verdict": parsed.get("verdict", "not available"),
        "best_seed": best[0],
        "best_step": best[1],
        "best_score": best[2],
        "best_q": best[3],
        "latest_report": latest_report.name if latest_report.exists() else "not available",
        "figures": [item for item in copied if item["src"]],
        "public_boundary": fallback["public_boundary"],
    }


def find_dailybrief_dir() -> Path | None:
    env = env_path("DAILYBRIEF_DIR")
    if env:
        return env
    desktop = Path.home() / "Desktop"
    if not desktop.exists():
        return None
    candidates = []
    for child in desktop.iterdir():
        if child.is_dir() and list(child.glob("2026-*.html")):
            candidates.append(child)
    if not candidates:
        return None
    return max(candidates, key=lambda item: len(list(item.glob("2026-*.html"))))


def load_dailybrief() -> dict[str, Any]:
    daily_dir = find_dailybrief_dir()
    fallback = {
        "html_count": 0,
        "date_range": "not available",
        "latest": "not available",
        "latest_title": "not available",
        "href_count": 0,
        "keyword_counts": {},
        "latest_topics": [],
    }
    if not daily_dir:
        return fallback
    htmls = sorted(daily_dir.glob("2026-*.html"))
    if not htmls:
        return fallback

    latest = htmls[-1]
    text = latest.read_text(encoding="utf-8", errors="replace")
    title = re.search(r"<title[^>]*>(.*?)</title>", text, re.I | re.S)
    heads = re.findall(r"<h[123][^>]*>(.*?)</h[123]>", text, re.I | re.S)
    body_text = re.sub(r"<script.*?</script>|<style.*?</style>", "", text, flags=re.I | re.S)
    body_text = html.unescape(re.sub("<.*?>", " ", body_text))
    keywords = {
        label: body_text.lower().count(label.lower())
        for label in ["PCSEL", "photon", "laser", "arxiv", "paper", "academic"]
    }
    radar_chart = write_bar_svg(
        PORTAL_IMAGE_DIR / "dailybrief_academic_radar.svg",
        "DailyBrief academic radar keyword counts",
        [(label, count) for label, count in keywords.items()],
        f"Latest local brief: {latest.stem}",
    )

    cleaned_heads = [
        html.unescape(re.sub("<.*?>", "", item)).strip()
        for item in heads
        if html.unescape(re.sub("<.*?>", "", item)).strip()
    ]

    academic_keywords = ("pcsel", "photon", "laser", "arxiv", "paper", "semiconductor", "quantum")
    academic_topics = []
    for item in cleaned_heads[1:]:
        if not any(keyword in item.lower() for keyword in academic_keywords):
            continue
        if item in academic_topics:
            continue
        academic_topics.append(item)
        if len(academic_topics) == 6:
            break

    return {
        "html_count": len(htmls),
        "date_range": f"{htmls[0].stem}-{htmls[-1].stem}",
        "latest": latest.name,
        "latest_title": html.unescape(re.sub("<.*?>", "", title.group(1))).strip() if title else latest.stem,
        "href_count": len(re.findall(r"href=", text, re.I)),
        "keyword_counts": keywords,
        "latest_topics": academic_topics,
        "radar_chart": radar_chart,
    }


def yaml_scalar(value: Any) -> str:
    if value is None:
        return "null"
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, (int, float)):
        return str(value)
    return json.dumps(str(value), ensure_ascii=True)


def yaml_dump(value: Any, indent: int = 0) -> list[str]:
    pad = " " * indent
    lines: list[str] = []
    if isinstance(value, dict):
        for key, item in value.items():
            if isinstance(item, (dict, list)):
                lines.append(f"{pad}{key}:")
                lines.extend(yaml_dump(item, indent + 2))
            else:
                lines.append(f"{pad}{key}: {yaml_scalar(item)}")
    elif isinstance(value, list):
        if not value:
            lines.append(f"{pad}[]")
        for item in value:
            if isinstance(item, (dict, list)):
                lines.append(f"{pad}-")
                lines.extend(yaml_dump(item, indent + 2))
            else:
                lines.append(f"{pad}- {yaml_scalar(item)}")
    else:
        lines.append(f"{pad}{yaml_scalar(value)}")
    return lines


def build_data() -> dict[str, Any]:
    pcsel_dir = env_path("PCSEL_AGENT_DIR")
    cwt_dir = env_path("CWT_REBUILD_DIR")
    rlcomsol_dir = env_path("RLCOMSOL_DIR")

    paper = load_paper_library(pcsel_dir)
    hx1 = load_hx1(pcsel_dir)
    cwt = load_cwt(cwt_dir)
    rlcomsol = load_rlcomsol(rlcomsol_dir)
    daily = load_dailybrief()

    return {
        "snapshot": {
            "updated": datetime.now().strftime("%Y-%m-%d"),
            "scope": "Public-safe aggregate snapshot from local research artifacts.",
            "boundary": "No raw Codex chats, local absolute paths, private PDFs, or unreleased simulation files are published.",
            "refresh_script": "scripts/update_research_portal.py",
        },
        "kpis": [
            {"label": "PCSEL library records", "value": paper["records"], "note": f"{paper['doi_count']} DOI-linked entries; {paper['recent_2020_plus']} records since 2020."},
            {"label": "HX1-940 sweep rows", "value": hx1["fdtd_rows"], "note": f"FDTD mesh comparison across {len(hx1['depths_nm'])} hole depths."},
            {"label": "COMSOL reference rows", "value": hx1["comsol_rows"], "note": "Target-window COMSOL rows paired with the FDTD credibility report."},
            {"label": "CWT provenance files", "value": cwt["provenance_count"], "note": f"{cwt['scripts_count']} reproduction scripts and {cwt['report_figures']} report figures."},
            {"label": "RLcomsol reports", "value": rlcomsol["reports_count"], "note": f"Latest seed panel verdict: {rlcomsol['verdict']}."},
            {"label": "DailyBrief HTML reports", "value": daily["html_count"], "note": f"Latest local academic radar: {daily['latest']}."},
        ],
        "paper_library": paper,
        "hx1": hx1,
        "cwt": cwt,
        "rlcomsol": rlcomsol,
        "dailybrief": daily,
    }


def main() -> None:
    data = build_data()
    DATA_FILE.write_text("\n".join(yaml_dump(data)) + "\n", encoding="utf-8")
    print(f"Wrote {DATA_FILE}")


if __name__ == "__main__":
    main()
