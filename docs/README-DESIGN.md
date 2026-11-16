# README design notes

## Direction

ASCII hands with pixel, point-cloud, and wireframe details. A supporting moon
workshop combines the coding astronaut, drifter, grower, dreamer, CRT desk,
helpful robot, exploded device, and mountain field station into one scene.
The name uses plain sans-serif type; the body uses short, conversational English.
Project facts and the substantial four-project showcase are retained.

The hands load fully formed, nearly touching with a small visible gap. The
animation only breathes gently in luminance; it never closes the gap. The
static WebP is selected for reduced motion where the renderer supports it.
Light and dark mastheads follow the reader's preferred colour scheme.
GitHub controls page typography and layout; this is a README, not a webpage.

## Sources checked on 2026-11-13

- Public profile: https://github.com/Natnael-Dev
- Live portfolio: https://natnaeltezazu.pro.et
- Public descriptions and READMEs for NatyMD-web, AgentHelm, SignalIntel,
  crafthub-marketplace, ghostreply, and teragrant-agent.
- DailyRead's public description identifies it as an offline-first Android
  reading-habit app for PDF and EPUB; no README was available at lookup time.
- Contact details come from the portfolio, not the obsolete profile README.
- TeraGrant, AgentHelm, and SignalIntel images are portfolio previews copied
  from the portfolio source and compressed. They are not new screenshots.
- CraftHub uses an editable architecture diagram based on its public README;
  the portfolio image did not clearly identify the project, so it was omitted.

Source links support descriptions, not independent performance guarantees.
No benchmark, contribution count, or completion claim is reproduced here.

## Assets

The ASCII-style artwork is an original interpretation of the classical
reaching-hands composition. `assets/creation-of-adam.webp` is the saved source.
The mastheads are editable SVG, with no scripts, embedded fonts, or network
dependencies. The README keeps descriptions and links as accessible text.

To rebuild the animation, install FFmpeg and run:

```powershell
powershell -NoProfile -File scripts/build-hero.ps1
python scripts/verify-readme.py
```

## Safe review and rollback

This redesign lives on `feat/renaissance-readme`. The original README is
preserved at commit `60244bcc1cd06cb3f29d80f4e59b46e1c5db0ae8` on `main`.
Pushing this feature branch does not change the public profile README.
Review the branch README on GitHub before merging anything.

If the redesign is later merged and you want the old README back, create a
new feature branch and restore only the README from the original commit:

```powershell
git switch -c feat/restore-original-readme
git restore --source=60244bcc1cd06cb3f29d80f4e59b46e1c5db0ae8 -- README.md
git add README.md
git commit -m "docs(profile): restore original README"
```

This preserves history and leaves other work alone. Do not force-push or
rewrite history to undo the redesign.

## Latest selection

The maker mark is now a small native ASCII robot floating among stars.
GhostReply replaces CraftHub in the showcase. Its public README identifies
it as pre-alpha, with WhatsApp working and Telegram in progress; this status
is reflected in the card. Intro wording is awaiting the owner’s selection.

## Project layout and motion

The approved Quiet intro is now used verbatim. Projects have full-width
workflow covers, concise text, and expandable portfolio previews, replacing
the cramped two-column project table. Covers are illustrative flows, not
live telemetry. Each has a static reduced-motion companion. The small robot
floats gently and stops under reduced motion. The skills table uses short
category labels. Rebuild covers with `python scripts/build-project-covers.py`.
