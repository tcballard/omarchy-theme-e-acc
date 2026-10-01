# Validation — 1 October 2026

Target: Omarchy Quattro semantic palette contract. Installed version and hardware: not exercised.

## Local checks

```text
foreground/background: 16.45:1 (target 4.5:1)
foreground/selection: 9.23:1 (target 4.5:1)
accent/background: 6.66:1 (target 3:1)
muted/background: 4.90:1 (target 4.5:1)
01-reactor.png: 1672x941, 2,179,186 bytes; decoded OK
02-velocity.png: 1672x941, 1,315,366 bytes; decoded OK
03-signal.png: 1672x941, 846,095 bytes; decoded OK
PASS: local palette, contrast, package and image checks
NOT RUN: Rust helper (cargo unavailable), live Omarchy, Git staging, registry validation
```

The bundled Rust scaffold/check was attempted but cargo is not installed. The package was authored manually from its documented semantic schema. Python TOML parsing, contrast calculations and full Pillow image decoding passed.

Upstream test source was consulted for semantic aliases and generated configuration behaviour:
https://github.com/omacom/omarchy/blob/quattro/test/cli
Direct retrieval of Tokyo Night and the shell template was unavailable. No application-specific overrides are shipped.

## Required live verification

- Apply on the user's Quattro version and record `omarchy-version` and source revision.
- Inspect bar, launcher, menus, notifications and lock screen.
- Check focus, disabled controls, selection and all ANSI colours in terminal/editor.
- Check a GTK application and any user template overrides.
- Cycle all three wallpapers and restore the previous theme.
- Once published, repeat through `omarchy theme install` to exercise Git staging.
- Capture a real 16:9 desktop screenshot for preview.png before registry submission.

No registry name reservation, public release, marketplace listing or live compatibility claim is made.

## Native 4K request

A reference-guided regeneration explicitly requested 3840×2160. The returned PNG decoded to 1672×941 again. It was not substituted into the theme. Native 4K remains pending; no resized file is labelled native 4K.

## Expanded collection checks

```text
foreground/background: 16.45:1 (target 4.5:1)
foreground/selection: 9.23:1 (target 4.5:1)
accent/background: 6.66:1 (target 3:1)
muted/background: 4.90:1 (target 4.5:1)
01-reactor.png: 1672x941, 2,179,186 bytes; decoded OK
02-velocity.png: 1672x941, 1,315,366 bytes; decoded OK
03-signal.png: 1672x941, 846,095 bytes; decoded OK
04-icon-carbon.png: 3840x2160, 43,023 bytes; decoded OK
05-icon-orange.png: 3840x2160, 43,096 bytes; decoded OK
06-planetary.png: 1672x941, 2,276,771 bytes; decoded OK
07-stellar.png: 1672x941, 1,984,608 bytes; decoded OK
08-galactic.png: 1672x941, 2,295,374 bytes; decoded OK
PASS: local palette, contrast, package and image checks
NOT RUN: Rust helper (cargo unavailable), live Omarchy, Git staging, registry validation
```

## Selected default collection

Signal leads; Reactor, Velocity and Icon Carbon are included. Other artwork is in extras/.

```text
foreground/background: 16.45:1 (target 4.5:1)
foreground/selection: 9.23:1 (target 4.5:1)
accent/background: 6.66:1 (target 3:1)
muted/background: 4.90:1 (target 4.5:1)
00-signal.png: 1672x941, 846,095 bytes; decoded OK
01-reactor.png: 1672x941, 2,179,186 bytes; decoded OK
02-velocity.png: 1672x941, 1,315,366 bytes; decoded OK
04-icon-carbon.png: 3840x2160, 43,023 bytes; decoded OK
PASS: local palette, contrast, package and image checks
NOT RUN: Rust helper (cargo unavailable), live Omarchy, Git staging, registry validation
```

## Final four-wallpaper selection

Reactor removed; Signal + Icon added.

```text
foreground/background: 16.45:1 (target 4.5:1)
foreground/selection: 9.23:1 (target 4.5:1)
accent/background: 6.66:1 (target 3:1)
muted/background: 4.90:1 (target 4.5:1)
00-signal.png: 1672x941, 846,095 bytes; decoded OK
02-velocity.png: 1672x941, 1,315,366 bytes; decoded OK
04-icon-carbon.png: 3840x2160, 43,023 bytes; decoded OK
05-signal-icon.png: 3840x2160, 62,807 bytes; decoded OK
PASS: local palette, contrast, package and image checks
NOT RUN: Rust helper (cargo unavailable), live Omarchy, Git staging, registry validation
```

## Hyperdrive update

Clean combined artwork moved to extras; Hyperdrive added to backgrounds.

```text
foreground/background: 16.45:1 (target 4.5:1)
foreground/selection: 9.23:1 (target 4.5:1)
accent/background: 6.66:1 (target 3:1)
muted/background: 4.90:1 (target 4.5:1)
00-signal.png: 1672x941, 846,095 bytes; decoded OK
02-velocity.png: 1672x941, 1,315,366 bytes; decoded OK
04-icon-carbon.png: 3840x2160, 43,023 bytes; decoded OK
05-hyperdrive.png: 1672x941, 2,618,624 bytes; decoded OK
PASS: local palette, contrast, package and image checks
NOT RUN: Rust helper (cargo unavailable), live Omarchy, Git staging, registry validation
```
