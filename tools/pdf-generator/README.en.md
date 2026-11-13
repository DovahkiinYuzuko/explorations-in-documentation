# PAPER.md PDF Generation Pipeline

**English** | [日本語](./README.md)

A repository-specific build pipeline that takes [`PAPER.md`](../../PAPER.md) as the Single Source of Truth and compiles it into an A4 academic preprint-style PDF (default output: `tools/pdf-generator/output/PAPER.pdf`) using Pandoc, Typst, and Playwright.

Rather than functioning as a general-purpose Markdown-to-PDF converter, this tool is tailored for automated builds in GitHub Releases ([`.github/workflows/release-paper.yml`](../../.github/workflows/release-paper.yml)) and local verification in the author's environment (Windows + WSL + Google Chrome).

### Contents
- [Files](#files)
- [Prerequisites and Dependencies](#prerequisites-and-dependencies)
- [Usage](#usage)
- [Conversion Pipeline and Layout](#conversion-pipeline-and-layout)
- [Design Scope and Limitations](#design-scope-and-limitations)

### Files

| File | Role |
| :--- | :--- |
| [`build_pdf.py`](./build_pdf.py) | Build script that executes Markdown preprocessing, Mermaid-to-PNG rendering, Pandoc conversion to Typst, and Typst PDF compilation. |
| [`template.typ`](./template.typ) | Typst layout template defining A4 page geometry, mixed Latin/Japanese typography, Booktabs-style tables, and quote block break controls. |
| [`requirements.txt`](./requirements.txt) | Python package specification (`playwright`) required by `build_pdf.py` for rendering Mermaid diagrams. |

During execution, the script creates a working directory at `tools/pdf-generator/.build/` to store intermediate artifacts (`body.md`, `abstract.md`, `body.typ`, `main.typ`, `mermaid_*.png`, etc.).

### Prerequisites and Dependencies

#### 1. Python Package
`playwright` is required for rendering Mermaid blocks into PNG images.

```bash
pip install -r tools/pdf-generator/requirements.txt
```

#### 2. External Binaries, Fonts, and Browser
Tool resolution branches depending on the host operating system:

| Environment | Pandoc / Typst Resolution | Font Path | Browser (for Mermaid Rendering) |
| :--- | :--- | :--- | :--- |
| **Windows (`os.name == "nt"`)** | `~/.local/bin/pandoc` and `~/.local/bin/typst` inside WSL | `$HOME/.local/share/fonts` inside WSL | Locally installed Google Chrome (auto-discovered) |
| **Linux / Inside WSL (including CI)** | `pandoc` / `typst` on `PATH` (fallback: `~/.local/bin/`) | `~/.local/share/fonts` (if present) and system fonts | Playwright Chromium (overridable via `PLAYWRIGHT_CHROMIUM_EXECUTABLE_PATH`) |

On Linux or CI environments, install Playwright's Chromium binary as well:

```bash
playwright install chromium
```

### Usage

Running the script with no arguments from the repository root reads `PAPER.md` and writes `tools/pdf-generator/output/PAPER.pdf`:

```bash
python tools/pdf-generator/build_pdf.py
```

Use `--input` and `--output` to specify custom paths:

```bash
python tools/pdf-generator/build_pdf.py --input PAPER.md --output PAPER.pdf
```

For automated distribution, [`.github/workflows/release-paper.yml`](../../.github/workflows/release-paper.yml) triggers on `v*` / `paper-v*` tag pushes or manual `workflow_dispatch`, runs the same build command on `ubuntu-latest`, and uploads the generated `PAPER.pdf` to GitHub Releases.

### Conversion Pipeline and Layout

To preserve GitHub rendering compatibility in `PAPER.md` while producing typeset PDF output, `build_pdf.py` and `template.typ` perform the following steps:

1. **Section Splitting and Automated TOC**: Extracts the first `# ` heading as the paper title and the `## 要旨` section as the Abstract, strips the manual `## 目次` section in favor of Typst's `#outline` (depth 2), and promotes remaining headings by one level (`##` to `#`).
2. **GitHub Syntax and Link Normalization**: Converts GitHub inline math (`$`...`$`) outside code fences to Pandoc-compatible `$...$`, rewrites `./` relative links to absolute GitHub URLs (`blob/HEAD`), and normalizes `<br>` tags into spaces inside table rows or line breaks in body text.
3. **High-Resolution Mermaid Rendering**: Embeds `mermaid` fenced blocks into HTML and captures PNG images on a white background at `device_scale_factor=4` via Playwright.
4. **Quote Block Break Control**: Splits Pandoc-generated `#quote(block: true)` blocks at `#strong[\(日本語訳)]` so the original quote and its Japanese translation + citation remain individually non-breakable (`breakable: false`).
5. **Mixed Latin/Japanese Typography**: Configures A4 pages (23mm top/bottom, 26mm left/right margins) with `Libertinus Serif` / `Noto Serif CJK JP` (10.5pt) for body text, `Noto Sans CJK JP` for headings and table headers, `New Computer Modern Math` for equations, and `DejaVu Sans Mono` for code.

### Design Scope and Limitations

- **Tailored to the Author's Windows + WSL Setup and CI Environment**
  - *Constraint Fact*: When invoked directly from Windows, the script relies on fixed paths inside WSL (`~/.local/bin/pandoc`, `~/.local/bin/typst`, `$HOME/.local/share/fonts`) rather than native Windows binaries, and searches only standard Windows installation paths for Google Chrome.
  - *Design Rationale*: Avoids maintaining duplicate Typst and CJK font installations on native Windows and prevents redundant Playwright Chromium downloads by reusing the existing local browser and a Linux-aligned WSL toolchain close to CI (`ubuntu-latest`).
  - *Workaround / Recommended Configuration*: Run the script directly from inside a WSL Linux shell (which resolves binaries via `PATH`), trigger builds via `workflow_dispatch` in GitHub Actions, or adjust the path constants in `build_pdf.py` to match your local setup.
- **Coupling to `PAPER.md` Structure and Repository Metadata**
  - *Constraint Fact*: Section parsing assumes Japanese headings (`## 要旨`, `## 目次`), relative links resolve against the hardcoded `GITHUB_BLOB_BASE` (`DovahkiinYuzuko/explorations-in-documentation/blob/HEAD`), Mermaid figures default to the alt text `統合モデル概念図`, and `template.typ` hardcodes the default author (`Yuzuko Underson (DovahkiinYuzuko)`) and running-header split delimiter (`：`).
  - *Design Rationale*: Designed as a dedicated build pipeline prioritizing typesetting accuracy and reproducibility for `PAPER.md` rather than a generic conversion utility.
  - *Workaround / Recommended Configuration*: When adapting this pipeline for another document or repository, override `--input` / `--output` and update the constants, heading checks, and `template.typ` defaults accordingly.
- **Network Requirement for Mermaid Diagrams**
  - *Constraint Fact*: Rendering Markdown containing `mermaid` code blocks requires internet access to load `https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.min.js`.
  - *Design Rationale*: Eliminates the need to install Node.js and `@mermaid-js/mermaid-cli` locally, keeping the runtime footprint limited to Python and a browser.
  - *Workaround / Recommended Configuration*: For offline builds, either exclude `mermaid` fenced blocks or point `MERMAID_CDN_URL` in `build_pdf.py` to a locally hosted copy of `mermaid.min.js`.
