=========
Changelog
=========

0.1.3 (2026-11-14)
------------------

- Standardized top-level ``About`` page (``docsrc/about/index.rst`` promoted to top header ``:order: 10``) with the three-pillar GEOMETOR semantic-extraction mission and archival provenance; retired ``docsrc/mission/`` stubs cleanly into Home and ``About``.

0.1.2 (2026-11-14)
------------------

- **changed**: Standardized Book Title Page, top-level Header Navigation (``Book``, ``People``, ``Bibliography``, ``Usage``), Reader's Guide (``docsrc/usage/``), featured Author/Translator profiles in ``People``, and English structural terminology.

0.1.1 (2026-11-13)
------------------

- **added**: Added track-aware primary-source folio map (``resources/aristotle/folio_map.json``) mapping 199 Bekker milestones and liber chapter spans to verified Greek and Oxford English locus lines with GitHub blob line anchors.

0.1.0 (2026-11-11)
------------------

- Initialized ``geometor-aristotle`` (Python ``>=3.13``, PEP 621 ``pyproject.toml``, ``ruff`` Google docstring & type annotation enforcement).
- Staged and SHA-256 verified 18 verbatim public-domain primary source files in ``resources/aristotle/sources/`` (10 Bekker 1831/1837 & W. D. Ross 1924 polytonic Greek editions and 8 Clarendon Press Oxford English translations) with ``resources/aristotle/sources_manifest.json``.
- Implemented ``geometor.aristotle.concordance`` mining **199 distinct Bekker loci** (246 textual occurrences across ``geometor/euclid``, ``geometor/hoenen``, and ``geometor/pacioli``) and linking all **84 covered Codex loci** to ``#bekker-<id>`` anchors.
- Implemented ``geometor.aristotle.sphinx_ext`` dynamically registering the ``-el`` (**Greek (Bekker)**) track in ``photon_platform.publish.book`` alongside ``-en``, ``-summary``, and ``-notes``.
- Compiled the 5-Liber, 9-unit, 54-chapter **Loci Geometrici et Noetici** multi-track Book Codex under ``docsrc/loci_geometrici/`` with dual-tradition commentaries (Heath + Hoenen/Aquinas), 36-term Greek/Latin glossary, 36-entry prosopography, and 29-entry bibliography.
- Added ``pytest`` verification suite in ``tests/test_aristotle.py`` covering Bekker parsing, SHA-256 source integrity, polytonic Greek & Oxford English extraction, concordance anchor resolution, Sphinx ``-el`` track registration, and apparatus role integrity.
