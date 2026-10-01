# e/acc

Carbon black. Reactor orange. Build the future.

A dark, palette-driven theme for Omarchy Quattro, with warm white text, graphite surfaces and four wallpapers: Signal, Reactor, Velocity and Icon Carbon.

![Signal wallpaper — artwork, not a desktop screenshot](backgrounds/00-signal.png)

## Wallpapers

- **Reactor:** an orange fusion core in a dark industrial chamber.
- **Velocity:** light trails accelerating towards the horizon.
- **Signal:** restrained e/acc typography on carbon black.
- **Icon Carbon:** Will DePue’s original e/acc symbol in orange on carbon black, rendered directly from vector at 3840×2160.

The orange icon variant and Kardashev experiments are retained in `extras/`, outside the default wallpaper collection.

Icon Carbon is a native 3840×2160 vector render. Signal, Reactor and Velocity are 1672×941, without upscaling; see docs/validation.md for exact dimensions. Signal is the lead wallpaper and sorts first. Use Omarchy's background picker to select it if your desktop retains another background.

## Try the preview

Extract the download, then run these commands from inside the extracted `omarchy-eacc-theme` directory on your Omarchy desktop:

```bash
mkdir -p "$HOME/.config/omarchy/themes"
if [ -e "$HOME/.config/omarchy/themes/eacc" ]; then
  echo "An eacc theme already exists. Back it up or rename it before installing."
else
  cp -R . "$HOME/.config/omarchy/themes/eacc"
  omarchy theme set eacc
fi
```

This applies the theme immediately. No build tools, extra fonts or packages are required. To revert, select your previous theme in the Omarchy theme picker.

After the implementation PR is merged, install with:

```bash
omarchy theme install https://github.com/tcballard/omarchy-theme-e-acc
```

Until then, use the local preview instructions above.

## Design

`colors.toml` defines the semantic palette and normal/bright terminal colours. Omarchy's own templates generate application configurations, including shell surfaces, terminals and editors. Native spacing, fonts and behaviour are retained. No shell overrides or install hooks are supplied.

Orange identifies focus and active controls. Mint, amber and coral retain distinct success, warning and error roles. Selection uses burnt orange with bright text. The palette supplies explicit background and foreground ramps.

## Status

Version **0.0.1-preview**. Palette syntax, contrast and image checks are recorded in [validation](docs/validation.md). Live Omarchy testing, Git-installed staging and a real desktop screenshot remain pending. Wallpaper artwork is not a fabricated desktop preview.

## Licence and artwork

Theme configuration and documentation: MIT. Wallpaper generation provenance and media terms: [CREDITS.md](CREDITS.md).
