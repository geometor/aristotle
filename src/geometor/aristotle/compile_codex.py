"""Primary source parser and Multi-Track Book Codex RST compiler for ``geometor-aristotle``."""

from __future__ import annotations

import re
import unicodedata
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Any

from geometor.aristotle.apparatus import (
    render_bibliography_rst,
    render_glossary_rst,
    render_persons_rst,
    write_apparatus_jsons,
)
from geometor.aristotle.commentary import UNIT_COMMENTARIES
from geometor.aristotle.concordance import build_concordance
from geometor.aristotle.units import CODEX_UNITS, ChapterSpec, UnitSpec


def _escape_rst_inline(text: str) -> str:
    """Escape stray RST inline characters in plain primary source text while preserving prose."""
    cleaned = text.replace("\\", "\\\\")
    cleaned = cleaned.replace("*", "\\*").replace("`", "\\`")
    cleaned = re.sub(r"(?<!\w)_|_(?!\w)", r"\_", cleaned)
    # Prevent accidental RST section underline if a line is pure punctuation
    cleaned = re.sub(r"\s+", " ", cleaned).strip()
    if re.match(r"^[-=~^\"'+*#]{3,}$", cleaned):
        return ""
    return cleaned


def _split_long_greek_paragraph(text: str, target_len: int = 820) -> list[str]:
    """Split an overly long single-block XML Greek chapter into balanced paragraphs at major stops."""
    text = re.sub(r"\s+", " ", text).strip()
    if len(text) <= target_len * 1.35:
        return [text] if text else []

    # Split after Greek period or ano teleia when followed by space
    sentences = re.split(r"(?<=[.·;])\s+", text)
    paragraphs: list[str] = []
    buf: list[str] = []
    cur_len = 0
    for sent in sentences:
        if not sent:
            continue
        buf.append(sent)
        cur_len += len(sent) + 1
        if cur_len >= target_len and sent.endswith((".", ";")):
            paragraphs.append(" ".join(buf))
            buf = []
            cur_len = 0
    if buf:
        if paragraphs and cur_len < 220:
            paragraphs[-1] = f"{paragraphs[-1]} {' '.join(buf)}"
        else:
            paragraphs.append(" ".join(buf))
    return paragraphs


def _serialize_xml_paragraph(elem: ET.Element, include_bekker_milestones: bool = False) -> str:
    """Extract clean NFC Unicode Greek text from a TEI ``<p>`` element."""
    chunks: list[str] = []

    def _walk(node: ET.Element) -> None:
        local = node.tag.split("}")[-1] if "}" in node.tag else node.tag
        if local == "milestone" and include_bekker_milestones:
            if node.get("resp") == "Bekker" and node.get("unit") == "page" and node.get("n"):
                chunks.append(f" [{node.get('n')}] ")
        elif local == "lb":
            chunks.append(" ")
        if node.text:
            chunks.append(node.text)
        for child in node:
            _walk(child)
            if child.tail:
                chunks.append(child.tail)

    _walk(elem)
    joined = unicodedata.normalize("NFC", "".join(chunks))
    return re.sub(r"\s+", " ", joined).strip()


def extract_greek_chapter(repo_root: Path, ch: ChapterSpec) -> list[str]:
    """Extract verbatim polytonic Greek paragraphs for ``ch`` from ``resources/aristotle/sources/el``.

    Args:
        repo_root: Root path of ``geometor/aristotle``.
        ch: Target ``ChapterSpec``.

    Returns:
        Non-empty list of verbatim Greek paragraphs.

    Raises:
        ValueError: If the requested chapter cannot be located or is empty.
    """
    el_dir = repo_root / "resources/aristotle/sources/el"

    if ch.work_id in {"physica", "de-caelo"}:
        fname = (
            f"physica_book{ch.book}_bekker1831.txt"
            if ch.work_id == "physica"
            else f"de_caelo_book{ch.book}_bekker1831.txt"
        )
        raw = (el_dir / fname).read_text(encoding="utf-8")
        pattern = re.compile(
            rf"^Κεφάλαιο\s+{ch.chapter}\b\s*\n-+\s*\n(.*?)(?=^Κεφάλαιο\s+\d+\b|\Z)",
            re.M | re.S,
        )
        m = pattern.search(raw)
        if not m:
            raise ValueError(f"Greek chapter not found: {ch.work_id} {ch.book}.{ch.chapter}")
        blocks = [
            re.sub(r"\s+", " ", blk).strip()
            for blk in re.split(r"\n\s*\n", m.group(1).strip())
            if blk.strip()
        ]
        if not blocks:
            raise ValueError(f"Empty Greek chapter: {ch.work_id} {ch.book}.{ch.chapter}")
        return blocks

    xml_map = {
        "categoriae": "tlg0086.tlg006.bekker1837.xml",
        "anal-prior": "tlg0086.tlg001.bekker1837.xml",
        "anal-post": "tlg0086.tlg001.bekker1837.xml",
        "topica": "tlg0086.tlg044.bekker1837.xml",
        "de-anima": "tlg0086.tlg002.bekker1837.xml",
        "metaphysica": "tlg0086.tlg025.ross1924.xml",
    }
    xml_path = el_dir / xml_map[ch.work_id]
    root = ET.parse(xml_path).getroot()
    ns = root.tag.split("}")[0] + "}" if root.tag.startswith("{") else ""

    target_div: ET.Element | None = None
    if ch.work_id == "categoriae":
        target_div = root.find(f".//{ns}div[@subtype='chapter'][@n='{ch.chapter}']")
    elif ch.work_id in {"anal-prior", "anal-post"}:
        bk_name = "priora" if ch.work_id == "anal-prior" else "posteriora"
        bk_div = root.find(f".//{ns}div[@subtype='book'][@n='{bk_name}']")
        if bk_div is not None:
            pt_div = bk_div.find(f".//{ns}div[@subtype='part'][@n='{ch.book}']")
            if pt_div is not None:
                target_div = pt_div.find(f".//{ns}div[@subtype='chapter'][@n='{ch.chapter}']")
    elif ch.work_id in {"topica", "de-anima"}:
        bk_div = root.find(f".//{ns}div[@subtype='book'][@n='{ch.book}']")
        if bk_div is not None:
            target_div = bk_div.find(f".//{ns}div[@subtype='chapter'][@n='{ch.chapter}']")
    elif ch.work_id == "metaphysica":
        bk_div = root.find(f".//{ns}div[@subtype='book'][@n='{ch.book}']")
        if bk_div is not None:
            target_div = bk_div.find(f".//{ns}div[@subtype='section'][@n='{ch.chapter}']")

    if target_div is None:
        raise ValueError(f"Greek XML div not found for {ch.work_id} {ch.book}.{ch.chapter}")

    paragraphs: list[str] = []
    inc_milestones = ch.work_id == "metaphysica"
    for p_elem in target_div.findall(f".//{ns}p"):
        p_txt = _serialize_xml_paragraph(p_elem, include_bekker_milestones=inc_milestones)
        if p_txt:
            paragraphs.extend(_split_long_greek_paragraph(p_txt))

    if not paragraphs:
        raise ValueError(f"No Greek paragraphs extracted for {ch.work_id} {ch.book}.{ch.chapter}")
    return paragraphs


_ROMAN_NUMERALS: dict[int, str] = {
    1: "I",
    2: "II",
    3: "III",
    4: "IV",
    5: "V",
    6: "VI",
    7: "VII",
    8: "VIII",
    9: "IX",
    10: "X",
    11: "XI",
    12: "XII",
    13: "XIII",
    14: "XIV",
}


def extract_english_chapter(repo_root: Path, ch: ChapterSpec) -> list[str]:
    """Extract verbatim Oxford English paragraphs for ``ch`` from ``resources/aristotle/sources/en``.

    Args:
        repo_root: Root path of ``geometor/aristotle``.
        ch: Target ``ChapterSpec``.

    Returns:
        Non-empty list of verbatim English paragraphs.

    Raises:
        ValueError: If the requested chapter cannot be located or is empty.
    """
    en_dir = repo_root / "resources/aristotle/sources/en"
    en_map = {
        "anal-post": "posterior_analytics_mure.txt",
        "categoriae": "categories_edghill.txt",
        "anal-prior": "prior_analytics_jenkinson.txt",
        "topica": "topics_pickard_cambridge.txt",
        "physica": "physics_hardie_gaye.txt",
        "de-caelo": "on_the_heavens_stocks.txt",
        "de-anima": "on_the_soul_smith.txt",
        "metaphysica": "metaphysics_ross.txt",
    }
    raw = (en_dir / en_map[ch.work_id]).read_text(encoding="utf-8")

    book_slice = raw
    if ch.book is not None:
        rom = _ROMAN_NUMERALS[ch.book]
        bk_pat = re.compile(
            rf"^BOOK\s+{rom}\b[^\n]*\n(.*?)(?=^BOOK\s+[IVX]+\b|\Z)",
            re.M | re.S,
        )
        m_bk = bk_pat.search(raw)
        if not m_bk:
            raise ValueError(f"English BOOK {rom} not found in {en_map[ch.work_id]}")
        book_slice = m_bk.group(1)

    part_pat = re.compile(
        rf"^Part\s+{ch.chapter}\b[^\n]*\n(.*?)(?=^(?:Part\s+\d+|SECTION\s+\d+|BOOK\s+[IVX]+)\b|\Z)",
        re.M | re.S,
    )
    m_pt = part_pat.search(book_slice)
    if not m_pt:
        raise ValueError(f"English Part {ch.chapter} not found for {ch.work_id} {ch.book}")

    paragraphs: list[str] = []
    for raw_blk in re.split(r"\n\s*\n", m_pt.group(1).strip()):
        blk = re.sub(r"\s+", " ", raw_blk).strip()
        if not blk or set(blk) == {"-"} or blk == "THE END":
            continue
        paragraphs.append(blk)

    if not paragraphs:
        raise ValueError(f"Empty English chapter for {ch.work_id} {ch.book}.{ch.chapter}")
    return paragraphs


def _collect_chapter_anchors(
    concordance_entries: list[dict[str, Any]],
    unit_slug: str,
) -> dict[tuple[str, int | None, int], dict[str, list[str]]]:
    """Group specific concordance ``codex_anchor`` IDs by ``(work_id, book, chapter)`` and column."""
    mapping: dict[tuple[str, int | None, int], dict[str, list[str]]] = {}
    for entry in concordance_entries:
        if not entry.get("in_codex") or entry.get("codex_unit") != unit_slug:
            continue
        anchor = str(entry.get("codex_anchor") or "")
        col_id = str(entry.get("bekker_column_id") or "")
        wk = str(entry.get("work_id") or "")
        bk = entry.get("book")
        ch_num = entry.get("chapter")
        if not anchor or not col_id:
            continue
        # Match to a specific chapter in the unit
        unit_obj = next(u for u in CODEX_UNITS if u.slug == unit_slug)
        matched_ch: ChapterSpec | None = None
        for ch_spec in unit_obj.chapters:
            if ch_spec.work_id == wk and ch_spec.book == bk and ch_spec.chapter == ch_num:
                matched_ch = ch_spec
                break
        if matched_ch is None:
            for ch_spec in unit_obj.chapters:
                if ch_spec.work_id == wk and col_id in ch_spec.bekker_cols:
                    matched_ch = ch_spec
                    break
        if matched_ch is None:
            matched_ch = unit_obj.chapters[0]
        key = (matched_ch.work_id, matched_ch.book, matched_ch.chapter)
        col_map = mapping.setdefault(key, {})
        anc_list = col_map.setdefault(col_id, [])
        if anchor not in anc_list:
            anc_list.append(anchor)
    return mapping


def _render_unit_en_rst(
    repo_root: Path,
    unit: UnitSpec,
    chapter_anchors: dict[tuple[str, int | None, int], dict[str, list[str]]],
    emitted_anchors: set[str],
) -> str:
    """Render the primary English track (``<slug>-en.rst``) for a Codex unit."""
    bar = "=" * len(unit.title_en)
    lines: list[str] = [
        f":order: {unit.order}",
        ":layout: book",
        f":title: {unit.short_title}",
        f":canonical_id: {unit.canonical_id}",
        f":original_id: {unit.bekker_range}",
        f":folio: {unit.bekker_range.replace('Bekker ', '')}",
        "",
        f".. _{unit.slug}:",
        f".. _{unit.slug}-en:",
        "",
        bar,
        unit.title_en,
        bar,
        "",
        f".. rubric:: {unit.liber_title} · {unit.bekker_range}",
        "",
        ".. epigraph::",
        "",
        f"   *«{unit.epigraph_el}»*",
        "",
        f"   “{unit.epigraph_en}” — **{unit.epigraph_locus}**",
        "",
    ]

    for idx, ch in enumerate(unit.chapters, start=1):
        ch_loc = f"{ch.book_label}.{ch.chapter}" if ch.book_label else f"Ch. {ch.chapter}"
        sec_title = f"{ch.work_title_en} {ch_loc} — {ch.theme_en} ({ch.bekker_range})"
        sec_bar = "-" * len(sec_title)
        ch_anchor = f"{unit.slug}-en-c{idx}"
        lines.extend(
            [
                f".. _{ch_anchor}:",
                "",
                sec_title,
                sec_bar,
                "",
                f"*Oxford Translation by {ch.translator} · Bekker {ch.bekker_range}*",
                "",
            ]
        )

        paragraphs = extract_english_chapter(repo_root, ch)
        cols = list(ch.bekker_cols)
        col_anchors = chapter_anchors.get((ch.work_id, ch.book, ch.chapter), {})

        # Map each Bekker column to its proportional paragraph index
        col_schedule: dict[int, list[str]] = {}
        for c_idx, col_id in enumerate(cols):
            p_idx = min(len(paragraphs) - 1, (c_idx * len(paragraphs)) // max(1, len(cols)))
            col_schedule.setdefault(p_idx, []).append(col_id)

        for p_idx, para in enumerate(paragraphs):
            for col_id in col_schedule.get(p_idx, []):
                base_anc = f"bekker-{col_id}"
                if base_anc not in emitted_anchors:
                    lines.append(f".. _{base_anc}:")
                    emitted_anchors.add(base_anc)
                for extra_anc in col_anchors.get(col_id, []):
                    if extra_anc not in emitted_anchors:
                        lines.append(f".. _{extra_anc}:")
                        emitted_anchors.add(extra_anc)
                lines.append("")
                lines.append(f".. folio:: Bekker {col_id}")
                lines.append("")

            esc_para = _escape_rst_inline(para)
            if esc_para:
                lines.append(esc_para)
                lines.append("")

        # Emit any remaining concordance anchors for this chapter whose column wasn't in ch.bekker_cols
        for _cid, anc_list in col_anchors.items():
            for extra_anc in anc_list:
                if extra_anc not in emitted_anchors:
                    lines.append(f".. _{extra_anc}:")
                    lines.append("")
                    emitted_anchors.add(extra_anc)

    return "\n".join(lines).rstrip() + "\n"


def _render_unit_el_rst(repo_root: Path, unit: UnitSpec) -> str:
    """Render the synchronized Bekker Greek track (``<slug>-el.rst``) for a Codex unit."""
    bar = "=" * len(unit.title_el)
    lines: list[str] = [
        ":layout: book",
        ":type: el",
        f":title: {unit.short_title} — Greek (Bekker)",
        f":canonical_id: {unit.canonical_id}",
        f":original_id: {unit.bekker_range}",
        f":folio: {unit.bekker_range.replace('Bekker ', '')}",
        "",
        f".. _{unit.slug}-el:",
        "",
        bar,
        unit.title_el,
        bar,
        "",
        f".. rubric:: Editio Graeca Bekkeriana (1831/1837; *Metaph.* rec. W. D. Ross 1924) · {unit.bekker_range}",
        "",
    ]

    emitted_el: set[str] = set()
    for idx, ch in enumerate(unit.chapters, start=1):
        ch_loc = f"{ch.book_label}.{ch.chapter}" if ch.book_label else f"Κεφ. {ch.chapter}"
        sec_title = f"{ch.work_title_el} {ch_loc} ({ch.bekker_range})"
        sec_bar = "-" * len(sec_title)
        lines.extend(
            [
                f".. _{unit.slug}-el-c{idx}:",
                "",
                sec_title,
                sec_bar,
                "",
            ]
        )

        paragraphs = extract_greek_chapter(repo_root, ch)
        cols = list(ch.bekker_cols)
        col_schedule: dict[int, list[str]] = {}
        for c_idx, col_id in enumerate(cols):
            p_idx = min(len(paragraphs) - 1, (c_idx * len(paragraphs)) // max(1, len(cols)))
            col_schedule.setdefault(p_idx, []).append(col_id)

        for p_idx, para in enumerate(paragraphs):
            for col_id in col_schedule.get(p_idx, []):
                el_anc = f"bekker-el-{col_id}"
                if el_anc not in emitted_el:
                    lines.append(f".. _{el_anc}:")
                    lines.append("")
                    emitted_el.add(el_anc)
                lines.append(f".. folio:: Bekker {col_id}")
                lines.append("")

            esc_para = _escape_rst_inline(para)
            if esc_para:
                lines.append(esc_para)
                lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def _render_unit_summary_rst(
    unit: UnitSpec,
    concordance_entries: list[dict[str, Any]],
) -> str:
    """Render the structural synopsis track (``<slug>-summary.rst``) for a Codex unit."""
    comm = UNIT_COMMENTARIES[unit.slug]
    title = f"{unit.title_en} — Structural Synopsis"
    bar = "=" * len(title)
    unit_entries = [
        e for e in concordance_entries if e.get("in_codex") and e.get("codex_unit") == unit.slug
    ]

    lines: list[str] = [
        ":layout: book",
        ":type: summary",
        f":title: {unit.short_title} — Summary",
        f":canonical_id: {unit.canonical_id}",
        f":original_id: {unit.bekker_range}",
        f":folio: {unit.bekker_range.replace('Bekker ', '')}",
        "",
        f".. _{unit.slug}-summary:",
        "",
        bar,
        title,
        bar,
        "",
        f".. rubric:: Argumentative Architecture & Bekker Conspectus ({unit.bekker_range})",
        "",
        "Architectural Thesis",
        "--------------------",
        "",
        comm.thesis,
        "",
        "Logical & Noetic Progression",
        "----------------------------",
        "",
    ]

    for step_head, step_body in comm.argument_steps:
        lines.extend(
            [
                f"**{step_head}**",
                "",
                f"{step_body}",
                "",
            ]
        )

    lines.extend(
        [
            "Chapter & Bekker Span Conspectus",
            "--------------------------------",
            "",
            ".. list-table::",
            "   :header-rows: 1",
            "   :widths: 24 18 40 18",
            "",
            "   * - Treatise & Chapter",
            "     - Bekker Span",
            "     - Thematic Scope",
            "     - Tracks",
        ]
    )

    for idx, ch in enumerate(unit.chapters, start=1):
        ch_loc = f"{ch.book_label}.{ch.chapter}" if ch.book_label else f"Ch. {ch.chapter}"
        lines.extend(
            [
                f"   * - *{ch.work_title_la}* {ch_loc}",
                f"     - ``{ch.bekker_range}``",
                f"     - {ch.theme_en}",
                f"     - :ref:`EN <{unit.slug}-en-c{idx}>` · :ref:`EL <{unit.slug}-el-c{idx}>`",
            ]
        )

    lines.append("")
    lines.extend(
        [
            "Reception Snapshot in the GEOMETOR Canon",
            "----------------------------------------",
            "",
            f"This unit encompasses **{len(unit_entries)} distinct Bekker loci** cited across ``geometor/euclid``, ``geometor/hoenen``, and ``geometor/pacioli``. See the companion :doc:`Critical Notes & Dual Commentary <{unit.slug}-notes>` and the master :doc:`Bekker Concordance </loci_geometrici/concordance>` for full folio and page back-references.",
            "",
        ]
    )
    return "\n".join(lines).rstrip() + "\n"


def _render_unit_notes_rst(
    unit: UnitSpec,
    concordance_entries: list[dict[str, Any]],
) -> str:
    """Render the dual-tradition critical commentary track (``<slug>-notes.rst``)."""
    comm = UNIT_COMMENTARIES[unit.slug]
    title = f"{unit.title_en} — Critical Commentary & Notes"
    bar = "=" * len(title)
    unit_entries = [
        e for e in concordance_entries if e.get("in_codex") and e.get("codex_unit") == unit.slug
    ]

    lines: list[str] = [
        ":layout: book",
        ":type: notes",
        f":title: {unit.short_title} — Notes",
        f":canonical_id: {unit.canonical_id}",
        f":original_id: {unit.bekker_range}",
        f":folio: {unit.bekker_range.replace('Bekker ', '')}",
        "",
        f".. _{unit.slug}-notes:",
        "",
        bar,
        title,
        bar,
        "",
        f".. rubric:: Historical-Mathematical (Heath) & Scholastic-Noetic (Hoenen) Apparatus · {unit.bekker_range}",
        "",
        "I. Mathematical-Historical Commentary (*Secundum Heath & Euclidem*)",
        "-------------------------------------------------------------------",
        "",
    ]

    for para in comm.heath_analysis:
        lines.append(para)
        lines.append("")

    lines.extend(
        [
            "II. Scholastic-Noetic Commentary (*Secundum Hoenen, Thomam & Paciolum*)",
            "-----------------------------------------------------------------------",
            "",
        ]
    )
    for para in comm.hoenen_analysis:
        lines.append(para)
        lines.append("")

    lines.extend(
        [
            "III. Locus-by-Locus Philological & Geometrical Notes",
            "----------------------------------------------------",
            "",
        ]
    )
    for crux_head, crux_body in comm.crux_notes:
        lines.extend(
            [
                f"**{crux_head}**",
                "",
                f"{crux_body}",
                "",
            ]
        )

    lines.extend(
        [
            "IV. Sister-Corpus Citations Indexed in This Unit",
            "------------------------------------------------",
            "",
        ]
    )
    if not unit_entries:
        lines.append("No external sister-corpus citations fall directly within this span.")
        lines.append("")
    else:
        lines.extend(
            [
                ".. list-table::",
                "   :header-rows: 1",
                "   :widths: 16 22 18 44",
                "",
                "   * - Bekker Locus",
                "     - Treatise & Chapter",
                "     - Sister Repos",
                "     - Cited Locations (Volume, Page / Folio & Display)",
            ]
        )
        for entry in unit_entries:
            anc = entry["codex_anchor"]
            b_disp = entry["bekker_display"]
            w_disp = f"*{entry['work_la']}* {entry['chapter_display']}".strip()
            repos_str = ", ".join(f"``{r}``" for r in entry["repos"])
            occ_summaries: list[str] = []
            for occ in entry["occurrences"][:4]:
                loc_parts = [p for p in (occ["volume"], occ["book"], f"p. {occ['page']}" if occ["page"] else "") if p]
                loc_str = ", ".join(loc_parts)
                occ_summaries.append(f"**{occ['repo']}** ({loc_str}): ``{occ['display']}``")
            if len(entry["occurrences"]) > 4:
                occ_summaries.append(f"(+{len(entry['occurrences']) - 4} more)")
            occ_cell = "; ".join(occ_summaries)
            lines.extend(
                [
                    f"   * - :ref:`{b_disp} <{anc}>`",
                    f"     - {w_disp}",
                    f"     - {repos_str}",
                    f"     - {occ_cell}",
                ]
            )
        lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def render_concordance_rst(concordance_payload: dict[str, Any]) -> str:
    """Render ``docsrc/loci_geometrici/concordance.rst`` from ``concordance.json``."""
    summary = concordance_payload["summary"]
    entries: list[dict[str, Any]] = concordance_payload["entries"]

    lines: list[str] = [
        ":order: 90",
        ":layout: book",
        ":type: apparatus",
        ":title: Bekker Concordance Across GEOMETOR",
        "",
        ".. _concordance:",
        "",
        "======================================",
        "Bekker Concordance Across GEOMETOR",
        "======================================",
        "",
        ".. rubric:: Master Cross-Corpus Register Linking *Euclid*, *Hoenen*, and *Pacioli* to Bekker (1831)",
        "",
        f"This concordance indexes **{summary['distinct_bekker_loci']} distinct Aristotelian Bekker loci** "
        f"(representing **{summary['total_sister_occurrences']} textual citation occurrences**) mined directly from "
        f"the three sister historical codices of the GEOMETOR canon:",
        "",
        f"- **geometor/euclid** (:cite:`Heath, Thirteen Books of Euclid's Elements <heath:euclid:1926>`): "
        f"**{summary['source_keys_by_repo']['euclid']}** Aristotle citation keys across Volumes I–III.",
        f"- **geometor/hoenen** (:cite:`Hoenen, De Noetica Geometriae <hoenen:noetica:1952>`): "
        f"**{summary['source_keys_by_repo']['hoenen']}** Aristotle citation keys across Capita I–VII & Appendix.",
        f"- **geometor/pacioli** (:cite:`Pacioli, De Divina Proportione <pacioli:divina:1509>`): "
        f"**{summary['source_keys_by_repo']['pacioli']}** Aristotle citation & folio entries across the 1509 *Compendio* and *Architectura*.",
        "",
        f"Of the {summary['distinct_bekker_loci']} distinct Bekker loci cited across the sister repositories, "
        f"**{summary['loci_in_codex']} foundational geometric and noetic loci** fall directly within the fifty-four "
        "full chapters edited in Libri I–V of *Loci Geometrici et Noetici* and link directly to their exact Bekker "
        "passage in this Codex.",
        "",
    ]

    # Group entries by treatise in canonical Bekker order
    grouped: dict[str, list[dict[str, Any]]] = {}
    work_titles: dict[str, str] = {}
    for entry in entries:
        wid = entry["work_id"]
        grouped.setdefault(wid, []).append(entry)
        work_titles[wid] = f"{entry['work_la']} ({entry['work_en']})"

    for wid, w_entries in grouped.items():
        sec_head = work_titles[wid]
        lines.extend(
            [
                f".. _concordance-{wid}:",
                "",
                sec_head,
                "-" * len(sec_head),
                "",
                ".. list-table::",
                "   :header-rows: 1",
                "   :widths: 14 12 24 50",
                "",
                "   * - Bekker",
                "     - Chapter",
                "     - Codex Unit",
                "     - GEOMETOR Sister Occurrences",
            ]
        )
        for entry in w_entries:
            b_disp = entry["bekker_display"]
            ch_disp = entry["chapter_display"] or "—"
            if entry["in_codex"] and entry["codex_anchor"]:
                b_cell = f":ref:`{b_disp} <{entry['codex_anchor']}>`"
                u_cell = f":doc:`{entry['codex_unit']} </loci_geometrici/{entry['codex_unit']}/{entry['codex_unit']}-en>`"
            else:
                b_cell = f"``{b_disp}``"
                u_cell = "*External corpus locus*"

            occ_items: list[str] = []
            for occ in entry["occurrences"][:5]:
                meta_bits = [
                    b
                    for b in (
                        occ["volume"],
                        occ["book"],
                        f"p. {occ['page']}" if occ["page"] else "",
                        f"fol. {occ['folio']}" if occ["folio"] and not occ["page"] else "",
                    )
                    if b
                ]
                meta_str = ", ".join(meta_bits)
                occ_items.append(f"**{occ['repo']}** ({meta_str}): ``{occ['display']}``")
            if len(entry["occurrences"]) > 5:
                occ_items.append(f"(+{len(entry['occurrences']) - 5} additional occurrences)")
            occ_cell = "; ".join(occ_items)

            lines.extend(
                [
                    f"   * - {b_cell}",
                    f"     - {ch_disp}",
                    f"     - {u_cell}",
                    f"     - {occ_cell}",
                ]
            )
        lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def render_codex_index_rst(concordance_payload: dict[str, Any]) -> str:
    """Render the Book Codex root ``docsrc/loci_geometrici/index.rst``."""
    summary = concordance_payload["summary"]
    lines: list[str] = [
        ":order: 1",
        ":layout: book",
        ":book_title: Loci Geometrici et Noetici",
        ":book_subtitle: Aristotle (384–322 BC) · Bekker Greek (1831) & Oxford English Codex",
        ":author: Aristotle of Stagira",
        ":book_theme: classical-serif",
        "",
        ".. _loci-geometrici:",
        "",
        "======================================================================",
        "Loci Geometrici et Noetici — Aristotle on Geometry, Episteme & Nous",
        "======================================================================",
        "",
        ".. rubric:: Synchronized Multi-Track Book Codex (English · Greek Bekker · Summary · Critical Notes)",
        "",
        "**Loci Geometrici et Noetici** gathers into a single critical edition the fifty-four foundational chapters across eight treatises of :person:`Aristotle <aristotle>` (*Categories*, *Prior Analytics*, *Posterior Analytics*, *Topics*, *Physics*, *De Caelo*, *De Anima*, and *Metaphysics*) that govern the deductive architecture of Euclidean geometry, continuous vs. discrete quantity, potential infinity, imaginative construction (:term:`phantasma <phantasma>`), and formal abstraction in :term:`intelligible matter <hyle-noete>`.",
        "",
        f"Every unit is presented across **four synchronized tracks**—**English** (public-domain Oxford Clarendon translations), **Greek (Bekker)** (verbatim Prussian Academy 1831/1837 & Ross 1924 polytonic Greek), **Summary**, and **Critical Notes** synthesizing :person:`Sir Thomas Heath's <heath>` mathematical-historical reconstructions with :person:`Fr. Peter Hoenen S.J.'s <hoenen>` and :person:`St. Thomas Aquinas's <thomas-aquinas>` scholastic-noetic analysis—indexed to **{summary['distinct_bekker_loci']} Bekker loci** across ``geometor/euclid``, ``geometor/hoenen``, and ``geometor/pacioli``.",
        "",
    ]

    # Group units by Liber
    libri_groups: list[tuple[str, str, list[UnitSpec]]] = []
    for unit in CODEX_UNITS:
        if not libri_groups or libri_groups[-1][0] != unit.liber_num:
            libri_groups.append((unit.liber_num, unit.liber_title, [unit]))
        else:
            libri_groups[-1][2].append(unit)

    for lib_num, lib_title, u_list in libri_groups:
        lines.extend(
            [
                lib_title,
                "-" * len(lib_title),
                "",
                ".. toctree::",
                "   :maxdepth: 1",
                f"   :caption: Liber {lib_num}",
                "",
            ]
        )
        for u in u_list:
            lines.append(f"   {u.slug}/{u.slug}-en")
        lines.append("")

    lines.extend(
        [
            "Critical Apparatus & Bekker Concordance",
            "---------------------------------------",
            "",
            ".. toctree::",
            "   :maxdepth: 1",
            "   :caption: Critical Apparatus",
            "",
            "   concordance",
            "   bibliography",
            "   persons",
            "   glossary",
            "",
            ".. toctree::",
            "   :hidden:",
            "",
        ]
    )
    for u in CODEX_UNITS:
        lines.append(f"   {u.slug}/{u.slug}-el")
        lines.append(f"   {u.slug}/{u.slug}-summary")
        lines.append(f"   {u.slug}/{u.slug}-notes")
    lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def compile_codex(repo_root: Path, workspace_root: Path | None = None) -> dict[str, Any]:
    """Build concordance, apparatus JSONs, and all Book Codex RST files under ``docsrc/loci_geometrici``.

    Args:
        repo_root: Root directory of ``geometor/aristotle``.
        workspace_root: Optional parent ``geometor`` workspace directory.

    Returns:
        Summary dictionary reporting generated unit, chapter, anchor, and concordance counts.
    """
    concordance_payload = build_concordance(repo_root, workspace_root=workspace_root)
    write_apparatus_jsons(repo_root)

    codex_dir = repo_root / "docsrc" / "loci_geometrici"
    codex_dir.mkdir(parents=True, exist_ok=True)

    entries = concordance_payload["entries"]
    emitted_anchors: set[str] = set()
    total_chapters = 0

    for unit in CODEX_UNITS:
        unit_dir = codex_dir / unit.slug
        unit_dir.mkdir(parents=True, exist_ok=True)
        ch_anchors = _collect_chapter_anchors(entries, unit.slug)

        en_rst = _render_unit_en_rst(repo_root, unit, ch_anchors, emitted_anchors)
        el_rst = _render_unit_el_rst(repo_root, unit)
        sum_rst = _render_unit_summary_rst(unit, entries)
        notes_rst = _render_unit_notes_rst(unit, entries)

        (unit_dir / f"{unit.slug}-en.rst").write_text(en_rst, encoding="utf-8")
        (unit_dir / f"{unit.slug}-el.rst").write_text(el_rst, encoding="utf-8")
        (unit_dir / f"{unit.slug}-summary.rst").write_text(sum_rst, encoding="utf-8")
        (unit_dir / f"{unit.slug}-notes.rst").write_text(notes_rst, encoding="utf-8")
        total_chapters += len(unit.chapters)

    (codex_dir / "index.rst").write_text(
        render_codex_index_rst(concordance_payload),
        encoding="utf-8",
    )
    (codex_dir / "concordance.rst").write_text(
        render_concordance_rst(concordance_payload),
        encoding="utf-8",
    )
    (codex_dir / "glossary.rst").write_text(render_glossary_rst(), encoding="utf-8")
    (codex_dir / "persons.rst").write_text(render_persons_rst(), encoding="utf-8")
    (codex_dir / "bibliography.rst").write_text(render_bibliography_rst(), encoding="utf-8")

    return {
        "units_compiled": len(CODEX_UNITS),
        "chapters_compiled": total_chapters,
        "bekker_anchors_emitted": len(emitted_anchors),
        "distinct_concordance_loci": concordance_payload["summary"]["distinct_bekker_loci"],
        "codex_concordance_loci": concordance_payload["summary"]["loci_in_codex"],
    }
