.. _about-bekker-edition:

===================================================
The Bekker Edition (1831) & the Oxford Translation
===================================================

.. rubric:: Textual Provenance, Canonical Pagination & Digital Verification

Universal Bekker Coordinates (1831)
-----------------------------------

Modern scholarship cites every treatise of :person:`Aristotle <aristotle>` according to the two-volume Greek critical edition prepared by :person:`August Immanuel Bekker <bekker>` for the Royal Prussian Academy of Sciences in Berlin (:cite:`Aristotelis Opera <bekker:1831>`, 1831; Oxford 11-volume reprint, 1837). Each page of Volumes I and II (pages ``1`` through ``1462``) is printed in two columns—left column ``a`` and right column ``b``—of roughly forty-five lines each.

A Bekker coordinate such as ``1051a21`` uniquely identifies:

* **Page** ``1051`` (in *Metaphysics* Book Θ, Chapter 9),
* **Column** ``a`` (left-hand column),
* **Line** ``21`` (*τὰ δὲ διαγράμματα εὑρίσκεται ἐνεργείᾳ* — "geometrical constructions are discovered in actuality").

Across the sister repositories of GEOMETOR, Bekker citations appear in heterogeneous typographic conventions: compact ``71a11`` in ``geometor/euclid``, spaced scholastic Latin ``I, 10 76 b 39`` or ``III, 7, 431 b 2`` in ``geometor/hoenen``, and medieval book-chapter titles (*Secundo Posteriorum*, *Primo Coeli*) in ``geometor/pacioli``. The concordance engine in :mod:`geometor.aristotle.concordance` normalizes all 246 sister-corpus citations into canonical Bekker records and anchors every covered locus to ``#bekker-<id>`` in the Codex.

Primary Source Provenance & SHA-256 Integrity
---------------------------------------------

All **eighteen primary Greek and English source files** staged under ``resources/aristotle/sources/`` derive exclusively from authoritative public-domain scholarly editions and are verified on every build via ``resources/aristotle/sources_manifest.json``:

* **Greek Critical Text (10 files)**:
  * *Categories*, *Prior Analytics*, *Posterior Analytics*, *Topics*, and *De Anima*: TEI-epidoc XML editions from the Scaife / First1KGreek Digital Library (``tlg0086``), preserving Bekker 1831/1837 milestone tags.
  * *Physics* (Books II, III, IV, VI) and *De Caelo* (Book I): Bekker 1831 polytonic Greek normalized to Unicode NFC.
  * *Metaphysics*: :person:`Sir William David Ross's <ross>` landmark Clarendon Press critical text (:cite:`Aristotle's Metaphysics <ross:metaphysics:1924>`, 1924) via Perseus / First1KGreek.
* **Oxford English Translation (8 files)**:
  * Complete public-domain Clarendon Press *Works of Aristotle Translated into English* (:cite:`ed. J. A. Smith & W. D. Ross <oxford:works:1908>`): :person:`E. M. Edghill <edghill>` (*Categories*), :person:`A. J. Jenkinson <jenkinson>` (*Prior Analytics*), :person:`G. R. G. Mure <mure>` (*Posterior Analytics*), :person:`W. A. Pickard-Cambridge <pickard-cambridge>` (*Topics*), :person:`R. P. Hardie <hardie>` & :person:`R. K. Gaye <gaye>` (*Physics*), :person:`J. L. Stocks <stocks>` (*De Caelo*), :person:`J. A. Smith <smith-ja>` (*De Anima*), and :person:`W. D. Ross <ross>` (*Metaphysics*).
