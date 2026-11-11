"""Bekker coordinate parser and cross-corpus Aristotle concordance builder.

Scans ``geometor/euclid``, ``geometor/hoenen``, and ``geometor/pacioli`` (when present
in the sibling workspace) to construct a unified Bekker concordance linking every cited
Aristotelian passage back to exact sister-project volumes, pages, folios, chapters, and
display strings, as well as forward to the corresponding unit and Bekker anchor in
*Loci Geometrici et Noetici*.
"""

from __future__ import annotations

import json
import re
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Any

from geometor.aristotle.units import CODEX_UNITS, ChapterSpec, UnitSpec

ROMAN_TO_INT: dict[str, int] = {
    "I": 1,
    "II": 2,
    "III": 3,
    "IV": 4,
    "V": 5,
    "VI": 6,
    "VII": 7,
    "VIII": 8,
    "IX": 9,
    "X": 10,
    "XI": 11,
    "XII": 12,
    "XIII": 13,
    "XIV": 14,
}

WORK_CANONICAL: dict[str, tuple[str, str, str, int, int]] = {
    "categoriae": ("categoriae", "Categoriae", "Categories", 1, 15),
    "cat": ("categoriae", "Categoriae", "Categories", 1, 15),
    "periherm": ("perihermeneias", "De Interpretatione", "On Interpretation", 16, 24),
    "perihermeneias": ("perihermeneias", "De Interpretatione", "On Interpretation", 16, 24),
    "anal-prior": ("anal-prior", "Analytica Priora", "Prior Analytics", 24, 70),
    "anal-post": ("anal-post", "Analytica Posteriora", "Posterior Analytics", 71, 100),
    "topics": ("topica", "Topica", "Topics", 100, 164),
    "topica": ("topica", "Topica", "Topics", 100, 164),
    "soph-el": ("soph-el", "Sophistici Elenchi", "Sophistical Refutations", 164, 184),
    "phys": ("physica", "Physica", "Physics", 184, 267),
    "physica": ("physica", "Physica", "Physics", 184, 267),
    "de-caelo": ("de-caelo", "De Caelo", "On the Heavens", 268, 313),
    "meteorologica": ("meteorologica", "Meteorologica", "Meteorology", 338, 390),
    "de-anima": ("de-anima", "De Anima", "On the Soul", 402, 435),
    "met": ("metaphysica", "Metaphysica", "Metaphysics", 980, 1093),
    "metaphysica": ("metaphysica", "Metaphysica", "Metaphysics", 980, 1093),
    "eth-nic": ("eth-nic", "Ethica Nicomachea", "Nicomachean Ethics", 1094, 1181),
}

# Explicit Bekker fallback coordinates for general/chapter-only citations outside bekker_index
FALLBACK_CHAPTER_BEKKER: dict[tuple[str, int | None, int | None], tuple[int, str, str]] = {
    ("perihermeneias", 1, None): (16, "a", "16a1–16a18"),
    ("perihermeneias", None, 1): (16, "a", "16a1–16a18"),
    ("anal-post", None, None): (71, "a", "71a1–100b17"),
    ("physica", None, None): (184, "a", "184a10–267b26"),
    ("physica", 3, None): (200, "b", "200b12–208a23"),
    ("physica", 5, None): (224, "a", "224a21–231a20"),
    ("de-caelo", 3, 8): (306, "b", "306b3–307b18"),
    ("metaphysica", 2, None): (993, "a", "993a30–995a20"),
    ("eth-nic", 5, 6): (1134, "a", "1134a16–1135a15"),
}


@dataclass(frozen=True, slots=True, order=True)
class BekkerRef:
    """Normalized, sortable Bekker reference coordinate.

    Attributes:
        page: Bekker page number (`1`–`1462` across the Prussian Academy edition).
        col: Column designator (``"a"`` or ``"b"``).
        line: Starting line number (`1`–`49`), or ``0`` when only column/chapter is cited.
        end_col: Ending column when a range spans columns, or empty string.
        end_line: Ending line number when a range is specified, or ``0``.
    """

    page: int
    col: str
    line: int = 0
    end_col: str = ""
    end_line: int = 0

    @property
    def column_id(self) -> str:
        """Return the Bekker half-page column identifier (e.g. ``"71a"``)."""
        return f"{self.page}{self.col}"

    @property
    def canonical_id(self) -> str:
        """Return compact canonical anchor token (e.g. ``"77b30"`` or ``"71a"``)."""
        if self.line > 0:
            return f"{self.page}{self.col}{self.line}"
        return f"{self.page}{self.col}"

    @property
    def display(self) -> str:
        """Return human-readable Bekker citation string (e.g. ``"72a14–24"``)."""
        if self.line <= 0:
            return f"{self.page}{self.col}"
        base = f"{self.page}{self.col}{self.line}"
        if self.end_line > 0:
            if self.end_col and self.end_col != self.col:
                return f"{base}–{self.end_col}{self.end_line}"
            return f"{base}–{self.end_line}"
        return base


@dataclass(slots=True)
class SisterOccurrence:
    """Single citation occurrence in one of the GEOMETOR sister repositories.

    Attributes:
        repo: Sister repository name (``"euclid"``, ``"hoenen"``, or ``"pacioli"``).
        cite_key: Original citation key in the sister repository.
        volume: Volume or edition identifier.
        book: Book/Caput/Part label within the sister work.
        section: Section or document path in the sister work.
        page: Printed page or recto/verso folio label.
        folio: Scan folio number if recorded.
        display: Verbatim citation string displayed in the sister text.
    """

    repo: str
    cite_key: str
    volume: str
    book: str
    section: str
    page: str
    folio: str
    display: str


@dataclass(slots=True)
class ConcordanceEntry:
    """Aggregated concordance record for a distinct Aristotelian Bekker locus.

    Attributes:
        locus_id: Unique canonical identifier (e.g. ``"anal-post:77b30"``).
        bekker: Normalized ``BekkerRef`` sort/display object.
        bekker_display: Human-readable Bekker span (e.g. ``"77b30"``).
        work_id: Canonical treatise slug (e.g. ``"anal-post"``).
        work_la: Latin treatise title.
        work_en: English treatise title.
        book: Book number if resolved, else ``None``.
        chapter: Chapter number if resolved, else ``None``.
        chapter_display: Formatted book.chapter label (e.g. ``"I.12"``).
        in_codex: Whether this locus is included in the primary text of *Loci Geometrici*.
        codex_unit: Target unit directory/file slug if ``in_codex`` is ``True``.
        codex_unit_title: Short title of the Codex unit if ``in_codex`` is ``True``.
        codex_anchor: Sphinx anchor label (e.g. ``"bekker-77b30"``) inside ``-en.rst``.
        repos: Sorted list of sister repositories citing this locus.
        occurrences: Deduplicated list of ``SisterOccurrence`` records.
    """

    locus_id: str
    bekker: BekkerRef
    bekker_display: str
    work_id: str
    work_la: str
    work_en: str
    book: int | None
    chapter: int | None
    chapter_display: str
    in_codex: bool
    codex_unit: str
    codex_unit_title: str
    codex_anchor: str
    repos: list[str] = field(default_factory=list)
    occurrences: list[SisterOccurrence] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        """Serialize entry to a JSON-compatible dictionary."""
        return {
            "locus_id": self.locus_id,
            "bekker_page": self.bekker.page,
            "bekker_col": self.bekker.col,
            "bekker_line": self.bekker.line,
            "bekker_end_col": self.bekker.end_col,
            "bekker_end_line": self.bekker.end_line,
            "bekker_column_id": self.bekker.column_id,
            "bekker_canonical": self.bekker.canonical_id,
            "bekker_display": self.bekker_display,
            "work_id": self.work_id,
            "work_la": self.work_la,
            "work_en": self.work_en,
            "book": self.book,
            "chapter": self.chapter,
            "chapter_display": self.chapter_display,
            "in_codex": self.in_codex,
            "codex_unit": self.codex_unit,
            "codex_unit_title": self.codex_unit_title,
            "codex_anchor": self.codex_anchor,
            "repos": sorted(set(self.repos)),
            "occurrence_count": len(self.occurrences),
            "occurrences": [asdict(o) for o in self.occurrences],
        }


_BEKKER_RE = re.compile(
    r"(?<![0-9A-Za-z])(\d{1,4})[\s._-]*([ab])(?![A-Za-z])"
    r"(?:[\s._:-]*(\d{1,3})(?![0-9]))?"
    r"(?:\s*(?:[-–—]+)\s*(?:([ab])[\s._-]*)?(\d{1,2})(?![0-9A-Za-z]))?",
)


def parse_bekker_locus(
    text: str,
    page_range: tuple[int, int] = (1, 1500),
) -> BekkerRef | None:
    """Extract a canonical ``BekkerRef`` from a raw locus or display string.

    Args:
        text: Raw locus token or citation display string (e.g. ``"I.2.72a14-24"``,
            ``"i-10-76-b-9"``, ``"Metaph. 1051 a 24"``, ``"1014a35-b5"``).
        page_range: Inclusive ``(min_page, max_page)`` bounds used to disambiguate
            treatise page numbers from book/chapter numbers.

    Returns:
        Parsed ``BekkerRef`` if a valid Bekker coordinate within ``page_range`` is
        found, otherwise ``None``.
    """
    lo, hi = page_range
    for match in _BEKKER_RE.finditer(text):
        page = int(match.group(1))
        if not (lo <= page <= hi):
            continue
        col = match.group(2).lower()
        line = int(match.group(3)) if match.group(3) else 0
        if line > 50:
            # Handle OCR typo like "431 a. 140" -> line 14
            line = int(str(line)[:2])
        end_col = (match.group(4) or "").lower()
        end_line = int(match.group(5)) if match.group(5) else 0
        if end_line > 50:
            end_line = 0
        return BekkerRef(
            page=page,
            col=col,
            line=line,
            end_col=end_col,
            end_line=end_line,
        )
    return None


def _parse_book_chapter(locus: str, display_samples: list[str]) -> tuple[int | None, int | None]:
    """Extract ``(book, chapter)`` integers from a locus string or display samples."""
    combined = f"{locus} | " + " | ".join(display_samples)

    # Pattern 1: b4-c11 or b1-c4
    m_bc = re.search(r"\bb(\d+)-c(\d+)\b", locus, re.I)
    if m_bc:
        return int(m_bc.group(1)), int(m_bc.group(2))

    # Pattern 2: Roman numeral + arabic chapter in locus or display, e.g. I.12, VI.4, I, 4, IX 9
    m_rom_ch = re.search(
        r"(?<![A-Za-z])(XIV|XIII|XII|XI|IX|VIII|VII|VI|IV|III|II|I|X|V)"
        r"(?:[\s.,_:-]+(?:cap\.?\s*|c\.?\s*)?(\d{1,2}))?\b",
        combined,
        re.I,
    )
    if m_rom_ch:
        rom = m_rom_ch.group(1).upper()
        if rom in ROMAN_TO_INT:
            bk = ROMAN_TO_INT[rom]
            ch = int(m_rom_ch.group(2)) if m_rom_ch.group(2) else None
            # Guard against matching Bekker page as chapter (e.g. "Met. IX 1051 a 32")
            if ch is not None and ch > 46:
                ch = None
            return bk, ch

    # Pattern 3: Arabic book.chapter at start of locus (e.g. "1.12:77b30", "2.19", "4.1", "1.1")
    m_num = re.match(r"^(\d{1,2})(?:[.:-](\d{1,2}))?(?:$|[.:-])", locus.strip())
    if m_num:
        b_val = int(m_num.group(1))
        c_val = int(m_num.group(2)) if m_num.group(2) else None
        if b_val <= 14 and (c_val is None or c_val <= 46):
            return b_val, c_val

    return None, None


def _int_to_roman(num: int) -> str:
    """Convert an integer `1..14` to its standard Roman numeral."""
    for rom, val in ROMAN_TO_INT.items():
        if val == num:
            return rom
    return str(num)


def _lookup_bekker_from_index(
    bekker_index: dict[str, dict[str, list[str]]],
    work_id: str,
    book: int | None,
    chapter: int | None,
) -> BekkerRef | None:
    """Resolve a chapter-only citation to its starting ``BekkerRef`` via ``bekker_index.json``."""
    fb = FALLBACK_CHAPTER_BEKKER.get((work_id, book, chapter))
    if fb is not None:
        return BekkerRef(page=fb[0], col=fb[1], line=0)

    idx_work_map = {
        "anal-prior": ("analytica", "1"),
        "anal-post": ("analytica", "2"),
        "categoriae": ("categoriae", ""),
        "topica": ("topica", ""),
        "physica": ("physica", ""),
        "de-caelo": ("de_caelo", ""),
        "de-anima": ("de_anima", ""),
        "metaphysica": ("metaphysica", ""),
    }
    if work_id not in idx_work_map:
        return None
    idx_key, prefix = idx_work_map[work_id]
    table = bekker_index.get(idx_key, {})

    candidates: list[str] = []
    if prefix:
        if book is not None and chapter is not None:
            candidates.append(f"{prefix}.{book}.{chapter}")
        elif book is not None:
            candidates.append(f"{prefix}.{book}.1")
    else:
        if book is not None and chapter is not None:
            candidates.append(f"{book}.{chapter}")
        elif chapter is not None:
            candidates.append(str(chapter))
        elif book is not None:
            candidates.append(f"{book}.1")

    for ck in candidates:
        cols = table.get(ck)
        if cols:
            first_col = cols[0]
            m = re.match(r"^(\d+)([ab])$", first_col)
            if m:
                return BekkerRef(page=int(m.group(1)), col=m.group(2), line=0)
    return None


def _infer_chapter_from_bekker(
    bekker_index: dict[str, dict[str, list[str]]],
    work_id: str,
    bekker: BekkerRef,
) -> tuple[int | None, int | None]:
    """Infer ``(book, chapter)`` from a ``BekkerRef`` when not explicitly stated in citation."""
    idx_work_map = {
        "anal-prior": ("analytica", "1."),
        "anal-post": ("analytica", "2."),
        "categoriae": ("categoriae", ""),
        "topica": ("topica", ""),
        "physica": ("physica", ""),
        "de-caelo": ("de_caelo", ""),
        "de-anima": ("de_anima", ""),
        "metaphysica": ("metaphysica", ""),
    }
    if work_id not in idx_work_map:
        return None, None
    idx_key, prefix = idx_work_map[work_id]
    table = bekker_index.get(idx_key, {})
    col_id = bekker.column_id
    for ch_key, cols in table.items():
        if prefix and not ch_key.startswith(prefix):
            continue
        if col_id in cols:
            rem = ch_key[len(prefix) :] if prefix else ch_key
            parts = rem.split(".")
            if len(parts) == 2:
                return int(parts[0]), int(parts[1])
            if len(parts) == 1 and parts[0].isdigit():
                return None, int(parts[0])
    return None, None


def _parse_bekker_span_bounds(bekker_range: str) -> tuple[tuple[int, str, int], tuple[int, str, int]] | None:
    """Parse a ChapterSpec ``bekker_range`` string like ``'71a1–71b8'`` into numeric bounds."""
    m = re.match(r"^(\d+)([ab])(\d+)?\s*[–-]\s*(?:(\d+))?([ab])(\d+)?$", bekker_range.strip())
    if not m:
        return None
    p1 = int(m.group(1))
    c1 = m.group(2)
    l1 = int(m.group(3)) if m.group(3) else 1
    p2 = int(m.group(4)) if m.group(4) else p1
    c2 = m.group(5)
    l2 = int(m.group(6)) if m.group(6) else 99
    return ((p1, c1, l1), (p2, c2, l2))


def match_codex_unit(
    work_id: str,
    book: int | None,
    chapter: int | None,
    bekker: BekkerRef,
) -> tuple[UnitSpec, ChapterSpec] | None:
    """Match a resolved Aristotelian citation to its ``(UnitSpec, ChapterSpec)`` in the Codex.

    Args:
        work_id: Canonical work identifier.
        book: Book number or ``None``.
        chapter: Chapter number or ``None``.
        bekker: Normalized ``BekkerRef`` coordinate.

    Returns:
        Matching ``(UnitSpec, ChapterSpec)`` if the locus is covered by Libri I–V,
        otherwise ``None``.
    """
    # Exact (work_id, book, chapter) match first
    if chapter is not None:
        for unit in CODEX_UNITS:
            for ch in unit.chapters:
                if ch.work_id == work_id and ch.book == book and ch.chapter == chapter:
                    return unit, ch

    # Fallback: check Bekker line bounds across chapters of the same treatise
    pt = (bekker.page, bekker.col, bekker.line if bekker.line > 0 else 20)
    for unit in CODEX_UNITS:
        for ch in unit.chapters:
            if ch.work_id != work_id:
                continue
            if book is not None and ch.book is not None and ch.book != book:
                continue
            bounds = _parse_bekker_span_bounds(ch.bekker_range)
            if bounds is not None and bounds[0] <= pt <= bounds[1]:
                return unit, ch
    return None


def _extract_pacioli_person_loci(pacioli_persons_path: Path) -> list[tuple[str, str, SisterOccurrence]]:
    """Map Fra Luca Pacioli's explicit Aristotle folio citations in ``persons.json``."""
    if not pacioli_persons_path.exists():
        return []
    persons = json.loads(pacioli_persons_path.read_text(encoding="utf-8"))
    ar = persons.get("aristotle")
    if not ar:
        return []

    mapped: list[tuple[str, str, SisterOccurrence]] = []
    for occ in ar.get("occurrences", []):
        folio = str(occ.get("folio", ""))
        page = str(occ.get("page", ""))
        book = str(occ.get("book", ""))
        section = str(occ.get("section", ""))
        display = str(occ.get("display", "Aristotle"))
        if folio in {"0005", "0006", "0022", "0023"}:
            wk, loc = "de-caelo", "III.8.306b3"
        elif folio in {"0017", "0018"}:
            wk, loc = "met", "II.1.993b20"
        elif folio in {"0019", "0020"}:
            wk, loc = "anal-post", "I.7.75a38"
        elif folio == "0021":
            wk, loc = "anal-post", "I.13.78b34"
        else:
            wk, loc = "met", "I.2.982b12"
        mapped.append(
            (
                wk,
                loc,
                SisterOccurrence(
                    repo="pacioli",
                    cite_key=f"person:aristotle@{folio}",
                    volume=str(occ.get("volume", "de_divina_proportione")),
                    book=book,
                    section=section,
                    page=page,
                    folio=folio,
                    display=display,
                ),
            )
        )
    return mapped


def build_concordance(
    repo_root: Path,
    workspace_root: Path | None = None,
) -> dict[str, Any]:
    """Mine Aristotle citations across GEOMETOR sister repos and write ``concordance.json``.

    Args:
        repo_root: Root directory of ``geometor/aristotle``.
        workspace_root: Optional parent ``geometor`` directory containing ``euclid``,
            ``hoenen``, and ``pacioli``. Defaults to ``repo_root.parent``.

    Returns:
        Complete concordance dictionary written to
        ``resources/aristotle/concordance.json``.
    """
    ws = workspace_root or repo_root.parent
    bekker_index_path = repo_root / "resources/aristotle/bekker_index.json"
    bekker_index: dict[str, dict[str, list[str]]] = (
        json.loads(bekker_index_path.read_text(encoding="utf-8"))
        if bekker_index_path.exists()
        else {}
    )

    entries_by_id: dict[str, ConcordanceEntry] = {}

    def _register(
        raw_work_slug: str,
        raw_locus: str,
        occ_list: list[SisterOccurrence],
    ) -> None:
        slug_clean = raw_work_slug.split(":")[-1].strip().lower()
        if slug_clean not in WORK_CANONICAL:
            return
        work_id, work_la, work_en, lo_p, hi_p = WORK_CANONICAL[slug_clean]
        displays = [o.display for o in occ_list if o.display]

        bekker = parse_bekker_locus(raw_locus, (lo_p, hi_p))
        if bekker is None:
            for disp in displays:
                bekker = parse_bekker_locus(disp, (lo_p, hi_p))
                if bekker is not None:
                    break

        book, chapter = _parse_book_chapter(raw_locus, displays)
        if bekker is None:
            bekker = _lookup_bekker_from_index(bekker_index, work_id, book, chapter)
        if bekker is None:
            bekker = BekkerRef(page=lo_p, col="a", line=0)

        if book is None and chapter is None:
            inf_b, inf_c = _infer_chapter_from_bekker(bekker_index, work_id, bekker)
            book, chapter = inf_b, inf_c
        elif chapter is None and bekker.line > 0:
            inf_b, inf_c = _infer_chapter_from_bekker(bekker_index, work_id, bekker)
            if inf_b == book and inf_c is not None:
                chapter = inf_c

        if book is not None and chapter is not None:
            ch_disp = f"{_int_to_roman(book)}.{chapter}"
        elif book is not None:
            ch_disp = _int_to_roman(book)
        elif chapter is not None:
            ch_disp = str(chapter)
        else:
            ch_disp = ""

        matched = match_codex_unit(work_id, book, chapter, bekker)
        in_codex = matched is not None
        codex_unit = matched[0].slug if matched else ""
        codex_unit_title = matched[0].short_title if matched else ""
        if matched:
            if bekker.line == 0 and ch_disp:
                ch_slug = re.sub(r"[^a-z0-9]+", "-", ch_disp.lower()).strip("-")
                codex_anchor = f"bekker-{bekker.canonical_id}-{work_id}-{ch_slug}"
            else:
                codex_anchor = f"bekker-{bekker.canonical_id}"
        else:
            codex_anchor = ""

        locus_id = f"{work_id}:{bekker.canonical_id}"
        if bekker.line == 0 and ch_disp:
            locus_id = f"{work_id}:{ch_disp}:{bekker.canonical_id}"

        existing = entries_by_id.get(locus_id)
        if existing is None:
            existing = ConcordanceEntry(
                locus_id=locus_id,
                bekker=bekker,
                bekker_display=bekker.display,
                work_id=work_id,
                work_la=work_la,
                work_en=work_en,
                book=book,
                chapter=chapter,
                chapter_display=ch_disp,
                in_codex=in_codex,
                codex_unit=codex_unit,
                codex_unit_title=codex_unit_title,
                codex_anchor=codex_anchor,
            )
            entries_by_id[locus_id] = existing
        elif len(bekker.display) > len(existing.bekker_display):
            existing.bekker_display = bekker.display

        seen_sigs = {
            (o.repo, o.cite_key, o.volume, o.section, o.page, o.folio, o.display)
            for o in existing.occurrences
        }
        for occ in occ_list:
            if occ.repo not in existing.repos:
                existing.repos.append(occ.repo)
            sig = (
                occ.repo,
                occ.cite_key,
                occ.volume,
                occ.section,
                occ.page,
                occ.folio,
                occ.display,
            )
            if sig not in seen_sigs:
                seen_sigs.add(sig)
                existing.occurrences.append(occ)

    sister_sources = [
        ("euclid", ws / "euclid/resources/heath/citations.json"),
        ("hoenen", ws / "hoenen/resources/de_noetica_geometriae/citations.json"),
        ("pacioli", ws / "pacioli/resources/de_divina_proportione/citations.json"),
    ]

    repo_key_counts: dict[str, int] = {"euclid": 0, "hoenen": 0, "pacioli": 0}

    for repo_name, cpath in sister_sources:
        if not cpath.exists():
            continue
        raw_citations: dict[str, Any] = json.loads(cpath.read_text(encoding="utf-8"))
        for cite_key, record in sorted(raw_citations.items()):
            is_aristotle = (
                cite_key.startswith("aristotle:")
                or record.get("author_key") == "aristotle"
                or record.get("author_slug") == "aristotle"
            )
            if not is_aristotle:
                continue
            repo_key_counts[repo_name] += 1
            work_slug = str(
                record.get("work_slug")
                or record.get("work_key")
                or cite_key.split(":")[1]
            )
            locus_str = str(record.get("locus") or "")
            raw_occs = record.get("occurrences") or record.get("work_occurrences") or []
            parsed_occs: list[SisterOccurrence] = []
            for ro in raw_occs:
                parsed_occs.append(
                    SisterOccurrence(
                        repo=repo_name,
                        cite_key=cite_key,
                        volume=str(ro.get("volume") or ro.get("work") or repo_name),
                        book=str(ro.get("book") or ro.get("title") or ""),
                        section=str(ro.get("section") or ro.get("doc") or ""),
                        page=str(ro.get("page") or ""),
                        folio=str(ro.get("folio") or ""),
                        display=str(ro.get("display") or cite_key),
                    )
                )
            if not parsed_occs:
                parsed_occs.append(
                    SisterOccurrence(
                        repo=repo_name,
                        cite_key=cite_key,
                        volume=repo_name,
                        book="",
                        section="",
                        page="",
                        folio="",
                        display=cite_key,
                    )
                )
            _register(work_slug, locus_str, parsed_occs)

    # Include Pacioli's folio-level Aristotle references from persons.json
    pacioli_persons = ws / "pacioli/resources/de_divina_proportione/persons.json"
    pacioli_extra = _extract_pacioli_person_loci(pacioli_persons)
    if pacioli_extra:
        repo_key_counts["pacioli"] += len(pacioli_extra)
        for wk_slug, loc_str, s_occ in pacioli_extra:
            _register(wk_slug, loc_str, [s_occ])

    sorted_entries = sorted(
        entries_by_id.values(),
        key=lambda e: (e.bekker.page, e.bekker.col, e.bekker.line, e.locus_id),
    )

    total_occurrences = sum(len(e.occurrences) for e in sorted_entries)
    in_codex_count = sum(1 for e in sorted_entries if e.in_codex)

    payload: dict[str, Any] = {
        "title": "Bekker Concordance Across the GEOMETOR Canon (Euclid, Hoenen, Pacioli)",
        "standard": "Immanuel Bekker, Aristotelis Opera (Prussian Academy, Berlin, 1831)",
        "summary": {
            "distinct_bekker_loci": len(sorted_entries),
            "loci_in_codex": in_codex_count,
            "total_sister_occurrences": total_occurrences,
            "source_keys_by_repo": repo_key_counts,
        },
        "entries": [e.to_dict() for e in sorted_entries],
    }

    out_path = repo_root / "resources/aristotle/concordance.json"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(
        json.dumps(payload, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    return payload
