"""Scholarly apparatus registries (Glossary, Persons, Bibliography) and RST generators."""

from __future__ import annotations

import json
import re
from pathlib import Path


def apparatus_slug(key: str) -> str:
    """Return deterministic anchor slug matching ``photon_platform.publish.roles.geometry``."""
    return re.sub(r"[^a-z0-9]+", "-", (key or "").lower()).strip("-")


GLOSSARY_DATA: dict[str, dict[str, str]] = {
    "episteme": {
        "headword": "ἐπιστήμη (epistēmē)",
        "greek": "ἐπιστήμη",
        "latin": "scientia",
        "translation": "Demonstrative scientific knowledge",
        "loci": "Anal. Post. I.2, 71b9–16; Metaph. E.1, 1025b18–28",
        "definition": "Unqualified scientific knowledge obtained when we know the necessary cause (aitia) through which a fact holds and see that it cannot be otherwise.",
    },
    "apodeixis": {
        "headword": "ἀπόδειξις (apodeixis)",
        "greek": "ἀπόδειξις",
        "latin": "demonstratio",
        "translation": "Scientific demonstration",
        "loci": "Anal. Post. I.2, 71b17–25; I.4–6, 73a21–75a37",
        "definition": "A syllogism productive of scientific knowledge (syllogismos epistēmonikos), proceeding from premisses that are true, primary, immediate, better known than, prior to, and causes of the conclusion.",
    },
    "nous": {
        "headword": "νοῦς (nous)",
        "greek": "νοῦς",
        "latin": "intellectus principiorum",
        "translation": "Intuitive intellect / intellectual intuition",
        "loci": "Anal. Post. II.19, 100b5–17; De Anima III.4–5, 429a10–430a25",
        "definition": "The supreme noetic state (hexis) that apprehends immediate, indemonstrable first principles; more exact and truer than epistēmē itself, serving as the principle of principle (archē archēs).",
    },
    "epagoge": {
        "headword": "ἐπαγωγή (epagōgē)",
        "greek": "ἐπαγωγή",
        "latin": "inductio",
        "translation": "Noetic induction",
        "loci": "Anal. Post. I.1, 71a8; I.18, 81a38–b9; II.19, 100b3–5",
        "definition": "Not probabilistic enumeration, but the genetic process by which sense-perception and memory bring the universal nature to a stand in the soul until nous intuits the necessary connection.",
    },
    "axioma": {
        "headword": "ἀξίωμα (axiōma)",
        "greek": "ἀξίωμα / τὰ κοινά",
        "latin": "dignitas / communis animi conceptio",
        "translation": "Axiom / Common Notion",
        "loci": "Anal. Post. I.2, 72a16–17; I.10, 76a37–b2; Metaph. B.2, 996b26–33",
        "definition": "An immediate principle that anyone who is going to learn anything must grasp of himself—prototypically the quantitative axiom 'if equals be subtracted from equals, the remainders are equal' (Euclid C.N. 3).",
    },
    "aitema": {
        "headword": "αἴτημα (aitēma)",
        "greek": "αἴτημα",
        "latin": "petitio / postulatum",
        "translation": "Postulate",
        "loci": "Anal. Post. I.10, 76b23–34",
        "definition": "A demonstrable or constructive assumption adopted without the learner's prior conviction or contrary to the learner's opinion; precursor to Euclid's five geometrical Postulates.",
    },
    "hypothesis": {
        "headword": "ὑπόθεσις (hypothesis)",
        "greek": "ὑπόθεσις",
        "latin": "suppositio",
        "translation": "Scientific hypothesis",
        "loci": "Anal. Post. I.2, 72a18–24; I.10, 76b3–39; Topics VIII.3, 158b30",
        "definition": "A thesis asserting the existence (to einai) of the primitive objects of a science's genus—such as units in arithmetic or points and lines in geometry—from which attributes are demonstrated.",
    },
    "horismos": {
        "headword": "ὁρισμός (horismos)",
        "greek": "ὁρισμός",
        "latin": "definitio",
        "translation": "Essential definition",
        "loci": "Anal. Post. I.2, 72a21–24; I.10, 76b35–39; Topics VI.4, 141a26–142b19",
        "definition": "A thesis stating what a thing is (ti esti) through prior and more intelligible terms without asserting its existence—e.g. defining a line as breadthless length.",
    },
    "kath-hauto": {
        "headword": "καθ’ αὑτό (kath' hauto)",
        "greek": "καθ’ αὑτό",
        "latin": "per se",
        "translation": "Essential / intrinsic predication",
        "loci": "Anal. Post. I.4, 73a34–b24",
        "definition": "An attribute belonging to a subject either inside its essential formula (as line in triangle) or containing the subject itself inside the attribute's own formula (as straight and curved belong to line).",
    },
    "katholou": {
        "headword": "καθόλου (katholou)",
        "greek": "καθόλου",
        "latin": "universale commensuratum",
        "translation": "Commensurate universal",
        "loci": "Anal. Post. I.4–5, 73b25–74b4; I.24, 85a13–86a30",
        "definition": "That which belongs to every instance (kata pantos), essentially (kath' hauto), and qua itself (hēi auto)—exemplified by the 2R angle-sum belonging commensurate-universally to triangle qua triangle rather than isosceles.",
    },
    "metabasis": {
        "headword": "μετάβασις εἰς ἄλλο γένος (metabasis)",
        "greek": "μετάβασις εἰς ἄλλο γένος",
        "latin": "transitus in aliud genus",
        "translation": "Prohibition of genus-crossing",
        "loci": "Anal. Post. I.7, 75a38–b20; De Caelo I.1, 268b1",
        "definition": "Aristotle's structural law that an arithmetical proof cannot establish a geometrical theorem concerning continuous magnitudes unless the genera stand in formal subalternation (as optics to geometry).",
    },
    "to-hoti-kai-dioti": {
        "headword": "τὸ ὅτι καὶ τὸ διότι (to hoti / to dioti)",
        "greek": "τὸ ὅτι / τὸ διότι",
        "latin": "demonstratio quia et propter quid",
        "translation": "Fact vs. reasoned causal fact",
        "loci": "Anal. Post. I.13, 78a22–79a16",
        "definition": "Distinction between empirical sciences that know the fact (optics, harmonics, observational astronomy) and pure mathematical sciences that supply the formal geometrical or arithmetical reason why.",
    },
    "akribeia": {
        "headword": "ἀκρίβεια (akribeia)",
        "greek": "ἀκρίβεια",
        "latin": "exactitudo / certitudo",
        "translation": "Scientific exactitude",
        "loci": "Anal. Post. I.27, 87a31–37; Metaph. M.3, 1078a9–17",
        "definition": "Precision proportional to conceptual simplicity and priority: arithmetic is more exact than geometry because the arithmetical monad lacks position, whereas the geometrical point adds position (thesis).",
    },
    "poson": {
        "headword": "ποσόν (poson)",
        "greek": "ποσόν",
        "latin": "quantitas",
        "translation": "Quantity",
        "loci": "Categoriae 6, 4b20–6a35; Metaph. Δ.13, 1020a7–32",
        "definition": "That which is divisible into constituent parts each capable of being a single determinate 'this'; the proper ontological domain of mathematics, bifurcated into discrete multitude and continuous magnitude.",
    },
    "diorismenon": {
        "headword": "διωρισμένον (diōrismenon)",
        "greek": "διωρισμένον ποσόν",
        "latin": "quantitas discreta",
        "translation": "Discrete quantity",
        "loci": "Categoriae 6, 4b20–37",
        "definition": "Quantity whose parts join at no common boundary (koinoi horoi), prototypically number (arithmos) and spoken logos.",
    },
    "syneches": {
        "headword": "συνεχές (syneches)",
        "greek": "συνεχές",
        "latin": "continuum",
        "translation": "The continuum / continuous quantity",
        "loci": "Categoriae 6, 4b20, 5a1–14; Phys. V.3, 227a10–17; VI.1–2, 231a21–233b32",
        "definition": "Quantity whose parts share a common boundary where their extremities become one, and which is divisible solely into parts that are themselves always further divisible (eis aei diaireta)—line, surface, body, time, and place.",
    },
    "adiaireton": {
        "headword": "ἀδιαίρετον (adiaireton)",
        "greek": "ἀδιαίρετον / ἀμερές",
        "latin": "indivisibile",
        "translation": "Indivisible / partless limit",
        "loci": "Phys. VI.1, 231a21–b18; De Anima III.6, 430b6–20; Metaph. Δ.6, 1016b24–31",
        "definition": "That which lacks parts in quantity or species; in geometry, the point is indivisible in every dimension yet possesses position, serving as limit (peras) of a line without ever composing it.",
    },
    "stigme": {
        "headword": "στιγμή (stigmē)",
        "greek": "στιγμή",
        "latin": "punctum",
        "translation": "Geometrical point",
        "loci": "Anal. Post. I.27, 87a36; Topics VI.4, 141b5–22; Phys. VI.1, 231a24–b18; Metaph. Δ.6, 1016b25",
        "definition": "Aristotle's standard term for the geometrical point (prior to Euclid's sēmeion): an indivisible substance having position (ousia athetos vs. thetos), functioning as boundary and division of continuous length.",
    },
    "monas": {
        "headword": "μονάς (monas)",
        "greek": "μονάς",
        "latin": "unitas",
        "translation": "Arithmetical unit / monad",
        "loci": "Anal. Post. I.27, 87a36; Metaph. Δ.6, 1016b24–26; M.8, 1084b26",
        "definition": "That which is quantitatively indivisible in every respect and without spatial position (athetos), serving as the primary measure of discrete number.",
    },
    "megethos": {
        "headword": "μέγεθος (megethos)",
        "greek": "μέγεθος",
        "latin": "magnitudo",
        "translation": "Continuous geometric magnitude",
        "loci": "De Caelo I.1, 268a6–13; Metaph. Δ.13, 1020a11–14",
        "definition": "Measurable continuous quantity: divisible in one dimension as line (grammē), in two as plane surface (epipedon), and completely in three as solid body (sōma).",
    },
    "plethos": {
        "headword": "πλῆθος (plēthos)",
        "greek": "πλῆθος",
        "latin": "multitudo",
        "translation": "Countable multitude / plurality",
        "loci": "Metaph. Δ.13, 1020a7–11; I.1, 1053a20–30",
        "definition": "Quantity countable into discontinuous parts; when limited and measured by the unit, multitude constitutes number (arithmos).",
    },
    "antanairesis": {
        "headword": "ἀνταναίρεσις (antanairesis)",
        "greek": "ἀνταναίρεσις",
        "latin": "subtractio reciproca",
        "translation": "Reciprocal subtraction (anthyphairesis)",
        "loci": "Topics VIII.3, 158b29–35",
        "definition": "The pre-Eudoxian definition of equality of ratios (preserved in Euclid Elements X.2–3): two magnitudes have the same ratio as two others when they undergo the exact same sequence of reciprocal subtractions.",
    },
    "asymmetron": {
        "headword": "ἀσύμμετρον (asymmetron)",
        "greek": "ἀσύμμετρον ἡ διάμετρος",
        "latin": "incommensurabile",
        "translation": "Incommensurability (of the diagonal)",
        "loci": "Anal. Prior. I.23, 41a23–30; Anal. Post. I.2, 71b26; Metaph. A.2, 983a15",
        "definition": "Aristotle'sparadigm of apodeictic necessity by reductio ad absurdum: if the diagonal of a square were commensurable with its side, odd numbers would become equal to even numbers.",
    },
    "chorismos": {
        "headword": "χωρισμὸς τῇ νοήσει (chōrismos)",
        "greek": "χωριστὰ τῇ νοήσει",
        "latin": "separatio secundum intellectum",
        "translation": "Separation in thought",
        "loci": "Phys. II.2, 193b31–35; Metaph. M.3, 1078a17–31",
        "definition": "The mathematician's legitimate methodological act of considering surfaces, volumes, lengths, and points apart from physical motion and sensible matter without asserting Platonic separate existence.",
    },
    "apeiron": {
        "headword": "ἄπειρον (apeiron)",
        "greek": "δυνάμει ἄπειρον",
        "latin": "infinitum potentiale",
        "translation": "The potential infinite",
        "loci": "Phys. III.4–7, 202b30–208a4",
        "definition": "Not an actually completed magnitude (which is impossible), but an open-ended potentiality whereby another part can always be taken—inwardly by bisection in magnitudes, outwardly by succession in numbers.",
    },
    "topos": {
        "headword": "τόπος (topos)",
        "greek": "τόπος",
        "latin": "locus",
        "translation": "Place",
        "loci": "Categoriae 6, 5a8–14; Phys. IV.1–5, 208a27–213a11",
        "definition": "The first motionless boundary of the containing body (to tou periechontos peras akinēton prōton, 212a20), grounding positional order without positing an empty self-subsistent void.",
    },
    "phantasia": {
        "headword": "φαντασία (phantasia)",
        "greek": "φαντασία",
        "latin": "imaginatio / phantasia",
        "translation": "Sensible imagination",
        "loci": "De Anima III.3, 427b14–429a9",
        "definition": "A movement generated by actual sense-perception that preserves spatial configuration and figure apart from external matter, bridging sensation (aisthēsis) and intellectual thought (noēsis).",
    },
    "phantasma": {
        "headword": "φάντασμα (phantasma)",
        "greek": "φάντασμα",
        "latin": "phantasma",
        "translation": "Imaginative diagram / presentation",
        "loci": "De Anima III.7, 431a14–17, 431b2; III.8, 432a3–14; De Mem. 1, 449b31–450a7",
        "definition": "The concrete imaginative presentation in which the intellect beholds universal formal structure; as the geometer draws a determinate finite triangle yet proves solely from its universal triangularity.",
    },
    "noesis": {
        "headword": "νόησις (noēsis)",
        "greek": "νόησις / ὁρᾶν τῇ νοήσει",
        "latin": "intellectio / intuitus mentis",
        "translation": "Intellectual vision / apprehension",
        "loci": "Anal. Post. I.12, 77b30–31; De Anima III.4–8, 429a10–432a14",
        "definition": "Direct intellectual insight reading formal necessity inside mathematical constructions; highlighted by Hoenen as the Aristotelian text refuting blind symbolic formalism.",
    },
    "aphairesis": {
        "headword": "τὰ ἐξ ἀφαιρέσεως (aphairesis)",
        "greek": "τὰ ἐν ἀφαιρέσει / τὰ ἐξ ἀφαιρέσεως",
        "latin": "abstractio mathematica",
        "translation": "Objects of mathematical abstraction",
        "loci": "Anal. Post. I.18, 81b3; De Caelo III.1, 299a15; De Anima III.7, 431b12–17",
        "definition": "Aristotle's technical designation for mathematical entities obtained by stripping away sensible contraries (weight, heat, hardness) while retaining continuous quantitative determination.",
    },
    "hyle-noete": {
        "headword": "ὕλη νοητή (hylē noētē)",
        "greek": "ὕλη νοητή",
        "latin": "materia intelligibilis",
        "translation": "Intelligible matter",
        "loci": "Metaph. Z.10, 1036a9–12; Z.11, 1036b32–1037a5; H.6, 1045a33–35",
        "definition": "Pure continuous spatial extension remaining after sensible qualities are abstracted; individuates multiple congruent circles or triangles that share the exact same formal definition.",
    },
    "energeia": {
        "headword": "ἐνέργεια (energeia)",
        "greek": "ἐνέργεια",
        "latin": "actus / operatio",
        "translation": "Actuality / constructive activity",
        "loci": "Metaph. Θ.6–9, 1048a25–1051a33",
        "definition": "Priority of act over potency; in Metaphysics Θ.9 (1051a21–33), geometrical theorems are discovered by actualizing latent divisions through auxiliary lines, making the causal middle term immediately manifest.",
    },
    "dynamis": {
        "headword": "δύναμις (dynamis)",
        "greek": "δύναμις",
        "latin": "potentia",
        "translation": "Potency / latent geometric capacity (and square)",
        "loci": "Phys. III.6, 206a14–25; Metaph. Δ.12, 1019b33 (square in geometry); Θ.9, 1051a24",
        "definition": "Both ontological potentiality (as latent chords and parallels exist potentially in a figure prior to construction, and infinite bisections exist potentially in a segment) and the technical Greek geometric term for a mathematical square.",
    },
    "entelecheia": {
        "headword": "ἐντελέχεια (entelecheia)",
        "greek": "ἐντελέχεια",
        "latin": "entelechia / actus perfectus",
        "translation": "Completed actuality",
        "loci": "Phys. III.1, 201a10–11; De Anima II.1, 412a27; Metaph. Θ.8, 1050a21–23",
        "definition": "Aristotle's coinage signifying internal completeness or attainment of form (telos); used in Physics III.1 to define motion as the entelecheia of the potential qua potential.",
    },
    "to-ti-en-einai": {
        "headword": "τὸ τί ἦν εἶναι (to ti ēn einai)",
        "greek": "τὸ τί ἦν εἶναι",
        "latin": "quod quid erat esse / quidditas",
        "translation": "Essence / formal quiddity",
        "loci": "Anal. Post. II.3–10; De Anima III.4, 429b10–22; Metaph. Z.4–11, 1029b1–1037b7",
        "definition": "What it is for a thing to be what it essentially is—e.g. 'to be straight' (to euthei einai) vs. the extended straight thing (to euthy) composed of form in continuum.",
    },
    "kalon": {
        "headword": "τὸ καλόν — τάξις, συμμετρία, τὸ ὡρισμένον (to kalon)",
        "greek": "τάξις, συμμετρία, τὸ ὡρισμένον",
        "latin": "pulchrum: ordo, commensuratio, determinatio",
        "translation": "Mathematical beauty: order, symmetry & definiteness",
        "loci": "Metaph. M.3, 1078a31–b6",
        "definition": "Aristotle's defence against Aristippus: mathematics pre-eminently exhibits the chief forms of beauty—order (taxis), symmetry/commensurability (symmetria), and determinate precision (to hōrismenon)—and acts as their causal explanation.",
    },
    "arithmos": {
        "headword": "ἀριθμός (arithmos)",
        "greek": "ἀριθμός",
        "latin": "numerus",
        "translation": "Discrete number (multitude measured by the unit)",
        "loci": "Categoriae 6, 4b23–31; Phys. III.7, 207b7; Metaph. Δ.13, 1020a13; I.6, 1057a3",
        "definition": "Limited multitude (plēthos peperasmenon) composed of indivisible units without spatial position; contrasted throughout Aristotle with continuous geometric magnitude (megethos).",
    },
    "aistheta-koina": {
        "headword": "αἰσθητὰ κοινά (aisthēta koina)",
        "greek": "τὰ κοινὰ αἰσθητά",
        "latin": "sensibilia communia",
        "translation": "Common sensibles (movement, rest, number, figure, magnitude)",
        "loci": "De Anima II.6, 418a17–20; III.1, 425a14–28; III.3, 428b22–25",
        "definition": "Quantitative and kinematic determinations—movement, rest, number, figure (schēma), and magnitude (megethos)—perceived jointly across multiple senses (chiefly sight and touch) and retained in spatial phantasms.",
    },
}


PERSONS_DATA: dict[str, dict[str, str]] = {
    "aristotle": {
        "name": "Aristotle of Stagira",
        "dates": "384 – 322 BC",
        "role": "Founder of the Peripatetic School & Architect of Demonstrative Science",
        "bio": "Student of Plato at the Academy (367–347 BC) and founder of the Lyceum. Formulated the logic of demonstrative science (apodeixis), the classification of axioms, postulates, and definitions, the theory of the continuum and potential infinite, and the noetics of mathematical abstraction in intelligible matter.",
    },
    "plato": {
        "name": "Plato of Athens",
        "dates": "c. 428 – 347 BC",
        "role": "Founder of the Academy & Philosopher of Mathematical Intermediates",
        "bio": "Established geometry at the heart of philosophical education (Meno, Republic VI–VII, Timaeus). Posited eternal, motionless mathematical intermediates (ta mathēmatika) between sensible particulars and transcendent Forms—the primary target of Aristotle's ontological critique in Metaphysics B and M.",
    },
    "pythagoras": {
        "name": "Pythagoras & the Pythagoreans",
        "dates": "6th – 4th c. BC",
        "role": "Italic School of Number, Harmonics & Cosmic Geometry",
        "bio": "Discovered harmonic ratios, the application of areas, and the incommensurability of the diagonal; cited by Aristotle in De Caelo I.1 on the triad of spatial dimensions and critiqued in Metaphysics A, M, and N for treating numbers as the material substance of sensible bodies.",
    },
    "zeno": {
        "name": "Zeno of Elea",
        "dates": "c. 495 – c. 430 BC",
        "role": "Eleatic Dialectician of Continuum & Motion Paradoxes",
        "bio": "Formulated the aporia of place (Physics IV.1, 209a23) and the four celebrated paradoxes of motion—Dichotomy, Achilles, Flying Arrow, and Stadium—analyzed and resolved by Aristotle in Physics VI.2 and VI.9 via the distinction between infinity by division and infinity of extent.",
    },
    "democritus": {
        "name": "Democritus of Abdera",
        "dates": "c. 460 – c. 370 BC",
        "role": "Atomist Natural Philosopher & Geometer of Cone Sections",
        "bio": "Posited indivisible corporeal atoms and void; opposed by Aristotle throughout Physics IV and VI, which prove that continuous magnitudes cannot be composed of indivisibles.",
    },
    "protagoras": {
        "name": "Protagoras of Abdera",
        "dates": "c. 490 – c. 420 BC",
        "role": "Sophist Critic of Geometrical Idealization",
        "bio": "Cited in Metaphysics B.2 (998a2–4) as attempting to refute geometers by arguing that a physical circle touches a straight ruler not at a single indivisible point, but along an extended stretch.",
    },
    "hippocrates-chios": {
        "name": "Hippocrates of Chios",
        "dates": "fl. c. 440 BC",
        "role": "Author of the Earliest Elements & Quadrature of Lunes",
        "bio": "Pioneered geometric reduction (apagōgē) and squared specific curvilinear lunes (meniskoi), though Aristotle critiques a fallacious general quadrature by lunes (Soph. El. 11; Phys. I.2, 185a16; Anal. Prior. II.25, 69a32).",
    },
    "antiphon": {
        "name": "Antiphon the Sophist",
        "dates": "5th c. BC",
        "role": "Inscriber of Polygons for Circle Quadrature",
        "bio": "Attempted to square the circle by endlessly doubling the sides of an inscribed polygon until its perimeter supposedly coincided with the circumference—violating the infinite divisibility of continuous magnitude (Phys. I.2, 185a17).",
    },
    "bryson": {
        "name": "Bryson of Heraclea",
        "dates": "fl. late 5th / early 4th c. BC",
        "role": "Sophistical Geometer of Circle Quadrature",
        "bio": "Critiqued in Posterior Analytics I.9 (75b40–76a3) for attempting to square the circle via an over-general non-geometrical principle regarding intermediates between circumscribed and inscribed polygons, violating genus-specificity.",
    },
    "archytas": {
        "name": "Archytas of Tarentum",
        "dates": "c. 428 – 347 BC",
        "role": "Pythagorean Geometer, Harmonic Theorist & Statesman",
        "bio": "Solved the duplication of the cube by three-dimensional intersection of cylinder, torus, and cone, and advanced mathematical harmonics and mechanics.",
    },
    "theaetetus": {
        "name": "Theaetetus of Athens",
        "dates": "c. 417 – c. 369 BC",
        "role": "Academic Geometer of Irrationals & the Five Regular Solids",
        "bio": "Classified quadratic irrational magnitudes through anthyphairesis (Topics VIII.3, 158b29–35; Elements Book X) and completed the construction of the five cosmic polyhedra (Elements Book XIII).",
    },
    "eudoxus": {
        "name": "Eudoxus of Cnidus",
        "dates": "c. 408 – c. 355 BC",
        "role": "Architect of the General Theory of Proportions & Method of Exhaustion",
        "bio": "Contemporary of Plato and Aristotle's senior colleague at the Academy. Created the universal theory of proportions (Elements Book V), enabling theorems such as alternating proportion (Anal. Post. I.5, 74a17–25) to be proved at once for numbers, lines, solids, and times.",
    },
    "menaechmus": {
        "name": "Menaechmus",
        "dates": "fl. c. 350 BC",
        "role": "Discoverer of Conic Sections & Theorist of Mathematical Principles",
        "bio": "Pupil of Eudoxus who debated the classification of mathematical principles, propositions, and constructions within the fourth-century Academy contemporaneous with Aristotle's Analytics.",
    },
    "euclid": {
        "name": "Euclid of Alexandria",
        "dates": "fl. c. 300 BC",
        "role": "Author of the Elements (Στοιχεῖα)",
        "bio": "Compiled the canonical thirteen books of the Elements a generation after Aristotle's death, systematizing Definitions, Postulates, and Common Notions in close structural dialogue with Posterior Analytics I.2 and I.10.",
    },
    "archimedes": {
        "name": "Archimedes of Syracuse",
        "dates": "c. 287 – 212 BC",
        "role": "Master of Exhaustion, Quadrature & Mathematical Physics",
        "bio": "Perfected the Eudoxian method of exhaustion and explicit continuity postulates ('Archimedes' Axiom', prefigured in Aristotle Physics III.6–7 and VI.2).",
    },
    "pappus": {
        "name": "Pappus of Alexandria",
        "dates": "fl. c. 320 AD",
        "role": "Late Antique Geometer & Author of the Mathematical Collection",
        "bio": "Preserved the Greek treasury of geometric analysis and synthesis (Synagoge Book VII), illuminating the distinction between problematic construction and theorematic demonstration.",
    },
    "alexander": {
        "name": "Alexander of Aphrodisias",
        "dates": "fl. c. 200 AD",
        "role": "The Exegete of Aristotle",
        "bio": "Authoritative Peripatetic commentator on Prior Analytics, Topics, and Metaphysics A–Δ; preserved key reconstructions of Aristotle's pre-Euclidean geometric proofs and Bryson's quadrature.",
    },
    "themistius": {
        "name": "Themistius",
        "dates": "c. 317 – c. 388 AD",
        "role": "Paraphrast of Posterior Analytics, Physics & De Anima",
        "bio": "Composed lucid Greek paraphrases of Aristotle's Posterior Analytics, Physics, and De Anima, frequently cited in Scholastic noetics and in Heath's mathematical reconstructions.",
    },
    "proclus": {
        "name": "Proclus Diadochus",
        "dates": "412 – 485 AD",
        "role": "Neoplatonic Commentator on Euclid's Elements Book I",
        "bio": "Synthesized Aristotelian demonstrative science (Anal. Post. I.10) with Neoplatonic philosophy of imagination as a 'screen' onto which understanding projects geometric figures.",
    },
    "philoponus": {
        "name": "John Philoponus",
        "dates": "c. 490 – c. 570 AD",
        "role": "Alexandrian Commentator on Analytics, Physics & De Anima",
        "bio": "Provided detailed reconstructions of Aristotle's mixed-angle proof of isosceles base angles (Anal. Prior. I.24, 41b13–22) and investigated three-dimensional spatial extension.",
    },
    "simplicius": {
        "name": "Simplicius of Cilicia",
        "dates": "c. 490 – c. 560 AD",
        "role": "Commentator on Physics & De Caelo",
        "bio": "Preserved Eudemus of Rhodes's History of Geometry (including Hippocrates's quadrature of lunes and Antiphon's polygon inscription) in his monumental commentary on Aristotle's Physics.",
    },
    "boethius": {
        "name": "Anicius Manlius Severinus Boethius",
        "dates": "c. 480 – 524 AD",
        "role": "Transmitter of the Organon & Coiner of the Quadrivium",
        "bio": "Translated Aristotle's Categories and Analytics into Latin and rendered axiōmata as communes animi conceptiones, shaping medieval Scholastic mathematics.",
    },
    "averroes": {
        "name": "Averroes (Ibn Rushd)",
        "dates": "1126 – 1198",
        "role": "The Commentator on Aristotle",
        "bio": "Author of the Long Commentaries on Posterior Analytics, Physics, De Caelo, De Anima, and Metaphysics; cited by Luca Pacioli (Metaph. II, comm. 16) for placing mathematics in primo gradu certitudinis.",
    },
    "albertus-magnus": {
        "name": "Albertus Magnus, St., O.P.",
        "dates": "c. 1200 – 1280",
        "role": "Doctor Universalis & Scholastic Commentator on Aristotle & Euclid",
        "bio": "Expounded the entire Aristotelian corpus alongside Euclidean geometry, emphasizing imaginative construction in intelligible matter.",
    },
    "thomas-aquinas": {
        "name": "Thomas Aquinas, St., O.P.",
        "dates": "1225 – 1274",
        "role": "Doctor Angelicus & Systematic Expositor of Aristotelian Noetics",
        "bio": "Authored classic commentaries on Posterior Analytics, Physics, De Caelo, De Anima, and Metaphysics, plus Super Boethium De Trinitate (q. 5–6), articulating formal mathematical abstraction in materia intelligibilis and judgment terminating in the imagination.",
    },
    "pacioli": {
        "name": "Fra Luca Pacioli, O.F.M.",
        "dates": "c. 1447 – 1517",
        "role": "Renaissance Mathematician & Author of De Divina Proportione (1509)",
        "bio": "Grounded Renaissance proportion theory, perspective, and the Platonic solids in Aristotelian-Averroist epistemological certainty, subalternation of sciences, and De Caelo cosmology.",
    },
    "bekker": {
        "name": "Immanuel Bekker",
        "dates": "1785 – 1871",
        "role": "Editor of the Prussian Academy Aristotelis Opera (1831)",
        "bio": "German classical philologist whose two-volume quarto Greek text of Aristotle (Berlin, 1831; pages 1a–1462b) established the universal scholarly standard of page, column, and line citation.",
    },
    "waitz": {
        "name": "Theodor Waitz",
        "dates": "1821 – 1864",
        "role": "Critical Editor & Commentator on Aristotle's Organon (1844–1846)",
        "bio": "Edited the two-volume Aristotelis Organon Graece (Leipzig, 1844–1846), extensively engaged by both Heath and Hoenen on geometric syllogisms and diagrams.",
    },
    "bonitz": {
        "name": "Hermann Bonitz",
        "dates": "1814 – 1888",
        "role": "Commentator on the Metaphysics & Compiler of the Index Aristotelicus (1870)",
        "bio": "Produced the foundational commentary on Aristotle's Metaphysics (1848–1849) and Volume V of the Prussian Academy edition, the monumental Index Aristotelicus (1870).",
    },
    "ross": {
        "name": "Sir William David Ross",
        "dates": "1877 – 1971",
        "role": "General Editor of the Oxford Translation & Critical Editor of Metaphysics, Physics & Analytics",
        "bio": "Co-directed the twelve-volume Oxford Translation of Aristotle (1908–1931) and edited the landmark Clarendon critical texts and commentaries on Metaphysics (1924), Physics (1936), Analytics (1949), and De Anima (1961).",
    },
    "heath": {
        "name": "Sir Thomas Little Heath",
        "dates": "1861 – 1940",
        "role": "Historian of Greek Mathematics, Translator of Euclid & Author of Mathematics in Aristotle",
        "bio": "Demonstrated across The Thirteen Books of Euclid's Elements (2nd ed. 1926) and his posthumous Mathematics in Aristotle (1949) how Aristotle's logical and physical treatises preserve the living workshop of pre-Euclidean fourth-century geometry.",
    },
    "mure": {
        "name": "Geoffrey Reginald Gilchrist Mure",
        "dates": "1893 – 1979",
        "role": "Oxford Translator of Aristotle's Posterior Analytics & Warden of Merton College",
        "bio": "Translated the Posterior Analytics for Volume I of the Oxford Works of Aristotle (1926/1928), rendering Aristotle's technical vocabulary of apodeictic science into classic English.",
    },
    "hoenen": {
        "name": "Petrus Hubertus Jacobus Hoenen, S.J.",
        "dates": "1880 – 1961",
        "role": "Professor at the Pontifical Gregorian University & Author of De Noetica Geometriae (1952)",
        "bio": "Dutch Jesuit mathematician-philosopher who recovered the Aristotelian-Thomistic doctrine of intellectual vision in the phantasm (77b30, 431b2, 1036a9, 1051a21) to resolve the modern crisis between sensory empiricism and axiomatic formalism.",
    },
    "hilbert": {
        "name": "David Hilbert",
        "dates": "1862 – 1943",
        "role": "Founder of Modern Formal Axiomatics (Grundlagen der Geometrie, 1899)",
        "bio": "Reconstructed Euclidean geometry via implicit axiomatic definitions stripped of intuitive spatial content—engaged critically by Hoenen as a brilliant deductive technique that nonetheless presupposes prior noetic intuition for consistency and meaning.",
    },
    "poincare": {
        "name": "Henri Poincaré",
        "dates": "1854 – 1912",
        "role": "Mathematician & Philosopher of Geometric Conventionalism and Intuition",
        "bio": "Defended synthetic mathematical intuition against pure logicism while treating metric axioms as conventions; contrasted in GEOMETOR with Aristotelian abstraction from continuous extension.",
    },
    "smith-ja": {
        "name": "John Alexander Smith",
        "dates": "1863 – 1939",
        "role": "Waynflete Professor of Moral and Metaphysical Philosophy, Oxford & Co-Editor of the Oxford Aristotle",
        "bio": "Co-edited The Works of Aristotle Translated into English with W. D. Ross and authored the classic 1931 Oxford translation of De Anima staged in Liber IV of this Codex.",
    },
    "edghill": {
        "name": "Ella Mary Edghill",
        "dates": "1881 – 1912",
        "role": "Classical Scholar & Oxford Translator of the Categories and De Interpretatione",
        "bio": "Translated Aristotle's Categories (1928 Clarendon Press edition) staged in Liber II.A of this Codex.",
    },
    "jenkinson": {
        "name": "Alfred James Jenkinson",
        "dates": "1877 – 1915",
        "role": "Fellow of Brasenose College, Oxford & Translator of the Prior Analytics",
        "bio": "Translated Aristotle's Prior Analytics for the Oxford Translation (Vol. I, 1928), staged in Liber II.A of this Codex.",
    },
    "pickard-cambridge": {
        "name": "William Adair Pickard-Cambridge",
        "dates": "1879 – 1957",
        "role": "Fellow of Worcester College, Oxford & Translator of the Topics",
        "bio": "Translated Aristotle's Topics and Sophistici Elenchi for the Oxford Translation (Vol. I, 1928), staged in Liber II.B of this Codex.",
    },
    "hardie": {
        "name": "Robert Purves Hardie",
        "dates": "1864 – 1942",
        "role": "Reader in Ancient Philosophy, University of Edinburgh & Co-Translator of the Physics",
        "bio": "Co-authored with R. K. Gaye the Clarendon Press Oxford translation of Aristotle's Physics (Vol. II, 1930), staged in Liber III.A and Liber III.B of this Codex.",
    },
    "gaye": {
        "name": "Russell Kerr Gaye",
        "dates": "1877 – 1909",
        "role": "Fellow of Trinity College, Cambridge & Co-Translator of the Physics",
        "bio": "Translated Books V–VIII of Aristotle's Physics (including Book VI on the continuum and Zeno's paradoxes) for the 1930 Oxford edition staged in Liber III.B.",
    },
    "stocks": {
        "name": "John Leofric Stocks",
        "dates": "1882 – 1937",
        "role": "Fellow of St John's College, Oxford & Translator of De Caelo",
        "bio": "Authored the Clarendon Press Oxford translation of Aristotle's De Caelo (1922/1930), staged in Liber III.B of this Codex.",
    },
}


CITATIONS_DATA: dict[str, dict[str, str]] = {
    "bekker:1831": {
        "author": "Bekker, Immanuel (ed.)",
        "work": "Aristotelis Opera, edidit Academia Regia Borussica, Vols. I–II (Berlin: Georg Reimer, 1831; Oxford repr. 1837)",
        "locus": "1a–1462b",
        "notes": "Canonical Greek critical text defining universal Bekker page, column (a/b), and line coordinates.",
    },
    "ross:metaphysics:1924": {
        "author": "Ross, Sir William David (ed.)",
        "work": "Aristotle's Metaphysics: A Revised Text with Introduction and Commentary, 2 vols. (Oxford: Clarendon Press, 1924)",
        "locus": "980a–1093b",
        "notes": "Standard critical Greek edition and commentary for Liber V of this Codex.",
    },
    "ross:physics:1936": {
        "author": "Ross, Sir William David (ed.)",
        "work": "Aristotle's Physics: A Revised Text with Introduction and Commentary (Oxford: Clarendon Press, 1936)",
        "locus": "184a–267b",
        "notes": "Standard critical commentary on Aristotle's abstraction, infinite, place, and continuum treatises.",
    },
    "ross:analytics:1949": {
        "author": "Ross, Sir William David (ed.)",
        "work": "Aristotle's Prior and Posterior Analytics: A Revised Text with Introduction and Commentary (Oxford: Clarendon Press, 1949)",
        "locus": "24a–100b",
        "notes": "Comprehensive philological and logical commentary on the Analytics.",
    },
    "waitz:organon:1844": {
        "author": "Waitz, Theodor (ed.)",
        "work": "Aristotelis Organon Graece, 2 vols. (Leipzig: Hahn, 1844–1846)",
        "locus": "Vols. I–II",
        "notes": "Nineteenth-century critical edition and Latin commentary cited throughout Heath and Hoenen.",
    },
    "bonitz:index:1870": {
        "author": "Bonitz, Hermann",
        "work": "Index Aristotelicus, Aristotelis Opera Vol. V (Berlin: Georg Reimer, 1870)",
        "locus": "pp. 1–878",
        "notes": "Exhaustive lexicon of Aristotle's Greek philosophical and mathematical terminology.",
    },
    "oxford:works:1908": {
        "author": "Smith, J. A., and W. D. Ross (eds.)",
        "work": "The Works of Aristotle Translated into English, Vols. I–III, VIII (Oxford: Clarendon Press, 1908–1931)",
        "locus": "Vols. I, II, III, VIII",
        "notes": "Public-domain Oxford English translations by Edghill, Jenkinson, Mure, Pickard-Cambridge, Hardie & Gaye, Stocks, Smith, and Ross staged in this Codex.",
    },
    "heath:euclid:1926": {
        "author": "Heath, Sir Thomas Little",
        "work": "The Thirteen Books of Euclid's Elements, 2nd ed., 3 vols. (Cambridge University Press, 1926) [geometor/euclid]",
        "locus": "Vols. I–III",
        "notes": "Contains 145 distinct Aristotelian locus citations reconstructing pre-Euclidean definitions, postulates, and proofs.",
    },
    "heath:math-aristotle:1949": {
        "author": "Heath, Sir Thomas Little",
        "work": "Mathematics in Aristotle (Oxford: Clarendon Press, 1949)",
        "locus": "pp. 1–291",
        "notes": "Systematic treatise-by-treatise mathematical commentary on every geometrical and arithmetical passage in the Aristotelian corpus.",
    },
    "hoenen:noetica:1952": {
        "author": "Hoenen, Petrus Hubertus Jacobus, S.J.",
        "work": "De Noetica Geometriae: Origine Theoriae Cognitionis, Analecta Gregoriana Vol. 56 (Rome: Pontificia Universitas Gregoriana, 1952) [geometor/hoenen]",
        "locus": "Cap. I–VII & Appendix",
        "notes": "Contains 64 Aristotelian locus keys developing the noetics of intellectual intuition in the phantasm and intelligible matter.",
    },
    "pacioli:divina:1509": {
        "author": "Pacioli, Fra Luca, O.F.M.",
        "work": "De Divina Proportione (Venice: Paganino Paganini, 1509) [geometor/pacioli]",
        "locus": "Compendio Cap. I–V & Architectura",
        "notes": "Renaissance treatise citing Aristotle on mathematical certitude, subalternation of perspective/music, and the five regular solids.",
    },
    "euclid:elements": {
        "author": "Euclid of Alexandria",
        "work": "Elements (Στοιχεῖα, ed. J. L. Heiberg, Leipzig, 1883–1888)",
        "locus": "Books I–XIII",
        "notes": "The canonical Greek synthesis of definitions, postulates, common notions, plane geometry, Eudoxian proportion, irrationals, and stereometry.",
    },
    "euclid:I.5": {
        "author": "Euclid of Alexandria",
        "work": "Elements, Book I, Proposition 5 (Pons Asinorum)",
        "locus": "I.5",
        "notes": "Equality of base angles in an isosceles triangle; contrasted with Aristotle's older mixed-angle proof in Prior Analytics I.24 (41b13–22).",
    },
    "euclid:I.29": {
        "author": "Euclid of Alexandria",
        "work": "Elements, Book I, Postulate 5 & Proposition 29 (Theory of Parallels)",
        "locus": "Post. 5; I.27–29",
        "notes": "Euclid's resolution of the circularity in parallel-line proofs diagnosed by Aristotle in Prior Analytics II.16 (65a4–9).",
    },
    "euclid:I.32": {
        "author": "Euclid of Alexandria",
        "work": "Elements, Book I, Proposition 32 (Interior Angles of a Triangle = 2R)",
        "locus": "I.32",
        "notes": "Proved via the parallel through the vertex; cited in Posterior Analytics I.5 (74a25–32), I.31 (87b35), and Metaphysics Θ.9 (1051a24–26).",
    },
    "euclid:III.31": {
        "author": "Euclid of Alexandria",
        "work": "Elements, Book III, Proposition 31 (Angle in a Semicircle is Right)",
        "locus": "III.31",
        "notes": "Proved in Metaphysics Θ.9 (1051a26–29) and Posterior Analytics II.11 (94a28–34) by erecting the radius from the center of the diameter.",
    },
    "euclid:V.def.5": {
        "author": "Euclid of Alexandria / Eudoxus of Cnidus",
        "work": "Elements, Book V, Definition 5 & Proposition 16 (General Proportion & Alternation)",
        "locus": "V.Def.5; V.16",
        "notes": "General Eudoxian theory of proportion heralded in Posterior Analytics I.5 (74a17–25) as superseding separate proofs for numbers, lines, solids, and times.",
    },
    "euclid:X.2": {
        "author": "Euclid of Alexandria / Theaetetus",
        "work": "Elements, Book X, Propositions 2–3 (Anthyphairetic Criterion of Incommensurability)",
        "locus": "X.2–3",
        "notes": "Geometric preservation of reciprocal subtraction (antanairesis), attested in Topics VIII.3 (158b29–35).",
    },
    "plato:meno": {
        "author": "Plato",
        "work": "Meno",
        "locus": "80d–86c",
        "notes": "Meno's paradox of inquiry and the geometric doubling of the square, explicitly answered in Posterior Analytics I.1 (71a29).",
    },
    "plato:republic": {
        "author": "Plato",
        "work": "Republic, Books VI–VII (Divided Line & Quadrivium)",
        "locus": "509d–511e, 525a–534d",
        "notes": "Distinction between discursive mathematical dianoia from hypotheses and dialectical noēsis.",
    },
    "plato:timaeus": {
        "author": "Plato",
        "work": "Timaeus",
        "locus": "48e–56c",
        "notes": "Identification of receptacle space (chōra) with matter and construction of physical bodies out of elementary plane triangles—critiqued in Physics IV.2 and De Caelo III.7–8.",
    },
    "proclus:in-euclidem": {
        "author": "Proclus Diadochus",
        "work": "In Primum Euclidis Elementorum Librum Commentarii (ed. G. Friedlein, Leipzig, 1873)",
        "locus": "pp. 48–84, 178–207",
        "notes": "Preserves the Eudemian summary of Greek geometry and compares Aristotelian axioms, postulates, and hypotheses with Euclid's Elements.",
    },
    "alexander:in-metaph": {
        "author": "Alexander of Aphrodisias",
        "work": "In Aristotelis Metaphysica Commentaria (ed. M. Hayduck, CAG I, Berlin, 1891)",
        "locus": "CAG I",
        "notes": "Classical Peripatetic commentary on Metaphysics A–Δ (with pseudo-Alexander / Michael of Ephesus on E–N).",
    },
    "simplicius:in-physica": {
        "author": "Simplicius of Cilicia",
        "work": "In Aristotelis Physicorum Libros Commentaria (ed. H. Diels, CAG IX–X, Berlin, 1882–1895)",
        "locus": "CAG IX–X",
        "notes": "Essential source on Antiphon, Bryson, Hippocrates of Chios, and Zeno's continuum arguments.",
    },
    "philoponus:in-anal-post": {
        "author": "John Philoponus",
        "work": "In Aristotelis Analytica Priora et Posteriora Commentaria (ed. M. Wallies, CAG XIII.2–3, Berlin, 1905–1909)",
        "locus": "CAG XIII.2–3",
        "notes": "Preserves ancient reconstructions of Aristotle's geometric examples in the Analytics.",
    },
    "aquinas:in-anal-post": {
        "author": "Thomas Aquinas, St., O.P.",
        "work": "Expositio Libri Posteriorum Analyticorum (Leonine ed., Vol. I*2, Rome, 1989)",
        "locus": "Lib. I–II",
        "notes": "Scholastic exposition of demonstrative science, axioms vs. postulates, subalternation, and intuitive epagōgē.",
    },
    "aquinas:in-boeth-trin": {
        "author": "Thomas Aquinas, St., O.P.",
        "work": "Super Boethium De Trinitate (Leonine ed., Vol. L, Rome, 1992)",
        "locus": "qq. 5–6",
        "notes": "Locus classicus on the three degrees of theoretical distinction/abstraction and the termination of mathematical judgment in the imagination (ad imaginationem).",
    },
    "averroes:in-metaph": {
        "author": "Averroes (Ibn Rushd)",
        "work": "Aristotelis Metaphysicorum Libri XIIII cum Averrois Cordubensis in eosdem Commentariis (Venice: Junta, 1562)",
        "locus": "Lib. II, comm. 14–16",
        "notes": "Classical Peripatetic-Arabic exposition of Metaphysics α.3 (995a14–17) on mathematical exactitude (akribeia) and abstraction from sensible matter.",
    },
    "hilbert:grundlagen:1899": {
        "author": "Hilbert, David",
        "work": "Grundlagen der Geometrie (Leipzig: Teubner, 1899)",
        "locus": "Chs. I–II",
        "notes": "Modern formalist axiomatization contrasted with Aristotelian intuitive first principles in the Codex commentary.",
    },
}


def write_apparatus_jsons(repo_root: Path) -> None:
    """Write ``glossary.json``, ``persons.json``, and ``citations.json`` to ``resources/``.

    Writes to both ``resources/loci_geometrici/`` and ``resources/`` so Sphinx hover
    tooltips resolve from any document subtree.

    Args:
        repo_root: Root directory of ``geometor/aristotle``.
    """
    for target_dir in (
        repo_root / "resources" / "loci_geometrici",
        repo_root / "resources",
    ):
        target_dir.mkdir(parents=True, exist_ok=True)
        (target_dir / "glossary.json").write_text(
            json.dumps(GLOSSARY_DATA, indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )
        (target_dir / "persons.json").write_text(
            json.dumps(PERSONS_DATA, indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )
        (target_dir / "citations.json").write_text(
            json.dumps(CITATIONS_DATA, indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )


def render_glossary_rst() -> str:
    """Render ``docsrc/loci_geometrici/glossary.rst`` with ``.. _term-<slug>:`` anchors."""
    lines = [
        ":order: 93",
        ":layout: book",
        ":type: apparatus",
        ":title: Glossary of Noetic & Geometric Terms",
        "",
        ".. _glossary:",
        "",
        "======================================",
        "Glossary of Noetic & Geometric Terms",
        "======================================",
        "",
        ".. rubric:: Greek, Scholastic Latin & Mathematical Lexicon of *Loci Geometrici et Noetici*",
        "",
        "Systematic lexicon of thirty-six foundational Aristotelian concepts governing demonstrative science (*epistēmē*), syllogistic necessity, continuous vs. discrete quantity, potential infinity, imaginative presentation (*phantasma*), and abstraction in intelligible matter (*hylē noētē*).",
        "",
    ]
    for key, entry in GLOSSARY_DATA.items():
        slug = apparatus_slug(key)
        lines.extend(
            [
                f".. _term-{slug}:",
                "",
                f"{entry['headword']}",
                "-" * len(entry["headword"]),
                "",
                f"- **Greek**: *{entry['greek']}*  |  **Scholastic Latin**: *{entry['latin']}*",
                f"- **Rendering**: {entry['translation']}",
                f"- **Primary Bekker Loci**: ``{entry['loci']}``",
                "",
                f"{entry['definition']}",
                "",
            ]
        )
    return "\n".join(lines).rstrip() + "\n"


def render_persons_rst() -> str:
    """Render ``docsrc/loci_geometrici/persons.rst`` with ``.. _person-<slug>:`` anchors."""
    lines = [
        ":order: 92",
        ":layout: book",
        ":type: apparatus",
        ":title: Index of Persons & Commentators",
        "",
        ".. _persons:",
        "",
        "===============================",
        "Index of Persons & Commentators",
        "===============================",
        "",
        ".. rubric:: Ancient Geometers, Peripatetic Exegetes, Scholastics & Modern Editors",
        "",
        "Biographical register of philosophers, mathematicians, ancient commentators, Scholastic doctors, and modern philologists engaged across *Loci Geometrici et Noetici* and the GEOMETOR canon.",
        "",
    ]
    for key, entry in PERSONS_DATA.items():
        slug = apparatus_slug(key)
        heading = f"{entry['name']} ({entry['dates']})"
        lines.extend(
            [
                f".. _person-{slug}:",
                "",
                heading,
                "-" * len(heading),
                "",
                f"**{entry['role']}**",
                "",
                f"{entry['bio']}",
                "",
            ]
        )
    return "\n".join(lines).rstrip() + "\n"


def render_bibliography_rst() -> str:
    """Render ``docsrc/loci_geometrici/bibliography.rst`` with ``.. _cite-<slug>:`` anchors."""
    lines = [
        ":order: 91",
        ":layout: book",
        ":type: apparatus",
        ":title: Bibliography & Editions",
        "",
        ".. _bibliography:",
        "",
        "=======================",
        "Bibliography & Editions",
        "=======================",
        "",
        ".. rubric:: Critical Greek Editions, Oxford Translations, Classical Treatises & Commentaries",
        "",
        "Authoritative editions, translations, classical mathematical propositions, and commentaries cited across the primary apparatus and analytical notes of *Loci Geometrici et Noetici*.",
        "",
    ]
    for key, entry in CITATIONS_DATA.items():
        slug = apparatus_slug(key)
        heading = f"{entry['author']} — {entry['work']}"
        lines.extend(
            [
                f".. _cite-{slug}:",
                "",
                f"**{heading}**",
                "",
                f"- **Citation Key**: ``{key}``  |  **Locus**: ``{entry['locus']}``",
                f"- **Significance**: {entry['notes']}",
                "",
            ]
        )
    return "\n".join(lines).rstrip() + "\n"
