GEOMETOR • aristotle
====================

**Visit the Online Archive:** https://geometor.github.io/aristotle/

**Aristotle • Organon, Posterior Analytics, Physics, De Anima, Metaphysics • semantic digital archive**

Mission
-------

``geometor/aristotle`` is part of the interconnected `GEOMETOR <https://geometor.com>`_ semantic digital archive. It provides a synchronized four-track Greek-English Book Codex and cross-corpus Bekker concordance assembling Aristotle's foundational texts on geometry, demonstrative science (*apodeixis*), abstraction, and the continuum (*Loci Geometrici et Noetici*). The archive liberates these landmark philosophical foundations from isolated print bounds into addressable semantic units, synchronized Bekker Greek and Oxford English tracks, primary-source citation provenance, and exact symbolic connections across the GEOMETOR corpus.

Books in This Archive
---------------------

- **`Organon Geometricum <https://geometor.github.io/aristotle/organon/>`_** — Foundational logical treatises from the *Categories*, *Prior Analytics*, and *Topics* establishing geometric definition, continuous quantity, and deductive syllogisms.
- **`Posterior Analytics <https://geometor.github.io/aristotle/analytica_posteriora/>`_** — Demonstrative science (*episteme*), indemonstrable first principles, Euclidean axioms, and the emergence of *nous*.
- **`Physica & De Caelo <https://geometor.github.io/aristotle/physica/>`_** — Mathematical abstraction without falsehood (*abstrahentium non est mendacium*), the potential infinite, place (*topos*), and the non-atomism of the continuum.
- **`De Anima <https://geometor.github.io/aristotle/de_anima/>`_** — Intellectual vision in geometry, imaginative phantasms (*phantasmata*), and the hand as the tool of tools.
- **`Metaphysica <https://geometor.github.io/aristotle/metaphysica/>`_** — Mathematical intermediates, intelligible matter (*hyle noete*), actuality (*energeia*), and the discovery of geometric truth by division in act.

Repository Contents
-------------------

- ``docsrc/`` — Four-track Book Codex, Bekker apparatus, and Sphinx documentation compiled by `PHOTON publish <https://github.com/photon-platform/publish>`_.
- ``resources/`` — Verbatim Greek and English source corpora, SHA-256 provenance manifests, Bekker indices, and sister-corpus concordances.
- ``src/geometor/aristotle/`` — Python modules for Bekker coordinate parsing, concordance mapping, and four-track codex compilation.

Local Build & Verification
--------------------------

.. code-block:: bash

   publish build
   uv run --no-sync pytest

Part of the GEOMETOR Knowledge Archive
--------------------------------------

Explore all **74 Book Codices** and **11 Mathematical Catalogs** at https://geometor.com/books/.
