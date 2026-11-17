:navigation: header
:order: 20
:nav_title: Usage

.. _aristotle-usage:

==================
Using This Edition
==================

.. rubric:: Interactive Reader's Guide to the Digital Scriptorium Edition of Aristotle on Geometry, Episteme & Nous

Welcome to the GEOMETOR critical edition of **Aristotle on Geometry, Episteme & Nous**. This digital edition unites the fifty-four foundational mathematical and noetic chapters of Aristotle across five Books, fifty-four chapters, and 199 Bekker loci. Below are the key interactive features available throughout the site.

1. Synchronized Reading Tracks
------------------------------

Every unit in the Book Codex provides four synchronized reading tracks accessible directly from the book header bar:

* **English (Oxford Translation)**: Folio-anchored primary English translation based on the canonical Oxford Translation of Aristotle (*The Works of Aristotle Translated into English*, ed. J. A. Smith and W. D. Ross; Clarendon Press, 1908–1952).
* **Greek (Bekker 1831 / Ross 1924)** (``-el``): Verbatim polytonic Greek text established from Immanuel Bekker's 1831 Prussian Academy edition collated with W. D. Ross's 1924 *Metaphysics*, with marginal Bekker page and column milestones.
* **Summary (Deductive Architecture)**: Argumentative thesis, step-by-step logical and noetic progression, and chapter-by-chapter Bekker span overviews.
* **Notes (Scholarly Commentary)**: Detailed philological and conceptual commentary synthesizing Sir Thomas L. Heath's mathematical reconstructions with Fr. Peter Hoenen's Thomistic noetics (*De Noetica Geometriae*, 1954) and St. Thomas Aquinas's *Sententia* commentaries.

Use the track switcher in the chapter header bar to toggle seamlessly between perspectives while preserving your reading position.

2. Primary-Source Folio Milestones
----------------------------------

Every chapter is tethered to the universal Bekker pagination standard:

* **Marginal Bekker Milestones**: Marginal pills (e.g., ``[71a]``, ``[71b]``, ``[1051a]``) link directly to digital witnesses and denote transitions between Bekker columns.
* **Header Folio Indicator**: The top metadata bar identifies the active treatise, book, chapter, and corresponding Bekker coordinate span.

3. Interactive Diagrams & Deductive Links
-----------------------------------------

The edition connects Aristotelian passages to classical Euclidean constructions:

* **Geometric Concepts & Justifications (``:g:``, ``:just:``)**: Direct cross-references to Euclid's *Elements* (e.g., triangle angle sum :eq:`2R`, Bryson's circle quadrature, the incommensurability of the diagonal).
* **Equations & Propositions (``:eq:``)**: Rendered LaTeX mathematical formulations for first-figure syllogistic forms (Barbara), continuous vs. discrete magnitude invariants, and antanairesis ratios.

4. Full-Text Search with In-Page Highlighting
---------------------------------------------

The global search box in the sidebar provides instantaneous search across English translations, polytonic Greek texts, and scholarly commentary:

* Search queries automatically append `?highlight=` parameters to destination URLs.
* Matched terms are highlighted directly within the text for rapid discovery of Greek philosophical terms (:term:`episteme`, :term:`nous`, :term:`phantasma`, :term:`hyle-noete`).

5. Categories, Tags & Collection Views
--------------------------------------

Document collections throughout the site (such as the :doc:`Development & Curation Log <../log/index>`) support multiple display modes:

* **Cards View**: Grid of entry cards with metadata badges and timestamps.
* **Banners View**: Wide summary presentation.
* **List View**: Dense tabular listing.
* **Taxonomy Facets**: Filter by topic tags (e.g., `apodeixis`, `continuum`, `phantasia`, `metaphysica`).

6. People, Bibliography & Glossary Tooltips
-------------------------------------------

* **People (``:person:``)**: Historical figures (such as :person:`Aristotle of Stagira <aristotle>`, :person:`Immanuel Bekker <bekker>`, :person:`W. D. Ross <ross>`, :person:`Plato <plato>`, :person:`Zeno <zeno>`, and :person:`Peter Hoenen <hoenen>`) display rich biographical hover cards linking to the :doc:`People Register <../people/index>`.
* **Citations (``:cite:``)**: Inline citations link directly to primary sources in the :doc:`Bibliography <../bibliography>`.
* **Technical Terms (``:term:``)**: Thirty-six Greek and Scholastic Latin philosophical terms link to definitions in the :doc:`Glossary <../glossary>`.
* **Theme Switching**: Toggle between Light and Dark themes via the header button to suit your reading environment.

7. Command-Line & Python API
----------------------------

The ``geometor.aristotle`` Python package provides tools for concordance analysis and Book Codex compilation.

Inside the ``geometor`` workspace:

.. code-block:: bash

   # Verify codex integrity, Bekker spans, and sister repo citations
   aristotle verify

   # Display summary of all 5 Books, 9 units, and 54 chapters
   aristotle summary

   # Recompile apparatus RST files
   aristotle compile

Python API Example:

.. code-block:: python

   from geometor.aristotle.units import CODEX_UNITS
   from geometor.aristotle.concordance import build_concordance
   from pathlib import Path

   # Inspect Book Codex units
   print(f"Loaded {len(CODEX_UNITS)} Book Codex units across 5 Books.")

   # Inspect the first unit (Posterior Analytics I.1-13)
   u1 = CODEX_UNITS[0]
   print(f"Unit 1: {u1.title_en} ({u1.bekker_range})")
   print(f"Chapters count: {len(u1.chapters)}")
