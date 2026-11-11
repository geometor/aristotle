# GEOMETOR • aristotle

***Loci Geometrici et Noetici* — Aristotle's Foundational Texts on Geometry, Demonstrative Science (*Epistēmē*), Abstraction, and the Continuum**

`geometor/aristotle` (`geometor-aristotle`) is a synchronized four-track **Book Codex** (`:layout: book`) published with [`photon-platform/publish`](https://github.com/photon-platform/publish). It gathers the **54 foundational chapters** across **8 Aristotelian treatises** cited throughout the GEOMETOR historical canon—[`geometor/euclid`](https://github.com/geometor/euclid) (Sir Thomas Heath's *Thirteen Books of Euclid's Elements*), [`geometor/hoenen`](https://github.com/geometor/hoenen) (Fr. Peter Hoenen S.J.'s *De Noetica Geometriae*), and [`geometor/pacioli`](https://github.com/geometor/pacioli) (Fra Luca Pacioli's *De Divina Proportione*).

---

## Four-Track Synchronized Book Codex

Every treatise unit in `docsrc/loci_geometrici/` is rendered across four synchronized tracks with track-preserving navigation:

1. **English (`-en.rst`)** — Verbatim public-domain Clarendon Press *Oxford Translations* (*Works of Aristotle*, ed. J. A. Smith & W. D. Ross, 1908–1931) anchored to exact Bekker columns (`.. folio:: Bekker <col>` and `.. _bekker-<id>:`).
2. **Greek (`-el.rst`, `Greek (Bekker)`)** — Verbatim polytonic Greek from Immanuel Bekker's Royal Prussian Academy edition (*Aristotelis Opera*, 1831/1837) and W. D. Ross's critical edition of the *Metaphysics* (1924).
3. **Summary (`-summary.rst`)** — Argumentative thesis, step-by-step logical progression, and chapter-level Bekker conspectus tables linking directly to both `EN` and `EL` tracks.
4. **Critical Notes (`-notes.rst`)** — Dual-tradition commentary synthesizing **Sir Thomas Heath's** mathematical-historical analysis of pre-Euclidean Greek geometry with **Fr. Peter Hoenen S.J.'s** and **St. Thomas Aquinas's** scholastic-noetic analysis of intellectual insight in the phantasm (*phantasma*) and intelligible matter (*hylē noētē*), plus sister-corpus back-reference tables.

---

## Corpus Architecture (Libri I–V · 9 Units · 54 Chapters)

| Liber & Unit | Treatises & Chapters | Bekker Span | Oxford Translators |
| :--- | :--- | :--- | :--- |
| **Liber I.A** (`liber-1a-apodeixis`) | *Posterior Analytics* I.1–13 (13 chs.) | `71a1–79a16` | G. R. G. Mure |
| **Liber I.B** (`liber-1b-universale-et-nous`) | *Posterior Analytics* I.24, 27, 31; II.19 (4 chs.) | `85a13–88a17, 99b15–100b17` | G. R. G. Mure |
| **Liber II.A** (`liber-2a-quantitas-et-syllogismus`) | *Categories* 6; *Prior Analytics* I.4, 23–24; II.16 (5 chs.) | `4b20–6a35, 25b–65a` | E. M. Edghill; A. J. Jenkinson |
| **Liber II.B** (`liber-2b-topica-definitiones`) | *Topics* VI.4; VIII.3 (2 chs.) | `141a23–142b19, 158a31–159a14` | W. A. Pickard-Cambridge |
| **Liber III.A** (`liber-3a-mathematicus-et-infinitum`) | *Physics* II.2; III.4–7 (5 chs.) | `193b22–194b15, 202b30–208a4` | R. P. Hardie & R. K. Gaye |
| **Liber III.B** (`liber-3b-topos-continuum-dimensio`) | *Physics* IV.1–5; VI.1–2, 9; *De Caelo* I.1 (9 chs.) | `208a–213a, 231a–240a, 268a–b` | R. P. Hardie & R. K. Gaye; J. L. Stocks |
| **Liber IV** (`liber-4-de-anima-phantasia`) | *De Anima* III.3–8 (6 chs.) | `427a17–432a14` | J. A. Smith |
| **Liber V.A** (`liber-5a-scientiae-et-quantitas`) | *Metaphysics* B.2; Δ.6, 13; E.1 (4 chs.) | `996a–998a, 1015b–1026a` | W. D. Ross |
| **Liber V.B** (`liber-5b-hyle-noete-energeia-pulchritudo`) | *Metaphysics* Z.10–11; Θ.9; M.1–3 (6 chs.) | `1034b–1037a, 1051a, 1076a–1078b` | W. D. Ross |

---

## Cross-Corpus Bekker Concordance

`resources/aristotle/concordance.json` and `docsrc/loci_geometrici/concordance.rst` index every Aristotelian locus cited across the sister repositories of GEOMETOR:

- **199 distinct Bekker loci** (**246 textual occurrences**):
  - `geometor/euclid`: **145** Aristotle citation keys across Heath's Volumes I–III
  - `geometor/hoenen`: **64** Aristotle citation keys across *De Noetica Geometriae*
  - `geometor/pacioli`: **17** Aristotle citation keys & folio passages across *De Divina Proportione*
- **84 foundational geometric and noetic loci** fall directly inside the 54 chapters of *Loci Geometrici et Noetici* and resolve to `#bekker-<id>` anchors.

---

## Repository Layout

```text
aristotle/
├── pyproject.toml                       # PEP 621 package metadata (Python >=3.13, ruff, pytest)
├── resources/
│   ├── aristotle/
│   │   ├── sources/el/                  # 10 verbatim Bekker 1831/1837 & Ross 1924 Greek editions
│   │   ├── sources/en/                  # 8 verbatim public-domain Oxford English translations
│   │   ├── sources_manifest.json        # SHA-256 checksum & provenance manifest (18 files)
│   │   ├── bekker_index.json            # Extracted Bekker column & milestone offsets
│   │   └── concordance.json             # Cross-corpus Bekker concordance (euclid, hoenen, pacioli)
│   └── loci_geometrici/                 # Hover-card apparatus JSONs (glossary, persons, citations)
├── src/geometor/aristotle/
│   ├── units.py                         # Canonical 5-Liber, 9-unit, 54-chapter specifications
│   ├── concordance.py                   # Bekker coordinate parser & sister-corpus miner
│   ├── apparatus.py                     # Lexicon (36 terms), prosopography (44 persons), bibliography (29 works)
│   ├── commentary.py                    # Dual-tradition (Heath + Hoenen/Aquinas) critical commentaries
│   ├── compile_codex.py                 # Primary Greek/English extractors & 4-track RST compiler
│   ├── sphinx_ext.py                    # Sphinx extension registering the -el Greek (Bekker) track
│   └── cli.py                           # CLI: verify, concordance, compile
├── docsrc/                              # Sphinx RST source (portal + loci_geometrici Book Codex)
└── tests/
    └── test_aristotle.py                # Philological, SHA-256, concordance, track & apparatus test suite
```

---

## Usage & Development

All commands run with Python `3.13` via `uv` and `photon-platform/publish`:

```bash
# Verify SHA-256 integrity of all 18 Greek & English primary sources
uv run --no-sync python -m geometor.aristotle.cli verify

# Rebuild cross-corpus Bekker concordance
uv run --no-sync python -m geometor.aristotle.cli concordance

# Compile apparatus JSONs and all 41 Book Codex RST files
uv run --no-sync python -m geometor.aristotle.cli compile

# Lint and run verification suite
ruff check src tests
pytest

# Build HTML documentation into docs/
publish build
```

---

## License

Code, critical apparatus, and editorial commentary are released under the [MIT License](LICENSE). Primary Greek texts (Bekker 1831/1837; Ross 1924) and Clarendon Press Oxford English translations are in the public domain.
