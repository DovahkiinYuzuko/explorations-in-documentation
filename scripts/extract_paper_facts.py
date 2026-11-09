#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
scripts/extract_paper_facts.py
--------------------------------------------------------------------------------
references/ 配下の学術論文PDFおよびMarkdown資料を、決定論的にZero-Loss（完全性保証）で
Markdownファイルへ抽出し、docs/research/extracted/ 配下に静的カタログとして保存する。
また、トークン効率の良いエージェント向け文献目録 index.md を自動生成する。

【除外ルール】
- references/エージェントスキル/ は除外（ドキュメント工学の論点外）

【Visual-First（画像主体）ルール】
- docs/research/catalog_config.toml に指定された画像主体のPDFは、
  怪文書の生成を防ぎ、エージェントが元PDFを直接画像認識するためのスマートな案内を出力する。

【Zero-Loss 原則】
- 通常の学術文献は、本文テキストを1文字も要約・省略・フィルタリングせず全量出力する。
- 2段組み（Two-Column）の読書順を座標ベースで復元する。
--------------------------------------------------------------------------------
"""

import sys
import os
import hashlib
import re
import tomllib
from pathlib import Path

# Windows console UTF-8 fix
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

try:
    import pymupdf
except ImportError:
    print("ERROR: pymupdf is required. Run 'pip install pymupdf'", file=sys.stderr)
    sys.exit(1)


def load_catalog_config(config_path: Path) -> dict:
    if config_path.exists():
        with open(config_path, "rb") as f:
            return tomllib.load(f)
    return {}


def compute_sha256(file_path: Path) -> str:
    h = hashlib.sha256()
    with open(file_path, "rb") as f:
        while chunk := f.read(65536):
            h.update(chunk)
    return h.hexdigest()


def find_findings(text: str) -> list[str]:
    """統計数値・実験条件の前後文脈ハイライトを抽出する。"""
    pattern = re.compile(
        r"(?:N\s*=\s*\d+|p\s*[<>=]\s*0?\.\d+|\b\d+(?:\.\d+)?%|[rtF]\s*=\s*-?\d+(?:\.\d+)?)",
        re.IGNORECASE,
    )
    matches = list(pattern.finditer(text))
    snippets = []
    seen = set()
    for m in matches:
        start = max(0, m.start() - 80)
        end = min(len(text), m.end() + 80)
        raw_snippet = text[start:end].replace("\r", " ").replace("\n", " ").strip()
        snippet = re.sub(r"\s+", " ", raw_snippet)
        key = snippet[:50]
        if key not in seen:
            seen.add(key)
            matched_val = m.group().strip()
            snippets.append(f"- **`{matched_val}`**: ... {snippet} ...")
        if len(snippets) >= 20:
            break
    return snippets


def extract_page_blocks(page) -> str:
    rect = page.rect
    width = rect.width
    x_mid = width / 2.0
    
    try:
        raw_blocks = page.get_text("blocks")
    except Exception:
        return page.get_text("text")

    text_blocks = [b for b in raw_blocks if b[6] == 0 and b[4].strip()]
    if not text_blocks:
        return ""

    left_blocks = []
    right_blocks = []
    span_blocks = []

    for b in text_blocks:
        x0, y0, x1, y1, text, block_no, btype = b
        bw = x1 - x0
        if bw > width * 0.60:
            span_blocks.append(b)
        elif x1 <= x_mid + 15:
            left_blocks.append(b)
        elif x0 >= x_mid - 15:
            right_blocks.append(b)
        else:
            span_blocks.append(b)

    is_two_column = len(left_blocks) >= 2 and len(right_blocks) >= 2

    if not is_two_column:
        sorted_blocks = sorted(text_blocks, key=lambda b: (b[1], b[0]))
    else:
        col_y_min = min(min(b[1] for b in left_blocks), min(b[1] for b in right_blocks))
        col_y_max = max(max(b[3] for b in left_blocks), max(b[3] for b in right_blocks))

        top_spans = [b for b in span_blocks if b[3] <= col_y_min + 15]
        bottom_spans = [b for b in span_blocks if b[1] >= col_y_max - 15]
        mid_spans = [b for b in span_blocks if b not in top_spans and b not in bottom_spans]

        top_spans.sort(key=lambda b: b[1])
        left_blocks.sort(key=lambda b: b[1])
        right_blocks.sort(key=lambda b: b[1])
        mid_spans.sort(key=lambda b: b[1])
        bottom_spans.sort(key=lambda b: b[1])

        sorted_blocks = top_spans + left_blocks + right_blocks + mid_spans + bottom_spans

    section_keywords = [
        "ABSTRACT", "INTRODUCTION", "BACKGROUND", "RELATED WORK",
        "METHODOLOGY", "METHOD", "METHODS", "DATA COLLECTION", "EMPIRICAL STUDY",
        "RESULTS", "FINDINGS", "DISCUSSION", "LIMITATIONS", "THREATS TO VALIDITY",
        "CONCLUSION", "CONCLUSIONS", "FUTURE WORK", "REFERENCES", "ACKNOWLEDGMENTS"
    ]
    
    formatted_paragraphs = []
    for b in sorted_blocks:
        raw_t = b[4].strip()
        first_line = raw_t.split("\n")[0].strip().upper()
        is_heading = any(first_line == kw or first_line.startswith(kw + ":") or first_line.startswith(kw + " -") for kw in section_keywords)
        if is_heading:
            formatted_paragraphs.append(f"### {raw_t}")
        else:
            formatted_paragraphs.append(raw_t)

    return "\n\n".join(formatted_paragraphs)


def process_visual_first_pdf(pdf_path: Path, out_path: Path, reason: str) -> dict:
    sha256 = compute_sha256(pdf_path)
    file_size = pdf_path.stat().st_size
    doc = pymupdf.open(str(pdf_path))
    num_pages = len(doc)
    total_images = sum(len(p.get_images()) for p in doc)
    meta = doc.metadata or {}

    rel_path_to_source = os.path.relpath(pdf_path, out_path.parent).replace("\\", "/")
    rel_source_from_root = pdf_path.as_posix()
    meta_title = meta.get("title", "").strip() or pdf_path.stem

    out_content = f"""---
source_file: "{rel_source_from_root}"
relative_link: "{rel_path_to_source}"
sha256: "{sha256}"
file_size_bytes: {file_size}
original_format: "pdf"
document_type: "visual_first_pdf"
extracted_pages: {num_pages}
embedded_images_count: {total_images}
text_extraction_status: "ignored_visual_first"
---

# {meta_title}

## 1. 書誌情報およびファイル概要 (Bibliographic Information)

- **元ファイル (Source)**: [{pdf_path.name}]({rel_path_to_source})
- **総ページ数**: {num_pages} ページ (埋め込み画像: {total_images} 枚)
- **ファイルサイズ**: {file_size:,} bytes
- **SHA-256**: `{sha256}`
- **ドキュメント種別**: Visual-First Document (画像主体デザイン資料)

---

## 2. エージェント参照プロトコル (Visual Inspection Protocol)

> [!NOTE]
> 本資料は `docs/research/catalog_config.toml` にて **「Visual-First ドキュメント」** としてテキスト抽出除外に指定されています。
>
> **理由**: {reason}
>
> **エージェントへの指示**:
> 本資料の本文テキスト抽出データは存在しません。元ファイルリンク `[{pdf_path.name}]({rel_path_to_source})` から **元PDFを直接開き、視覚認識ツールを用いて画像・レイアウト・実例スクリーンショットを直接視認・分析** してください。
"""

    out_path.parent.mkdir(parents=True, exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(out_content)

    return {
        "title": meta_title,
        "type": "Visual-First PDF",
        "pages": num_pages,
        "size_kb": file_size // 1024,
    }


def process_pdf(pdf_path: Path, out_path: Path) -> dict:
    sha256 = compute_sha256(pdf_path)
    file_size = pdf_path.stat().st_size
    doc = pymupdf.open(str(pdf_path))
    num_pages = len(doc)
    meta = doc.metadata or {}

    page_texts = []
    for page_idx, page in enumerate(doc, start=1):
        try:
            ptxt = extract_page_blocks(page)
        except Exception:
            ptxt = page.get_text("text").strip()
        page_texts.append(f"--- \n*Page {page_idx}*\n\n{ptxt}")

    full_body = "\n\n".join(page_texts)
    findings = find_findings(full_body)

    rel_path_to_source = os.path.relpath(pdf_path, out_path.parent).replace("\\", "/")
    rel_source_from_root = pdf_path.as_posix()

    meta_title = meta.get("title", "").strip() or pdf_path.stem
    meta_author = meta.get("author", "").strip() or "Unknown"
    meta_subject = meta.get("subject", "").strip() or "N/A"

    out_content = f"""---
source_file: "{rel_source_from_root}"
relative_link: "{rel_path_to_source}"
sha256: "{sha256}"
file_size_bytes: {file_size}
original_format: "pdf"
document_type: "academic_paper_pdf"
extracted_pages: {num_pages}
meta_title: "{meta_title.replace('"', "'")}"
meta_author: "{meta_author.replace('"', "'")}"
meta_subject: "{meta_subject.replace('"', "'")}"
---

# {meta_title}

## 1. 書誌情報およびファイル概要 (Bibliographic Information)

- **元ファイル (Source)**: [{pdf_path.name}]({rel_path_to_source})
- **総ページ数**: {num_pages} ページ
- **ファイルサイズ**: {file_size:,} bytes
- **SHA-256**: `{sha256}`
- **メタデータ 著者**: {meta_author}
- **メタデータ 主題**: {meta_subject}

---

## 2. 抽出された統計数値・実験条件 (Auto-Extracted Findings)

"""
    if findings:
        out_content += "\n".join(findings) + "\n\n"
    else:
        out_content += "*※本ドキュメントからは特定の統計数値パターン（N=, p<, %等）は検出されませんでした（定性研究・理論的考察文献）。*\n\n"

    out_content += """---

## 3. 本文全量テキスト (Full Text - Zero-Loss Guarantee)

""" + full_body + "\n"

    out_path.parent.mkdir(parents=True, exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(out_content)

    return {
        "title": meta_title,
        "type": "Paper PDF",
        "pages": num_pages,
        "size_kb": file_size // 1024,
    }


def process_markdown(md_path: Path, out_path: Path) -> dict:
    sha256 = compute_sha256(md_path)
    file_size = md_path.stat().st_size
    with open(md_path, "r", encoding="utf-8", errors="replace") as f:
        raw_content = f.read()

    findings = find_findings(raw_content)
    rel_path_to_source = os.path.relpath(md_path, out_path.parent).replace("\\", "/")
    rel_source_from_root = md_path.as_posix()
    doc_title = md_path.stem

    out_content = f"""---
source_file: "{rel_source_from_root}"
relative_link: "{rel_path_to_source}"
sha256: "{sha256}"
file_size_bytes: {file_size}
original_format: "markdown"
document_type: "reference_markdown"
extracted_pages: 1
meta_title: "{doc_title}"
meta_author: "N/A"
meta_subject: "Markdown Reference Document"
---

# {doc_title}

## 1. 書誌情報およびファイル概要 (Bibliographic Information)

- **元ファイル (Source)**: [{md_path.name}]({rel_path_to_source})
- **ファイル形式**: 原本Markdown
- **ファイルサイズ**: {file_size:,} bytes
- **SHA-256**: `{sha256}`

---

## 2. 抽出された統計数値・実験条件 (Auto-Extracted Findings)

"""
    if findings:
        out_content += "\n".join(findings) + "\n\n"
    else:
        out_content += "*※本ドキュメントからは特定の統計数値パターン（N=, p<, %等）は検出されませんでした（定性研究・理論的考察文献）。*\n\n"

    out_content += """---

## 3. 本文全量テキスト (Full Text - Zero-Loss Guarantee)

""" + raw_content + "\n"

    out_path.parent.mkdir(parents=True, exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(out_content)

    return {
        "title": doc_title,
        "type": "Markdown",
        "pages": 1,
        "size_kb": file_size // 1024,
    }


def generate_index_markdown(catalog_records: list[dict], index_path: Path):
    """トークン効率の良いエージェント向け文献目録 index.md を生成する。"""
    categories = {}
    for r in catalog_records:
        cat = r["category"]
        if cat not in categories:
            categories[cat] = []
        categories[cat].append(r)

    lines = [
        "# 参考文献目録 (References Index)",
        "",
        "本ドキュメントは `references/` 配下の一次資料（全57件）および `docs/research/extracted/` の静的カタログへの高速アクセス用インデックスです。",
        "",
        "> [!TIP]",
        "> エージェントは論文調査時、巨大PDFを直接パースするのではなく、**[抽出カタログ]** のMarkdownを `read_file` してください。",
        "> `Visual-First PDF` と表示された資料のみ、**[元ファイル]** のPDFを直接画像認識ツールで参照してください。",
        "",
        "---",
        "",
    ]

    for cat, items in sorted(categories.items()):
        lines.append(f"## {cat} ({len(items)} 件)")
        lines.append("")
        lines.append("| 文献名 / タイトル | 種別 | 抽出カタログ (Markdown) | 元資料 (Source) | サイズ |")
        lines.append("| :--- | :---: | :--- | :--- | :---: |")
        for item in sorted(items, key=lambda x: x["filename"]):
            ext_link = f"[{item['extracted_name']}]({item['rel_extracted']})"
            src_link = f"[{item['filename']}]({item['rel_source']})"
            lines.append(
                f"| **{item['info']['title']}** | `{item['info']['type']}` | {ext_link} | {src_link} | {item['info']['size_kb']} KB |"
            )
        lines.append("")

    with open(index_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"Generated clean index: {index_path}")


def main():
    root_dir = Path(".")
    ref_dir = root_dir / "references"
    out_base_dir = root_dir / "docs" / "research" / "extracted"
    config_path = root_dir / "docs" / "research" / "catalog_config.toml"
    index_path = root_dir / "index.md"

    if not ref_dir.exists():
        print(f"ERROR: {ref_dir} does not exist.", file=sys.stderr)
        sys.exit(1)

    config = load_catalog_config(config_path)
    visual_cfg = config.get("visual_first_documents", {})
    visual_files = set(visual_cfg.get("files", []))
    visual_reason = visual_cfg.get("reason", "Visual-first document.")

    print("Starting deterministic zero-loss extraction...")
    print(f"Source Directory: {ref_dir}")
    print(f"Target Directory: {out_base_dir}")
    print(f"Visual-First Ignored Files: {visual_files}")

    total_processed = 0
    total_pdf = 0
    total_visual = 0
    total_md = 0
    catalog_records = []

    for root, dirs, files in os.walk(ref_dir):
        if "エージェントスキル" in root:
            continue

        for f in sorted(files):
            src_path = Path(root) / f
            ext = src_path.suffix.lower()

            if ext not in [".pdf", ".md"]:
                continue

            rel_to_ref = src_path.relative_to(ref_dir)
            category = rel_to_ref.parts[0] if len(rel_to_ref.parts) > 1 else "misc"

            if ext == ".pdf":
                out_filename = src_path.stem + ".md"
                out_path = out_base_dir / category / out_filename

                if src_path.name in visual_files:
                    info = process_visual_first_pdf(src_path, out_path, visual_reason)
                    total_visual += 1
                    print(f"[{total_processed+1:02d}] Visual-First PDF: {category}/{src_path.name} -> {out_filename}")
                else:
                    info = process_pdf(src_path, out_path)
                    total_pdf += 1
                    print(f"[{total_processed+1:02d}] Extracted PDF:    {category}/{src_path.name} -> {out_filename}")
                total_processed += 1
            elif ext == ".md":
                out_filename = src_path.name
                out_path = out_base_dir / category / out_filename
                info = process_markdown(src_path, out_path)
                total_md += 1
                total_processed += 1
                print(f"[{total_processed:02d}] Synced MD:        {category}/{src_path.name} -> {out_filename}")

            catalog_records.append({
                "category": category,
                "filename": src_path.name,
                "extracted_name": out_filename,
                "rel_source": src_path.as_posix(),
                "rel_extracted": out_path.as_posix(),
                "info": info,
            })

    # index.md 生成
    generate_index_markdown(catalog_records, index_path)

    print("\n" + "=" * 60)
    print(f"SUCCESS: Total files extracted/synced: {total_processed}")
    print(f"  - PDFs converted (Academic): {total_pdf}")
    print(f"  - PDFs visual-first (Guide): {total_visual}")
    print(f"  - Markdowns synced:         {total_md}")
    print("=" * 60)


if __name__ == "__main__":
    main()
