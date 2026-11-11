"""Sphinx extension registering the Bekker Greek (``-el``) companion track in ``publish``."""

from __future__ import annotations

import os
import re
from types import ModuleType
from typing import Any

_PATCHED_ATTR = "_geometor_aristotle_el_patched"
_EL_SUFFIX_ENTRY = (r"^(.+)[._-]el$", "el", "Greek (Bekker)")
_EL_AUX_PATTERN = re.compile(r"^.+[._-]el$")


def register_greek_track(book_mod: ModuleType | object | None = None) -> bool:
    """Register the ``el`` (Greek Bekker) companion track on ``photon_platform.publish.book``.

    Args:
        book_mod: Optional pre-imported ``photon_platform.publish.book`` module (or mock
            object in unit tests). When ``None``, imports it dynamically.

    Returns:
        ``True`` if ``photon_platform.publish.book`` is available and patched, ``False``
        otherwise.
    """
    if book_mod is None:
        try:
            from photon_platform.publish import book as imported_book
        except ImportError:
            return False
        book_mod = imported_book

    if getattr(book_mod, _PATCHED_ATTR, False):
        return True

    suffix_patterns = getattr(book_mod, "_TRACK_SUFFIX_PATTERNS", None)
    if isinstance(suffix_patterns, list) and not any(k == "el" for _, k, _ in suffix_patterns):
        suffix_patterns.append(_EL_SUFFIX_ENTRY)

    aux_basenames = getattr(book_mod, "_AUX_TRACK_BASENAMES", None)
    if isinstance(aux_basenames, set):
        aux_basenames.add("el")

    aux_patterns = getattr(book_mod, "_AUX_TRACK_PATTERNS", None)
    if isinstance(aux_patterns, list):
        aux_patterns.append(_EL_AUX_PATTERN)

    orig_detect = getattr(book_mod, "detect_companion_tracks")
    extract_stem = getattr(book_mod, "_extract_unit_stem")

    def _detect_with_greek(env: object, pagename: str) -> list[dict[str, Any]]:
        found_docs: set[str] = set(getattr(env, "found_docs", set()))
        if not found_docs:
            return []

        tracks: list[dict[str, Any]] = list(orig_detect(env, pagename))
        doc_dir = os.path.dirname(pagename)
        basename = os.path.basename(pagename)
        stem = str(extract_stem(basename, doc_dir))

        def _qual(local_name: str) -> str:
            return f"{doc_dir}/{local_name}" if doc_dir else local_name

        is_unit_dir = not doc_dir or stem == os.path.basename(doc_dir)
        el_cands = [_qual(f"{stem}.el"), _qual(f"{stem}_el"), _qual(f"{stem}-el")]
        if is_unit_dir:
            el_cands.append(_qual("el"))

        el_doc = next((cand for cand in el_cands if cand in found_docs), None)
        if el_doc is None:
            return tracks

        # Handle case where only -en and -el exist (orig_detect returned [] because len < 2)
        if not tracks:
            en_cands = [_qual(f"{stem}.en"), _qual(f"{stem}_en"), _qual(f"{stem}-en")]
            if is_unit_dir:
                en_cands.append(_qual("en"))
            en_doc = next((cand for cand in en_cands if cand in found_docs), None)
            if en_doc and en_doc != el_doc:
                return [
                    {
                        "key": "en",
                        "label": "English",
                        "docname": en_doc,
                        "active": en_doc == pagename,
                    },
                    {
                        "key": "el",
                        "label": "Greek (Bekker)",
                        "docname": el_doc,
                        "active": el_doc == pagename,
                    },
                ]
            return []

        if any(tr.get("docname") == el_doc for tr in tracks):
            return tracks

        el_entry: dict[str, Any] = {
            "key": "el",
            "label": "Greek (Bekker)",
            "docname": el_doc,
            "active": el_doc == pagename,
        }

        insert_idx = len(tracks)
        for idx, tr in enumerate(tracks):
            if tr.get("key") == "en":
                insert_idx = idx + 1
                break
            if tr.get("key") in {"commentary", "summary", "notes", "folio"}:
                insert_idx = idx
                break
        tracks.insert(insert_idx, el_entry)
        return tracks

    setattr(book_mod, "detect_companion_tracks", _detect_with_greek)
    setattr(book_mod, _PATCHED_ATTR, True)
    return True


def setup(app: object) -> dict[str, Any]:
    """Sphinx extension entry point registering Bekker Greek multi-track support.

    Args:
        app: Active Sphinx application instance.

    Returns:
        Sphinx extension metadata dictionary.
    """
    _ = app
    register_greek_track()
    return {
        "version": "0.1.0",
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
