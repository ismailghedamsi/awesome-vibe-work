#!/usr/bin/env python3
"""Generate README.md for awesome-vibe-work from data/vibe-work.json.

README tables are generated, not hand-edited: edit data/vibe-work.json,
then run this script.
"""
import json
import os

ROOT = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(ROOT, "data", "vibe-work.json")
OUT = os.path.join(ROOT, "README.md")

# slug, title, blurb — finalized from the 2026-10-11 research pass.
CATEGORIES = [
    ("office-productivity", "Office & productivity",
     "Full apps for documents, spreadsheets, presentations, notes and everyday work — the kind of software that used to take a team years."),
    ("creative-tools", "Creative tools",
     "Image, vector, video, PDF, motion-graphics and layout apps — the vibe-built answer to the Adobe suite."),
    ("games", "Games",
     "Playable games whose code was written mostly by AI agents, from viral experiments to polished releases."),
    ("developer-tools", "Developer tools",
     "Editors, CLIs, and dev utilities that were themselves built by AI — agents building for agents."),
    ("web-apps", "Web apps & SaaS",
     "Shipped web products and utilities with real users, built the vibe way."),
    ("mobile-apps", "Mobile apps",
     "iOS and Android apps that shipped to stores with AI-written codebases."),
    ("music-audio", "Music & audio",
     "Synths, DAWs, and audio toys composed in code by machines."),
    ("data-viz", "Data & visualization",
     "Dashboards, visualizers, and data tools with vibe-built front ends and engines."),
]


def anchor(title):
    return title.lower().replace(" ", "-").replace("&", "").replace("--", "-")


def main():
    works = json.load(open(DATA))
    by_cat = {slug: [] for slug, _, _ in CATEGORIES}
    for w in works:
        by_cat[w["category"]].append(w)

    total = len(works)
    verified = sum(1 for w in works if w["verified"])
    oss = sum(1 for w in works if w["license"] not in ("Proprietary", "Unknown"))

    lines = []
    lines.append("# Awesome Vibe Work [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)\n")
    lines.append("> A curated collection of **great vibe work** — real, shipped software built primarily by AI agents. Not demos, not mockups: usable apps with real users, where the bulk of the code was written by machines.\n")
    lines.append("Every entry was checked against its official repo, site, or announcement on **2026-10-11**. Inclusion requires an official statement (repo README, author post, launch announcement) that the work was AI/vibe-built; entries that could not be verified carry an honest `verified: false` flag in the machine-readable catalog ([`data/vibe-work.json`](data/vibe-work.json)). Descriptions are our own words, never copied from sources.\n")
    lines.append(f"**{total} projects** across **{len(CATEGORIES)} categories** · {verified} verified · {oss} open-source.\n")
    lines.append("## Contents\n")
    for slug, title, _ in CATEGORIES:
        if by_cat[slug]:
            lines.append(f"- [{title}](#{anchor(title)})")
    lines.append("- [Guides](#guides)")
    lines.append("- [Contributing](#contributing)")
    lines.append("- [License](#license)\n")
    lines.append("---\n")

    for slug, title, blurb in CATEGORIES:
        entries = sorted(by_cat[slug], key=lambda w: w["name"].lower())
        if not entries:
            continue
        lines.append(f"## {title}\n")
        lines.append(blurb + "\n")
        lines.append("| Name | What it does | License | Vibe cred |")
        lines.append("|---|---|---|---|")
        for w in entries:
            desc = w["description"].replace("|", "\\|")
            link = f"[{w['name']}]({w['repo'] or w['homepage']})"
            cred = w["vibe_note"].replace("|", "\\|")
            if not w["verified"]:
                cred += " ⚠ *claim unverified*"
            lines.append(f"| {link} | {desc} | {w['license']} | {cred} |")
        lines.append("")

    lines.append("## Guides\n")
    lines.append("- [What counts as vibe work?](docs/what-is-vibe-work.md) — the inclusion bar, and how we verify it.")
    lines.append("- [Categories](docs/categories.md) — scope notes for each category.")
    lines.append("- [Excluded & retired](docs/excluded-and-retired.md) — projects we checked and rejected, with reasons.\n")
    lines.append("## Contributing\n")
    lines.append("See [CONTRIBUTING.md](CONTRIBUTING.md). Add entries to `data/vibe-work.json`, then regenerate this README with `python3 generate_readme.py`.\n")
    lines.append("## License\n")
    lines.append("This list is MIT licensed — see [LICENSE](LICENSE). Project names, descriptions of functionality, and links belong to their respective owners.\n")

    with open(OUT, "w") as f:
        f.write("\n".join(lines) + "\n")
    print(f"wrote {OUT} ({total} entries)")


if __name__ == "__main__":
    main()
