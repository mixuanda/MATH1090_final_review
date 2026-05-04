# Source Audit: Chapter 7 Sets with Structure

Primary chapter file: `tex/chapter07_structure.tex`.

## Sources Used

- `build/extracted/MATH1090_Lecture_Notes_Apr18.txt`, Chapter 7, lines around 2516-2744.
- `build/extracted/MATH1090_Worksheet10.txt`.

## Lecture Notes Coverage

| Item | Status | Notes |
| --- | --- | --- |
| Binary operations and Boolean integers | Covered | Introduced before Exercise 65. |
| Lecture Notes Exercise 65 | Covered | Boolean additive inverses checked by cases. |
| Lecture Notes Exercise 66 | Covered | Examples include subtraction, union, intersection, function composition, and maximum. |
| Lecture Notes Exercise 67 | Covered | Ring definition given with additive abelian group, associative multiplication, and distributive laws. |
| Monoids and identity uniqueness | Covered | Includes monoid definition and identity uniqueness proof. |
| Lecture Notes Exercise 68 | Covered | Uses `(N,+)` as monoid not group. |
| Groups, homomorphisms, isomorphisms | Covered | Definitions included. |
| Lecture Notes Exercise 69 | Covered | Noncommuting matrices in `GL(2,R)`. |
| Lecture Notes Exercise 70 | Covered | Explicit isomorphism from Spoolean `C` to Boolean `B`. |
| Symmetric groups | Covered | Definition of `S_X` and `S_n`. |
| Lecture Notes Exercise 71 | Covered | Lists all bijections of two- and three-element sets. |
| Lecture Notes Exercise 72 | Covered | Explicit isomorphism `S_2 -> Z_2`. |

## Final-review Refinement Notes

- 2026-05-04 Worker C pass deepened `tex/chapter07_structure.tex` with textbook-style Chinese prose and English mathematical terms.
- Added method-oriented explanations for structured sets, binary operation closure, Cayley-style tables, monoid and group checklists, homomorphism/isomorphism verification, symmetric groups, conjugacy, and Worksheet 10 problem-solving patterns.
- Added expanded theorem/proposition discussion for identity uniqueness, inverse behavior, socks-shoes property, cancellation, homomorphism preservation of identity/inverses, and `S_X` as a group.
- Preserved the existing Chapter 7 `exerciseblock` labels and all `solution` / `explanation` environments.

## Worksheet 10 Coverage

| Item | Status | Notes |
| --- | --- | --- |
| Worksheet 10 Exercise 1 | Covered | Proves right inverse is two-sided using associativity. |
| Worksheet 10 Exercise 2 | Covered | Proves conjugacy is reflexive, symmetric, and transitive. |
| Worksheet 10 Exercise 3 | Covered | Describes the eight square symmetries algebraically via `r` and `s`; no TikZ drawing. |
| Worksheet 10 Exercise 4 | Covered | Lists all conjugacy classes of `D_8`. |
| Worksheet 10 Exercise 5 | Covered | Constructs inclusion `S_2 -> S_3` and sign map `S_3 -> S_2`. |

## Ambiguities

- Worksheet 10 asks to draw pictures for the elements of `D_8`. The chapter gives an algebraic description by vertex permutations, which is more stable in LaTeX text and still identifies all eight symmetries.
- The extracted worksheet writes `f : Z/nZ -> Z/nZ` while describing `D_8`; the chapter uses the square-vertex model `Z/4Z`, which matches a square.
