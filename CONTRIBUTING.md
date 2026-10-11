# Contributing

Thanks for helping keep this the most current directory of great macOS apps!

## Adding an entry

1. **Check it fits:** the entry must be a real, installable macOS app or tool (not a web-only service, not a Windows-only port, not an iOS-only app). This list covers all license types — open-source, free, freemium, paid, and subscription apps all belong here. Discontinued apps, malware-flagged tools, and pure web services don't count. A PR must point at a primary source: the vendor's official site or the project's official repo.
2. **Add to the right section** of `README.md` — categories are defined in `docs/categories.md`.
3. **One entry = one row.** Tables have columns: Name | What it does | License / pricing | Open source? | Native?. "Native" means built on macOS frameworks (AppKit/SwiftUI/Catalyst); Electron and web-wrapper apps are not native.
   Tag verification honestly: every entry in this list is checked against its official source; if you couldn't verify a fact, say so rather than softening it.
4. **Add the matching record** to `data/apps.json` with these exact fields:

| field | type | values |
|---|---|---|
| `name` | string | app / tool name |
| `description` | string | one sentence |
| `category` | string | `productivity` / `developer-tools` / `utilities-menu-bar` / `window-management` / `media-design` / `security-privacy` / `ai-powered` / `file-management` / `terminal-shell` / `system-performance` / `note-taking-writing` |
| `homepage` | string | official https:// URL |
| `repo` | string | public repo URL (open-source apps only; omit otherwise) |
| `license` | string | exact OSS license id (e.g. `MIT`), or `Commercial` |
| `pricing` | string | `Open source` / `Free` / `Freemium` / `Paid (one-time)` / `Subscription` |
| `native` | bool | `true` if built on native macOS frameworks |
| `verified` | bool | `true` only if you confirmed the entry on an official source |
| `verified_on` | string | ISO date, e.g. `2026-10-06` |

5. **Keep the README generated:** run `python3 generate_readme.py` after editing `data/apps.json` — the README tables are produced from the data file, not edited by hand.

## Verification standard

- Homepage links must resolve to the vendor's real site or the Mac App Store page.
- Pricing and license claims come from the official pricing page, App Store listing, or repo license file — never inferred.
- Entries that can't be verified on an official source carry `verified: false`.
- Notable exclusions (checked but rejected) go in `docs/excluded-and-retired.md` with a reason.
