#!/usr/bin/env python3
"""Zero-dependency emoji and Markdown shortcode detector for doc-refine.

Detects unintended Unicode emoji (UTS #51 / UAX #29) and known Gemoji Markdown
shortcodes while excluding code blocks, inline code spans, URLs, timestamps,
IPv6 addresses, Windows paths, and VS15 text-presentation symbols.

Requires Python 3.10+ standard library only. Never modifies target files.
"""

from __future__ import annotations

import argparse
from bisect import bisect_right
from dataclasses import asdict, dataclass
import ipaddress
import json
from pathlib import Path
import re
import sys
from typing import Iterable

SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

import emoji_data  # noqa: E402

VS15 = "\uFE0E"
VS16 = "\uFE0F"
ZWJ = "\u200D"
KEYCAP_MARK = "\u20E3"
CANCEL_TAG = "\U000E007F"
BLACK_FLAG = "\U0001F3F4"
REGIONAL_START = 0x1F1E6
REGIONAL_END = 0x1F1FF
TAG_START = 0xE0020
TAG_END = 0xE007E
KEYCAP_BASES = frozenset("#*0123456789")
MARKDOWN_EXTENSIONS = frozenset({".md", ".markdown", ".mdx", ".mkd", ".mdown"})

SHORTCODE_CANDIDATE_RE = re.compile(r"(?<![\w:/\\]):([A-Za-z0-9_+-]+):(?=(?::skin-tone-[2-6]:)?(?![\w:]))")
FENCE_OPEN_RE = re.compile(r"^[ ]{0,3}(?:>[ ]*){0,3}(`{3,}|~{3,})(.*)$")
HTML_COMMENT_RE = re.compile(r"<!--.*?-->", re.DOTALL)
HTML_RAW_BLOCK_RE = re.compile(
    r"<(pre|code|script|style)(?:\s[^>]*)?>.*?</\1\s*>",
    re.IGNORECASE | re.DOTALL,
)
REF_DEF_RE = re.compile(r"^[ ]{0,3}\[[^\]]+\]:[ \t]*\S.*$", re.MULTILINE)
AUTOLINK_RE = re.compile(r"<(?:https?://|mailto:)[^\s>]+>", re.IGNORECASE)
BARE_URL_RE = re.compile(r"https?://[^\s<>()\[\]\"'`]+(?:\([^\s()]*\)[^\s<>()\[\]\"'`]*)*", re.IGNORECASE)
INLINE_LINK_DEST_RE = re.compile(r"\[(?:\\.|[^\[\]])*\](\((?:\\.|[^()\n])*\))")
HTML_TAG_RE = re.compile(r"</?[A-Za-z][A-Za-z0-9-]*(?:\s+[^>\n]*)?>")
YAML_FRONTMATTER_RE = re.compile(r"\A(?:---\n.*?\n---|\+\+\+\n.*?\n\+\+\+)(?:\n|\Z)", re.DOTALL)
SKIN_TONE_SUFFIX_RE = re.compile(r"^:skin-tone-[2-6]:")
IPV6_CANDIDATE_RE = re.compile(r"[0-9A-Fa-f:]+(?:/\d+)?")


@dataclass(frozen=True)
class Detection:
    """Single detected emoji or shortcode occurrence."""

    file: str
    line: int
    column: int
    end_column: int
    match: str
    category: str
    tier: str
    codepoints: str


def _configure_stdio() -> None:
    """Ensure UTF-8 output on Windows consoles to avoid cp932 encoding errors."""
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8", errors="replace")


def _in_ranges(cp: int, ranges: tuple[tuple[int, int], ...]) -> bool:
    """Binary-search check whether codepoint falls inside sorted inclusive ranges."""
    lo = 0
    hi = len(ranges) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        start, end = ranges[mid]
        if cp < start:
            hi = mid - 1
        elif cp > end:
            lo = mid + 1
        else:
            return True
    return False


def _build_trie(sequences: Iterable[str]) -> dict:
    """Build a character prefix trie for longest-match RGI emoji lookup."""
    root: dict = {}
    for seq in sequences:
        node = root
        for ch in seq:
            node = node.setdefault(ch, {})
        node[""] = True
    return root


RGI_TRIE = _build_trie(emoji_data.RGI_SEQUENCES)


def _match_rgi_trie(text: str, start: int) -> int | None:
    """Return end index of the longest RGI sequence starting at `start`, or None."""
    node = RGI_TRIE
    last_end: int | None = None
    idx = start
    length = len(text)
    while idx < length:
        ch = text[idx]
        if ch not in node:
            break
        node = node[ch]
        idx += 1
        if "" in node:
            last_end = idx
    return last_end


def _is_regional(cp: int) -> bool:
    return REGIONAL_START <= cp <= REGIONAL_END


def _is_emoji_modifier(cp: int) -> bool:
    return _in_ranges(cp, emoji_data.EMOJI_MODIFIER_RANGES)


def _is_ep_or_emoji(cp: int) -> bool:
    return _in_ranges(cp, emoji_data.EXTENDED_PICTOGRAPHIC_RANGES) or _in_ranges(
        cp, emoji_data.EMOJI_RANGES
    )


def _consume_zwj_element(text: str, pos: int) -> int | None:
    """Consume one UTS #51 zwj_element starting at `pos`."""
    length = len(text)
    if pos >= length:
        return None
    cp = ord(text[pos])
    if _is_regional(cp):
        if pos + 1 < length and _is_regional(ord(text[pos + 1])):
            return pos + 2
        return None
    if not _is_ep_or_emoji(cp):
        return None
    end = pos + 1
    if end < length:
        nxt = text[end]
        nxt_cp = ord(nxt)
        if _is_emoji_modifier(nxt_cp):
            end += 1
        elif nxt == VS16:
            end += 1
            if end < length and text[end] == KEYCAP_MARK:
                end += 1
        elif nxt == VS15:
            end += 1
        elif nxt == KEYCAP_MARK and text[pos] in KEYCAP_BASES:
            end += 1
    return end


def _match_structural(text: str, start: int) -> tuple[int, str] | None:
    """Match structural emoji candidates (UTS #51 possible_emoji / tags / RI / keycaps)."""
    length = len(text)
    ch = text[start]
    cp = ord(ch)

    # 1. Subdivision tag sequence: Black Flag + tag chars + CANCEL TAG
    if ch == BLACK_FLAG and start + 1 < length and TAG_START <= ord(text[start + 1]) <= TAG_END:
        idx = start + 1
        while idx < length and TAG_START <= ord(text[idx]) <= TAG_END:
            idx += 1
        if idx < length and text[idx] == CANCEL_TAG:
            return idx + 1, "tag_sequence"

    # 2. Keycap sequence: [#*0-9] + optional VS16 + U+20E3
    if ch in KEYCAP_BASES:
        idx = start + 1
        if idx < length and text[idx] == VS16:
            idx += 1
        if idx < length and text[idx] == KEYCAP_MARK:
            return idx + 1, "keycap"
        return None

    # 3. Regional Indicator pair or singleton
    if _is_regional(cp):
        if start + 1 < length and _is_regional(ord(text[start + 1])):
            return start + 2, "regional_pair"
        return start + 1, "regional_singleton"

    # 4. Orphan tag character
    if TAG_START <= cp <= TAG_END or cp == ord(CANCEL_TAG):
        return start + 1, "orphan_tag"

    # 5. Possible emoji / ZWJ sequence
    elem_end = _consume_zwj_element(text, start)
    if elem_end is None:
        return None
    end = elem_end
    while end + 1 < length and text[end] == ZWJ:
        next_end = _consume_zwj_element(text, end + 1)
        if next_end is None:
            break
        end = next_end
    return end, "possible_emoji"


def _mask_span_preserve_newlines(chars: list[str], start: int, end: int) -> None:
    """Replace characters in [start, end) with spaces while keeping newlines intact."""
    for idx in range(start, end):
        if chars[idx] != "\n":
            chars[idx] = " "


def _mask_fenced_blocks(chars: list[str], text: str) -> None:
    """Mask CommonMark-style fenced code blocks (``` or ~~~)."""
    lines = text.splitlines(keepends=True)
    offset = 0
    in_fence = False
    fence_char = ""
    fence_len = 0

    for line in lines:
        line_end = offset + len(line)
        stripped_nl = line.rstrip("\n")
        if not in_fence:
            match = FENCE_OPEN_RE.match(stripped_nl)
            if match:
                fence_token, info = match.group(1), match.group(2)
                if not (fence_token[0] == "`" and "`" in info):
                    in_fence = True
                    fence_char = fence_token[0]
                    fence_len = len(fence_token)
                    _mask_span_preserve_newlines(chars, offset, line_end)
        else:
            _mask_span_preserve_newlines(chars, offset, line_end)
            close_match = re.match(
                rf"^[ ]{{0,3}}(?:>[ ]*){{0,3}}{re.escape(fence_char)}{{{fence_len},}}[ \t]*$",
                stripped_nl,
            )
            if close_match:
                in_fence = False
                fence_char = ""
                fence_len = 0
        offset = line_end


def _mask_indented_blocks(chars: list[str], text: str) -> None:
    """Conservatively mask indented code blocks preceded by a blank line."""
    lines = text.splitlines(keepends=True)
    offset = 0
    prev_blank_or_code = True
    list_marker_re = re.compile(r"^[ ]{4,}(?:[-+*]|\d{1,9}[.)])\s")

    for line in lines:
        line_end = offset + len(line)
        current_slice = "".join(chars[offset:line_end])
        stripped = current_slice.rstrip("\n")
        is_blank = stripped.strip() == ""
        is_indented = (current_slice.startswith("    ") or current_slice.startswith("\t")) and not is_blank
        if is_indented and prev_blank_or_code and not list_marker_re.match(stripped):
            _mask_span_preserve_newlines(chars, offset, line_end)
            prev_blank_or_code = True
        else:
            prev_blank_or_code = is_blank
        offset = line_end


def _mask_inline_code_spans(chars: list[str], text: str) -> None:
    """Mask inline code spans respecting matching backtick run lengths (CommonMark 6.1)."""
    idx = 0
    length = len(chars)
    while idx < length:
        if chars[idx] != "`":
            idx += 1
            continue
        run_start = idx
        while idx < length and chars[idx] == "`":
            idx += 1
        tick_len = idx - run_start
        search_pos = idx
        closed = False
        while search_pos < length:
            if chars[search_pos] == "\n" and search_pos + 1 < length and chars[search_pos + 1] == "\n":
                break
            if chars[search_pos] == "`":
                close_start = search_pos
                while search_pos < length and chars[search_pos] == "`":
                    search_pos += 1
                if search_pos - close_start == tick_len:
                    _mask_span_preserve_newlines(chars, run_start, search_pos)
                    idx = search_pos
                    closed = True
                    break
            else:
                search_pos += 1
        if not closed:
            # Unclosed backtick string is literal text per CommonMark
            pass


def _mask_regex_matches(chars: list[str], pattern: re.Pattern[str], group: int = 0) -> None:
    """Apply a regex against the current masked buffer and space-mask matched groups."""
    snapshot = "".join(chars)
    for match in pattern.finditer(snapshot):
        start, end = match.span(group)
        _mask_span_preserve_newlines(chars, start, end)


def mask_markdown(text: str, mask_indented_code: bool = True) -> tuple[str, str]:
    """Return (unicode_scan_text, shortcode_scan_text) with non-prose spans space-masked."""
    chars = list(text)
    _mask_fenced_blocks(chars, text)
    if mask_indented_code:
        _mask_indented_blocks(chars, text)
    _mask_regex_matches(chars, HTML_COMMENT_RE)
    _mask_regex_matches(chars, HTML_RAW_BLOCK_RE)
    _mask_inline_code_spans(chars, text)
    _mask_regex_matches(chars, REF_DEF_RE)
    _mask_regex_matches(chars, AUTOLINK_RE)
    _mask_regex_matches(chars, INLINE_LINK_DEST_RE, group=1)
    _mask_regex_matches(chars, BARE_URL_RE)
    _mask_regex_matches(chars, HTML_TAG_RE)

    unicode_text = "".join(chars)
    fm_match = YAML_FRONTMATTER_RE.match(unicode_text)
    if fm_match:
        fm_chars = list(chars)
        _mask_span_preserve_newlines(fm_chars, fm_match.start(), fm_match.end())
        shortcode_text = "".join(fm_chars)
    else:
        shortcode_text = unicode_text
    return unicode_text, shortcode_text


def _build_line_starts(text: str) -> list[int]:
    starts = [0]
    for idx, ch in enumerate(text):
        if ch == "\n":
            starts.append(idx + 1)
    return starts


def _offset_to_line_col(line_starts: list[int], offset: int) -> tuple[int, int]:
    line_idx = bisect_right(line_starts, offset) - 1
    return line_idx + 1, (offset - line_starts[line_idx]) + 1


def _format_codepoints(span: str) -> str:
    return " ".join(f"U+{ord(ch):04X}" for ch in span)


def _should_report_unicode(span: str, is_rgi: bool, struct_kind: str | None, strict: bool) -> tuple[bool, str, str]:
    """Decide whether a candidate Unicode span should be reported and classify it."""
    if span.endswith(VS15):
        return False, "", ""

    if len(span) == 1:
        cp = ord(span)
        if span in KEYCAP_BASES:
            return False, "", ""
        if struct_kind in ("regional_singleton", "orphan_tag"):
            return True, "non_rgi_candidate", "structural"
        if _in_ranges(cp, emoji_data.EMOJI_PRESENTATION_RANGES):
            return True, "unicode_emoji", "strict"
        if span in emoji_data.EMOJI_COMPONENT_SEQUENCES:
            return strict, "unicode_emoji", "strict"
        if _in_ranges(cp, emoji_data.EMOJI_RANGES):
            # Text-default Emoji (e.g., ©, ®, ™, ↔, ✔, ❤, ⚠) without VS16
            if strict and cp >= 0x0080 and cp not in (0x00A9, 0x00AE, 0x2122):
                return True, "unicode_emoji", "strict"
            return False, "", ""
        if _in_ranges(cp, emoji_data.EXTENDED_PICTOGRAPHIC_RANGES):
            # Unassigned future emoji block character
            return True, "non_rgi_candidate", "structural"
        return False, "", ""

    if is_rgi:
        return True, "unicode_emoji", "strict"
    return True, "non_rgi_candidate", "structural"


def _scan_unicode_emojis(
    text: str,
    file_label: str,
    line_starts: list[int],
    strict: bool,
    strict_only: bool,
) -> list[Detection]:
    detections: list[Detection] = []
    idx = 0
    length = len(text)

    while idx < length:
        rgi_end = _match_rgi_trie(text, idx)
        struct_res = None if strict_only else _match_structural(text, idx)

        if rgi_end is None and struct_res is None:
            idx += 1
            continue

        struct_end, struct_kind = struct_res if struct_res is not None else (0, None)
        if rgi_end is not None and rgi_end >= struct_end:
            end = rgi_end
            is_rgi = True
        else:
            end = struct_end
            is_rgi = False

        span = text[idx:end]
        # Disqualify single character or sequence immediately followed by VS15
        if end < length and text[end] == VS15:
            idx = end + 1
            continue

        report, category, tier = _should_report_unicode(span, is_rgi, struct_kind, strict)
        if report:
            line, col = _offset_to_line_col(line_starts, idx)
            detections.append(
                Detection(
                    file=file_label,
                    line=line,
                    column=col,
                    end_column=col + len(span),
                    match=span,
                    category=category,
                    tier=tier,
                    codepoints=_format_codepoints(span),
                )
            )
        idx = end

    return detections


def _is_inside_ipv6_token(text: str, start: int, end: int) -> bool:
    """Return True if [start, end) is embedded inside a valid IPv6 address literal."""
    left = start
    while left > 0 and not text[left - 1].isspace() and text[left - 1] not in "[](){}<>,\"'":
        left -= 1
    right = end
    while right < len(text) and not text[right].isspace() and text[right] not in "[](){}<>,\"'":
        right += 1
    token = text[left:right]
    if "%" in token:
        token = token.split("%", 1)[0]
    if "/" in token:
        token = token.split("/", 1)[0]
    try:
        ipaddress.IPv6Address(token)
        return True
    except ValueError:
        return False


def _scan_shortcodes(text: str, file_label: str, line_starts: list[int]) -> list[Detection]:
    detections: list[Detection] = []
    idx = 0
    for match in SHORTCODE_CANDIDATE_RE.finditer(text):
        start, end = match.span()
        if start < idx:
            continue
        name = match.group(1).lower()
        if name not in emoji_data.GEMOJI_SHORTCODES:
            continue
        if _is_inside_ipv6_token(text, start, end):
            continue
        skin_match = SKIN_TONE_SUFFIX_RE.match(text[end:])
        if skin_match:
            end += skin_match.end()
        span = text[start:end]
        line, col = _offset_to_line_col(line_starts, start)
        detections.append(
            Detection(
                file=file_label,
                line=line,
                column=col,
                end_column=col + len(span),
                match=span,
                category="emoji_shortcode",
                tier="gemoji",
                codepoints="",
            )
        )
        idx = end
    return detections


def detect_text(
    text: str,
    *,
    file_label: str = "<input>",
    markdown: bool = True,
    strict: bool = False,
    strict_only: bool = False,
    mask_indented_code: bool = True,
) -> list[Detection]:
    """Detect Unicode emoji and known Markdown shortcodes in `text`."""
    normalized = text.replace("\r\n", "\n").replace("\r", "\n")
    line_starts = _build_line_starts(normalized)
    if markdown:
        unicode_text, shortcode_text = mask_markdown(normalized, mask_indented_code=mask_indented_code)
    else:
        unicode_text = normalized
        shortcode_text = normalized

    results = _scan_unicode_emojis(unicode_text, file_label, line_starts, strict=strict, strict_only=strict_only)
    if markdown:
        results.extend(_scan_shortcodes(shortcode_text, file_label, line_starts))
    results.sort(key=lambda d: (d.line, d.column, d.category))
    return results


def _iter_target_files(paths: list[Path]) -> list[Path]:
    files: list[Path] = []
    for path in paths:
        if path.is_file():
            files.append(path)
        elif path.is_dir():
            for child in sorted(path.rglob("*")):
                if child.is_file():
                    files.append(child)
        else:
            raise FileNotFoundError(f"Path not found: {path}")
    return files


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Detect Unicode emoji and Markdown emoji shortcodes without modifying files."
    )
    parser.add_argument("paths", nargs="*", type=Path, help="Files or directories to inspect.")
    md_group = parser.add_mutually_exclusive_group()
    md_group.add_argument("--markdown", action="store_true", help="Force Markdown masking and shortcode check.")
    md_group.add_argument("--no-markdown", action="store_true", help="Disable Markdown masking and shortcode check.")
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Also report non-ASCII text-default Emoji symbols (e.g. U+2764, U+26A0) without VS16.",
    )
    parser.add_argument(
        "--strict-only",
        action="store_true",
        help="Disable structural/future-block fallback tier and match bundled RGI/Emoji_Presentation only.",
    )
    parser.add_argument(
        "--no-indented-code-mask",
        action="store_true",
        help="Do not mask 4-space indented code blocks in Markdown mode.",
    )
    parser.add_argument("--json", action="store_true", help="Output findings as JSON.")
    parser.add_argument("--version", action="store_true", help="Show bundled Unicode version metadata and exit.")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    _configure_stdio()
    args = parse_args(argv)

    if args.version:
        print(
            f"detect_emoji.py (Unicode {emoji_data.UNICODE_VERSION}, "
            f"RGI={emoji_data.RGI_SEQUENCE_COUNT}, "
            f"Gemoji={emoji_data.GEMOJI_SHORTCODE_COUNT}, "
            f"generated={emoji_data.GENERATED_AT})"
        )
        return 0

    if not args.paths:
        print("FAILURE: At least one file or directory path is required (or pass --version).", file=sys.stderr)
        return 2

    try:
        target_files = _iter_target_files(args.paths)
    except FileNotFoundError as exc:
        print(f"FAILURE: {exc}", file=sys.stderr)
        return 2

    all_findings: list[Detection] = []
    for file_path in target_files:
        try:
            content = file_path.read_text(encoding="utf-8-sig")
        except (OSError, UnicodeDecodeError) as exc:
            print(f"FAILURE: Could not read {file_path}: {exc}", file=sys.stderr)
            return 2

        use_markdown = (
            True
            if args.markdown
            else False
            if args.no_markdown
            else file_path.suffix.lower() in MARKDOWN_EXTENSIONS
        )
        findings = detect_text(
            content,
            file_label=str(file_path),
            markdown=use_markdown,
            strict=args.strict,
            strict_only=args.strict_only,
            mask_indented_code=not args.no_indented_code_mask,
        )
        all_findings.extend(findings)

    if args.json:
        payload = {
            "unicode_version": emoji_data.UNICODE_VERSION,
            "count": len(all_findings),
            "findings": [asdict(item) for item in all_findings],
        }
        print(json.dumps(payload, ensure_ascii=False, indent=2))
    else:
        for item in all_findings:
            cp_info = f" [{item.codepoints}]" if item.codepoints else ""
            print(
                f"{item.file}:{item.line}:{item.column}: "
                f"{item.category}({item.tier}) {item.match}{cp_info}"
            )
        print(f"SUMMARY: {len(all_findings)} finding(s) across {len(target_files)} file(s).")

    return 1 if all_findings else 0


if __name__ == "__main__":
    sys.exit(main())
