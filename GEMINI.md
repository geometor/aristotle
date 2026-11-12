# GEOMETOR • aristotle

Context and architectural reference for `geometor/aristotle` (*Loci Geometrici et Noetici*).

## Purpose

`geometor/aristotle` provides the primary Aristotelian textual and epistemological foundation for the GEOMETOR historical canon, uniting:

1. **Demonstrative Logic & Pre-Euclidean Principles** (*Categories*, *Prior Analytics*, *Posterior Analytics*, *Topics*) cited across `geometor/euclid` (Sir Thomas Heath).
2. **Abstraction, Continuous Magnitude & Potential Infinity** (*Physics* II–IV, VI; *De Caelo* I) cited across `geometor/euclid`, `geometor/pacioli`, and `geometor/hoenen`.
3. **Common Sensibles, the Spatial Phantasm & Intelligible Matter** (*De Anima* III; *Metaphysics* α, B, Γ, Δ, E, Z, Θ, K, M) anchoring Fr. Peter Hoenen S.J.'s *De Noetica Geometriae* (`geometor/hoenen`).

## Architectural Invariants

- **Pure Philological Edition**: Unlike constructive packages (`model`, `elements`, `pappus`), `geometor/aristotle` intentionally contains **zero Python geometric construction scripts or generated diagrams**. All primary texts are 100% verbatim public-domain Greek (Bekker 1831/1837; Ross 1924) and Clarendon Press Oxford English translations verified against SHA-256 digests in `resources/aristotle/sources_manifest.json`.
- **Four-Track Book Codex (`:layout: book`)**: `geometor.aristotle.sphinx_ext` dynamically registers `("-el", "el", "Greek (Bekker)")` into `photon_platform.publish.book` at Sphinx initialization so every unit renders synchronized `English` (`-en`), `Greek (Bekker)` (`-el`), `Summary` (`-summary`), and `Notes` (`-notes`) tracks without modifying `photon-platform/publish`.
- **Cross-Corpus Bekker Concordance**: `geometor.aristotle.concordance` parses heterogeneous Bekker citations across `euclid`, `hoenen`, and `pacioli` (199 distinct loci, 246 occurrences) and binds all 84 covered Codex loci to `.. _bekker-<id>:` anchors in `-en.rst`.

## Key Modules (`src/geometor/aristotle/`)

- `units.py`: Immutable `ChapterSpec` and `UnitSpec` registry (`CODEX_UNITS`: 5 Libri, 9 units, 54 chapters).
- `concordance.py`: `BekkerRef`, `parse_bekker_locus()`, `match_codex_unit()`, and `build_concordance()`.
- `apparatus.py`: `GLOSSARY_DATA` (36 Greek/Latin terms), `PERSONS_DATA` (36 figures), `CITATIONS_DATA` (29 editions/propositions), JSON exporters, and apparatus RST renderers.
- `commentary.py`: `UnitCommentary` and `UNIT_COMMENTARIES` providing dual-tradition (Heath + Hoenen/Aquinas) notes for all 9 units.
- `compile_codex.py`: TEI-XML & plain-text chapter extractors (`extract_greek_chapter`, `extract_english_chapter`) and `compile_codex()`.
- `sphinx_ext.py`: `register_greek_track()` and Sphinx `setup(app)`.
- `cli.py`: `geometor-aristotle` entry point (`verify`, `concordance`, `compile`).

## Commands

- Verify primary sources: `uv run --no-sync python -m geometor.aristotle.cli verify`
- Recompile Codex & apparatus: `uv run --no-sync python -m geometor.aristotle.cli compile`
- Lint & test: `ruff check src tests` and `pytest`
- Build Sphinx Book Codex: `publish build`
