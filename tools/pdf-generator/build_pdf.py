#!/usr/bin/env python3
"""PAPER.md を Single Source of Truth とし、Pandoc と Typst を用いて論文形式 PDF を生成するスクリプト。"""

from __future__ import annotations

import argparse
import html
import logging
import os
import re
import shutil
import subprocess
import sys
from datetime import datetime, timezone, timedelta
from pathlib import Path

logging.basicConfig(
    level=logging.INFO,
    format="[%(levelname)s] %(message)s",
)
logger = logging.getLogger("pdf-generator")

GENERATOR_DIR = Path(__file__).resolve().parent
REPO_ROOT = GENERATOR_DIR.parents[1]
DEFAULT_INPUT = REPO_ROOT / "PAPER.md"
DEFAULT_OUTPUT = GENERATOR_DIR / "output" / "PAPER.pdf"
BUILD_DIR = GENERATOR_DIR / ".build"
TEMPLATE_PATH = GENERATOR_DIR / "template.typ"

GITHUB_BLOB_BASE = "https://github.com/DovahkiinYuzuko/explorations-in-documentation/blob/HEAD"

CHROME_CANDIDATES = [
    Path(r"C:\Program Files\Google\Chrome\Application\chrome.exe"),
    Path(r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"),
    Path.home() / "AppData" / "Local" / "Google" / "Chrome" / "Application" / "chrome.exe",
]

MERMAID_CDN_URL = "https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.min.js"
PANDOC_INPUT_FORMAT = (
    "markdown+tex_math_dollars+footnotes+pipe_tables+strikeout+lists_without_preceding_blankline"
)


def to_wsl_path(path: Path) -> str:
    """Windows パスを WSL の /mnt/<drive>/... 形式へ変換する。"""
    resolved = path.resolve()
    drive = resolved.drive.rstrip(":").lower()
    if not drive:
        return resolved.as_posix()
    tail = resolved.as_posix().split(":", 1)[1].lstrip("/")
    return f"/mnt/{drive}/{tail}"


def resolve_local_chrome() -> Path:
    """Windows 環境にインストール済みの Google Chrome 実行ファイルを探索する。"""
    for candidate in CHROME_CANDIDATES:
        if candidate.is_file():
            return candidate
    raise FileNotFoundError(
        "既存の Google Chrome が見つかりませんでした。"
        "Chromium の自動ダウンロードを抑止するため、Chrome の導入先を確認してください。"
    )


def split_paper_sections(raw_text: str) -> tuple[str, str, str]:
    """Markdown からタイトル・要旨本文・目次除去後の本体を抽出する。"""
    lines = raw_text.splitlines()
    title = "論文タイトル未設定"
    title_idx = -1

    for idx, line in enumerate(lines):
        if line.startswith("# "):
            title = line[2:].strip()
            title_idx = idx
            break

    content_lines = lines[title_idx + 1 :] if title_idx >= 0 else lines

    abstract_lines: list[str] = []
    body_lines: list[str] = []

    mode = "body"
    in_fence = False
    for line in content_lines:
        stripped = line.strip()
        if stripped.startswith("```"):
            in_fence = not in_fence

        if not in_fence and line.startswith("## "):
            heading_text = line[3:].strip()
            if heading_text.startswith("要旨"):
                mode = "abstract"
                continue
            if heading_text == "目次":
                mode = "toc_skip"
                continue
            mode = "body"

        if mode == "abstract":
            abstract_lines.append(line)
        elif mode == "toc_skip":
            continue
        else:
            body_lines.append(line)

    abstract_text = "\n".join(abstract_lines).strip()
    body_text = "\n".join(body_lines).strip() + "\n"
    return title, abstract_text, body_text


def shift_heading_levels(md_text: str) -> str:
    """コードフェンス外の見出しレベルを 1 段繰り上げる（## -> #）。"""
    out: list[str] = []
    in_fence = False
    for line in md_text.splitlines():
        if line.strip().startswith("```"):
            in_fence = not in_fence
            out.append(line)
            continue
        if not in_fence and re.match(r"^#{2,6}\s+", line):
            out.append(line[1:])
        else:
            out.append(line)
    return "\n".join(out)


def normalize_inline_math_and_tags(md_text: str) -> str:
    """コードフェンス外の GitHub 数式記法 ($`...`$) と <br> および相対リンクを正規化する。"""
    out_lines: list[str] = []
    in_fence = False

    inline_math_pattern = re.compile(r"\$`([^`]+?)`\$")
    rel_link_pattern = re.compile(r"\]\(\./([^)]+)\)")
    br_pattern = re.compile(r"<br\s*/?>", re.IGNORECASE)

    for line in md_text.splitlines():
        stripped = line.strip()
        if stripped.startswith("```"):
            in_fence = not in_fence
            out_lines.append(line)
            continue

        if in_fence:
            out_lines.append(line)
            continue

        # GitHub 固有の $`...`$ を Pandoc tex_math_dollars 準拠の $...$ へ変換
        converted = inline_math_pattern.sub(lambda m: f"${m.group(1).strip()}$", line)
        # 相対リンクを GitHub リポジトリ上の絶対 URL へ変換
        converted = rel_link_pattern.sub(rf"]({GITHUB_BLOB_BASE}/\1)", converted)

        # テーブル行内の <br> は読点・空白または明示区切りへ、通常行は強制改行へ変換
        if converted.lstrip().startswith("|"):
            converted = br_pattern.sub(" ", converted)
        else:
            converted = br_pattern.sub("  \n", converted)

        out_lines.append(converted)

    return "\n".join(out_lines)


def render_mermaid_to_png(mermaid_code: str, out_png: Path) -> None:
    """Playwright を用いて Mermaid コードを透過なし高解像度 PNG へ描画する。"""
    from playwright.sync_api import sync_playwright

    html_doc = f"""<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8" />
  <style>
    body {{
      margin: 0;
      padding: 16px;
      background: #ffffff;
      font-family: "Noto Sans CJK JP", "Noto Sans JP", "Yu Gothic", sans-serif;
    }}
    .mermaid {{
      display: inline-block;
    }}
    .mermaid .nodeLabel {{
      white-space: nowrap;
    }}
  </style>
  <script src="{MERMAID_CDN_URL}"></script>
</head>
<body>
  <div class="mermaid" id="diagram">{html.escape(mermaid_code)}</div>
  <script>
    mermaid.initialize({{
      startOnLoad: true,
      theme: "neutral",
      flowchart: {{ useMaxWidth: false, htmlLabels: true, wrappingWidth: 600 }}
    }});
  </script>
</body>
</html>
"""
    html_path = out_png.with_suffix(".html")
    html_path.write_text(html_doc, encoding="utf-8")

    with sync_playwright() as playwright:
        if os.name == "nt":
            chrome_exe = resolve_local_chrome()
            logger.info("既存 Google Chrome を使用して Mermaid を描画します: %s", chrome_exe)
            browser = playwright.chromium.launch(
                executable_path=str(chrome_exe),
                headless=True,
            )
        else:
            custom_exe = os.environ.get("PLAYWRIGHT_CHROMIUM_EXECUTABLE_PATH")
            launch_kwargs = {"headless": True}
            if custom_exe:
                launch_kwargs["executable_path"] = custom_exe
            logger.info("Linux/CI 環境の Playwright Chromium を使用して Mermaid を描画します。")
            browser = playwright.chromium.launch(**launch_kwargs)

        try:
            page = browser.new_page(
                viewport={"width": 1600, "height": 900},
                device_scale_factor=4,
            )
            page.goto(html_path.as_uri(), wait_until="networkidle")
            svg_locator = page.locator("#diagram svg")
            svg_locator.wait_for(state="visible", timeout=20000)
            svg_locator.screenshot(path=str(out_png))
        finally:
            browser.close()


def replace_mermaid_blocks(md_text: str, assets_dir: Path) -> str:
    """Markdown 内の mermaid コードフェンスを高解像度 PNG 画像参照へ置換する。"""
    assets_dir.mkdir(parents=True, exist_ok=True)
    pattern = re.compile(r"```mermaid\s*\n(.*?)\n```", re.DOTALL)
    counter = 0

    def _replace(match: re.Match[str]) -> str:
        nonlocal counter
        counter += 1
        code = match.group(1).strip()
        out_png = assets_dir / f"mermaid_{counter}.png"
        render_mermaid_to_png(code, out_png)
        logger.info("Mermaid 図 %d を生成しました: %s", counter, out_png)
        return f"![統合モデル概念図]({out_png.name})"

    return pattern.sub(_replace, md_text)


def postprocess_typst_body(typst_text: str) -> str:
    """Pandoc が出力した Typst 記述の画像幅と引用ブロック分割境界を調整する。"""
    text = re.sub(
        r'image\("(mermaid_\d+\.png)"\)',
        r'image("\1", width: 100%)',
        typst_text,
    )
    # #quote(block: true)[ ... #strong[\(日本語訳)] ... ] を
    # Original (breakable: false) と 日本語訳+出所 (breakable: false) に分割する
    quote_pattern = re.compile(
        r"(#quote\(block: true\)\[\s*\n)(.*?)(#strong\[\\\(日本語訳\)\].*?)(\n\])",
        re.DOTALL,
    )
    return quote_pattern.sub(
        r"\1#block(breakable: false)[\n\2]\n#block(breakable: false)[\n\3\n]\4",
        text,
    )


def run_pandoc_and_typst(
    body_md: Path,
    abstract_md: Path | None,
    main_typ: Path,
    output_pdf: Path,
    title: str,
    date_str: str,
) -> None:
    """Pandoc による Typst 変換と Typst による PDF コンパイルを実行する。"""
    body_typ = BUILD_DIR / "body.typ"
    abstract_typ = BUILD_DIR / "abstract.typ"

    if os.name == "nt":
        # Windows 実行時は WSL セッションの連続起動競合を避けるため 1 回の呼び出しで完結させる
        write_main_typ(main_typ, title, date_str, has_abstract=abstract_md is not None)
        wsl_build = to_wsl_path(BUILD_DIR)
        wsl_output = to_wsl_path(output_pdf)
        wsl_body_md = to_wsl_path(body_md)
        wsl_body_typ = to_wsl_path(body_typ)
        wsl_main_typ = to_wsl_path(main_typ)

        cmds = [
            f'~/.local/bin/pandoc "{wsl_body_md}" -f {PANDOC_INPUT_FORMAT} -t typst -o "{wsl_body_typ}"',
        ]
        if abstract_md is not None:
            wsl_abs_md = to_wsl_path(abstract_md)
            wsl_abs_typ = to_wsl_path(abstract_typ)
            cmds.append(
                f'~/.local/bin/pandoc "{wsl_abs_md}" -f {PANDOC_INPUT_FORMAT} -t typst -o "{wsl_abs_typ}"'
            )

        wsl_gen_dir = to_wsl_path(GENERATOR_DIR)
        cmds.append(
            f'python3 -c "import sys; sys.path.insert(0, \'{wsl_gen_dir}\'); '
            f'from pathlib import Path; from build_pdf import postprocess_typst_body; '
            f'p = Path(\'{wsl_body_typ}\'); '
            f'p.write_text(postprocess_typst_body(p.read_text(encoding=\'utf-8\')), encoding=\'utf-8\')"'
        )
        cmds.append(
            f'~/.local/bin/typst compile --root "{wsl_build}" '
            f'--font-path "$HOME/.local/share/fonts" '
            f'"{wsl_main_typ}" "{wsl_output}"'
        )

        bash_script = "set -euo pipefail; " + "; ".join(cmds)
        logger.info("WSL Pandoc + Typst による変換・PDF ビルドを開始します。")
        subprocess.run(["wsl", "-e", "bash", "-lc", bash_script], check=True)
    else:
        pandoc_bin = shutil.which("pandoc") or str(Path.home() / ".local" / "bin" / "pandoc")
        typst_bin = shutil.which("typst") or str(Path.home() / ".local" / "bin" / "typst")

        logger.info("Pandoc による Typst 変換を開始します: %s", pandoc_bin)
        subprocess.run(
            [
                pandoc_bin,
                str(body_md),
                "-f",
                PANDOC_INPUT_FORMAT,
                "-t",
                "typst",
                "-o",
                str(body_typ),
            ],
            check=True,
        )
        if abstract_md is not None:
            subprocess.run(
                [
                    pandoc_bin,
                    str(abstract_md),
                    "-f",
                    PANDOC_INPUT_FORMAT,
                    "-t",
                    "typst",
                    "-o",
                    str(abstract_typ),
                ],
                check=True,
            )

        body_typ.write_text(
            postprocess_typst_body(body_typ.read_text(encoding="utf-8")),
            encoding="utf-8",
        )
        write_main_typ(main_typ, title, date_str, has_abstract=abstract_md is not None)

        typst_cmd = [
            typst_bin,
            "compile",
            "--root",
            str(BUILD_DIR),
        ]
        user_fonts = Path.home() / ".local" / "share" / "fonts"
        if user_fonts.is_dir():
            typst_cmd.extend(["--font-path", str(user_fonts)])
        typst_cmd.extend([str(main_typ), str(output_pdf)])

        logger.info("Typst による PDF ビルドを開始します: %s", typst_bin)
        subprocess.run(typst_cmd, check=True)


def write_main_typ(main_typ: Path, title: str, date_str: str, has_abstract: bool) -> None:
    """テンプレートと変換済み本文を結合する main.typ を書き出す。"""
    shutil.copy2(TEMPLATE_PATH, BUILD_DIR / "template.typ")

    escaped_title = title.replace("\\", "\\\\").replace('"', '\\"')
    escaped_date = date_str.replace("\\", "\\\\").replace('"', '\\"')

    abstract_expr = 'include "abstract.typ"' if has_abstract else "none"
    content = (
        '#import "template.typ": paper_template\n\n'
        f'#show: paper_template.with(\n'
        f'  title: "{escaped_title}",\n'
        f'  date_str: "{escaped_date}",\n'
        f'  abstract_body: {abstract_expr},\n'
        f')\n\n'
        '#include "body.typ"\n'
    )
    main_typ.write_text(content, encoding="utf-8")


def build_pdf(input_path: Path, output_path: Path) -> None:
    """指定された Markdown ファイルから論文形式の PDF を生成する。"""
    logger.info("ENTRY build_pdf: input=%s, output=%s", input_path, output_path)
    if not input_path.is_file():
        raise FileNotFoundError(f"入力ファイルが見つかりません: {input_path}")

    BUILD_DIR.mkdir(parents=True, exist_ok=True)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    raw_text = input_path.read_text(encoding="utf-8")
    title, abstract_raw, body_raw = split_paper_sections(raw_text)

    body_shifted = shift_heading_levels(body_raw)
    body_normalized = normalize_inline_math_and_tags(body_shifted)
    body_with_imgs = replace_mermaid_blocks(body_normalized, BUILD_DIR)

    body_md = BUILD_DIR / "body.md"
    body_md.write_text(body_with_imgs, encoding="utf-8")

    abstract_md: Path | None = None
    if abstract_raw:
        abstract_normalized = normalize_inline_math_and_tags(abstract_raw)
        abstract_md = BUILD_DIR / "abstract.md"
        abstract_md.write_text(abstract_normalized, encoding="utf-8")

    jst = timezone(timedelta(hours=9))
    date_str = datetime.now(jst).strftime("%Y-%m-%d")
    main_typ = BUILD_DIR / "main.typ"

    run_pandoc_and_typst(
        body_md=body_md,
        abstract_md=abstract_md,
        main_typ=main_typ,
        output_pdf=output_path,
        title=title,
        date_str=date_str,
    )
    logger.info("SUCCESS build_pdf: 生成完了 -> %s (%d bytes)", output_path, output_path.stat().st_size)


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="PAPER.md から論文形式 PDF を生成します。")
    parser.add_argument(
        "--input",
        type=Path,
        default=DEFAULT_INPUT,
        help=f"入力 Markdown ファイルパス (既定: {DEFAULT_INPUT})",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=DEFAULT_OUTPUT,
        help=f"出力 PDF ファイルパス (既定: {DEFAULT_OUTPUT})",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(sys.argv[1:] if argv is None else argv)
    try:
        build_pdf(args.input.resolve(), args.output.resolve())
        return 0
    except Exception as exc:
        logger.error("FAILURE build_pdf: %s", exc)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
