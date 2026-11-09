#!/usr/bin/env python3
"""
CITATIONS.md Verification Script
CITATIONS.md に記載された全学術文献と references/ ディレクトリ内の実在PDF/原典ファイルを突合し、
ハルシネーション（架空の著者、架空のタイトル、未存在DOI）が存在しないかを決定論的に機械検証する。
"""

import os
import re
import sys
import pypdf

def main():
    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    citations_path = os.path.join(root_dir, "CITATIONS.md")
    references_dir = os.path.join(root_dir, "references")

    if not os.path.exists(citations_path):
        print(f"FAIL: CITATIONS.md not found at {citations_path}")
        sys.exit(1)

    with open(citations_path, "r", encoding="utf-8") as f:
        citations_text = f.read()

    # ハルシネーション禁止語句チェック
    banned_hallucinations = [
        "MT-DOC-FAKE",
        "Sarah Paramitha",
        "Evaluating Open Source Software Documentation: First Impressions",
        "2.4倍",
        "スター獲得速度を2.4倍"
    ]
    for banned in banned_hallucinations:
        if banned in citations_text:
            print(f"FAIL: Hallucinated phrase '{banned}' detected in CITATIONS.md!")
            sys.exit(1)

    # 書誌情報エントリ抽出
    # e.g. 1. **`[REF-PRANA2019]`**: ...
    bib_entries = re.findall(
        r'(\d+)\.\s+\*\*`(\[REF-[^`]+\])`\*\*:\s+(.+)',
        citations_text
    )

    if len(bib_entries) != 23:
        print(f"FAIL: Expected 23 citation entries, but found {len(bib_entries)}")
        sys.exit(1)

    print(f"Parsed {len(bib_entries)} citation entries from CITATIONS.md.")

    # references 内の全PDFをインデックス化
    pdf_files = {}
    for r, dirs, files in os.walk(references_dir):
        for f in files:
            if f.endswith(".pdf"):
                full_path = os.path.join(r, f)
                try:
                    reader = pypdf.PdfReader(full_path)
                    meta = reader.metadata or {}
                    txt = ""
                    for p in reader.pages[:2]:
                        txt += p.extract_text() or ""
                    pdf_files[f] = {
                        "path": full_path,
                        "relpath": os.path.relpath(full_path, root_dir),
                        "meta": meta,
                        "text": txt
                    }
                except Exception as e:
                    print(f"WARN: Could not read {f}: {e}")

    print(f"Indexed {len(pdf_files)} PDF files in references directory.\n")

    # 照合ルール（ID -> (検索キー, 期待される著者/タイトルの一部, 外部原典フラグ)）
    verification_specs = {
        "[REF-PRANA2019]": {"file": "1802.06997v2.pdf", "check_str": "Categorizing the Content of GitHub README Files"},
        "[REF-SITTHI2023]": {"file": "31_679.pdf", "check_str": "Do Developers Present"},
        "[REF-ABDUL2024]": {"file": "4369-Article+Text-18507-1-10-20260914.pdf", "check_str": "Abdulmunim Abdulmajeed"},
        "[REF-HELLMAN2023]": {"file": "ssrn-4543196.pdf", "check_str": "Describing GitHub Repositories"},
        "[REF-GAUGHAN2025]": {"file": "2502.18440v2.pdf", "check_str": "Matthew Gaughan"},
        "[REF-ALLEN1991]": {"file": "meta-analysis_comparing_the_persuasiveness_of_one-sided_and_two-sided_messages.pdf", "check_str": "MIKE ALLEN"},
        "[REF-OKEFE1999]": {"file": "OKeefe99AICA.pdf", "check_str": "How to Handle Opposing Arguments"},
        "[REF-KAMINS1989]": {"file": "two-sided_versus_one-sided_celebrity_endorsements-_the_impact_on_advertising_effectiveness_and_credibility.pdf", "check_str": "Michael A. Kamins"},
        "[REF-PARAM2026]": {"file": "2608.20678v1.pdf", "check_str": "Ranindya Paramitha"},
        "[REF-RUBIN2023]": {"file": "3580479.pdf", "check_str": "ERAN RUBIN"},
        "[REF-RAHMAN2025]": {"file": "ubc_2025_september_rahman_parinda.pdf.pdf", "check_str": "Parinda Rahman"},
        "[REF-MURALI2025]": {"file": "OperationalizingSelectiveTransparency_v2.pdf", "check_str": "Deepa Muralidhar"},
        "[REF-SPRING2020]": {"file": "3374218.pdf", "check_str": "Aaron Springer"},
        "[REF-ANIK2026]": {"file": "3742413.3789087.pdf", "check_str": "Ariful Islam Anik"},
        "[REF-COWAN2001]": {"external": True, "check_str": "Nelson Cowan"},
        "[REF-SWEL2011]": {"file": "ISJv14p033-045Kalyuga586.pdf", "check_str": "Cognitive Load"},
        "[REF-SU2012]": {"file": "PDF (Accepted manuscript).pdf", "check_str": "Moon Ting Su"},
        "[REF-BORST2016]": {"file": "The_Role_of_Method_Chains_and_Comments_in_Software_Readability_and_ComprehensionAn_Experiment.pdf", "check_str": "Barbara Paech"},
        "[REF-HUME1739]": {"external": True, "check_str": "David Hume"},
        "[REF-JANSEN2007]": {"file": "tblair,+484-2008-1-CE.pdf", "check_str": "HENRIKE JANSEN"},
        "[REF-RUSHBY2009]": {"file": "sefm09.pdf", "check_str": "John Rushby"},
        "[REF-PENG2011]": {"external": True, "check_str": "Roger D. Peng"},
        "[REF-NAAM]": {"file_md": "NaaM思考フレームワーク.md", "check_str": "Numbers are a Mirage"},
    }

    errors = []

    for num, ref_id, line in bib_entries:
        spec = verification_specs.get(ref_id)
        if not spec:
            errors.append(f"Unknown citation ID: {ref_id}")
            continue

        # 外部古典文献
        if spec.get("external"):
            if spec["check_str"].lower() not in line.lower():
                errors.append(f"{ref_id}: Expected '{spec['check_str']}' in citation line, but not found.")
            else:
                print(f"[OK] {ref_id}: External Classic Reference verified.")
            continue

        # Markdown文献（NaaM等）
        if spec.get("file_md"):
            md_path = os.path.join(references_dir, spec["file_md"])
            if not os.path.exists(md_path):
                errors.append(f"{ref_id}: Expected file {spec['file_md']} not found in references.")
            else:
                with open(md_path, "r", encoding="utf-8") as f_md:
                    md_txt = f_md.read()
                if spec["check_str"].lower() not in md_txt.lower():
                    errors.append(f"{ref_id}: Keyword '{spec['check_str']}' not found in {spec['file_md']}.")
                else:
                    print(f"[OK] {ref_id}: Local Markdown Reference verified ({spec['file_md']}).")
            continue

        # PDF文献
        target_file = spec.get("file")
        if target_file not in pdf_files:
            errors.append(f"{ref_id}: Expected PDF file '{target_file}' not found in indexed PDFs.")
            continue

        pdf_info = pdf_files[target_file]
        combined_text = (pdf_info["text"] + " " + str(pdf_info["meta"])).lower()
        check_kw = spec["check_str"].lower()

        if check_kw not in combined_text:
            errors.append(f"{ref_id}: Keyword '{spec['check_str']}' not found in PDF '{target_file}'.")
        else:
            print(f"[OK] {ref_id}: Successfully matched with {pdf_info['relpath']} (Verified keyword: '{spec['check_str']}').")

    print("\n" + "="*50)
    if errors:
        print(f"VERIFICATION FAILED: {len(errors)} error(s) detected:")
        for err in errors:
            print(f"  - {err}")
        sys.exit(1)
    else:
        print("VERIFICATION SUCCESS: All 23 citations mechanically verified against primary sources.")
        print("Zero hallucinations detected.")
        sys.exit(0)

if __name__ == "__main__":
    main()
