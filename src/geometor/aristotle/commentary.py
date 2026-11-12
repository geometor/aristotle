"""Scholarly summaries and dual-tradition critical commentary (Heath & Hoenen) for Libri I–V."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class UnitCommentary:
    """Editorial synopsis and analytical commentary for one Book Codex unit.

    Attributes:
        thesis: Concise architectural thesis of the unit.
        argument_steps: Ordered structural breakdown of the chapters in the unit.
        heath_analysis: Historical-mathematical commentary engaging Sir Thomas Heath
            and Euclid's *Elements*.
        hoenen_analysis: Epistemological-noetic commentary engaging Fr. Peter Hoenen S.J.,
            St. Thomas Aquinas, and Fra Luca Pacioli.
        crux_notes: Detailed locus-by-locus philological and mathematical notes.
    """

    thesis: str
    argument_steps: tuple[tuple[str, str], ...]
    heath_analysis: tuple[str, ...]
    hoenen_analysis: tuple[str, ...]
    crux_notes: tuple[tuple[str, str], ...]


UNIT_COMMENTARIES: dict[str, UnitCommentary] = {
    "liber-1a-apodeixis": UnitCommentary(
        thesis=(
            "In *Analytica Posteriora* I.1–13 (`71a1–79a16`), :person:`Aristotle <aristotle>` constructs the first "
            "rigorous meta-theory of deductive mathematical science (:term:`epistēmē <episteme>`). Answering "
            ":person:`Plato's <plato>` *Meno* paradox (`71a29`; :cite:`Meno 80d <plato:meno>`), Aristotle demonstrates "
            "that all intellectual teaching proceeds from pre-existent knowledge of two irreducible kinds—comprehension "
            "of meaning (*ti sēmainei*) and grasp of existence (*hoti estin*)—and classifies the indemonstrable starting "
            "points of geometry into :term:`definitions <horismos>`, :term:`hypotheses <hypothesis>`, "
            ":term:`postulates <aitema>`, and :term:`common axioms <axioma>`."
        ),
        argument_steps=(
            (
                "I.1–3 (71a1–73a20) — Pre-existent Knowledge, Apodeixis & Anti-Circularity",
                "Establishes that :term:`scientific demonstration <apodeixis>` requires premisses that are true, primary, immediate, better known by nature, prior to, and causes of the conclusion; refutes both sceptical infinite regress and circular proof.",
            ),
            (
                "I.4–6 (73a21–75a37) — Essential (Kath' Hauto) & Commensurate Universal (Katholou)",
                "Defines the three criteria of commensurate universality: holding of all (*kata pantos*), essentially (:term:`kath' hauto <kath-hauto>`), and *qua* the subject itself (*hēi auto*). Illustrates failure of commensurate universality when `2R` is proved separately of equilateral, isosceles, and scalene triangles rather than triangle *qua* triangle (`74a25–32`), and celebrates :person:`Eudoxus's <eudoxus>` general proof of alternating proportion (`74a17–25`).",
            ),
            (
                "I.7–9 (75a38–76a30) — Genus-Specificity & Critique of Bryson's Quadrature",
                "Formulates the prohibition of :term:`genus-crossing <metabasis>` (*metabasis eis allo genos*, `75a38`): arithmetic cannot prove properties of continuous geometric magnitudes except where one science is formally subalternated to another (as optics to geometry). Exposes :person:`Bryson's <bryson>` circle quadrature (`75b40`) as sophistical because it appeals to an unmediated non-geometrical generality.",
            ),
            (
                "I.10–11 (76a31–77a35) — The Architecture of Mathematical First Principles",
                "Draws the canonical distinction between common :term:`axioms <axioma>` ('equals subtracted from equals leave equals'), existential :term:`hypotheses <hypothesis>` (the unit, points, and lines), :term:`definitions <horismos>` (which state essence without asserting existence), and constructive :term:`postulates <aitema>` (`76b23–34`). Defends geometry against Platonic separate Forms (`77a5`).",
            ),
            (
                "I.12–13 (77a36–79a16) — Pseudographema, Intellectual Vision & Subalternation",
                "Distinguishes geometrical fallacies (*pseudographēmata*) from dialectical sophisms, utters the famous noetic maxim *'these things are as it were seen by intellectual vision'* (`ταῦτα δ’ ἐστὶν οἷον ὁρᾶν τῇ νοήσει`, `77b30`), and separates knowledge of the bare fact (:term:`to hoti <to-hoti-kai-dioti>`) from causal demonstration (:term:`to dioti <to-hoti-kai-dioti>`) across optics, harmonics, and astronomy.",
            ),
        ),
        heath_analysis=(
            "In :cite:`The Thirteen Books of Euclid's Elements <heath:euclid:1926>` (Vol. I, Ch. IX, pp. 117–151) and :cite:`Mathematics in Aristotle <heath:math-aristotle:1949>` (pp. 37–57), :person:`Sir Thomas Heath <heath>` demonstrates that *Posterior Analytics* I.2 and I.10 provide the exact theoretical blueprint that :person:`Euclid <euclid>` realized a generation later in Book I of the :cite:`Elements <euclid:elements>`. Aristotle's triad of *definitions* (`ὅροι`), *hypotheses/postulates* (`αἰτήματα`), and *common notions/axioms* (`τὰ κοινά` / `ἀξιώματα`) maps directly onto Euclid's tripartite opening apparatus.",
            "Particularly decisive for the history of fourth-century Greek mathematics is `74a17–25`: Aristotle remarks that *'formerly'* alternating proportion ($A : B = C : D \\implies A : C = B : D$) was proved separately for numbers, lines, solids, and times, whereas *'now'* it is proved universally of a single unnamed super-genus encompassing all of them. Heath identifies this watershed with :person:`Eudoxus of Cnidus's <eudoxus>` general theory of proportion preserved in :cite:`Elements V, Def. 5 & Prop. 16 <euclid:V.def.5>`.",
            "Equally revealing is Aristotle's critique of :person:`Bryson's <bryson>` circle quadrature (`75b37–76a3`). Whereas :person:`Antiphon <antiphon>` inscribed polygons until he imagined straight segments coinciding with the arc, Bryson circumscribed and inscribed squares/polygons and argued that because a circle is greater than all inscribed polygons and less than all circumscribed polygons, there must exist a square equal to the circle—an argument true at a purely quantitative level of continuity, yet geometrically non-constructive because it supplies no proper geometric middle term linking rectilinear and curvilinear bounds.",
        ),
        hoenen_analysis=(
            "In :cite:`De Noetica Geometriae <hoenen:noetica:1952>` (Caput I, §§ 1–2, pp. 9–18; Caput VII, n. 1), :person:`Fr. Peter Hoenen S.J. <hoenen>` elevates *Posterior Analytics* I.12 (`77b30–31`)—`ταῦτα δ’ ἐστὶν οἷον ὁρᾶν τῇ νοήσει` (*'and these mathematical things are as it were seen by intellectual vision'*)—into the hermeneutic keystone of geometric epistemology. Against nineteenth- and twentieth-century axiomatic formalism (:person:`Hilbert <hilbert>`, :cite:`Grundlagen der Geometrie <hilbert:grundlagen:1899>`), Hoenen insists that Aristotle never treated axioms and postulates as arbitrary uninterpreted stipulations: the deductively rigorous architecture of *apodeixis* rests upon an authentic :term:`noetic intuition <noesis>` (*intuitus mentis*) that reads necessary Nexus directly in mathematical reality.",
            "Engaging :person:`St. Thomas Aquinas's <thomas-aquinas>` :cite:`Expositio Libri Posteriorum Analyticorum <aquinas:in-anal-post>` (Lib. I, lect. 2 & lect. 19), Hoenen analyzes the subtle crux at `71a14–24` concerning how 'triangle' functions in geometric recognition: when a geometer recognizes an inscribed figure in a semicircle as a triangle (`71a19–21`), induction and intellectual insight occur *simultaneously* (*ἅμα ἐπαγόμενος*) because the singular diagram in imagination transparently exhibits the universal formal nature.",
            "In :cite:`De Divina Proportione <pacioli:divina:1509>` (Compendio Cap. II–III, fols. `2r–3r`), :person:`Fra Luca Pacioli <pacioli>` invokes *Posterior Analytics* I.7 (`75a38–b20`) and I.13 (`78b34–79a16`) to establish the Renaissance dignity of linear perspective alongside music, arithmetic, and geometry as subalternate mathematical sciences.",
        ),
        crux_notes=(
            (
                "71a19–24 — Recognition of the Triangle in the Semicircle",
                "Aristotle refers to recognizing a concrete figure drawn inside a semicircle as a triangle and immediately deducing `2R`. As :person:`Ross <ross>` (:cite:`Analytics, 1949 <ross:analytics:1949>`, ad loc.) and :person:`Heath <heath>` explain, the minor premiss ('this figure is a triangle') is grasped simultaneously with inspection of the construction, while the universal major ('every triangle has interior angles equal to two right angles', :cite:`Elements I.32 <euclid:I.32>`) is possessed beforehand.",
            ),
            (
                "74a17–25 — Eudoxus and the Unnamed Genus of Magnitude/Proportion",
                "Greek lacked a single noun spanning discrete number, spatial magnitude, and temporal duration (`ἀνώνυμον ἦν τι τούτοις πᾶσιν ἕν`). Aristotle's testimony proves that Book V of Euclid's *Elements* was already established in the Lyceum while preserving the ontological distinction between discrete :term:`multitude <plethos>` and continuous :term:`magnitude <megethos>` enforced in I.7.",
            ),
            (
                "76a31–77a4 — Axiom, Hypothesis, Definition, and Postulate",
                "Aristotle notes (`76b39–77a3`) that the geometer is unaffected by the crude redness or crookedness of the line drawn in dust (`οὐ γὰρ ᾗ τήνδε γέγραφεν... ἀλλὰ τὰ δηλούμενα διὰ τούτων`), because demonstration concerns the universal intelligible object signified through the diagram rather than the chalk or sand mark.",
            ),
            (
                "77b30–31 — Οἷον ὁρᾶν τῇ νοήσει ('As It Were Seen by Intellectual Vision')",
                "Speaking of geometric analysis where expressions are converted into definite figures, Aristotle observes that ambiguity vanishes because mathematical objects are 'as it were beheld by intellectual vision'—confirming the synergy of diagrammatic construction and :term:`noēsis <noesis>`.",
            ),
        ),
    ),
    "liber-1b-universale-et-nous": UnitCommentary(
        thesis=(
            "In *Analytica Posteriora* I.24, I.27, I.31, and II.19 (`85a–88a`, `99b–100b`), :person:`Aristotle <aristotle>` "
            "completes the epistemology of demonstrative science by establishing why commensurate universal proof excels "
            "particular proof, why arithmetic exceeds geometry in :term:`exactitude <akribeia>`, why sensory observation "
            "(*aisthēsis*) can never cross the threshold into scientific necessity (`87b35`), and how :term:`induction <epagoge>` "
            "from sense-perception culminates in :term:`nous <nous>` as the principle of principles."
        ),
        argument_steps=(
            (
                "I.24 (85a13–86a30) — Superiority of Universal over Particular Demonstration",
                "Refutes the illusion that particular proof is 'more direct', proving that only universal demonstration exhibits the intrinsic *propter quid* cause—why the exterior angles of any polygon sum to four right angles (`85b38`) or why triangle *qua* triangle possesses `2R` (`85b5`).",
            ),
            (
                "I.27 (87a31–87a37) — Exactitude (Akribeia): Monad without Position vs. Point with Position",
                "Ranks theoretical sciences by conceptual simplicity: a science from fewer principles is prior to and more exact than one 'by addition' (*ek prostheseōs*)—as arithmetic (`monas` = substance without position) is prior to geometry (`stigmē` = substance having position).",
            ),
            (
                "I.31 (87b28–88a17) — Refutation of Geometric Empiricism (87b35)",
                "Proves that sense-perception is necessarily bound to 'this here and now' (*tode ti, pou, kai nyn*). Even if we could directly *see* on a sensory triangle that its angles equal two right angles, we would still lack :term:`epistēmē <episteme>` and seek universal demonstration.",
            ),
            (
                "II.19 (99b15–100b17) — Genetic Ascent from Perception to Nous",
                "Resolves how immediate first principles become known without innate Platonic recollection: perception leaves memory, repeated memories form one experience (*empeiria*), and the universal comes to rest in the soul like a rallying battle-line (`100a12`), enabling :term:`nous <nous>` to intuit primary principles with certainty exceeding demonstration itself.",
            ),
        ),
        heath_analysis=(
            ":person:`Heath <heath>` (:cite:`Thirteen Books <heath:euclid:1926>`, Vol. I, p. 322; :cite:`Mathematics in Aristotle <heath:math-aristotle:1949>`, pp. 61–68) highlights `85b37–86a3` as our earliest explicit Greek attestation of the general theorem extending :cite:`Elements I.32 <euclid:I.32>`: that the exterior angles of *any* rectilinear figure (triangle, quadrilateral, etc.), when the sides are produced in order, are together equal to four right angles (`4R`). Proclus later preserved this corollary in his commentary on Euclid I.32.",
            "In `87a35–37`, Aristotle records the Pythagorean-Academic definition of the arithmetical :term:`unit <monas>` as 'substance without position' (`οὐσία ἄθετος`) and the geometrical :term:`point <stigme>` as 'substance having position' (`οὐσία θετός`). As Heath notes (Vol. I, p. 155), :person:`Euclid <euclid>` deliberately replaced this ontological definition in *Elements* I, Def. 1 (`Σημεῖόν ἐστιν, οὗ μέρος οὐθέν` — 'A point is that which has no part') to keep geometry independent of Pythagorean monadic ontology while retaining indivisibility.",
        ),
        hoenen_analysis=(
            "For :person:`Hoenen <hoenen>` (:cite:`De Noetica Geometriae <hoenen:noetica:1952>`, Caput III, n. 1, p. 71; Caput V, pp. 159–189), *Posterior Analytics* I.31 (`87b35–39`) and II.19 (`99b15–100b17`) form a single indivisible arch. In Caput III, Hoenen deploys `87b35`—*'even if it were possible to perceive by sense that the triangle has its angles equal to two right angles, we should still seek a demonstration'*—to demolish John Stuart Mill's and Hermann von Helmholtz's geometric empiricism. Sensory measurement always halts before a **threshold of exactitude** (*limen exactitudinis*); it can at best report approximate physical coincidence here and now, never strict equality (`= 2R`) or universal necessity.",
            "Conversely, in Caput V, Hoenen reads *Posterior Analytics* II.19 alongside :person:`Aquinas <thomas-aquinas>` (:cite:`In Anal. Post. II, lect. 20 <aquinas:in-anal-post>`) to show that :term:`epagōgē <epagoge>` is the exact opposite of Humean enumerative induction. Because mathematical form exists individuated in sensible and imaginative extension, a *single* clear imaginative presentation suffices—once sensible irrelevancies are abstracted—for :term:`nous <nous>` to apprehend the universal nexus immediately and infallibly.",
        ),
        crux_notes=(
            (
                "85b4–15 — Isosceles vs. Triangle Qua Triangle",
                "Aristotle contrasts knowing `2R` of bronze isosceles triangles with knowing it of triangle *qua* triangle: removing 'bronze' and 'isosceles' leaves `2R` intact, whereas removing 'figure' or 'limit' destroys it—exhibiting the exact method of isolating the commensurate subject.",
            ),
            (
                "87a35–37 — Ek Prostheseōs ('By Addition')",
                "Geometry arises 'by addition' to arithmetic not by adding empirical noise, but by adding spatial position (*thesis*) and continuous dimensionality to indivisibility.",
            ),
            (
                "87b35–88a5 — Sense-Perception vs. Universal Demonstration on the Moon & Triangle",
                "Even standing on the moon and watching the earth interpose itself (`87b39`) would reveal only an individual eclipse occurring *now*, until intellect grasps the universal middle term from the perceived instance.",
            ),
            (
                "100a12–100b17 — The Simile of the Routed Army & Nous as Archē Archēs",
                "Just as one soldier halting in a rout brings a second and then the whole phalanx back to order, one retained percept stabilizes the universal concept in the soul until *nous* grasps the immediate principle.",
            ),
        ),
    ),
    "liber-2a-quantitas-et-syllogismus": UnitCommentary(
        thesis=(
            "Liber II.A gathers :person:`Aristotle's <aristotle>` foundational logical-ontological texts on :term:`quantity <poson>` "
            "and geometric deduction from the *Organon*: *Categories* 6 (`4b20–6a35`) establishing the irreducible bifurcation "
            "between :term:`discrete <diorismenon>` and :term:`continuous <syneches>` quantity, and *Prior Analytics* I.4, "
            "I.23–24, and II.16 (`25b`, `40b–41b`, `64b–65a`) exhibiting syllogistic necessity, the *reductio* proof of the "
            ":term:`incommensurability of the diagonal <asymmetron>`, the pre-Euclidean proof of *Elements* I.5, and the "
            "circularity lurking in pre-Euclidean parallel-line theories."
        ),
        argument_steps=(
            (
                "Categories 6 (4b20–6a35) — Discrete vs. Continuous Quantity",
                "Divides quantity into *discrete* (number, spoken speech—parts share no common boundary) and *continuous* (line, surface, solid body, time, place—parts join at a common boundary: point for line, line for plane, plane for body). Establishes equality and inequality (`ἴσον τε καὶ ἄνισον`, `6a26`) as the distinctive proprietary mark of all quantity.",
            ),
            (
                "Prior Analytics I.4 (25b26–26b33) — First-Figure Syllogism (Barbara)",
                "Formulates the canonical universal syllogism (`25b37–39`): *'If A is predicated of all B, and B of all C, A must be predicated of all C'*—introducing schematic letter-variables into formal logic on the model of Greek geometric lettering.",
            ),
            (
                "Prior Analytics I.23 (40b17–41b5) — Syllogism per Impossibile & the Diagonal (41a23–30)",
                "Shows that ostensive and *reductio* proofs alike reduce to the three syllogistic figures, citing the famous Pythagorean proof that if the diagonal of a square is assumed commensurable with its side, odd numbers turn out equal to even (`περισσὰ ἴσα γίνεσθαι τοῖς ἀρτίοις`, `41a26–27`).",
            ),
            (
                "Prior Analytics I.24 (41b6–41b35) — Pre-Euclidean Proof of Isosceles Base Angles (41b13–22)",
                "Illustrates why every demonstration requires at least one universal premiss through a remarkable pre-Euclidean proof of :cite:`Elements I.5 <euclid:I.5>` utilizing mixed (rectilinear-curvilinear) angles of a circle!",
            ),
            (
                "Prior Analytics II.16 (64b28–65a37) — Petitio Principii in Parallel Lines (65a4–9)",
                "Diagnoses begging the question (*to en archēi aiteisthai*) in contemporary fourth-century geometers who 'think they draw parallel lines' (`οἱ τὰς παραλλήλους οἰόμενοι γράφειν`, `65a4`) while unconsciously assuming facts logically equivalent to the Parallel Postulate itself.",
            ),
        ),
        heath_analysis=(
            "Few chapters in antiquity are more precious to the historian of geometry than *Prior Analytics* I.23, I.24, and II.16. First, at `41a23–30`, Aristotle preserves the authentic Pythagorean *reductio* proving the irrationality of $\\sqrt{2}$ (which once stood as an appendix to Book X of :cite:`Euclid's Elements <euclid:elements>`, Vol. III, p. 2). Assuming $d/s = m/n$ in lowest terms, $d^2 = 2s^2 \\implies m^2 = 2n^2$, making $m$ even ($m = 2k$), whence $4k^2 = 2n^2 \\implies n^2 = 2k^2$, making $n$ also even despite being odd—so odd numbers equal even!",
            "Second, at `41b13–22`, :person:`Heath <heath>` (:cite:`Thirteen Books <heath:euclid:1926>`, Vol. I, pp. 252–253; :cite:`Mathematics in Aristotle <heath:math-aristotle:1949>`, pp. 23–25) reconstructs Aristotle's archaic proof of *Pons Asinorum* (:cite:`Elements I.5 <euclid:I.5>`). Let $AB$, $AC$ be equal radii of a circle centered at $A$, with chord $BC$. Aristotle takes the two 'angles of the semicircle' ($\\angle AC,\\text{arc }CB$ and $\\angle AB,\\text{arc }BC$) as equal (`A = B`), and the two mixed 'angles of the segment' ($\\angle CB,\\text{arc }BC$ and $\\angle BC,\\text{arc }CB$) as equal (`C = D`), and subtracts the equal segment-angles from the equal semicircle-angles to leave the rectilinear base angles $\\angle ABC = \\angle ACB$ (`E = F`)! Because :person:`Euclid <euclid>` banished mixed horn-like/segment angles from deductive geometry (save one vestige in III.16), Euclid invented his famous purely rectilinear construction in I.5.",
            "Third, at `65a4–9`, Aristotle exposes a circularity in Academy-era theories of parallels (`οἱ τὰς παραλλήλους οἰόμενοι γράφειν`). Heath (Vol. I, pp. 190–194, 202–204) shows that fourth-century geometers tried to prove parallel-line properties without a parallel postulate—for example by assuming a direction/equidistance lemma that covertly presupposes :cite:`Elements I.29 <euclid:I.29>`. Directly responding to Aristotle's critique, Euclid cut the Gordian knot by laying down his monumental Fifth Postulate.",
        ),
        hoenen_analysis=(
            "In :cite:`De Noetica Geometriae <hoenen:noetica:1952>` (Caput IV, n. 27 & n. 30, pp. 145–149), :person:`Hoenen <hoenen>` examines *Prior Analytics* I.4 (`25b37–39`) and I.23 alongside :person:`Theodor Waitz's <waitz>` commentary (:cite:`Organon, 1844 <waitz:organon:1844>`, Vol. I, pp. 427–429). Modern symbolic logicians frequently claim Aristotle's lettered schema (*A, B, C*) as the birth of content-free syntactic formalism. Hoenen demonstrates the exact opposite: Aristotle borrowed schematic letters from geometric diagrams (`ἔκθεσις`), and in `41b13–22` shows that even when a geometric proof is cast into syllogistic form, the minor premisses (`C = D` for the angles of the segment) and subtraction axiom (`equals from equals`) require active intellectual inspection of continuous :term:`intelligible matter <hyle-noete>`.",
            "Furthermore, *Categories* 6 (`4b20–5a14`) provides the ontological bedrock for Hoenen's defence of geometric continuity against nineteenth-century 'arithmetization of the continuum': discrete number (:term:`diōrismenon <diorismenon>`) and continuous extension (:term:`syneches <syneches>`) differ in their very mode of unity, because parts of a line unite at a shared indivisible boundary (:term:`stigmē <stigme>`), whereas units of a number never touch or share a common limit.",
        ),
        crux_notes=(
            (
                "4b20–5a14 — Common Boundary (Koinos Horos) as Criterion of the Continuum",
                "In *Categories* 6, Aristotle defines continuous quantity via the existence of a common boundary at which adjacent parts meet: the point for a line, the line for a surface, the surface for a solid, and the 'now' (*to nyn*) for past and future time. In *Physics* V.3 and VI.1 he refines this into 'extremities being one' (`ὧν τὰ ἔσχατα ἕν`).",
            ),
            (
                "25b37–39 — Geometric Origins of Syllogistic Lettering",
                "Aristotle's schematic variables (`Α, Β, Γ`) derive directly from lettering endpoints and regions in Greek geometric diagrams, where spatial inclusion models universal predication.",
            ),
            (
                "41b13–22 — Mixed Curvilinear Angles Before Euclid",
                "Aristotle's casual use of mixed angles (`αἱ τῶν τμημάτων γωνίαι`) proves how fluidly pre-Euclidean textbooks appealed to symmetrical superposition in circles before Euclid imposed strict rectilinear rigor.",
            ),
            (
                "65a4–9 — The Genesis of Euclid's Fifth Postulate",
                "Aristotle's diagnosis of circular parallel proofs (`λανθάνουσι γὰρ αὐτοὶ ἑαυτοὺς τοιαῦτα λαμβάνοντες ἃ οὐχ οἷόν τε ἀποδεῖξαι μὴ οὐσῶν τῶν παραλλήλων`) is our single most important witness to why Euclid elevated Postulate 5 into an explicit unproved constructive/geometric postulate.",
            ),
        ),
    ),
    "liber-2b-topica-definitiones": UnitCommentary(
        thesis=(
            "In *Topics* VI.4 (`141a23–142b19`) and VIII.3 (`158a31–159a14`), :person:`Aristotle <aristotle>` establishes "
            "the canon of scientific :term:`definition <horismos>`—insisting that geometric entities must be defined through "
            "what is *prior and more intelligible by nature* rather than through sensible posterior effects—and preserves "
            "the priceless pre-Eudoxian definition of geometric proportion through :term:`antanairesis <antanairesis>` "
            "(reciprocal subtraction, `158b29–35`)."
        ),
        argument_steps=(
            (
                "Topics VI.4 (141a23–142b19) — Intelligible Priority in Defining Point, Line, Plane & Solid",
                "Distinguishes what is better known 'to us' (*hēmin*, sensible solid bodies) from what is better known 'unqualifiedly / by nature' (*haplōs*, point -> line -> plane -> solid). Critiques definitions that invert natural priority by defining point as 'limit of a line' or line as 'limit of a plane' (`141b19–22`), as well as circular definitions.",
            ),
            (
                "Topics VIII.3 (158a31–159a14) — Primary Hypotheses & Proportion via Antanairesis (158b29–35)",
                "Explains why certain arguments are difficult to attack or establish because they stand near primary hypotheses, illustrating how in mathematics even proving that Parallelograms/Triangles of the same height are proportional to their bases (:cite:`Elements VI.1 <euclid:elements>`) was once arduous before the clear definition of 'having the same ratio' via *antanairesis* (`τὴν αὐτὴν ἀνταναίρεσιν ἔχει τὰ χωρία καὶ αἱ βάσεις`, `158b33–34`).",
            ),
        ),
        heath_analysis=(
            ":person:`Heath <heath>` cites *Topics* VI.4 *eleven separate times* in Volume I of :cite:`The Thirteen Books of Euclid's Elements <heath:euclid:1926>` (pp. 146, 155–171) because it illuminates every single opening definition of Euclid Book I (`Defs. 1–7, 13–14`). Aristotle reports both ways fourth-century geometers defined the hierarchy of dimensions: (a) negatively/generatively from the prior (`point` -> `line` as breadthless length -> `surface`), and (b) as *limits* (`πέρατα`) from the posterior (`point` as extremity of a line, `line` as extremity of a surface). Remarkably, :person:`Euclid <euclid>` included *both* in Book I! Definitions 1, 2, and 5 define point, line (`μῆκος ἀπλατές`), and surface intrinsically, while Definitions 3 (`Γραμμῆς δὲ πέρατα σημεῖα`) and 6 (`Ἐπιφανείας δὲ πέρατα γραμμαί`) link them as extremities so both intelligible priority and pedagogical accessibility are satisfied!",
            "Even more momentous for modern scholarship is *Topics* VIII.3 (`158b29–35`). Following Oskar Becker (1933) and :person:`Heath <heath>` (:cite:`Mathematics in Aristotle <heath:math-aristotle:1949>`, pp. 80–83; cf. :person:`Alexander of Aphrodisias <alexander>`, *In Top.* 545.12), this six-line passage unlocked the lost pre-Eudoxian theory of general geometric proportions developed by :person:`Theaetetus <theaetetus>`! Before :person:`Eudoxus <eudoxus>` created Definition 5 of Book V, Greek geometers extended proportionality to incommensurable magnitudes by defining $A : B = C : D$ to mean that the Euclidean division algorithm of **reciprocal subtraction** (:term:`antanairesis <antanairesis>`, i.e., continued-fraction expansion; preserved in :cite:`Elements X.2–3 <euclid:X.2>`) produces the exact same infinite sequence of integer quotients $[q_0; q_1, q_2, \\dots]$ for $(A, B)$ and $(C, D)$!",
        ),
        hoenen_analysis=(
            "From the standpoint of geometric noetics (:cite:`De Noetica Geometriae <hoenen:noetica:1952>`, Caput I, § 4 & Caput IV), *Topics* VI.4 and VIII.3 jointly reveal how genuine mathematical progress refines *definitions* through deeper insight into continuous extension. In VI.4 (`141b5–14`), Aristotle notes that only a trained scientific intellect (*akribēs dianoia*) grasps the uncompounded intelligible priority of point and line, whereas ordinary sense-bound minds begin from three-dimensional tangible bodies—explaining why pedagogical *via inventionis* proceeds from sensible solids via abstraction while deductive *via doctrinae* descends from simplest principles.",
            "And in *Topics* VIII.3 (`158b32–35`), note Aristotle's striking remark: *'once the definition is stated, what is said becomes immediately manifest (`εὐθέως φανερὸν τὸ λεγόμενον`), for the areas and the bases have the same antanairesis.'* Subtracting base from base induces an identical geometric subtraction of rectangle/parallelogram from rectangle/parallelogram—an immediate visual-noetic invariance read directly off the subdivided figure!",
        ),
        crux_notes=(
            (
                "141b5–22 — Prior by Nature vs. Prior to Us in Geometry",
                "Sensible bodies are first in the order of genetic perception (*quoad nos*), but point, line, and plane are prior in essential simplicity (*quoad naturam*) because solid presupposes surface and surface presupposes line.",
            ),
            (
                "142a22–31 — Circular Definitions of the Straight Line",
                "Aristotle warns against covertly using the definiendum in the definiens, illustrating contemporary Academy attempts to define the straight line (cf. Plato *Parmenides* 137e: 'that of which the middle stands in front of both extremes').",
            ),
            (
                "158b29–35 — Antanairesis and the Golden Ratio",
                "In GEOMETOR, *antanairesis* connects Aristotle directly to the **Divine Proportion** ($\\phi = \\frac{1+\\sqrt{5}}{2}$): dividing a line in extreme and mean ratio produces the simplest possible non-terminating *antanairesis* $[1; 1, 1, 1, \\dots]$, immediately proving irrationality by self-similar geometric recursion.",
            ),
        ),
    ),
    "liber-3a-mathematicus-et-infinitum": UnitCommentary(
        thesis=(
            "In *Physics* II.2 (`193b22–194b15`) and III.4–7 (`202b30–208a4`), :person:`Aristotle <aristotle>` demarcates "
            "the exact ontological boundary between physics and geometry—showing how the mathematician legitimately "
            ":term:`separates <chorismos>` surfaces, volumes, lengths, and points in thought from sensible motion without "
            "incurring falsity (`193b31–35`)—and constructs his revolutionary theory of the :term:`potential infinite <apeiron>` "
            "(*dynamei apeiron*), proving that geometers require no actual infinite line (`207b27–34`)."
        ),
        argument_steps=(
            (
                "Physics II.2 (193b22–194b15) — Natural Philosopher vs. Mathematician: Curve vs. Snub",
                "Physical bodies contain surfaces, volumes, lines, and points (`193b24`), yet the mathematician treats them *not qua boundaries of natural mobile bodies*. Contrasts 'the curved' (*to kampylon*, defined without sensible matter) with 'the snub' (*to simon*, concavity essentially bound up with nose-flesh), while noting that optics, harmonics, and astronomy are 'the more physical branches of mathematics' (`τὰ φυσικώτερα τῶν μαθημάτων`, `194a7`).",
            ),
            (
                "Physics III.4–5 (202b30–206a8) — Aporiai of the Infinite & Refutation of Actual Infinite Body",
                "Catalogues the five classical reasons why thinkers posit an infinite—time, infinite divisibility of magnitudes, unceasing generation, finite boundaries, and inexhaustibility in thought (`203b15–30`)—and demonstrates both physically and generally that no actual infinite sensible or mathematical body can exist.",
            ),
            (
                "Physics III.6 (206a9–207a32) — Potential Existence of the Infinite (Dynamei Apeiron)",
                "Saves both continuous division and number without an actual infinite: the infinite exists *potentially*, like a day or the Olympic games whose being consists in one thing always coming into existence after another (`206a21–25`). Reverses the vulgar definition: the infinite is *not* 'that outside which nothing is', but **'that outside which there is always something'** (`οὗ ἀεί τι ἔξω ἐστίν`, `206b33–207a2`).",
            ),
            (
                "Physics III.7 (207a33–208a4) — Inverse Asymmetry of Number & Magnitude; Sufficiency for Geometry",
                "Establishes the exact duality: number has a minimum (the indivisible :term:`monad <monas>`) and is potentially infinite by *addition*, whereas continuous :term:`magnitude <megethos>` has a maximum (bounded by the finite cosmos) and is potentially infinite by *division* (`207b1–15`). Concludes (`207b27–34`) that this deprives mathematicians of nothing: they need only a finite straight line as long as they please (`ὅσην ἂν βούλωνται πεπερασμένην`), since any given ratio in the largest magnitude can be cut identically in the smallest!",
            ),
        ),
        heath_analysis=(
            ":person:`Heath <heath>` (:cite:`Thirteen Books <heath:euclid:1926>`, Vol. I, pp. 199, 232–234; :cite:`Mathematics in Aristotle <heath:math-aristotle:1949>`, pp. 98–113) shows that *Physics* III.7 (`207b27–34`) directly explains the wording of **Euclid's Second Postulate**! Notice that :person:`Euclid <euclid>` does *not* postulate an actually infinite straight line; instead, Postulate 2 reads: `Καὶ πεπερασμένην εὐθεῖαν κατὰ τὸ συνεχὲς ἐπ’ εὐθείας ἐκβαλεῖν` (*'To produce a finite straight line continuously in a straight line'*—i.e., to whatever finite length a construction requires). Euclid's constructively extensible finite segment is the exact formalization of Aristotle's `ὅσην ἂν βούλωνται πεπερασμένην` (`207b30`)!",
            "Furthermore, in `206a16–29` and `206b3–12`, Aristotle clearly distinguishes convergent geometric bisection (cutting off a constant *ratio*, such as $\\frac{1}{2}, \\frac{1}{4}, \\frac{1}{8}, \\dots$, which never exhausts the finite segment) from subtracting a fixed *equal finite magnitude* repeatedly, which necessarily exhausts and surpasses any finite whole (`πᾶν γὰρ πεπερασμένον ἀναιρεῖ ὁτῳοῦν ὡρισμένῳ`, `206b11–12`)—an explicit formulation of the **Axiom of Archimedes / Eudoxus** (:cite:`Elements V, Def. 4 & X.1 <euclid:V.def.5>`).",
        ),
        hoenen_analysis=(
            "In :cite:`De Noetica Geometriae <hoenen:noetica:1952>` (Caput I, § 3; Caput VI), *Physics* II.2 (`193b31–35`) provides the charter for Aristotelian-Thomistic **formal abstraction** (:term:`separatio in intellectu / abstractio formalis <chorismos>`). Unlike the Platonists ('those who speak of Ideas', `193b36`), who hypostatize physical attributes that cannot even be thought apart from flesh and motion, the geometer isolates continuous quantity (`τὸ κοῖλον` / `τὸ καμπύλον`), which genuinely possesses intrinsic intelligibility prior to sensible qualities (`οὐδὲ γίγνεται ψεῦδος χωριζόντων` — 'nor does any falsity arise when they separate them', `193b35`, echoed in Scholasticism as *abstrahentium non est mendacium*).",
            "Equally vital for Hoenen (Caput IV & VI) is Aristotle's diagnosis at `203b22–25` of why mathematicians are tempted by an actual infinite: *'because in thought (`ἐν τῇ νοήσει`) it never gives out.'* Aristotle answers at `208a14–19` that thinking something larger does not make it exist outside thought; geometric truth tracks real potential divisibility grounded in continuous extension, anticipating constructive mathematics' critique of ungrounded cantorian actualities.",
        ),
        crux_notes=(
            (
                "193b31–194a7 — 'The Snub' (To Simon) vs. 'The Concave' (To Koilon)",
                "Aristotle's celebrated contrast: 'concave' contains only pure spatial curvature in intelligible extension, whereas 'snub' embeds sensible matter (a nose) inside its very essence—mirroring geometry vs. physics.",
            ),
            (
                "206b33–207a14 — Inversion of Parmenides' & Melissus' Concept of Perfection",
                "Against Melissus, Aristotle sides with :person:`Parmenides <plato>` and the Pythagoreans: the whole and complete (*teleion*) is what possesses limit and form, whereas the *apeiron* is the indeterminate *matter* (`ὕλη`) of magnitude completion.",
            ),
            (
                "207b27–34 — Scale Invariance (Homothety) Replaces Actual Infinity",
                "Aristotle proves with extraordinary geometric elegance why cosmic finitude never restricts Euclidean geometry: any ratio or construction requiring an 'arbitrarily huge' diagram can be executed homothetically by dividing an arbitrarily small segment in the exact same ratio (`τεμεῖν γὰρ ἔστιν εἰς τὸν αὐτὸν λόγον τῷ μεγίστῳ μεγέθει ἕτερον πηλικονοῦν`, `207b31–33`).",
            ),
        ),
    ),
    "liber-3b-topos-continuum-dimensio": UnitCommentary(
        thesis=(
            "Liber III.B unites the crowning physical-geometrical analyses of spatial order, continuity, and dimensionality: "
            "*Physics* IV.1–5 (`208a27–213a11`) defining :term:`place <topos>` as the innermost motionless boundary of the "
            "containing body, *Physics* VI.1–2 & VI.9 (`231a21–233b32`, `239b5–240a18`) proving that no :term:`continuum <syneches>` "
            "can be composed of indivisible points and resolving :person:`Zeno's <zeno>` four paradoxes, and *De Caelo* I.1 "
            "(`268a1–b10`) demonstrating the completeness of three spatial dimensions."
        ),
        argument_steps=(
            (
                "Physics IV.1–3 (208a27–210b31) — Existence & Aporiai of Place (Topos)",
                "Establishes the reality of place from mutual replacement (*antimetastasis*, `208b1`) and natural directional motions, notes that mathematical objects, though lacking physical place, exhibit positional right/left relative to us (`208b22–25`), refutes :person:`Plato's <plato>` identification of space (*chōra*) with matter in the :cite:`Timaeus <plato:timaeus>` (`209b11–17`), and distinguishes eight senses of 'in' (`210a14–24`).",
            ),
            (
                "Physics IV.4–5 (210b32–213a11) — Place as Motionless Innermost Boundary (212a20)",
                "Eliminates form, matter, and self-subsistent three-dimensional interval (*diastēma*), concluding that :term:`place <topos>` is **the first motionless boundary of that which contains** (`τὸ τοῦ περιέχοντος πέρας ἀκίνητον πρῶτον`, `212a20–21`), solving Zeno's regress of places (`210b22`, `212b29`).",
            ),
            (
                "Physics VI.1–2 (231a21–233b32) — Indivisibility of Points & Isomorphism of Space, Time & Motion",
                "Demonstrates apodictically that no continuum can be made of indivisibles (`ἀδύνατον ἐξ ἀδιαιρέτων εἶναί τι συνεχές, οἷον γραμμὴν ἐκ στιγμῶν`, `231a24–25`), because partless points have neither extremities that can become one nor parts to touch part-to-part, nor can two points even be 'successive' (*ephexēs*) since a divisible line always lies between any two distinct points (`231b9`). Proves via reciprocal comparison of faster and slower motions (`232b20–233a12`) that magnitude, time, and motion share identical infinite divisibility.",
            ),
            (
                "Physics VI.9 (239b5–240a18) — Refutation of Zeno's Four Paradoxes of Motion",
                "States and refutes :person:`Zeno's <zeno>` Dichotomy (`239b11`), Achilles (`239b14`), Flying Arrow (`239b5`, `239b30`—resting on the false premise that time is composed of indivisible 'nows'), and Moving Rows / Stadium (`239b33–240a18`).",
            ),
            (
                "De Caelo I.1 (268a1–268b10) — Completeness of Three Spatial Dimensions",
                "Defines the continuous as divisible into ever-divisibles and body as divisible in every way (`πάντῃ διαιρετόν`): magnitude in one dimension is line, in two plane, in three solid body (`268a6–8`), beyond which there is **no transition into another dimension-genus** (`οὐκ ἔστιν εἰς ἄλλο γένος μετάβασις`, `268b1`).",
            ),
        ),
        heath_analysis=(
            ":person:`Heath <heath>` (:cite:`Mathematics in Aristotle <heath:math-aristotle:1949>`, pp. 120–139, 159–160; :cite:`Thirteen Books <heath:euclid:1926>`, Vol. I, pp. 156, 158, 232) marvels at the sheer mathematical rigor of *Physics* VI.1–2. Aristotle's proof (`232b20–233a17`) that any hypothesis of atomic magnitudes or atomic time-quanta collapses under a rational velocity ratio (e.g. $3 : 2$ at `233b19–32`, forcing the supposedly indivisible middle time-atom to be bisected!) is a masterpiece of Greek proportion theory.",
            "In resolving :person:`Zeno's <zeno>` Dichotomy (`233a21–31`, `239b11–14`), Aristotle identifies the exact fallacy that confused thinkers for two millennia: Zeno illicitly played off the **infinity by division** of the spatial interval against the **finitude in extent** of the time, forgetting that the finite time $T$ possesses the *exact same* potential infinity by division ($\\frac{T}{2}, \\frac{T}{4}, \\frac{T}{8}, \\dots$) as the finite segment $L$!",
            "In *De Caelo* I.1 (`268b1–6`), which Heath cites directly on *Elements* XI, Def. 1 ('A solid is that which has length, breadth, and depth', Vol. III, p. 260), Aristotle notes that while one passes from length (1D) to surface (2D) and from surface to body (3D), no fourth perpendicular spatial magnitude exists in physical/intuitive extension.",
        ),
        hoenen_analysis=(
            "In :cite:`De Noetica Geometriae <hoenen:noetica:1952>` (Caput IV, n. 7; Caput VI; Appendix, n. 10, pp. 251–255), :person:`Hoenen <hoenen>` devotes sustained attention to *Physics* IV.1–5 and VI.1. First, in the Appendix (`212b14`), Hoenen analyzes Aristotle's boundary definition of :term:`place <topos>` to show how relational localization (*ubi*) anchors physical geometry in actual bodies while mathematical geometry abstracts pure positional extension (*situs*).",
            "Second, Hoenen underscores *Physics* VI.1 (`231a21–b18`) as an eternal warning against reducing the geometric continuum to a set-theoretic dust of unextended points! Modern point-set topology models a line segment $[0, 1]$ via a set of real-number coordinates, which is a powerful analytical representation; yet noetically and ontologically, as Aristotle proved, unextended points can never generate extension by juxtaposition (`στιγμῶν δ’ αἰεὶ τὸ μεταξὺ γραμμή`, `231b9`). Continuous extension is *primary*, and points exist within it as indivisible boundaries and potential divisions.",
            "In :cite:`De Divina Proportione <pacioli:divina:1509>` (Dedication, fols. `A1r–A1v`; Compendio Cap. V, fols. `3v–4r`), :person:`Luca Pacioli <pacioli>` repeatedly invokes Aristotle's *De Caelo* (*In Coelo et Mundo*) alongside Plato's *Timaeus* on the cosmic perfection of solid geometry and the five regular bodies.",
        ),
        crux_notes=(
            (
                "208b22–25 — Relative Position in Mathematical Objects",
                "Though pure mathematical figures are not in physical *topos*, they acquire right, left, above, and below relative to the observer's orientation—anticipating handedness and chirality in space.",
            ),
            (
                "212a20–21 — Topos as Two-Dimensional Surface Boundary",
                "By defining place as the innermost *motionless* surface of the surrounding medium (as a boat in a flowing river is in the whole river-basin *qua* motionless rather than the shifting water), Aristotle avoids an infinite regress of three-dimensional spaces.",
            ),
            (
                "231b6–10 — Density of Points vs. Primacy of the Line",
                "Aristotle's theorem `'between any two points there is always a line'` (`στιγμῶν δ’ αἰεὶ τὸ μεταξὺ γραμμή`) anticipates Hilbert's axioms of order/density while preserving the ontological priority of continuous interval over point-limits.",
            ),
            (
                "239b5–9, 30–33 — Zeno's Flying Arrow & Indivisible 'Nows'",
                "Motion and rest both require an extended interval of time; in an indivisible instant (*to nyn*, analogous to a point on a line), a body neither moves nor rests (`234a24–b9`), dissolving the Arrow paradox at its root.",
            ),
        ),
    ),
    "liber-4-de-anima-phantasia": UnitCommentary(
        thesis=(
            "In *De Anima* III.3–8 (`427a17–432a14`), :person:`Aristotle <aristotle>` unveils the cognitive psychology "
            "that makes geometry possible for an embodied intellect: distinguishing :term:`imagination <phantasia>` from "
            "both sensation and judgment, distinguishing receptive and active :term:`intellect <nous>`, explaining how the "
            "mind thinks undivided continuous lengths and indivisible boundaries (`430b6–20`), and establishing the "
            "canonical law that **the soul never thinks without a phantasm** (`431a16`, `432a8`) and thinks mathematicals "
            "(:term:`ta ex aphaireseōs <aphairesis>`, `431b12–17`) within imaginative forms."
        ),
        argument_steps=(
            (
                "De Anima III.3 (427a17–429a9) — Isolation of Phantasia Between Sensation & Belief",
                "Separates perceiving, imagining, and judging: perception of proper sensibles is true, belief (*doxa*) entails conviction (*pistis*), whereas :term:`phantasia <phantasia>` is a movement arising from actual perception (`κίνησις ὑπὸ τῆς αἰσθήσεως τῆς κατ’ ἐνέργειαν γιγνομένη`, `429a1–2`) capable of Voluntary figurative construction before the mind's eye (`πρὸ ὀμμάτων γὰρ ἔστι ποιήσασθαι`, `427b18`).",
            ),
            (
                "De Anima III.4–5 (429a10–430a25) — Receptive & Active Intellect; Continuum vs. Essence of Straight",
                "Shows that intellect must be unmixed to receive all intelligible forms (`429a18`). Crucially distinguishes (`429b10–22`) three tiers: (1) flesh and 'the snub' (sensible matter + form), (2) **'the straight'** (*to euthy*, analogous to the snub because it involves continuous extension, `μετὰ συνεχοῦς γάρ`, `429b19`) vs. 'to be straight' (:term:`to euthei einai <to-ti-en-einai>`), and (3) wholly immaterial essences. Introduces productive intellect (*nous poiētikos*) acting like light (`ὡς ἕξις τις, οἷον τὸ φῶς`, `430a15`).",
            ),
            (
                "De Anima III.6 (430a26–431a1) — Thinking of Indivisibles, Undivided Length & Point",
                "Explains how the mind thinks an actually undivided line segment (`μῆκος ἀδιαίρετον ἐνεργείᾳ`) in an undivided time, whereas a :term:`point <stigme>` and every division are made known like privation (`ὥσπερ ἡ στέρησις`, `430b20–21`).",
            ),
            (
                "De Anima III.7–8 (431a1–432a14) — Noesis in Phantasmata & Objects of Abstraction (431b12–17)",
                "Declares that to the thinking soul :term:`phantasmata <phantasma>` serve as percepts (`431a14–17`), that the faculty of knowledge thinks the forms in the images (`τὰ μὲν οὖν εἴδη τὸ νοητικὸν ἐν τοῖς φαντάσμασι νοεῖ`, `431b2`), and that the mind thinks **mathematical objects of abstraction** (`τὰ ἐν ἀφαιρέσει λεγόμενα`, `431b12`) just as one might think concavity in isolation from the nose-flesh in which it occurs (`431b12–17`). Concludes in III.8 that intellect is the 'form of forms' (`εἶδος εἰδῶν`, `432a2`) and that without perception and phantasmata nobody could ever learn or understand anything (`432a7–9`).",
            ),
        ),
        heath_analysis=(
            ":person:`Heath <heath>` (:cite:`Thirteen Books <heath:euclid:1926>`, Vol. I, p. 156; :cite:`Mathematics in Aristotle <heath:math-aristotle:1949>`, pp. 195–199) singles out `430b20–21`—*'the point and every division, and whatever is indivisible in this sense, is made known just like privation (`δηλοῦται ὥσπερ ἡ στέρησις`)'*—as the deepest explanation of why :person:`Euclid <euclid>` opened the *Elements* with a *negative* definition of the point (`οὗ μέρος οὐθέν`, 'that which has no part') and defined the line as 'breadthless length' (`μῆκος ἀπλατές`).",
            "Heath also connects *De Anima* III.4 (`429b18–20`) directly with *Metaphysics* Z.10 (`1036a9–12`): when Aristotle says that 'the straight' (*to euthy*) is like 'the snub' because *'it is bound up with the continuum'* (`μετὰ συνεχοῦς γάρ`), Aristotle is explicitly identifying the pure spatial continuum with **intelligible matter** (:term:`hylē noētē <hyle-noete>`), judged by a distinct cognitive deployment from sensible flesh!",
        ),
        hoenen_analysis=(
            "Liber IV is the absolute heartland of :person:`Peter Hoenen's <hoenen>` :cite:`De Noetica Geometriae <hoenen:noetica:1952>` (Caput I, § 2, pp. 14–17; Caput V–VII). Look at the triad of Bekker citations that Hoenen weaves together throughout his treatise: `431a16–17` (`οὐδέποτε νοεῖ ἄνευ φαντάσματος ἡ ψυχή`), `431b2` (`τὰ μὲν οὖν εἴδη τὸ νοητικὸν ἐν τοῖς φαντάσμασι νοεῖ`), and `432a8–9` (`ὅταν τε θεωρῇ, ἀνάγκη ἅμα φάντασμά τι θεωρεῖν`).",
            "Why did modern philosophy split disastrously between Kantian synthetic *a priori* intuition on one side and Hilbertian/Russellian blind symbolism on the other? Because post-Cartesian rationalism imagined pure intellect operating *without* imagination, while British empiricism reduced thought *to* sensory images! Aristotle's *De Anima* III.7–8 heals that rupture: human :term:`noēsis <noesis>` is neither blind sensory picturing nor disembodied angelism, but **abstractive insight reading universal necessity inside the concrete imaginative diagram** (*conversio ad phantasmata*). As :person:`Aquinas <thomas-aquinas>` formulated it in :cite:`Super Boethium De Trinitate <aquinas:in-boeth-trin>` (q. 6, a. 2), natural science terminates at sense, metaphysics at pure intellect, and **mathematics terminates at the imagination** (*ad imaginationem*)!",
            "In :cite:`De Divina Proportione <pacioli:divina:1509>` (Compendio Cap. II, fols. `2r–2v`), :person:`Luca Pacioli <pacioli>` invokes *De Anima* III.8 (`432a7–9` — *nihil est in intellectu quin prius fuerit in sensu*) to defend the primacy of visual geometric perspective among the portals of human wisdom.",
        ),
        crux_notes=(
            (
                "427b18–20 — Voluntary Geometric Construction Before the Eyes",
                "Unlike involuntary belief, *phantasia* lies within our constructive power (`ἐφ’ ἡμῖν ἐστιν ὅταν βουλώμεθα`): the geometer actively projects and transforms figures before the mind's eye.",
            ),
            (
                "429b18–22 — 'With Continuum' (Meta Synechous) & Dual Cognitive Faculty",
                "In abstract mathematicals (`ἐπὶ τῶν ἐν ἀφαιρέσει ὄντων`), 'the straight' contains continuous extension (`μετὰ συνεχοῦς`) as its intelligible substrate, whereas its formal essence (`τὸ εὐθεῖ εἶναι`) is pure rectilinear determination.",
            ),
            (
                "430b6–20 — Actual Undividedness vs. Potential Divisibility of a Segment",
                "When thinking a line segment `AB` as a single side of a triangle, the intellect thinks it in an undivided act as one whole; only when it bisects `AB` at `C` does it think the two halves successively in two half-times!",
            ),
            (
                "431b12–17 & 432a3–14 — Phantasmata Without Matter",
                "Phantasmata are like percepts *except that they are without physical matter* (`πλὴν ἄνευ ὕλης`, `432a9`), yet they are *not* thoughts (`τί διοίσει τὰ πρῶτα νοήματα τῶν φαντασμάτων;`, `432a12`): thoughts are universal formal contents that cannot exist apart from phantasmata without being reducible to them.",
            ),
        ),
    ),
    "liber-5a-scientiae-et-quantitas": UnitCommentary(
        thesis=(
            "Liber V.A gathers the architectonic chapters of :person:`Aristotle's <aristotle>` *Metaphysics* on axioms, "
            "mathematical objects, unity, quantity, and the classification of the sciences: Book B.2 (`996a18–998a19`) "
            "raising the sharp aporiai of sensible vs. ideal geometry (:person:`Protagoras's <protagoras>` circle-tangent "
            "objection, `998a2–4`), Book $\\Delta$.6 & 13 (`1015b16–1017a6`, `1020a7–32`) defining the indivisible measure "
            "and :term:`quantity <poson>`, and Book E.1 (`1025b3–1026a32`) establishing the canonical tripartition of "
            "theoretical philosophy into physics, mathematics, and theology/first philosophy."
        ),
        argument_steps=(
            (
                "Metaphysics B (III).2 (996a18–998a19) — Aporiai of Axioms & Mathematical Intermediates",
                "Asks whether one science studies both substance and the common :term:`axioms <axioma>` used by all mathematicians (`996b26–33`), and confronts the dilemma of :person:`Plato's <plato>` 'intermediates' (*ta metaxy*): sensible lines are not straight as the geometer defines them, nor does a physical circle touch a ruler at a single point as :person:`Protagoras <protagoras>` objected (`997b35–998a6`), yet positing a separate duplicate heaven and duplicate mathematical solids generates absurdities (`997b12–34`).",
            ),
            (
                "Metaphysics Δ (V).6 (1015b16–1017a6) — Ontological Lexicon of Unity & the Indivisible Measure",
                "Defines 'the one' (*to hen*) by continuity (`1015b36`), wholeness of form, and above all **being the primary indivisible measure of each genus** (`τὸ γὰρ ἓν εἶναι ἀρχή τινί ἐστιν ἀριθμοῦ εἶναι· τὸ γὰρ πρῶτον μέτρον ἀρχή`, `1016b17–21`). Distinguishes indivisible in every respect and without position (:term:`monad <monas>`) from indivisible in every respect with position (:term:`point <stigme>`, `1016b24–26`), one-dimensionally divisible (line), two-dimensionally (plane), and three-dimensionally (body).",
            ),
            (
                "Metaphysics Δ (V).13 (1020a7–1020a32) — Ontological Lexicon of Quantity (Poson)",
                "Gives the classic definition of :term:`quantity <poson>` (`1020a7–14`): that which is divisible into two or more constituent parts each by nature a 'one' and a 'this'—a :term:`multitude <plethos>` if countable (*arithmēton*, divisible into non-continuous parts) and a :term:`magnitude <megethos>` if measurable (*metrēton*, divisible into continuous parts: length, breadth, depth).",
            ),
            (
                "Metaphysics E (VI).1 (1025b3–1026a32) — Tripartition of Theoretical Science",
                "Divides all rational knowledge into practical, productive, and theoretical (`1025b25`), and differentiates the three **theoretical philosophies** (`1026a18–19`): *physics* (objects inseparable and movable), *mathematics* (some branches studying objects immovable though presumably not separate, `ὡς ἀκίνητα καὶ ὡς χωριστὰ θεωρεῖ`, `1026a9–10`), and *first philosophy / theology* (objects both separate and immovable).",
            ),
        ),
        heath_analysis=(
            "In :cite:`The Thirteen Books of Euclid's Elements <heath:euclid:1926>` (Vol. I, pp. 155–166; Vol. II, p. 113; Vol. III, p. 260), *Metaphysics* $\\Delta$.6 and $\\Delta$.13 are among :person:`Heath's <heath>` most heavily cited Aristotelian texts (`1016a2`, `1016a13`, `1016b24–27`, `1020a11–13`). Together they supply the complete philosophical lexicon behind Book I (points, lines, planes), Book V (magnitudes), Book VII (units and numbers), and Book XI (solids) of the *Elements*.",
            "In *Metaphysics* B.2 (`997b35–998a6`), Aristotle preserves two vivid fourth-century mathematical illustrations against naive physicalism: (1) :person:`Protagoras's <protagoras>` empirical attack claiming a bronze hoop touches a straightedge along a finite segment rather than at a single point (compare :cite:`Elements III.2 & III.16 <euclid:elements>`), and (2) astronomy's treatment of stars—visibly larger than points—as mathematical point-centers on celestial spheres (`998a4–6`). As Heath (:cite:`Mathematics in Aristotle <heath:math-aristotle:1949>`, pp. 201–203) observes, Book B stages the dialectical knot that Book M.1–3 will untie.",
        ),
        hoenen_analysis=(
            "In :cite:`De Noetica Geometriae <hoenen:noetica:1952>` (Caput I–II & VI), :person:`Hoenen <hoenen>` highlights *Metaphysics* B.2 (`997b35`, cited directly in Hoenen's apparatus!) and E.1 (`1026a7–19`) as the historical fountainhead of the **three degrees of formal abstraction** codified by :person:`Aquinas <thomas-aquinas>` (:cite:`Super Boethium De Trinitate <aquinas:in-boeth-trin>`, q. 5, aa. 1 & 3). Protagoras's objection proves conclusively that geometrical concepts are *not* passive copies of crude sensory edges; yet Aristotle's refutation of Platonic intermediates proves they are *not* inhabitants of a separate third world either. Instead, mathematics studies real quantitative structures present in physical bodies, considered *qua* immovable and abstracted from sensible matter!",
            "In :cite:`De Divina Proportione <pacioli:divina:1509>` (Compendio Cap. I–III, fols. `1r–3r`), :person:`Fra Luca Pacioli <pacioli>` builds his opening manifesto of Renaissance mathematical humanism directly upon Aristotle's classification of theoretical sciences and :person:`Averroes's <averroes>` commentary (:cite:`In Metaph. II, comm. 16 <averroes:in-metaph>`): mathematical demonstrations stand *in primo gradu certitudinis*.",
        ),
        crux_notes=(
            (
                "996b26–33 — Who Investigates the Common Axioms?",
                "Aristotle poses the aporia solved in Book $\\Gamma$ (IV).3: although geometers and arithmeticians *use* the common axioms restricted to their own genus (magnitudes or numbers), it belongs to First Philosophy to investigate them universally *qua* being.",
            ),
            (
                "997b35–998a6 — Protagoras's Tangent to the Circle",
                "Euclid III.16 proves rigorously that no straight line can enter the space between a circle's tangent and its circumference, vindicating ideal geometric continuity against Protagoras's sensory ruler.",
            ),
            (
                "1020a7–14 — Arithmēton (Countable) vs. Metrēton (Measurable)",
                "This crisp binary—*multitude* is counted by indivisible units, *magnitude* is measured by a chosen continuous unit length without ever becoming discrete—explains why Greek mathematics treated ratio of magnitudes separately from fraction of integers.",
            ),
            (
                "1026a23–32 — Universal Mathematics (Katholou Mathēmatikē)",
                "Echoing *Posterior Analytics* I.5 (`74a17–25`), Aristotle contrasts particular mathematical sciences (geometry, astronomy) with 'universal mathematics common to all' (`ἡ δὲ καθόλου κοινὴ περὶ πάντων`, `1026a27`), i.e. Eudoxus's general proportion theory.",
            ),
        ),
    ),
    "liber-5b-hyle-noete-energeia-pulchritudo": UnitCommentary(
        thesis=(
            "Liber V.B crowns the entire *Loci Geometrici et Noetici* Codex with the three supreme peaks of Aristotelian "
            "philosophy of mathematics: *Metaphysics* Z.10–11 (`1034b20–1037a20`) introducing **intelligible matter** "
            "(:term:`hylē noētē <hyle-noete>`, `1036a9–12`), *Metaphysics* $\\Theta$.9 (`1051a4–33`) revealing that "
            "geometrical theorems are discovered by **actualizing** (:term:`energeia <energeia>`, `1051a21–33`) latent "
            "divisions in construction, and *Metaphysics* M.1–3 (`1076a8–1078b6`) articulating the *qua*-ontology of "
            "mathematicals and celebrating **mathematical beauty** (:term:`to kalon <kalon>`: order, symmetry, and "
            "definiteness, `1078a31–b6`)."
        ),
        argument_steps=(
            (
                "Metaphysics Z (VII).10–11 (1034b20–1037a20) — Formal Parts vs. Intelligible Matter (1036a9)",
                "Solves why 'semicircle' is *not* part of the definition of 'circle', whereas 'right angle' *is* presupposed in the definition of 'acute angle' (`1035b4–12`): semicircles are parts of an individual circle's **intelligible matter** (`ὕλη δὲ ἡ μὲν αἰσθητή ἐστιν ἡ δὲ νοητή, αἰσθητὴ μὲν οἷον χαλκὸς καὶ ξύλον... νοητὴ δὲ ἡ ἐν τοῖς αἰσθητοῖς ὑπάρχουσα μὴ ᾗ αἰσθητά, οἷον τὰ μαθηματικά`, `1036a9–12`). Even when all bronze and stone are abstracted, an individual mathematical circle still possesses pure spatial extension individuating its congruent parts (`1036b32–1037a5`).",
            ),
            (
                "Metaphysics Θ (IX).9 (1051a4–1051a33) — Constructive Actuality (Energeia) in Geometrical Discovery",
                "Demonstrates the cognitive priority of :term:`actuality <energeia>` over :term:`potency <dynamis>` (`1051a21–33`): *'Geometrical constructions (`τὰ διαγράμματα`) are discovered by an activity (`ἐνεργείᾳ`); for it is by dividing (`διαιροῦντες`) that they discover them.'* Gives two immortal Euclidean proofs: (1) why a triangle's interior angles equal `2R`—the moment the parallel to the base is drawn (`ἀνῆκτο ἡ παρὰ τὴν πλευράν`), it is immediately clear on seeing it (`ἰδόντι ἂν ἦν εὐθὺς δῆλον`, `1051a24–26`); and (2) why the angle in a semicircle is universally a right angle (:cite:`Elements III.31 <euclid:III.31>`)—by erecting the third equal radius from the midpoint of the diameter (`1051a26–29`).",
            ),
            (
                "Metaphysics M (XIII).1–2 (1076a8–1077b16) — Critique of Immanent & Separate Mathematical Solids",
                "Refutes both the view that mathematical solids exist as separate entities *inside* sensible bodies (which would place two solids in the same place and make sensible bodies indivisible) and the Platonic view that they exist *apart* from sensible bodies (which generates an infinite cascade of duplicate astronomical spheres and elevates what is prior only in *formula* [`τῷ λόγῳ`] over what is prior in *substance* [`τῇ οὐσίᾳ`, `1077a36–b11`]).",
            ),
            (
                "Metaphysics M (XIII).3 (1077b17–1078b6) — Qua-Predication & Mathematical Beauty (1078a31–b6)",
                "Establishes Aristotle's positive **qua-theory** (`ᾗ`): just as truths hold of moving things *qua* moving apart from what they are, geometry studies sensible bodies *not qua sensible, but qua lengths and planes* (`1077b22–34`), achieving higher :term:`exactitude <akribeia>` the simpler its aspect (`1078a9–17`). Closes with the sublime defence of **mathematical beauty** (`1078a31–b6`): whereas the good concerns action, *the beautiful (`τὸ καλόν`) exists also in motionless things*, and its supreme forms are **order (`τάξις`), symmetry (`συμμετρία`), and definiteness (`τὸ ὡρισμένον`)**, which the mathematical sciences pre-eminently demonstrate!",
            ),
        ),
        heath_analysis=(
            ":person:`Sir Thomas Heath <heath>` (:cite:`Thirteen Books <heath:euclid:1926>`, Vol. I, p. 317; Vol. II, p. 63; :cite:`Mathematics in Aristotle <heath:math-aristotle:1949>`, pp. 216–219) celebrates *Metaphysics* $\\Theta$.9 (`1051a21–33`) as the most vivid window into Greek heuristic proof anywhere in surviving classical literature!",
            "Look closely at Aristotle's two theorems in `1051a24–29`: First, for the `2R` angle-sum of $\\triangle ABC$, Aristotle extends the base $BC$ and draws the auxiliary line through a vertex parallel to the opposite side (`ἀνῆκτο ἡ παρὰ τὴν πλευράν`)—the **exact Pythagorean/Euclidean construction** preserved in :cite:`Elements I.32 <euclid:I.32>`! Second, to prove that *every* angle $\\angle BAC$ inscribed in a semicircle on diameter $BC$ with center $O$ is a right angle (:cite:`Elements III.31 <euclid:III.31>`), Aristotle's geometer draws the radius $OA$ from the midpoint (`ἐκ μέσου`) equal to the two half-diameters $OB = OC$ (actually Aristotle describes the symmetric case where $OA$ is erected perpendicular or simply equal to the half-diameters; cf. *Anal. Post.* II.11, `94a28–34`), splitting $\\triangle ABC$ into isosceles triangles so that seeing the `2R` theorem makes the right angle instantaneously luminous!",
            "Notice Aristotle's Greek noun in `1051a21`: `τὰ διαγράμματα` means not merely static drawings, but *geometrical propositions/proofs-through-construction*! Before the geometer's mind divides the figure (`διαιροῦντες`), the auxiliary parallel and radius exist only *potentially* (`δυνάμει`) inside continuous space; the act of constructive thought (`νοήσει ἐνέργεια`, `1051a30–31`) brings them into actuality!",
        ),
        hoenen_analysis=(
            "In :cite:`De Noetica Geometriae <hoenen:noetica:1952>` (Caput V–VII & Appendix, n. 18, p. 262), *Metaphysics* Z.10 (`1036a9–12`) and $\\Theta$.9 (`1051a21–33`) converge to complete Hoenen's entire philosophical edifice. Why can geometry discover genuinely *new*, synthetic-yet-necessary truths through construction—truths neither tautologically contained in verbal definitions nor empirically guessed from physical rulers?",
            "Because of the partnership of **intelligible matter** (`ὕλη νοητή`, `1036a9`) and **constructive noetic actuality** (`νοήσει ἐνέργεια`, `1051a30`)! Pure logical concepts without extension cannot be divided into two congruent semicircles or traversed by an auxiliary parallel; sensible bronze cannot guarantee strict zero-breadth parallelism. Only because the intellect abstracts continuous spatial extension (*materia intelligibilis*) preserved in the :term:`phantasma <phantasma>`, and actively **constructs divisions** (`διαιροῦντες γὰρ εὑρίσκουσιν`) inside it, does the causal nexus flash forth directly to intellectual vision: **`ἰδόντι ἂν ἦν εὐθὺς δῆλον` — 'it would have been immediately clear to one who simply saw it!'** (`1051a26`).",
            "Finally, *Metaphysics* M.3 (`1078a31–b6`) links Aristotle directly to the foundational ethos of **GEOMETOR** and :person:`Pacioli's <pacioli>` *Divine Proportion*: mathematics is not value-neutral calculation, for in demonstrating **order (`τάξις`), symmetry/proportion (`συμμετρία`), and definiteness (`τὸ ὡρισμένον`)**, constructive geometry reveals the intelligible architecture of :term:`beauty <kalon>` itself.",
        ),
        crux_notes=(
            (
                "1036a9–12 — The Locus Classicus of Hylē Noētē (Intelligible Matter)",
                "`νοητὴ δὲ ἡ ἐν τοῖς αἰσθητοῖς ὑπάρχουσα μὴ ᾗ αἰσθητά, οἷον τὰ μαθηματικά`: intelligible matter is *not* a ghost-substance floating outside the world, but the real continuous dimensionality *present in sensible things considered not qua sensible*.",
            ),
            (
                "1036b32–1037a5 — Critique of the Elder Platonists/Pythagoreans Reducing All Form to Number",
                "Against Speusippus/Xenocrates who tried to eliminate continuous extension and reduce the line's essence to the number 'two' (`δυάς`), Aristotle insists that geometric figures essentially include continuous intelligible substrate alongside formal ratio.",
            ),
            (
                "1051a21–33 — Diagrammatic Actuality as Engine of Discovery",
                "Here `77b30` (*Anal. Post.* I.12), `431b2` (*De Anima* III.7), `1036a9` (*Metaph.* Z.10), and `1051a21` (*Metaph.* $\\Theta$.9) lock together into a single seamless theory of constructive geometric cognition—precisely what GEOMETOR models computationally through exact symbolic construction DAGs.",
            ),
            (
                "1078a31–b6 — Taxis, Symmetria, To Hōrismenon",
                "Against Aristippus the Cyrenaic (who disparaged mathematics for ignoring 'good and bad', cf. *Metaph.* B.2, `996a32`), Aristotle distinguishes moral finality from formal-mathematical *kalon*: motionless geometric invariants exhibit supreme order, proportion, and determinate precision, and furthermore serve as *causes* (`ὡς αἴτια`) of harmony in nature.",
            ),
        ),
    ),
}
