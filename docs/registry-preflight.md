# Upstream registry preflight

Validator commit: d8fb987ba0b6c78347d87207543b47186a6788e0. Run against the local PR candidate; remote default-branch metadata is not part of this local run.

### https://github.com/tcballard/omarchy-theme-e-acc: ❌ needs changes

**Errors (must fix):**
- `PREVIEW_MISSING` — No preview.png at the repository root. Omarchy shows this file in its theme switcher, so add a 16:9 screenshot of the theme on a real desktop as preview.png.

**Warnings:**
- `REPO_NAME_CONVENTION` — Recommended repo name is omarchy-theme-e-acc-theme (it installs as "theme-e-acc" either way).
- `NON_THEME_PAYLOAD` `scripts/check.py` — Script, launcher or binary. It stays in your repository; a marketplace install does not check it out.

**Detected:**
- slug `theme-e-acc` · dark · hue orange · native palette (colors.toml)
- 4 background(s), 4.6 MB · preview `none` · 22 files
- a marketplace install puts 7 of them on your machine: `LICENSE`, `README.md`, `backgrounds/00-signal.png`, `backgrounds/02-velocity.png`, `backgrounds/04-icon-carbon.png`, `backgrounds/05-hyperdrive.png`, `colors.toml`