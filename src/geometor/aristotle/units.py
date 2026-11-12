"""Canonical specification of the 5 Libri and 9 multi-track Book Codex units."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class ChapterSpec:
    """Metadata and source selectors for a single Aristotelian chapter in the Codex.

    Attributes:
        work_id: Canonical work identifier (e.g. ``"anal-post"``, ``"physica"``).
        work_title_en: Standard English title of the treatise.
        work_title_el: Polytonic Greek title of the treatise.
        work_title_la: Traditional Scholastic/Bekker Latin title of the treatise.
        book: Book number (1-indexed), or ``None`` for single-book treatises (*Categories*).
        book_label: Roman/Greek book label (e.g. ``"I"``, ``"B (III)"``), or empty string.
        chapter: Chapter number (1-indexed).
        bekker_range: Human-readable Bekker span (e.g. ``"71a1–71b8"``).
        bekker_cols: Ordered tuple of Bekker half-page columns spanned by this chapter.
        theme_en: Concise thematic subtitle for the chapter heading.
        translator: Public-domain Oxford English translator credit.
    """

    work_id: str
    work_title_en: str
    work_title_el: str
    work_title_la: str
    book: int | None
    book_label: str
    chapter: int
    bekker_range: str
    bekker_cols: tuple[str, ...]
    theme_en: str
    translator: str


@dataclass(frozen=True, slots=True)
class UnitSpec:
    """Specification of one multi-track Book Codex unit (``-en``, ``-el``, ``-summary``, ``-notes``).

    Attributes:
        slug: Directory and file stem under ``docsrc/loci_geometrici/``.
        order: Sequential ``:order:`` integer for the Book Codex TOC.
        liber_num: Roman numeral of the parent Liber (``"I"`` through ``"V"``).
        liber_title: Full title of the parent Liber.
        short_title: Concise unit title for navigation bars and TOCs.
        title_en: Full English track page title.
        title_el: Full Greek track page title.
        canonical_id: Short canonical locus badge (e.g. ``"Anal. Post. I.1–13"``).
        bekker_range: Full Bekker span badge (e.g. ``"Bekker 71a1–79a16"``).
        epigraph_el: Verbatim Greek epigraph from the unit's primary text.
        epigraph_en: Corresponding Oxford English translation of the epigraph.
        epigraph_locus: Bekker coordinate of the epigraph.
        chapters: Ordered tuple of ``ChapterSpec`` chapters included in this unit.
    """

    slug: str
    order: int
    liber_num: str
    liber_title: str
    short_title: str
    title_en: str
    title_el: str
    canonical_id: str
    bekker_range: str
    epigraph_el: str
    epigraph_en: str
    epigraph_locus: str
    chapters: tuple[ChapterSpec, ...]


CODEX_UNITS: tuple[UnitSpec, ...] = (
    UnitSpec(
        slug="liber-1a-apodeixis",
        order=10,
        liber_num="I",
        liber_title="Liber I — Analytica Posteriora: Demonstrative Science, Axioms & Nous",
        short_title="Liber I.A: Apodeixis, Axioms & Intellectual Vision (Anal. Post. I.1–13)",
        title_en="Liber I.A — Demonstrative Science, Axioms & Intellectual Vision",
        title_el="Ἀναλυτικῶν Ὑστέρων Α.1–13 — Περὶ ἀποδείξεως καὶ ἀρχῶν",
        canonical_id="Anal. Post. I.1–13",
        bekker_range="Bekker 71a1–79a16",
        epigraph_el="ταῦτα δ’ ἐστὶν οἷον ὁρᾶν τῇ νοήσει.",
        epigraph_en="And these things are as it were seen by intellectual vision.",
        epigraph_locus="Anal. Post. I.12, 77b30–31",
        chapters=(
            ChapterSpec("anal-post", "Posterior Analytics", "Ἀναλυτικῶν Ὑστέρων", "Analytica Posteriora", 1, "I", 1, "71a1–71b8", ("71a", "71b"), "Pre-existent Knowledge & Mathematical Learning", "G. R. G. Mure"),
            ChapterSpec("anal-post", "Posterior Analytics", "Ἀναλυτικῶν Ὑστέρων", "Analytica Posteriora", 1, "I", 2, "71b9–72b4", ("71b", "72a", "72b"), "Nature of Scientific Knowledge (Episteme) & First Principles", "G. R. G. Mure"),
            ChapterSpec("anal-post", "Posterior Analytics", "Ἀναλυτικῶν Ὑστέρων", "Analytica Posteriora", 1, "I", 3, "72b5–73a20", ("72b", "73a"), "Refutation of Infinite Regress & Circular Demonstration", "G. R. G. Mure"),
            ChapterSpec("anal-post", "Posterior Analytics", "Ἀναλυτικῶν Ὑστέρων", "Analytica Posteriora", 1, "I", 4, "73a21–74a3", ("73a", "73b", "74a"), "Predication 'Of All', Essential (Kath' Hauto) & Universal (Katholou)", "G. R. G. Mure"),
            ChapterSpec("anal-post", "Posterior Analytics", "Ἀναλυτικῶν Ὑστέρων", "Analytica Posteriora", 1, "I", 5, "74a4–74b4", ("74a", "74b"), "Errors in Attaining the Commensurate Universal (Triangle 2R & Alternating Proportion)", "G. R. G. Mure"),
            ChapterSpec("anal-post", "Posterior Analytics", "Ἀναλυτικῶν Ὑστέρων", "Analytica Posteriora", 1, "I", 6, "74b5–75a37", ("74b", "75a"), "Demonstration from Necessary & Essential Premises", "G. R. G. Mure"),
            ChapterSpec("anal-post", "Posterior Analytics", "Ἀναλυτικῶν Ὑστέρων", "Analytica Posteriora", 1, "I", 7, "75a38–75b20", ("75a", "75b"), "Prohibition of Genus-Crossing (Metabasis eis allo genos)", "G. R. G. Mure"),
            ChapterSpec("anal-post", "Posterior Analytics", "Ἀναλυτικῶν Ὑστέρων", "Analytica Posteriora", 1, "I", 8, "75b21–75b36", ("75b",), "Eternal Validity of Demonstrative Conclusions", "G. R. G. Mure"),
            ChapterSpec("anal-post", "Posterior Analytics", "Ἀναλυτικῶν Ὑστέρων", "Analytica Posteriora", 1, "I", 9, "75b37–76a30", ("75b", "76a"), "Proper Principles & Bryson's Quadrature of the Circle", "G. R. G. Mure"),
            ChapterSpec("anal-post", "Posterior Analytics", "Ἀναλυτικῶν Ὑστέρων", "Analytica Posteriora", 1, "I", 10, "76a31–77a4", ("76a", "76b", "77a"), "Definitions, Axioms (Koinai Ennoiai), Hypotheses & Postulates (Aitemata)", "G. R. G. Mure"),
            ChapterSpec("anal-post", "Posterior Analytics", "Ἀναλυτικῶν Ὑστέρων", "Analytica Posteriora", 1, "I", 11, "77a5–77a35", ("77a",), "Common Principles Across Distinct Sciences without Platonic Forms", "G. R. G. Mure"),
            ChapterSpec("anal-post", "Posterior Analytics", "Ἀναλυτικῶν Ὑστέρων", "Analytica Posteriora", 1, "I", 12, "77a36–78a21", ("77a", "77b", "78a"), "Geometrical Interrogation, Pseudographema & Intellectual Vision (77b30)", "G. R. G. Mure"),
            ChapterSpec("anal-post", "Posterior Analytics", "Ἀναλυτικῶν Ὑστέρων", "Analytica Posteriora", 1, "I", 13, "78a22–79a16", ("78a", "78b", "79a"), "Knowledge of the Fact (To Hoti) vs. Reasoned Fact (To Dioti) in Subalternate Sciences", "G. R. G. Mure"),
        ),
    ),
    UnitSpec(
        slug="liber-1b-universale-et-nous",
        order=11,
        liber_num="I",
        liber_title="Liber I — Analytica Posteriora: Demonstrative Science, Axioms & Nous",
        short_title="Liber I.B: Universal Proof, Exactitude & Intuitive Nous (Anal. Post. I.24, 27, 31; II.19)",
        title_en="Liber I.B — Universal Demonstration, Exactitude & Intuitive Nous",
        title_el="Ἀναλυτικῶν Ὑστέρων Α.24, 27, 31 & Β.19 — Καθόλου, ἀκρίβεια καὶ νοῦς",
        canonical_id="Anal. Post. I.24, 27, 31; II.19",
        bekker_range="Bekker 85a13–88a17, 99b15–100b17",
        epigraph_el="λείπεται νοῦν εἶναι τῶν ἀρχῶν.",
        epigraph_en="It remains that it is intuitive reason that grasps the primary premisses.",
        epigraph_locus="Anal. Post. II.19, 100b12",
        chapters=(
            ChapterSpec("anal-post", "Posterior Analytics", "Ἀναλυτικῶν Ὑστέρων", "Analytica Posteriora", 1, "I", 24, "85a13–86a30", ("85a", "85b", "86a"), "Superiority of Universal over Particular Demonstration", "G. R. G. Mure"),
            ChapterSpec("anal-post", "Posterior Analytics", "Ἀναλυτικῶν Ὑστέρων", "Analytica Posteriora", 1, "I", 27, "87a31–87a37", ("87a",), "Comparative Exactitude (Akribeia): Unit without Position vs. Point with Position", "G. R. G. Mure"),
            ChapterSpec("anal-post", "Posterior Analytics", "Ἀναλυτικῶν Ὑστέρων", "Analytica Posteriora", 1, "I", 31, "87b28–88a17", ("87b", "88a"), "Insufficiency of Sense-Perception (Aisthesis) for Geometric Science", "G. R. G. Mure"),
            ChapterSpec("anal-post", "Posterior Analytics", "Ἀναλυτικῶν Ὑστέρων", "Analytica Posteriora", 2, "II", 19, "99b15–100b17", ("99b", "100a", "100b"), "Genetic Ascent from Perception via Epagoge to Nous of First Principles", "G. R. G. Mure"),
        ),
    ),
    UnitSpec(
        slug="liber-2a-quantitas-et-syllogismus",
        order=20,
        liber_num="II",
        liber_title="Liber II — Organon Geometricum: Quantity, Syllogism & Definitions",
        short_title="Liber II.A: Quantity & Geometric Syllogism (Cat. 6; Anal. Prior. I.4, 23–24; II.16)",
        title_en="Liber II.A — Discrete & Continuous Quantity and Geometric Syllogism",
        title_el="Κατηγορίαι 6 & Ἀναλυτικὰ Πρότερα Α.4, 23–24, Β.16 — Περὶ ποσοῦ καὶ συλλογισμοῦ",
        canonical_id="Cat. 6; Anal. Prior. I.4, 23–24; II.16",
        bekker_range="Bekker 4b20–6a35, 25b–26a, 40b–41b, 64b–65a",
        epigraph_el="Τούτου δὲ τὸ μὲν διωρισμένον ἐστί, τὸ δὲ συνεχές.",
        epigraph_en="Quantity is either discrete or continuous.",
        epigraph_locus="Categoriae 6, 4b20",
        chapters=(
            ChapterSpec("categoriae", "Categories", "Κατηγορίαι", "Categoriae", None, "", 6, "4b20–6a35", ("4b", "5a", "5b", "6a"), "Discrete vs. Continuous Quantity: Number, Line, Surface, Body, Time & Place", "E. M. Edghill"),
            ChapterSpec("anal-prior", "Prior Analytics", "Ἀναλυτικῶν Προτέρων", "Analytica Priora", 1, "I", 4, "25b26–26b33", ("25b", "26a", "26b"), "First-Figure Syllogism (Barbara) & Universal Necessity (25b37–39)", "A. J. Jenkinson"),
            ChapterSpec("anal-prior", "Prior Analytics", "Ἀναλυτικῶν Προτέρων", "Analytica Priora", 1, "I", 23, "40b17–41b5", ("40b", "41a", "41b"), "Syllogistic Reduction & Proof of Incommensurability of the Diagonal (41a23–30)", "A. J. Jenkinson"),
            ChapterSpec("anal-prior", "Prior Analytics", "Ἀναλυτικῶν Προτέρων", "Analytica Priora", 1, "I", 24, "41b6–41b35", ("41b",), "Universal Premiss in Proof & Pre-Euclidean Proof of Isosceles Base Angles (41b13–22)", "A. J. Jenkinson"),
            ChapterSpec("anal-prior", "Prior Analytics", "Ἀναλυτικῶν Προτέρων", "Analytica Priora", 2, "II", 16, "64b28–65a37", ("64b", "65a"), "Petitio Principii & Circularity in Pre-Euclidean Parallel-Line Proofs (65a4–9)", "A. J. Jenkinson"),
        ),
    ),
    UnitSpec(
        slug="liber-2b-topica-definitiones",
        order=21,
        liber_num="II",
        liber_title="Liber II — Organon Geometricum: Quantity, Syllogism & Definitions",
        short_title="Liber II.B: Geometric Definitions & Antanairesis (Topics VI.4; VIII.3)",
        title_en="Liber II.B — Intelligible Priority in Definitions & Antanairesis",
        title_el="Τοπικῶν Ζ.4 & Θ.3 — Περὶ ὁρισμῶν καὶ ἀνταναιρέσεως",
        canonical_id="Topics VI.4; VIII.3",
        bekker_range="Bekker 141a23–142b19, 158a31–159a14",
        epigraph_el="τὴν αὐτὴν ἀνταναίρεσιν ἔχει τὰ χωρία καὶ αἱ βάσεις.",
        epigraph_en="The areas and the bases have the same reciprocal subtraction (antanairesis).",
        epigraph_locus="Topica VIII.3, 158b33–34",
        chapters=(
            ChapterSpec("topica", "Topics", "Τοπικῶν", "Topica", 6, "VI", 4, "141a23–142b19", ("141a", "141b", "142a", "142b"), "Prior by Nature vs. Prior to Us: Defining Point, Line, Plane & Solid", "W. A. Pickard-Cambridge"),
            ChapterSpec("topica", "Topics", "Τοπικῶν", "Topica", 8, "VIII", 3, "158a31–159a14", ("158a", "158b", "159a"), "Primary Hypotheses & Pre-Eudoxian Proportion by Antanairesis (158b29–35)", "W. A. Pickard-Cambridge"),
        ),
    ),
    UnitSpec(
        slug="liber-3a-mathematicus-et-infinitum",
        order=30,
        liber_num="III",
        liber_title="Liber III — Physica & De Caelo: Abstraction, Infinite, Place & Continuum",
        short_title="Liber III.A: Mathematical Separation & Potential Infinite (Phys. II.2; III.4–7)",
        title_en="Liber III.A — Physicist vs. Mathematician & the Potential Infinite",
        title_el="Φυσικῆς Ἀκροάσεως Β.2 & Γ.4–7 — Χωρισμὸς μαθηματικὸς καὶ ἄπειρον",
        canonical_id="Phys. II.2; III.4–7",
        bekker_range="Bekker 193b22–194b15, 202b30–208a4",
        epigraph_el="χωριστὰ γὰρ τῇ νοήσει κινήσεώς ἐστι, καὶ οὐδὲν διαφέρει, οὐδὲ γίγνεται ψεῦδος χωριζόντων.",
        epigraph_en="For in thought they are separable from motion, and it makes no difference, nor does any falsity result, if they are separated.",
        epigraph_locus="Physica II.2, 193b33–35",
        chapters=(
            ChapterSpec("physica", "Physics", "Φυσικῆς Ἀκροάσεως", "Physica", 2, "II", 2, "193b22–194b15", ("193b", "194a", "194b"), "Distinction Between Natural Philosophy & Mathematics: Separation in Thought", "R. P. Hardie & R. K. Gaye"),
            ChapterSpec("physica", "Physics", "Φυσικῆς Ἀκροάσεως", "Physica", 3, "III", 4, "202b30–204a7", ("202b", "203a", "203b", "204a"), "Predecessors on the Infinite (Apeiron) & Five Grounds for Belief in It", "R. P. Hardie & R. K. Gaye"),
            ChapterSpec("physica", "Physics", "Φυσικῆς Ἀκροάσεως", "Physica", 3, "III", 5, "204a8–206a8", ("204a", "204b", "205a", "205b", "206a"), "Impossibility of an Actual Infinite Sensible or Mathematical Body", "R. P. Hardie & R. K. Gaye"),
            ChapterSpec("physica", "Physics", "Φυσικῆς Ἀκροάσεως", "Physica", 3, "III", 6, "206a9–207a32", ("206a", "206b", "207a"), "Potential Existence of the Infinite by Division & Addition", "R. P. Hardie & R. K. Gaye"),
            ChapterSpec("physica", "Physics", "Φυσικῆς Ἀκροάσεως", "Physica", 3, "III", 7, "207a33–208a4", ("207a", "207b", "208a"), "Asymmetry of Number & Magnitude; Why Geometers Need Only Arbitrary Finite Lengths", "R. P. Hardie & R. K. Gaye"),
        ),
    ),
    UnitSpec(
        slug="liber-3b-topos-continuum-dimensio",
        order=31,
        liber_num="III",
        liber_title="Liber III — Physica & De Caelo: Abstraction, Infinite, Place & Continuum",
        short_title="Liber III.B: Place, Continuum, Zeno & Threefold Dimension (Phys. IV.1–5; VI.1–2, 9; De Caelo I.1)",
        title_en="Liber III.B — Place, the Continuum, Zeno's Paradoxes & Threefold Dimension",
        title_el="Φυσικῆς Δ.1–5, Ζ.1–2, 9 & Περὶ Οὐρανοῦ Α.1 — Τόπος, συνεχὲς καὶ διαστάσεις",
        canonical_id="Phys. IV.1–5; VI.1–2, 9; De Caelo I.1",
        bekker_range="Bekker 208a–213a, 231a–233b, 239b–240a, 268a–b",
        epigraph_el="ἀδύνατον ἐξ ἀδιαιρέτων εἶναί τι συνεχές, οἷον γραμμὴν ἐκ στιγμῶν, εἴπερ ἡ γραμμὴ μὲν συνεχές, ἡ στιγμὴ δὲ ἀδιαίρετον.",
        epigraph_en="It is impossible that anything continuous should be composed of indivisibles: for instance, a line cannot be composed of points, the line being continuous and the point indivisible.",
        epigraph_locus="Physica VI.1, 231a24–26",
        chapters=(
            ChapterSpec("physica", "Physics", "Φυσικῆς Ἀκροάσεως", "Physica", 4, "IV", 1, "208a27–209a30", ("208a", "208b", "209a"), "Existence & Aporiai of Place (Topos) & the Six Directions", "R. P. Hardie & R. K. Gaye"),
            ChapterSpec("physica", "Physics", "Φυσικῆς Ἀκροάσεως", "Physica", 4, "IV", 2, "209a31–210a13", ("209a", "209b", "210a"), "Place Neither Form nor Matter (Critique of Plato's Timaeus Receptacle)", "R. P. Hardie & R. K. Gaye"),
            ChapterSpec("physica", "Physics", "Φυσικῆς Ἀκροάσεως", "Physica", 4, "IV", 3, "210a14–210b31", ("210a", "210b"), "Senses of Being 'In' Something & Whether a Thing Can Be in Itself", "R. P. Hardie & R. K. Gaye"),
            ChapterSpec("physica", "Physics", "Φυσικῆς Ἀκροάσεως", "Physica", 4, "IV", 4, "210b32–212a30", ("210b", "211a", "211b", "212a"), "Definition of Place as the Innermost Motionless Boundary of the Containing Body", "R. P. Hardie & R. K. Gaye"),
            ChapterSpec("physica", "Physics", "Φυσικῆς Ἀκροάσεως", "Physica", 4, "IV", 5, "212a31–213a11", ("212a", "212b", "213a"), "Place of the Heaven & Resolution of the Topos Aporiai", "R. P. Hardie & R. K. Gaye"),
            ChapterSpec("physica", "Physics", "Φυσικῆς Ἀκροάσεως", "Physica", 6, "VI", 1, "231a21–232a22", ("231a", "231b", "232a"), "Structure of the Continuum: Why Lines Cannot Be Composed of Indivisible Points", "R. P. Hardie & R. K. Gaye"),
            ChapterSpec("physica", "Physics", "Φυσικῆς Ἀκροάσεως", "Physica", 6, "VI", 2, "232a23–233b32", ("232a", "232b", "233a", "233b"), "Isomorphic Divisibility of Magnitude & Time; First Refutation of Zeno", "R. P. Hardie & R. K. Gaye"),
            ChapterSpec("physica", "Physics", "Φυσικῆς Ἀκροάσεως", "Physica", 6, "VI", 9, "239b5–240a18", ("239b", "240a"), "Zeno's Four Arguments Against Motion (Dichotomy, Achilles, Arrow & Stadium)", "R. P. Hardie & R. K. Gaye"),
            ChapterSpec("de-caelo", "On the Heavens", "Περὶ Οὐρανοῦ", "De Caelo", 1, "I", 1, "268a1–268b10", ("268a", "268b"), "Completeness of Three Spatial Dimensions: Line, Surface & Solid Body", "J. L. Stocks"),
        ),
    ),
    UnitSpec(
        slug="liber-4-de-anima-phantasia",
        order=40,
        liber_num="IV",
        liber_title="Liber IV — De Anima: Imagination, Phantasma & Noetic Abstraction",
        short_title="Liber IV: Phantasia, Phantasma & Ta ex Aphaireseos (De Anima III.3–8)",
        title_en="Liber IV — Imagination, Phantasma & Mathematical Abstraction",
        title_el="Περὶ Ψυχῆς Γ.3–8 — Φαντασία, φάντασμα καὶ τὰ ἐξ ἀφαιρέσεως",
        canonical_id="De Anima III.3–8",
        bekker_range="Bekker 427a17–432a14",
        epigraph_el="διὸ οὐδέποτε νοεῖ ἄνευ φαντάσματος ἡ ψυχή.",
        epigraph_en="That is why the soul never thinks without an image (phantasma).",
        epigraph_locus="De Anima III.7, 431a16–17",
        chapters=(
            ChapterSpec("de-anima", "On the Soul", "Περὶ Ψυχῆς", "De Anima", 3, "III", 3, "427a17–429a9", ("427a", "427b", "428a", "428b", "429a"), "Distinction of Imagination (Phantasia) from Perception & Judgement", "J. A. Smith"),
            ChapterSpec("de-anima", "On the Soul", "Περὶ Ψυχῆς", "De Anima", 3, "III", 4, "429a10–430a9", ("429a", "429b", "430a"), "Receptive Intellect, Flesh vs. Snub, & Continuum vs. Essence of Straight", "J. A. Smith"),
            ChapterSpec("de-anima", "On the Soul", "Περὶ Ψυχῆς", "De Anima", 3, "III", 5, "430a10–430a25", ("430a",), "Active & Productive Intellect (Nous Poietikos) as Light", "J. A. Smith"),
            ChapterSpec("de-anima", "On the Soul", "Περὶ Ψυχῆς", "De Anima", 3, "III", 6, "430a26–431a1", ("430a", "430b", "431a"), "Thinking of Indivisibles: Undivided Length & Point/Division", "J. A. Smith"),
            ChapterSpec("de-anima", "On the Soul", "Περὶ Ψυχῆς", "De Anima", 3, "III", 7, "431a1–431b19", ("431a", "431b"), "Thinking in Phantasmata & Grasping Mathematicals (Ta ex Aphaireseos, 431b12–17)", "J. A. Smith"),
            ChapterSpec("de-anima", "On the Soul", "Περὶ Ψυχῆς", "De Anima", 3, "III", 8, "431b20–432a14", ("431b", "432a"), "The Soul as Place of Forms & Intrinsic Dependence of Noesis upon Phantasmata", "J. A. Smith"),
        ),
    ),
    UnitSpec(
        slug="liber-5a-scientiae-et-quantitas",
        order=50,
        liber_num="V",
        liber_title="Liber V — Metaphysica: Mathematical Sciences, Intelligible Matter, Actuality & Beauty",
        short_title="Liber V.A: Unity, Quantity & Theoretical Sciences (Metaph. B.2; Δ.6, 13; E.1)",
        title_en="Liber V.A — Mathematical Intermediates, Unity, Quantity & Theoretical Sciences",
        title_el="Τῶν μετὰ τὰ Φυσικὰ Β.2, Δ.6 & 13, Ε.1 — Ἕν, ποσὸν καὶ θεωρητικαὶ ἐπιστῆμαι",
        canonical_id="Metaph. B.2; Δ.6, 13; E.1",
        bekker_range="Bekker 996a–998a, 1015b–1017a, 1020a, 1025b–1026a",
        epigraph_el="ὥστε τρεῖς ἂν εἶεν φιλοσοφίαι θεωρητικαί, μαθηματική, φυσική, θεολογική.",
        epigraph_en="There must, then, be three theoretical philosophies, mathematics, physics, and what we may call theology.",
        epigraph_locus="Metaphysica E.1, 1026a18–19",
        chapters=(
            ChapterSpec("metaphysica", "Metaphysics", "Τῶν μετὰ τὰ Φυσικά", "Metaphysica", 3, "B (III)", 2, "996a18–998a19", ("996a", "996b", "997a", "997b", "998a"), "Aporiai on Axioms, Mathematical Intermediates & Protagoras's Tangent (997b35–998a6)", "W. D. Ross"),
            ChapterSpec("metaphysica", "Metaphysics", "Τῶν μετὰ τὰ Φυσικά", "Metaphysica", 5, "Δ (V)", 6, "1015b16–1017a6", ("1015b", "1016a", "1016b", "1017a"), "Lexicon of Unity (To Hen): Continuity, Indivisible Measure, Point & Monad (1016b24–31)", "W. D. Ross"),
            ChapterSpec("metaphysica", "Metaphysics", "Τῶν μετὰ τὰ Φυσικά", "Metaphysica", 5, "Δ (V)", 13, "1020a7–1020a32", ("1020a",), "Lexicon of Quantity (Poson): Numberable Multitude (Plethos) vs. Measurable Magnitude (Megethos)", "W. D. Ross"),
            ChapterSpec("metaphysica", "Metaphysics", "Τῶν μετὰ τὰ Φυσικά", "Metaphysica", 6, "E (VI)", 1, "1025b3–1026a32", ("1025b", "1026a"), "Tripartition of Theoretical Science: Physics, Mathematics & First Philosophy", "W. D. Ross"),
        ),
    ),
    UnitSpec(
        slug="liber-5b-hyle-noete-energeia-pulchritudo",
        order=51,
        liber_num="V",
        liber_title="Liber V — Metaphysica: Mathematical Sciences, Intelligible Matter, Actuality & Beauty",
        short_title="Liber V.B: Intelligible Matter, Diagrammatic Actuality & Beauty (Metaph. Z.10–11; Θ.9; M.1–3)",
        title_en="Liber V.B — Intelligible Matter, Constructive Actuality & Mathematical Beauty",
        title_el="Τῶν μετὰ τὰ Φυσικὰ Ζ.10–11, Θ.9, Μ.1–3 — Ὕλη νοητή, ἐνέργεια καὶ τὸ καλόν",
        canonical_id="Metaph. Z.10–11; Θ.9; M.1–3",
        bekker_range="Bekker 1034b–1037a, 1051a, 1076a–1078b",
        epigraph_el="καὶ τὰ διαγράμματα εὑρίσκεται ἐνεργείᾳ· διαιροῦντες γὰρ εὑρίσκουσιν. εἰ δ’ ἦν διῃρημένα, φανερὰ ἂν ἦν· νῦν δ’ ἐνυπάρχει δυνάμει.",
        epigraph_en="It is by an activity also that geometrical constructions are discovered; for we find them by dividing. If the figures had been already divided, the constructions would have been obvious; but as it is they are present only potentially.",
        epigraph_locus="Metaphysica Θ.9, 1051a21–24",
        chapters=(
            ChapterSpec("metaphysica", "Metaphysics", "Τῶν μετὰ τὰ Φυσικά", "Metaphysica", 7, "Z (VII)", 10, "1034b20–1036a25", ("1034b", "1035a", "1035b", "1036a"), "Parts of Definition vs. Parts of Matter & Introduction of Intelligible Matter (Hyle Noete, 1036a9)", "W. D. Ross"),
            ChapterSpec("metaphysica", "Metaphysics", "Τῶν μετὰ τὰ Φυσικά", "Metaphysica", 7, "Z (VII)", 11, "1036a26–1037a20", ("1036a", "1036b", "1037a"), "Formal Essence vs. Sensible & Intelligible Matter of the Circle", "W. D. Ross"),
            ChapterSpec("metaphysica", "Metaphysics", "Τῶν μετὰ τὰ Φυσικά", "Metaphysica", 9, "Θ (IX)", 9, "1051a4–1051a33", ("1051a",), "Constructive Actuality (Energeia) in Geometrical Discovery: Triangle 2R & Semicircle Angle (1051a21–33)", "W. D. Ross"),
            ChapterSpec("metaphysica", "Metaphysics", "Τῶν μετὰ τὰ Φυσικά", "Metaphysica", 13, "M (XIII)", 1, "1076a8–1076a37", ("1076a",), "Programmatic Inquiry into the Mode of Existence of Mathematical Objects", "W. D. Ross"),
            ChapterSpec("metaphysica", "Metaphysics", "Τῶν μετὰ τὰ Φυσικά", "Metaphysica", 13, "M (XIII)", 2, "1076a38–1077b16", ("1076a", "1076b", "1077a", "1077b"), "Refutation of Immanent & Separate Mathematical Solids: Priority in Formula vs. Substance", "W. D. Ross"),
            ChapterSpec("metaphysica", "Metaphysics", "Τῶν μετὰ τὰ Φυσικά", "Metaphysica", 13, "M (XIII)", 3, "1077b17–1078b6", ("1077b", "1078a", "1078b"), "Qua-Theory of Mathematical Objects & Mathematical Beauty: Order, Symmetry & Definiteness (1078a31–b6)", "W. D. Ross"),
        ),
    ),
)
