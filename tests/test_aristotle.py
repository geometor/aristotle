"""Verification suite for ``geometor.aristotle`` (*Loci Geometrici et Noetici*)."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

import pytest

from geometor.aristotle import CODEX_UNITS, __version__
from geometor.aristotle.apparatus import (
    CITATIONS_DATA,
    GLOSSARY_DATA,
    PERSONS_DATA,
    apparatus_slug,
)
from geometor.aristotle.cli import verify_manifest
from geometor.aristotle.commentary import UNIT_COMMENTARIES
from geometor.aristotle.compile_codex import (
    extract_english_chapter,
    extract_greek_chapter,
)
from geometor.aristotle.concordance import match_codex_unit, parse_bekker_locus
from geometor.aristotle.sphinx_ext import register_greek_track

REPO_ROOT = Path(__file__).resolve().parents[1]
PUBLISH_SRC = REPO_ROOT.parents[1] / "photon-platform" / "publish" / "src"

_GREEK_CHAR_RE = re.compile(r"[\u0370-\u03ff\u1f00-\u1fff]")
_ANCHOR_DEF_RE = re.compile(r"^\.\.\s+_([A-Za-z0-9._-]+):\s*$", re.MULTILINE)
_ROLE_RE = re.compile(r":(term|person|cite):`([^`]+)`")


def test_package_version_and_unit_inventory() -> None:
    """Verify package version and canonical 5-Liber, 9-unit, 54-chapter structure."""
    assert __version__ == "0.1.0"
    assert len(CODEX_UNITS) == 9
    total_chapters = sum(len(u.chapters) for u in CODEX_UNITS)
    assert total_chapters == 54
    for unit in CODEX_UNITS:
        assert unit.slug in UNIT_COMMENTARIES


@pytest.mark.parametrize(
    ("raw_text", "expected_id", "expected_display", "work_id", "book", "chapter"),
    [
        ("An. Post. I.1, 71a11", "71a11", "71a11", "anal-post", 1, 1),
        ("An. Post. I.2, 72a14-24", "72a14", "72a14–24", "anal-post", 1, 2),
        ("Anal. Priora I, 4 25 b 37-39", "25b37", "25b37–39", "anal-prior", 1, 4),
        ("i-10-76-b-9", "76b9", "76b9", "anal-post", 1, 10),
        ("1020.a.13.11", "1020a13", "1020a13", "metaphysica", 5, 13),
        ("268.b.6", "268b6", "268b6", "de-caelo", 1, 1),
        ("431a.140", "431a14", "431a14", "de-anima", 3, 7),
    ],
)
def test_parse_bekker_locus_edge_formats(
    raw_text: str,
    expected_id: str,
    expected_display: str,
    work_id: str,
    book: int,
    chapter: int,
) -> None:
    """Verify Bekker coordinate normalization across euclid, hoenen, and pacioli formats."""
    ref = parse_bekker_locus(raw_text)
    assert ref is not None
    assert ref.canonical_id == expected_id
    assert ref.display == expected_display
    matched = match_codex_unit(work_id, book, chapter, ref)
    assert matched is not None


def test_sources_manifest_sha256_integrity() -> None:
    """Confirm all 18 staged Greek and English primary source files pass SHA-256 checks."""
    manifest_path = REPO_ROOT / "resources" / "aristotle" / "sources_manifest.json"
    assert manifest_path.is_file()
    payload = json.loads(manifest_path.read_text(encoding="utf-8"))
    assert len(payload["sources"]) == 18
    ok, errors = verify_manifest(REPO_ROOT)
    assert ok is True
    assert errors == []


def test_all_54_chapters_extract_authentic_greek_and_english() -> None:
    """Verify every chapter in CODEX_UNITS yields clean polytonic Greek and Oxford English."""
    for unit in CODEX_UNITS:
        for ch in unit.chapters:
            greek_paras = extract_greek_chapter(REPO_ROOT, ch)
            assert len(greek_paras) >= 1, f"Empty Greek paragraphs for {ch}"
            joined_el = "\n".join(greek_paras)
            assert _GREEK_CHAR_RE.search(joined_el), f"Missing Greek characters in {ch}"
            assert "<!DOCTYPE" not in joined_el
            assert "<html" not in joined_el
            assert "mw-parser-output" not in joined_el

            english_paras = extract_english_chapter(REPO_ROOT, ch)
            assert len(english_paras) >= 1, f"Empty English paragraphs for {ch}"
            joined_en = "\n".join(english_paras)
            assert "Provided by The Internet Classics Archive" not in joined_en
            assert len(joined_en) > 200


def test_no_embedded_geometry_construction_scripts() -> None:
    """Ensure historical fidelity: zero Python construction scripts or plotted diagrams."""
    for py_file in (REPO_ROOT / "src" / "geometor" / "aristotle").glob("*.py"):
        source = py_file.read_text(encoding="utf-8")
        assert "geometor.model" not in source
        assert "geometor.explorer" not in source

    for rst_file in (REPO_ROOT / "docsrc").rglob("*.rst"):
        text = rst_file.read_text(encoding="utf-8")
        assert ".. plot::" not in text
        assert "svg.euclid-graphic" not in text


def test_concordance_indexes_sister_repos_and_resolves_codex_anchors() -> None:
    """Verify concordance covers euclid, hoenen, and pacioli and all codex anchors exist."""
    concordance_path = REPO_ROOT / "resources" / "aristotle" / "concordance.json"
    assert concordance_path.is_file()
    payload = json.loads(concordance_path.read_text(encoding="utf-8"))
    summary = payload["summary"]

    assert summary["distinct_bekker_loci"] >= 195
    assert summary["loci_in_codex"] >= 80
    assert summary["source_keys_by_repo"]["euclid"] >= 140
    assert summary["source_keys_by_repo"]["hoenen"] >= 60
    assert summary["source_keys_by_repo"]["pacioli"] >= 15

    unit_anchors: dict[str, set[str]] = {}
    for unit in CODEX_UNITS:
        en_path = REPO_ROOT / "docsrc" / "loci_geometrici" / unit.slug / f"{unit.slug}-en.rst"
        assert en_path.is_file()
        unit_anchors[unit.slug] = set(_ANCHOR_DEF_RE.findall(en_path.read_text(encoding="utf-8")))

    in_codex_entries = [e for e in payload["entries"] if e["in_codex"]]
    assert len(in_codex_entries) == summary["loci_in_codex"]
    for entry in in_codex_entries:
        u_slug = entry["codex_unit"]
        anc = entry["codex_anchor"]
        assert u_slug in unit_anchors
        assert anc in unit_anchors[u_slug], f"Missing anchor {anc} in {u_slug}-en.rst"


def test_sphinx_ext_registers_greek_track() -> None:
    """Verify register_greek_track adds -el Greek (Bekker) to photon_platform.publish.book."""
    if PUBLISH_SRC.is_dir() and str(PUBLISH_SRC) not in sys.path:
        sys.path.insert(0, str(PUBLISH_SRC))
    book_mod = pytest.importorskip("photon_platform.publish.book")
    inserted = register_greek_track(book_mod)
    assert inserted is True
    assert "el" in book_mod._AUX_TRACK_BASENAMES
    assert any(k == "el" and label == "Greek (Bekker)" for _, k, label in book_mod._TRACK_SUFFIX_PATTERNS)

    class _DummyEnv:
        found_docs = {
            "loci_geometrici/liber-1a-apodeixis/liber-1a-apodeixis-en",
            "loci_geometrici/liber-1a-apodeixis/liber-1a-apodeixis-el",
            "loci_geometrici/liber-1a-apodeixis/liber-1a-apodeixis-summary",
            "loci_geometrici/liber-1a-apodeixis/liber-1a-apodeixis-notes",
        }

    tracks = book_mod.detect_companion_tracks(
        _DummyEnv(),
        "loci_geometrici/liber-1a-apodeixis/liber-1a-apodeixis-en",
    )
    assert [t["key"] for t in tracks] == ["en", "el", "summary", "notes"]
    assert [t["label"] for t in tracks] == ["English", "Greek (Bekker)", "Summary", "Notes"]


def test_all_four_tracks_present_for_each_codex_unit() -> None:
    """Verify each of the 9 Codex units has synchronized -en, -el, -summary, and -notes RST files."""
    codex_dir = REPO_ROOT / "docsrc" / "loci_geometrici"
    for unit in CODEX_UNITS:
        for suffix in ("en", "el", "summary", "notes"):
            track_file = codex_dir / unit.slug / f"{unit.slug}-{suffix}.rst"
            assert track_file.is_file(), f"Missing track file {track_file}"
            content = track_file.read_text(encoding="utf-8")
            assert ":layout: book" in content


def test_apparatus_roles_resolve_across_docsrc() -> None:
    """Verify 100% of :term:, :person:, and :cite: roles in docsrc resolve to apparatus entries."""
    codex_dir = REPO_ROOT / "docsrc" / "loci_geometrici"
    glossary_anchors = set(_ANCHOR_DEF_RE.findall((codex_dir / "glossary.rst").read_text(encoding="utf-8")))
    persons_anchors = set(_ANCHOR_DEF_RE.findall((codex_dir / "persons.rst").read_text(encoding="utf-8")))
    bib_anchors = set(_ANCHOR_DEF_RE.findall((codex_dir / "bibliography.rst").read_text(encoding="utf-8")))

    glossary_slugs = {apparatus_slug(k) for k in GLOSSARY_DATA}
    person_slugs = {apparatus_slug(k) for k in PERSONS_DATA}
    cite_slugs = {apparatus_slug(k) for k in CITATIONS_DATA}

    for rst_file in (REPO_ROOT / "docsrc").rglob("*.rst"):
        if "modules/api" in str(rst_file):
            continue
        text = rst_file.read_text(encoding="utf-8")
        for role, body in _ROLE_RE.findall(text):
            target = body.split("<", 1)[1].rstrip(">").strip() if "<" in body and body.endswith(">") else body.strip()
            slug = apparatus_slug(target)
            if role == "term":
                assert slug in glossary_slugs, f"Unresolved :term:`{body}` in {rst_file}"
                assert f"term-{slug}" in glossary_anchors
            elif role == "person":
                assert slug in person_slugs, f"Unresolved :person:`{body}` in {rst_file}"
                assert f"person-{slug}" in persons_anchors
            elif role == "cite":
                assert slug in cite_slugs, f"Unresolved :cite:`{body}` in {rst_file}"
                assert f"cite-{slug}" in bib_anchors
