#!/usr/bin/env python3
"""Curate research JSON into the awesome-vibe-work data schema."""
import json, re

SRC = "/home/hatch/workspace/research/vibe-work-research.json"
OUT = "/home/hatch/workspace/awesome-vibe-work-build/data/vibe-work.json"

CATMAP = {
    "Creative Suite": "creative-tools",
    "Games": "games",
    "Productivity": "office-productivity",
    "Music & Audio": "music-audio",
    "Data & Dashboards": "data-viz",
    "Mobile Apps": "mobile-apps",
    "Developer Tools": "developer-tools",
}
META_SPLIT = {"Awesome-Vibe-Coding": "web-apps", "VibeRL": "developer-tools"}

# Short, human-readable provenance for the "Vibe cred" column.
OVERRIDES = {
    "VibeOffice": "AGENTS.md: built by parallel coding agents",
    "PhotoCraft": "Creator: AI helped recreate 7 top Adobe apps",
    "VectorCraft": "Creator: AI helped recreate 7 top Adobe apps",
    "FilmCraft": "Creator: AI helped recreate 7 top Adobe apps",
    "LightCraft": "Creator: AI helped recreate 7 top Adobe apps",
    "PdfCraft": "Creator: AI helped recreate 7 top Adobe apps",
    "EffectCraft": "Creator: AI helped recreate 7 top Adobe apps",
    "DesignCraft": "Creator: AI helped recreate 7 top Adobe apps",
    "Photon Studio": "Dev: vibe-coded, 20k users on ~$2k of tokens",
    "fly.pieter.com": "Site footer: 100% made with AI",
    "Quasar Saz": "README: vibe-coded by a dog's keystrokes via Claude Code",
    "Awesome-Vibe-Coding": "Author: built entirely through vibe coding",
    "VibeRL": "Author: built with Kimi K2 + Claude Code",
    "World of ClaudeCraft": "Vibe-coded in a weekend",
    "NeoMud": "Site: 100% vibe-coded with AI",
    "rewire": "Docs: 100% vibe coded with Claude Code",
    "MeshAnd": "README: every line written by Claude Code",
    "Immich Editor": "README: code written by Claude Code, directed by one person",
    "Augenblick": "README: 100% vibe coded with Codex, Claude Code, Cursor",
    "Neetings": "README: 99% vibe coded",
    "RacerX": "Repo: 100% vibe-coded DAW for Linux",
}

def shorten(ev):
    ev = ev.strip().rstrip(".")
    if len(ev) <= 72:
        return ev
    cut = ev[:72].rsplit(" ", 1)[0]
    return cut + "…"

def main():
    raw = json.load(open(SRC))
    out = []
    for e in raw:
        name = e["name"]
        if e["category"] == "Meta":
            cat = META_SPLIT[name]
        else:
            cat = CATMAP[e["category"]]
        entry = {
            "name": name,
            "description": e["description"].strip(),
            "category": cat,
            "homepage": e["site_url"],
            "repo": e["repo_url"],
            "license": e["license"] if e["license"] != "unknown" else "Unknown",
            "verified": bool(e["verified"]),
            "verified_on": "2026-10-11",
            "vibe_note": OVERRIDES.get(name, shorten(e["vibe_evidence"])),
        }
        out.append(entry)

    # Verified corrections from independent checks (2026-10-11)
    for entry in out:
        if entry["name"] == "Quasar Saz":
            entry["repo"] = "https://github.com/cleak/quasar-saz"
            entry["license"] = "MIT"

    out.sort(key=lambda x: (x["category"], x["name"].lower()))
    json.dump(out, open(OUT, "w"), indent=2, ensure_ascii=False)
    print(f"wrote {len(out)} entries")
    from collections import Counter
    print(Counter(x["category"] for x in out))
    print("unverified:", [x["name"] for x in out if not x["verified"]])

if __name__ == "__main__":
    main()
