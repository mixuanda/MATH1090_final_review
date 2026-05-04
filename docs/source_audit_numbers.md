# Source Audit: Chapter 3 Numbers

Scope: `tex/chapter03_integers_rationals.tex`.

Owned files changed in this pass:

- `tex/chapter03_integers_rationals.tex`
- `docs/source_audit_numbers.md`

Sources used:

- `build/extracted/MATH1090_Lecture_Notes_Apr18.txt`
- `build/extracted/MATH1090_Worksheet4 (1).txt`
- `build/extracted/MATH1090_Worksheet5 (2).txt`
- `build/extracted/HW5 PDF.txt`
- `build/extracted/MATH1090_HW4.txt` with null bytes stripped for reading; this file is the Homework 6 Rationals extraction.
- `build/extracted/Elementary Set Theory.txt` for quotient set, equivalence class, representative, and natural surjection background.
- `build/extracted/halmos__naive_set_theory.txt` for successor set, Axiom of Infinity, minimal inductive set, and Von Neumann ordinal background.

## Coverage Checklist

### Lecture Notes Chapter 3

- [x] Lecture Notes Exercise 25: cyclic `{0,1,2}` successor example; only `0` as successor fails.
- [x] Lecture Notes Exercise 26: recursive addition justified through Peano recursion and induction uniqueness.
- [x] Lecture Notes Exercise 27: `0+n=n` by induction.
- [x] Lecture Notes Exercise 28: recursive calculation of `2*3`.
- [x] Lecture Notes Exercise 29: addition and multiplication commutativity and associativity from recursive definitions.
- [x] Lecture Notes Exercise 30: distributivity `a*(b+c)=a*b+a*c`.
- [x] Lecture Notes Exercise 31: `N` plus disconnected `{a,b,c}` cycle; induction fails only.
- [x] Lecture Notes Exercise 32: `~_Z` on `N^2` is an equivalence relation.
- [x] Lecture Notes Exercise 33: subtraction on `Z` via additive inverse `-[(a,b)]=[(b,a)]`.
- [x] Lecture Notes Exercise 34: well-defined multiplication on `Z`.
- [x] Lecture Notes Exercise 35: integer addition and multiplication laws.
- [x] Lecture Notes Exercise 36: `~_Q` on `Z x (Z\{0})` is an equivalence relation.
- [x] Lecture Notes Exercise 37: well-defined multiplication on `Q`.
- [x] Lecture Notes Exercise 38: rational addition and multiplication laws.
- [x] Starred section 3.7: Von Neumann ordinals, `S(x)=x union {x}`, inductive sets, Axiom of Infinity, smallest inductive set, and Peano axiom verification.

### Worksheet 4

- [x] Worksheet 4 Exercise 1: proof of `S(a)+b=S(a+b)`.
- [x] Worksheet 4 Exercise 2: addition commutativity using Exercise 1.
- [x] Worksheet 4 Exercise 3: examples failing only injectivity and only induction.

### Worksheet 5

- [x] Worksheet 5 Exercise 1: well-definedness of three proposed relations on `Q`.
- [x] Worksheet 5 Exercise 2: Euclidean algorithm identity `gcd(a,b)=gcd(b,c)`.
- [x] Worksheet 5 Exercise 3: geometric power series has supremum `2` in `Q`.
- [x] Worksheet 5 Exercise 4: rational interval contains a rational subset with no supremum in `Q`.

### Homework 5

- [x] Homework 5 Problem 1: every nonzero natural number is a unique successor.
- [x] Homework 5 Problem 2: `0+n=n`.
- [x] Homework 5 Problem 3: `n+1=1+n`.
- [x] Homework 5 Problem 4: well-defined multiplication of integers.

### Homework 6

- [x] Homework 6 Problem 1: no rational solution to `x^2=2026`.
- [x] Homework 6 Problem 2: if `5x+7y=1`, then `gcd(x,y)=1`.
- [x] Homework 6 Problem 3: no rational solution to `x^2+2x=1`.
- [x] Homework 6 Problem 4: decimal set interpreted as `{1.23, 1.233, 1.2333, ...}` has supremum `37/30` in `Q`.
- [x] Homework 6 Problem 5: factorial partial sums have no rational supremum, using a tail estimate and denominator-clearing contradiction.

## Source Ambiguity

- `build/extracted/MATH1090_HW4.txt` is named like Homework 4 but its readable header is `Homework 6 Rationals`; Chapter 3 treats it as Homework 6, matching the task instruction.
- The repository also contains `build/extracted/MATH1090_HW6.txt`, but the requested source list names `MATH1090_HW4.txt` as the Homework 6 extraction. This pass did not rely on `MATH1090_HW6.txt`.
- Homework 6 Problem 4's extracted statement is terse: `1.23...3` with omitted digits all `3`. The chapter records the standard finite-decimal interpretation `{1.23, 1.233, 1.2333, ...}` and notes the resulting rational supremum `37/30`.
- Homework 6 Problem 5's OCR around the displayed inequality is corrupted. The chapter uses the reliable statement of the sequence and proves the needed tail bound `0 < f(n)-f(m) < 2/(m+1)!`, which is sufficient for the requested supremum contradiction.
- Set-theory references were used for background vocabulary and construction discipline, not as extra exercise sources: quotient set and representative language comes from `Elementary Set Theory.txt`; ordinal and minimal successor-set language comes from `halmos__naive_set_theory.txt`.

## Local QA Notes

- Required exercise titles are intentionally exact and discoverable, for example `\begin{exerciseblock}[Lecture Notes Exercise 25]`, `\begin{exerciseblock}[Worksheet 5 Exercise 1]`, and `\begin{exerciseblock}[Homework 6 Problem 1]`.
- Each required exercise block is followed by non-empty `solution` and `explanation` environments.
- Targeted grep should be run after edits for banned handwaving phrases and mojibake markers in the two owned files.
- Final-review refinement pass deepened Chapter 3 explanation blocks with transfer guidance for induction-variable choice, quotient representatives, well-definedness, gcd/divisibility, rational order, supremum arguments, and Von Neumann model verification.
