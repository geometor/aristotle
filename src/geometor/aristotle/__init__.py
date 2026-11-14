"""GEOMETOR • aristotle: Foundational Texts on Geometry, Episteme, Abstraction & the Continuum.

Provides tools to mine the cross-corpus Bekker concordance across ``geometor/euclid``,
``geometor/hoenen``, and ``geometor/pacioli``, verify verbatim public-domain Greek and
Oxford English primary sources, and compile the synchronized four-track Book Codex
(*Loci Geometrici et Noetici*).
"""

from __future__ import annotations

from geometor.aristotle.compile_codex import (
    compile_codex,
    extract_english_chapter,
    extract_greek_chapter,
)
from geometor.aristotle.concordance import (
    BekkerRef,
    build_concordance,
    parse_bekker_locus,
)
from geometor.aristotle.sphinx_ext import register_greek_track
from geometor.aristotle.units import CODEX_UNITS, ChapterSpec, UnitSpec

__version__ = "0.1.1"

__all__ = [
    "__version__",
    "BekkerRef",
    "CODEX_UNITS",
    "ChapterSpec",
    "UnitSpec",
    "build_concordance",
    "compile_codex",
    "extract_english_chapter",
    "extract_greek_chapter",
    "parse_bekker_locus",
    "register_greek_track",
]
