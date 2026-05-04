# Source Audit: Chapter 4 Reals Through Dedekind Cuts

Scope: `tex/chapter04_reals_dedekind.tex`.

Owned files updated in this pass:

- `tex/chapter04_reals_dedekind.tex`
- `docs/source_audit_reals.md`

Sources used:

- `build/extracted/MATH1090_Lecture_Notes_Apr18.txt`
- `build/extracted/MATH1090_Worksheet6.txt`
- `build/extracted/MATH1090_Worksheet7.txt`
- `build/extracted/MATH1090_HW7.txt`
- `build/extracted/MATH1090_HW8.txt`
- `reference/Elementary Set Theory.pdf`, via `build/extracted/Elementary Set Theory.txt`
- `reference/halmos__naive_set_theory.pdf`, via `build/extracted/halmos__naive_set_theory.txt`

Textbook-reference role:

- The set-theory references were used for textbook-level style around ordered sets, initial-segment intuition, least-upper-bound language, and set-based construction discipline.
- The actual exercise statements and required item coverage come from the MATH1090 lecture notes, worksheets, and homework extracts listed above.

## Coverage Checklist

Every required item below has a discoverable `exerciseblock` title, a non-empty `solution`, and a non-empty `explanation`.

### Lecture Notes Exercises 39--56

| Required item | Status | Chapter coverage |
| --- | --- | --- |
| Lecture Notes Exercise 39 | Covered | Restricted order on a subset of a totally ordered set |
| Lecture Notes Exercise 40 | Covered | Translation compatibility and product of non-negative rationals |
| Lecture Notes Exercise 41 | Covered | \(\Z\) has no maximum or minimum |
| Lecture Notes Exercise 42 | Covered with stated correction | Positive \(s\) with \(s^2>2\) is an upper bound for \(S=\{x\in\Q:x^2<2\}\) |
| Lecture Notes Exercise 43 | Covered | Perturbation upward when \(s^2<2\) |
| Lecture Notes Exercise 44 | Covered with stated correction | Perturbation downward for positive \(s\) with \(s^2>2\) |
| Lecture Notes Exercise 45 | Covered | Pair and one-set Dedekind cut equivalence |
| Lecture Notes Exercise 46 | Covered | Rational cuts and injective embedding \(i:\Q\to\R\) |
| Lecture Notes Exercise 47 | Covered | Negative of a rational cut |
| Lecture Notes Exercise 48 | Covered | Completeness of Dedekind cuts by union and infimum by negation |
| Lecture Notes Exercise 49 | Covered | Decimal expansion from a Dedekind cut |
| Lecture Notes Exercise 50 | Covered | Positive cut \(r\) with \(r^2=2\) |
| Lecture Notes Exercise 51 | Covered | Symbolic \(\varepsilon\)-\(N\) convergence definition |
| Lecture Notes Exercise 52 | Covered | Constant zero sequence has limit \(0\) |
| Lecture Notes Exercise 53 | Covered | Cauchy and non-Cauchy examples |
| Lecture Notes Exercise 54 | Covered | Rationals as constant Cauchy-sequence classes |
| Lecture Notes Exercise 55 | Covered | Representatives of \(1/2\) |
| Lecture Notes Exercise 56 | Covered | Multiplicative inverse of a nonzero Cauchy class |

### Starred Section 4.13

| Required item | Status | Chapter coverage |
| --- | --- | --- |
| 4.13 Cauchy sequences | Covered | Cauchy definition, equivalence-class construction, rational embedding, representatives, operations context, and inverse proof |

### Worksheet 6

| Required item | Status | Chapter coverage |
| --- | --- | --- |
| Worksheet 6 Exercise 1 | Covered | Four Dedekind cut examples/non-examples |
| Worksheet 6 Exercise 2 | Covered | \(p^{\R}+q^{\R}=(p+q)^{\R}\) |
| Worksheet 6 Exercise 3 | Covered | Existence, uniqueness, rational case, and irrational formula for \(-A\) |
| Worksheet 6 Exercise 4 | Covered | Irrational \(\sqrt2\) cut and product \(A\cdot A=2^{\R}\) |

### Worksheet 7

| Required item | Status | Chapter coverage |
| --- | --- | --- |
| Worksheet 7 Exercise 1 | Covered | Triangle and reverse triangle inequalities |
| Worksheet 7 Exercise 2 | Covered | Limits \(0\), \(1\), and divergence of \(2^n\) |
| Worksheet 7 Exercise 3 | Covered | Convergent sequences are bounded |
| Worksheet 7 Exercise 4 | Covered | Absolute values preserve limits |
| Worksheet 7 Exercise 5 | Covered | \(\sqrt{n+1}-\sqrt n\to0\) |

### Homework 7

| Required item | Status | Chapter coverage |
| --- | --- | --- |
| Homework 7 Problem 1 | Covered | Four set-operation cases for Dedekind cuts |
| Homework 7 Problem 2 | Covered | Lower-bounded non-empty subset has infimum |
| Homework 7 Problem 3 | Covered | Associativity of Dedekind-cut addition |
| Homework 7 Problem 4 | Covered | \(\{x\in\Q:x^3<5\}\) is a Dedekind cut |

### Homework 8

| Required item | Status | Chapter coverage |
| --- | --- | --- |
| Homework 8 Problem 1 | Covered | Trichotomy around \(0^{\R}\) |
| Homework 8 Problem 2 | Covered | Multiplicative inverse for positive and negative cuts, plus uniqueness |
| Homework 8 Problem 3 | Covered | Archimedean property by completeness and supremum |
| Homework 8 Problem 4 | Covered | Square-root existence and uniqueness by supremum method |

## Source Ambiguity

- Lecture Notes Exercise 42 in the extracted text appears as a positive-upper-bound step for \(S=\{x\in\Q:x^2<2\}\). The statement is false if interpreted as all rationals with only \(s^2>2\), because negative \(s\) cannot be an upper bound while \(0\in S\). The chapter states and proves the mathematically valid positive version.
- Lecture Notes Exercise 44 has the same positive-bound context. The chapter states \(s>0\) and \(s^2>2\), then constructs a smaller positive upper bound.
- The decimal-expansion paragraph in the extracted lecture notes has a damaged closing parenthesis in the definition of the upper-bound set \(B\). The chapter uses the intended construction: lower and upper decimal truncations determine nested rational intervals.
- The extracted Definition 37 in starred 4.13 appears OCR-damaged, writing \(x_n\leq y_n\) with mismatched quantified variables. The chapter covers the requested Cauchy-sequence construction and inverse proof, but does not rely on the damaged order definition.

## Validation Notes

Final-review refinement round on 2026-05-04:

- Expanded Chapter 4 prose around ordered fields, completeness, Dedekind cuts, operations on cuts, decimal expansions, sequence limits, Cauchy sequences, and Homework 8 theorem patterns.
- Added exercise-method guidance inside existing `explanation` environments while preserving all exact `exerciseblock` labels and every existing `solution` / `explanation` environment.
- Corrected the additive-inverse gap argument in Worksheet 6 Exercise 3 so the inequality uses \(x<a-b\) after choosing \(0<b-a<-x\).

Checks run in this final-review refinement:

- Targeted grep for the banned handwaving phrases listed in the task, limited to the two owned files.
  - Result: no matches.
- Targeted grep for the known mojibake characters used by the local QA script, limited to the two owned files.
  - Result: no matches.
- Scoped Chapter 4 Python count for all exercise blocks.
  - Result: passed; `exerciseblocks=35 missing_solution_or_explanation=0`.
- `git diff --check -- tex/chapter04_reals_dedekind.tex docs/source_audit_reals.md`
  - Result: passed; no whitespace errors.

Earlier validation retained from the previous Chapter 4 rewrite:

- `python3 scripts/qa_exercise_coverage.py`
  - Result: whole-repo check currently fails on older missing/short items outside this task's ownership scope, mostly earlier chapters and homework items. Chapter 4's required items were checked separately as above.
- Full-document `latexmk` was attempted with temporary output under `/private/tmp/math1090-build`.
  - Result: currently blocked before Chapter 4 by an existing alignment error in `tex/chapter01_logic.tex:419`, outside this task's ownership scope.
- Isolated Chapter 4 XeLaTeX check was run through the project preamble with temporary output under `/private/tmp/math1090-ch4`.
  - Result: passed; produced `/private/tmp/math1090-ch4/chapter4_check.pdf`.
  - Caveat: the isolated build reports CJK font-shape substitution warnings from the document font setup.
