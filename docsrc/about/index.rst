:navigation: header
:order: 10
:nav_title: About

.. _about:
.. _about-index:
.. _mission:

About
=====

.. rubric:: Extracting Historical Semantic Knowledge & Repurposing It for Exact Symbolic Reasoning

About This Edition
------------------

**GEOMETOR • aristotle** (*Loci Geometrici et Noetici*) establishes the philosophical and epistemological keystone of the GEOMETOR historical canon. Gathering fifty-four foundational chapters across eight treatises of :person:`Aristotle of Stagira <aristotle>` (384–322 BC), this edition reconstructs Aristotle's seminal theories of demonstrative science (:term:`apodeixis <apodeixis>`), first principles, continuous magnitude, intelligible matter (:term:`hylē noētē <hyle-noete>`), and diagrammatic discovery in actuality (:term:`energeia <energeia>`).

The codex is presented across four synchronized tracks powered by ``photon-platform/publish``: unabridged English from the classic Clarendon Press *Oxford Translation*, verbatim polytonic Greek from :person:`Immanuel Bekker's <bekker>` 1831 Prussian Academy edition and :person:`W. D. Ross's <ross>` 1924 Oxford text of the *Metaphysics*, comprehensive structural summaries, and dual-tradition critical notes. These notes unite :person:`Sir Thomas Heath's <heath>` mathematical-historical reconstruction with :person:`Fr. Peter Hoenen S.J.'s <hoenen>` and :person:`St. Thomas Aquinas's <thomas-aquinas>` scholastic noetics of insight in the spatial :term:`phantasm <phantasma>`. Every passage is mapped to universal Bekker coordinates and integrated into a Master Concordance of 199 loci across the GEOMETOR corpus.

Within the broader GEOMETOR canon, this codex provides the primary epistemological justification for exact constructive geometry:

* **Pre-Euclidean First Principles in** ``geometor/euclid``: Resolving 145 distinct Aristotelian Bekker citations in Heath's commentary on the *Elements*—governing axioms, postulates, nominal definitions, and Eudoxian general proportion.
* **Noetic Insight in the Phantasm in** ``geometor/hoenen`` & ``geometor/aquinas``: Grounding 64 Aristotelian Bekker keys on how the intellect beholds universal spatial necessities (*noēsis*) in intelligible extension displayed through the imagination.
* **Demonstrative Subalternation in** ``geometor/pacioli``: Sustaining Fra Luca Pacioli's defence of mathematical certitude (*nel primo grado di certezza*) and the three-dimensional completeness of continuous bodies.

The GEOMETOR Mission
--------------------

The GEOMETOR project, directed by **phi ARCHITECT**, is dedicated to the systematic recovery, exact formalization, and dynamic re-expression of foundational geometric and philosophical knowledge. The mission unfolds across three essential pillars:

* **Extracting Historical Semantic Knowledge**: Moving beyond passive page scans and OCR to recover the living deductive structure of 2,300+ years of geometric, axiomatic, and philosophical treatises—elevating prose, marginal citations, primary-source folios (via ``publish folio``), and calibrated Ink-to-Vector ``.euclid-graphic`` diagrams into structured, machine-addressable semantic graphs.
* **Exact Symbolic Grounding (``geometor.model``)**: Anchoring geometric constructions in 100% exact symbolic algebra (using ``SymPy``) and Rational Trigonometry invariants (quadrance, spread, cross-ratio) over exact algebraic fields rather than floating-point approximations.
* **Repurposing Knowledge Across Mediums**: Re-deploying extracted semantic and algebraic structures across synchronized multi-track **Book Codices** and EPUB 3 editions (via ``photon-platform/publish``), computable deductive canons (``geometor.elements``, ``geometor.etc``, ``geometor.pappus``, ``geometor.divine``), interactive SVG laboratories (``geometor.explorer``), QHD visual broadcasts, and neuro-symbolic program synthesis (``geometor.seer``) across ``geometor.com``.

Sources, Provenance & Methodology
---------------------------------

Archival Sources & Critical Editions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* **Immanuel Bekker (1831/1837)**: *Aristotelis Opera*, edidit Academia Regia Borussica, Berlin: Georgium Reimerum, 1831; Oxford University Press reprint, 1837 (Vols. I–II, canonical pagination 1a–1462b).
* **The Oxford Translation of Aristotle**: Clarendon Press, 1908–1952, under the editorship of J. A. Smith and W. D. Ross (including translations by Edghill, Jenkinson, Mure, Pickard-Cambridge, Hardie, Gaye, Stocks, and Ross).
* **W. D. Ross (1924)**: *Aristotle's Metaphysics: A Revised Text with Introduction and Commentary*, 2 vols., Oxford: Clarendon Press.

Digital Scriptorium Methodology
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* **100% Verbatim Primary Texts**: Complete, unabridged chapters preserving organic dialectical and demonstrative context, with SHA-256 provenance verification.
* **Universal Bekker Coordinates**: Every passage mapped to standard page, column, and line coordinates with automatic deep linking.
* **Strict Content / Code Separation**: Textual and philological integrity maintained free of embedded script executions; mathematical models implemented in clean, separate Python modules.

Philological & Philosophical Essays
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* :doc:`The Bekker Edition (1831) & the Oxford Translation <bekker-edition>`
* :doc:`Aristotle's Four Pillars of Geometric Cognition <aristotle-and-geometor>`

.. toctree::
   :maxdepth: 1
   :hidden:

   bekker-edition
   aristotle-and-geometor
