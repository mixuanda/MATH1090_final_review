# Source Audit: Chapter 6 Big sets

Scope: `tex/chapter06_big_sets.tex`.

## Ownership

- Edited only `tex/chapter06_big_sets.tex` and this audit file.
- The chapter was replaced from scratch because the previous file contained
  mojibake throughout.

## Sources Used

- `build/extracted/MATH1090_Lecture_Notes_Apr18.txt`
  - Chapter 6 sections 6.1--6.7.
  - Lecture Notes Exercise 62 through Lecture Notes Exercise 64.
  - Starred sections 6.2, 6.3, 6.5, 6.6, and 6.7.
- `build/extracted/MATH1090_Worksheet8.txt`
  - Worksheet 8 Exercise 1 through Worksheet 8 Exercise 4.
- `build/extracted/MATH1090_HW9.txt`
  - Homework 9 Problem 3 and Homework 9 Problem 4.
- `reference/Elementary Set Theory.pdf`
  - Checked through `build/extracted/Elementary Set Theory.txt`; extraction was
    not very useful for the requested advanced cardinality topics, so it served
    only as general set-theory background.
- `reference/halmos__naive_set_theory.pdf`
  - Checked through `build/extracted/halmos__naive_set_theory.txt`; used as
    textbook-level background for Axiom of Choice, Zorn's Lemma, Cantor's
    theorem, cardinal numbers, and the continuum hypothesis.

## Required Coverage Checklist

- [x] `Lecture Notes Exercise 62`
  - Exact title present.
  - Contains non-empty `solution` and non-empty `explanation`.
  - Proves \(\card{\N}=\card{\Z}\) by explicit bijection.
- [x] `Lecture Notes Exercise 63`
  - Exact title present.
  - Contains non-empty `solution` and non-empty `explanation`.
  - Covers bounded open, closed, half-closed, and unbounded intervals using
    affine maps, compression injections, logarithm maps, and
    Cantor--Bernstein.
- [x] `Lecture Notes Exercise 64`
  - Exact title present.
  - Contains non-empty `solution` and non-empty `explanation`.
  - Proves Archimedean property from the least upper bound property.
- [x] `Lecture Notes Section 6.2 Continuum hypothesis`
  - Exact discoverable section exerciseblock present.
  - Contains non-empty `solution` and non-empty `explanation`.
  - States CH and its ZFC independence role.
- [x] `Lecture Notes Section 6.3 Axiom of choice and Zorn's Lemma`
  - Exact discoverable section exerciseblock present.
  - Contains non-empty `solution` and non-empty `explanation`.
  - Covers choice functions, surjection-to-injection consequence, countable
    union of countable sets, chain, upper bound, maximal element, and Zorn's
    Lemma.
- [x] `Lecture Notes Section 6.5 Cantor set`
  - Exact discoverable section exerciseblock present.
  - Contains non-empty `solution` and non-empty `explanation`.
  - Covers construction, ternary characterization, removed-length series, and
    \(\card{C}=\card{\R}\).
- [x] `Lecture Notes Section 6.6 Density`
  - Exact discoverable section exerciseblock present.
  - Contains non-empty `solution` and non-empty `explanation`.
  - Covers density definition, \(\Z\) not dense, \(\Q\) dense, and dense in a
    subset.
- [x] `Lecture Notes Section 6.7 Well-ordering`
  - Exact discoverable section exerciseblock present.
  - Contains non-empty `solution` and non-empty `explanation`.
  - Covers finite ordinals, \(\N\), \(\Z\), \(\Q^+\), countable sets, and the
    Well-Ordering Theorem.
- [x] `Worksheet 8 Exercise 1`
  - Exact title present.
  - Contains non-empty `solution` and non-empty `explanation`.
  - Uses inverse of the Lecture Notes Exercise 62 bijection.
- [x] `Worksheet 8 Exercise 2`
  - Exact title present.
  - Contains non-empty `solution` and non-empty `explanation`.
  - Proves \(\card{\N\times\N}=\card{\N}\) with Cantor pairing.
- [x] `Worksheet 8 Exercise 3`
  - Exact title present.
  - Contains non-empty `solution` and non-empty `explanation`.
  - Identifies \(\card{\N}<\card{[0,1]}\).
- [x] `Worksheet 8 Exercise 4`
  - Exact title present.
  - Contains non-empty `solution` and non-empty `explanation`.
  - Proves \(\card{(0,1)}=\card{[0,1]}\) using Cantor--Bernstein.
- [x] `Homework 9 Problem 3`
  - Exact title present.
  - Contains non-empty `solution` and non-empty `explanation`.
  - Gives a concrete \(X=Y=\N\) counterexample for both proposed maps.
- [x] `Homework 9 Problem 4`
  - Exact title present.
  - Contains non-empty `solution` and non-empty `explanation`.
  - Proves \(\card{\N\times\N\times\N}=\card{\N}\) by iterating Cantor
    pairing.

## Source Ambiguity

- Lecture Notes Exercise 63 says "all intervals have the same cardinality".
  This is false if empty intervals or singleton intervals such as \([a,a]\)
  are included. The chapter states this caveat and solves the standard
  non-degenerate real-interval version.
- `build/extracted/Elementary Set Theory.txt` contains little searchable text
  relevant to the requested cardinality and choice-principle exposition. The
  PDF was still treated as a general background reference, while detailed
  statements came from the lecture notes and Halmos extraction.
- `build/extracted/halmos__naive_set_theory.txt` is noisy OCR/extraction text.
  It was useful for confirming topic placement and standard formulations, but
  the chapter does not quote it.

## Local Validation Notes

- Run the required targeted banned-phrase grep on the two owned files.
- Run a targeted mojibake/rare-garbage grep on the two owned files.
- Run a LaTeX build after the grep checks.
