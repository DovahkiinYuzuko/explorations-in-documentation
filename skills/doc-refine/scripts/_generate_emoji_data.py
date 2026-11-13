#!/usr/bin/env python3
"""Maintainer script to fetch official Unicode and Gemoji data and generate emoji_data.py.

This script uses only the Python 3.10+ standard library and is intended to be run
explicitly by a maintainer when updating the bundled emoji tables.
"""

from __future__ import annotations

import argparse
from datetime import datetime, timezone
import json
from pathlib import Path
import re
import sys
import urllib.error
import urllib.request

UNICODE_URLS = {
    "emoji_data": "https://unicode.org/Public/UCD/latest/ucd/emoji/emoji-data.txt",
    "emoji_variation_sequences": "https://unicode.org/Public/UCD/latest/ucd/emoji/emoji-variation-sequences.txt",
    "emoji_sequences": "https://unicode.org/Public/emoji/latest/emoji-sequences.txt",
    "emoji_zwj_sequences": "https://unicode.org/Public/emoji/latest/emoji-zwj-sequences.txt",
    "emoji_test": "https://unicode.org/Public/emoji/latest/emoji-test.txt",
}
GEMOJI_URL = "https://raw.githubusercontent.com/github/gemoji/master/db/emoji.json"
DEFAULT_OUTPUT_PATH = Path(__file__).resolve().parent / "emoji_data.py"
USER_AGENT = "doc-refine-emoji-generator/1.0"
FETCH_TIMEOUT_SEC = 30

VERSION_RE = re.compile(r"^#\s*Version:\s*([0-9]+\.[0-9]+(?:\.[0-9]+)?)", re.MULTILINE)


def _configure_stdio() -> None:
    """Ensure stdout and stderr handle UTF-8 cleanly on Windows consoles."""
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8", errors="replace")


def fetch_text(url: str, timeout: int = FETCH_TIMEOUT_SEC) -> str:
    """Fetch UTF-8 text from a remote URL."""
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(request, timeout=timeout) as response:
        return response.read().decode("utf-8")


def extract_version(text: str, source_name: str) -> str:
    """Extract major.minor version string from a Unicode data file header."""
    match = VERSION_RE.search(text)
    if not match:
        raise ValueError(f"Could not find '# Version:' header in {source_name}")
    parts = match.group(1).split(".")
    return f"{parts[0]}.{parts[1]}"


def merge_ranges(codepoints: set[int]) -> tuple[tuple[int, int], ...]:
    """Compress a set of integer codepoints into sorted, inclusive (start, end) ranges."""
    if not codepoints:
        return ()
    sorted_cps = sorted(codepoints)
    ranges: list[tuple[int, int]] = []
    start = prev = sorted_cps[0]
    for cp in sorted_cps[1:]:
        if cp == prev + 1:
            prev = cp
        else:
            ranges.append((start, prev))
            start = prev = cp
    ranges.append((start, prev))
    return tuple(ranges)


def parse_codepoint_range(token: str) -> tuple[int, int]:
    """Parse '1F600' or '1F600..1F64F' into an inclusive (start, end) tuple."""
    if ".." in token:
        start_hex, end_hex = token.split("..", 1)
        return int(start_hex, 16), int(end_hex, 16)
    cp = int(token, 16)
    return cp, cp


def parse_emoji_data(text: str) -> dict[str, tuple[tuple[int, int], ...]]:
    """Parse emoji-data.txt into merged codepoint ranges keyed by Unicode property."""
    target_props = (
        "Emoji",
        "Emoji_Presentation",
        "Emoji_Modifier",
        "Emoji_Modifier_Base",
        "Emoji_Component",
        "Extended_Pictographic",
    )
    buckets: dict[str, set[int]] = {prop: set() for prop in target_props}
    for raw_line in text.splitlines():
        line = raw_line.split("#", 1)[0].strip()
        if not line:
            continue
        fields = [part.strip() for part in line.split(";")]
        if len(fields) < 2:
            continue
        prop = fields[1]
        if prop in buckets:
            start, end = parse_codepoint_range(fields[0])
            buckets[prop].update(range(start, end + 1))
    return {prop: merge_ranges(cps) for prop, cps in buckets.items()}


def parse_variation_sequences(text: str) -> tuple[frozenset[int], frozenset[int]]:
    """Parse emoji-variation-sequences.txt into (vs15_text_bases, vs16_emoji_bases)."""
    vs15_bases: set[int] = set()
    vs16_bases: set[int] = set()
    for raw_line in text.splitlines():
        line = raw_line.split("#", 1)[0].strip()
        if not line:
            continue
        fields = [part.strip() for part in line.split(";")]
        if len(fields) < 2:
            continue
        cps = [int(hx, 16) for hx in fields[0].split()]
        if len(cps) != 2:
            continue
        base_cp, selector_cp = cps
        if selector_cp == 0xFE0E:
            vs15_bases.add(base_cp)
        elif selector_cp == 0xFE0F:
            vs16_bases.add(base_cp)
    return frozenset(vs15_bases), frozenset(vs16_bases)


def parse_emoji_test(text: str) -> tuple[frozenset[str], frozenset[str]]:
    """Parse emoji-test.txt into (rgi_sequences, component_sequences)."""
    rgi_sequences: set[str] = set()
    component_sequences: set[str] = set()
    valid_rgi_statuses = {"fully-qualified", "minimally-qualified", "unqualified"}
    for raw_line in text.splitlines():
        line = raw_line.split("#", 1)[0].strip()
        if not line:
            continue
        fields = [part.strip() for part in line.split(";")]
        if len(fields) < 2:
            continue
        status = fields[1]
        seq = "".join(chr(int(hx, 16)) for hx in fields[0].split())
        if status in valid_rgi_statuses:
            rgi_sequences.add(seq)
        elif status == "component":
            component_sequences.add(seq)
    return frozenset(rgi_sequences), frozenset(component_sequences)


def parse_extra_sequences(text: str) -> frozenset[str]:
    """Extract sequence strings from emoji-sequences.txt or emoji-zwj-sequences.txt."""
    sequences: set[str] = set()
    for raw_line in text.splitlines():
        line = raw_line.split("#", 1)[0].strip()
        if not line:
            continue
        fields = [part.strip() for part in line.split(";")]
        if not fields:
            continue
        cp_token = fields[0]
        if ".." in cp_token:
            start, end = parse_codepoint_range(cp_token)
            for cp in range(start, end + 1):
                sequences.add(chr(cp))
        else:
            sequences.add("".join(chr(int(hx, 16)) for hx in cp_token.split()))
    return frozenset(sequences)


def parse_gemoji_shortcodes(raw_json: str) -> frozenset[str]:
    """Extract all Gemoji shortcode aliases as lowercase strings."""
    entries = json.loads(raw_json)
    shortcodes: set[str] = set()
    for entry in entries:
        for alias in entry.get("aliases", []):
            if isinstance(alias, str) and alias:
                shortcodes.add(alias.lower())
    return frozenset(shortcodes)


def _format_ranges(ranges: tuple[tuple[int, int], ...], indent: str = "    ") -> str:
    lines = [f"{indent}(0x{start:04X}, 0x{end:04X})," for start, end in ranges]
    return "(\n" + "\n".join(lines) + "\n)"


def _format_int_set(values: frozenset[int], indent: str = "    ") -> str:
    sorted_vals = sorted(values)
    chunks = [
        indent + ", ".join(f"0x{cp:04X}" for cp in sorted_vals[i : i + 10]) + ","
        for i in range(0, len(sorted_vals), 10)
    ]
    return "frozenset({\n" + "\n".join(chunks) + "\n})"


def _format_str_set(values: frozenset[str], indent: str = "    ", escape_unicode: bool = True) -> str:
    sorted_vals = sorted(values)
    if escape_unicode:
        items = ['"' + "".join(f"\\U{ord(ch):08X}" if ord(ch) > 0xFFFF else f"\\u{ord(ch):04X}" for ch in s) + '"' for s in sorted_vals]
        per_line = 4
    else:
        items = [repr(s) for s in sorted_vals]
        per_line = 8
    chunks = [
        indent + ", ".join(items[i : i + per_line]) + ","
        for i in range(0, len(items), per_line)
    ]
    return "frozenset({\n" + "\n".join(chunks) + "\n})"


def render_module(
    unicode_version: str,
    generated_at: str,
    prop_ranges: dict[str, tuple[tuple[int, int], ...]],
    vs15_bases: frozenset[int],
    vs16_bases: frozenset[int],
    rgi_sequences: frozenset[str],
    component_sequences: frozenset[str],
    shortcodes: frozenset[str],
) -> str:
    """Render the generated Python data module."""
    return f'''"""Auto-generated Unicode & Gemoji detection tables.

Generated by _generate_emoji_data.py. Do not edit manually.
Sources:
  - Unicode Emoji & UCD Data (Version {unicode_version})
  - GitHub gemoji (https://github.com/github/gemoji)
"""

from __future__ import annotations

UNICODE_VERSION = {unicode_version!r}
GENERATED_AT = {generated_at!r}
RGI_SEQUENCE_COUNT = {len(rgi_sequences)}
GEMOJI_SHORTCODE_COUNT = {len(shortcodes)}

EMOJI_RANGES: tuple[tuple[int, int], ...] = {_format_ranges(prop_ranges["Emoji"])}

EMOJI_PRESENTATION_RANGES: tuple[tuple[int, int], ...] = {_format_ranges(prop_ranges["Emoji_Presentation"])}

EMOJI_MODIFIER_RANGES: tuple[tuple[int, int], ...] = {_format_ranges(prop_ranges["Emoji_Modifier"])}

EMOJI_MODIFIER_BASE_RANGES: tuple[tuple[int, int], ...] = {_format_ranges(prop_ranges["Emoji_Modifier_Base"])}

EMOJI_COMPONENT_RANGES: tuple[tuple[int, int], ...] = {_format_ranges(prop_ranges["Emoji_Component"])}

EXTENDED_PICTOGRAPHIC_RANGES: tuple[tuple[int, int], ...] = {_format_ranges(prop_ranges["Extended_Pictographic"])}

VS15_TEXT_BASES: frozenset[int] = {_format_int_set(vs15_bases)}

VS16_EMOJI_BASES: frozenset[int] = {_format_int_set(vs16_bases)}

RGI_SEQUENCES: frozenset[str] = {_format_str_set(rgi_sequences, escape_unicode=True)}

EMOJI_COMPONENT_SEQUENCES: frozenset[str] = {_format_str_set(component_sequences, escape_unicode=True)}

GEMOJI_SHORTCODES: frozenset[str] = {_format_str_set(shortcodes, escape_unicode=False)}
'''


def read_bundled_metadata(output_path: Path) -> tuple[str | None, int | None]:
    """Read UNICODE_VERSION and GEMOJI_SHORTCODE_COUNT from existing emoji_data.py."""
    if not output_path.exists():
        return None, None
    content = output_path.read_text(encoding="utf-8")
    ver_match = re.search(r'^UNICODE_VERSION\s*=\s*[\'"]([^\'"]+)[\'"]', content, re.MULTILINE)
    cnt_match = re.search(r"^GEMOJI_SHORTCODE_COUNT\s*=\s*(\d+)", content, re.MULTILINE)
    ver = ver_match.group(1) if ver_match else None
    cnt = int(cnt_match.group(1)) if cnt_match else None
    return ver, cnt


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Fetch official Unicode and Gemoji datasets and generate emoji_data.py."
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=DEFAULT_OUTPUT_PATH,
        help="Destination Python module path (default: scripts/emoji_data.py)",
    )
    parser.add_argument(
        "--check-only",
        action="store_true",
        help="Check whether upstream Unicode version or Gemoji count differs from bundled data without writing.",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    _configure_stdio()
    args = parse_args(argv)

    try:
        raw_texts = {name: fetch_text(url) for name, url in UNICODE_URLS.items()}
        gemoji_raw = fetch_text(GEMOJI_URL)
    except (urllib.error.URLError, TimeoutError, OSError) as exc:
        print(f"FAILURE: Failed to fetch upstream data: {exc}", file=sys.stderr)
        return 2

    versions = {name: extract_version(text, name) for name, text in raw_texts.items()}
    unique_versions = set(versions.values())
    if len(unique_versions) != 1:
        print(f"FAILURE: Version mismatch across Unicode files: {versions}", file=sys.stderr)
        return 2
    unicode_version = next(iter(unique_versions))

    prop_ranges = parse_emoji_data(raw_texts["emoji_data"])
    vs15_bases, vs16_bases = parse_variation_sequences(raw_texts["emoji_variation_sequences"])
    rgi_from_test, component_seqs = parse_emoji_test(raw_texts["emoji_test"])
    seq_from_seq = parse_extra_sequences(raw_texts["emoji_sequences"])
    seq_from_zwj = parse_extra_sequences(raw_texts["emoji_zwj_sequences"])
    # Combine all RGI sequences across emoji-test.txt, emoji-sequences.txt, and emoji-zwj-sequences.txt
    rgi_sequences = frozenset(rgi_from_test | seq_from_seq | seq_from_zwj)
    shortcodes = parse_gemoji_shortcodes(gemoji_raw)

    if args.check_only:
        bundled_ver, bundled_cnt = read_bundled_metadata(args.output)
        print(
            f"Bundled: version={bundled_ver}, shortcodes={bundled_cnt} | "
            f"Upstream: version={unicode_version}, shortcodes={len(shortcodes)}, rgi_sequences={len(rgi_sequences)}"
        )
        if bundled_ver != unicode_version or bundled_cnt != len(shortcodes):
            print("UPDATE_AVAILABLE: Upstream data differs from bundled data.")
            return 1
        print("UP_TO_DATE: Bundled data matches upstream.")
        return 0

    generated_at = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    module_source = render_module(
        unicode_version=unicode_version,
        generated_at=generated_at,
        prop_ranges=prop_ranges,
        vs15_bases=vs15_bases,
        vs16_bases=vs16_bases,
        rgi_sequences=rgi_sequences,
        component_sequences=component_seqs,
        shortcodes=shortcodes,
    )
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(module_source, encoding="utf-8", newline="\n")
    print(
        f"SUCCESS: Generated {args.output} "
        f"(Unicode {unicode_version}, RGI sequences={len(rgi_sequences)}, "
        f"Extended_Pictographic ranges={len(prop_ranges['Extended_Pictographic'])}, "
        f"Gemoji shortcodes={len(shortcodes)})"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
