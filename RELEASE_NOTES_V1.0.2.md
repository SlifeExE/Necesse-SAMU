# Necesse SAMU – Release Notes 1.0.2

Improvements
- Per‑mod version reporting with colors:
  - Updated: "Updated <Mod> <old> -> <new>" (yellow)
  - Up‑to‑date: "<Mod> <version> already up to date" (light green)
  - New install: "Installing <Mod> <version>" (cyan)
- Copy only when necessary:
  - Selects the newest JAR per mod (by filename prefix and mtime) before copying.
  - Skips copying if the same version is already present.
- Post‑copy safety cleanup keeps a single version per mod prefix.
- Pause on exit (configurable via `pause_on_exit`, default true) so the window doesn’t close immediately.
- Better diagnostics when no JARs are found (prints searched paths).

Other changes
- Project rename: SMU -> SAMU (Server and Mod Updater); updated executable name and docs.
- Icon handling in build scripts: prefers `icon.png`, regenerates `icon.ico`, and cleans old PyInstaller state.
- README clarified Quick Start, server update prompt, and custom icon instructions.

