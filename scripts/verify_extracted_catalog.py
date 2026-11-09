#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
scripts/verify_extracted_catalog.py
--------------------------------------------------------------------------------
docs/research/extracted/ 配下の静的カタログが、references/ 配下の元資料（全57件）と
1対1で完全一致し、偽陰性（欠落）や破損がないことを決定論的に検証・アサートするオラクル。
catalog_config.toml の Visual-First 設定および index.md の完全性も検証する。
--------------------------------------------------------------------------------
"""

import sys
import os
import hashlib
import tomllib
from pathlib import Path

# Windows console UTF-8 fix
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass


def compute_sha256(file_path: Path) -> str:
    h = hashlib.sha256()
    with open(file_path, "rb") as f:
        while chunk := f.read(65536):
            h.update(chunk)
    return h.hexdigest()


def main():
    root_dir = Path(".")
    ref_dir = root_dir / "references"
    extracted_dir = root_dir / "docs" / "research" / "extracted"
    config_path = root_dir / "docs" / "research" / "catalog_config.toml"
    index_path = root_dir / "index.md"

    print("=" * 60)
    print("Deterministic Catalog Verification Oracle")
    print(f"Source:    {ref_dir}")
    print(f"Extracted: {extracted_dir}")
    print(f"Config:    {config_path}")
    print(f"Index:     {index_path}")
    print("=" * 60)

    if not extracted_dir.exists():
        print(f"FAIL: Extracted directory {extracted_dir} does not exist.", file=sys.stderr)
        sys.exit(1)

    # 0. Config読み込み
    visual_files = set()
    if config_path.exists():
        with open(config_path, "rb") as f:
            cfg = tomllib.load(f)
            visual_files = set(cfg.get("visual_first_documents", {}).get("files", []))
    print(f"Loaded visual-first ignored files: {visual_files}")

    # 1. 元ファイルリストの収集（エージェントスキル除外）
    source_files = []
    for root, dirs, files in os.walk(ref_dir):
        if "エージェントスキル" in root:
            continue
        for f in files:
            p = Path(root) / f
            if p.suffix.lower() in [".pdf", ".md"]:
                source_files.append(p)

    expected_count = 57
    actual_source_count = len(source_files)
    print(f"Total target source files collected: {actual_source_count} (Expected: {expected_count})")
    assert actual_source_count == expected_count, f"Source count mismatch: {actual_source_count} != {expected_count}"

    # 2. 抽出済みMarkdownファイルの収集
    extracted_files = list(extracted_dir.glob("**/*.md"))
    actual_extracted_count = len(extracted_files)
    print(f"Total extracted markdown files:      {actual_extracted_count} (Expected: {expected_count})")
    assert actual_extracted_count == expected_count, f"Extracted count mismatch: {actual_extracted_count} != {expected_count}"

    # 3. 1対1整合性検証
    errors = []
    verified_count = 0

    for src_path in sorted(source_files):
        rel_to_ref = src_path.relative_to(ref_dir)
        category = rel_to_ref.parts[0] if len(rel_to_ref.parts) > 1 else "misc"
        
        if src_path.suffix.lower() == ".pdf":
            expected_out_name = src_path.stem + ".md"
        else:
            expected_out_name = src_path.name

        target_out_path = extracted_dir / category / expected_out_name
        if not target_out_path.exists():
            errors.append(f"Missing output file: {target_out_path}")
            continue

        out_size = target_out_path.stat().st_size
        if out_size == 0:
            errors.append(f"Empty output file: {target_out_path}")
            continue

        src_sha256 = compute_sha256(src_path)

        with open(target_out_path, "r", encoding="utf-8") as f:
            content = f.read()

        if f'sha256: "{src_sha256}"' not in content:
            errors.append(f"SHA-256 mismatch or missing in {target_out_path}")
            continue

        import re
        link_match = re.search(r'relative_link:\s*"([^"]+)"', content)
        if not link_match:
            errors.append(f"relative_link missing in {target_out_path}")
            continue

        rel_link_val = link_match.group(1)
        resolved_link = (target_out_path.parent / rel_link_val).resolve()
        if not resolved_link.exists():
            errors.append(f"Broken relative link in {target_out_path}: {rel_link_val} (Resolved: {resolved_link})")
            continue

        # Visual-First PDF vs Regular Document 分岐検証
        if src_path.name in visual_files:
            if 'document_type: "visual_first_pdf"' not in content:
                errors.append(f"Expected visual_first_pdf header in {target_out_path}")
                continue
            if "## 2. エージェント参照プロトコル (Visual Inspection Protocol)" not in content:
                errors.append(f"Visual Inspection Protocol section missing in {target_out_path}")
                continue
        else:
            if "## 3. 本文全量テキスト (Full Text - Zero-Loss Guarantee)" not in content:
                errors.append(f"Full text section missing in {target_out_path}")
                continue

        verified_count += 1

    # 4. index.md の存在と健全性検証
    if not index_path.exists() or index_path.stat().st_size == 0:
        errors.append(f"index.md is missing or empty at {index_path}")
    else:
        with open(index_path, "r", encoding="utf-8") as f:
            idx_content = f.read()
        if "## CVR・離脱防止テクニック" not in idx_content:
            errors.append("index.md missing expected categories")

    if errors:
        print("\n" + "!" * 60, file=sys.stderr)
        print(f"VERIFICATION FAILED: {len(errors)} error(s) found:", file=sys.stderr)
        for err in errors:
            print(f"  - {err}", file=sys.stderr)
        print("!" * 60, file=sys.stderr)
        sys.exit(1)

    print("\n" + "=" * 60)
    print(f"SUCCESS: All {verified_count}/{expected_count} catalog documents perfectly verified.")
    print("  - 100% 1-to-1 match with source files")
    print("  - Visual-First files correctly isolated and guided")
    print("  - SHA-256 integrity verified")
    print("  - Relative links intact and tested")
    print("  - index.md successfully validated")
    print("=" * 60)


if __name__ == "__main__":
    main()
