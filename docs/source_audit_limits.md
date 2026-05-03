# Source Audit: Chapter 5 Limits and Continuity

## Files Read

- `build/extracted/MATH1090_Lecture_Notes_Apr18.txt`
- `build/extracted/MATH1090_HW9.txt`

## Required Coverage Checklist

- [x] `Lecture Notes Exercise 57`
  - Source: Lecture Notes Chapter 5, Section 5.2.2.
  - Covered by exact title `\begin{exerciseblock}[Lecture Notes Exercise 57]`.
  - Content: finds a valid `delta = 0.025` for `epsilon = 0.1` in
    `lim_{x -> -2}(4x+3) = -5`, with a complete inequality check.
- [x] `Lecture Notes Exercise 58`
  - Source: Lecture Notes Chapter 5, Section 5.2.2.
  - Covered by exact title `\begin{exerciseblock}[Lecture Notes Exercise 58]`.
  - Content: epsilon-delta proof of `lim_{x -> 4} sqrt(x) = 2`, using the
    conjugate estimate `|sqrt(x)-2| = |x-4|/(sqrt(x)+2)`.
- [x] `Lecture Notes Exercise 59`
  - Source: Lecture Notes Chapter 5, Section 5.3.
  - Covered by exact title `\begin{exerciseblock}[Lecture Notes Exercise 59]`.
  - Content: nonexistence proof for `lim_{x -> 0} sin(1/x)` using two positive
    sequences approaching `0` whose function values are `1` and `-1`, then
    translated into the epsilon-delta contradiction.
- [x] `Lecture Notes Exercise 60`
  - Source: Lecture Notes Chapter 5, Section 5.4.
  - Covered by exact title `\begin{exerciseblock}[Lecture Notes Exercise 60]`.
  - Content: constructs `f(x)=|x|/x` and `g(x)=-|x|/x` near `0`, proves both
    individual limits do not exist, and proves the sum has limit `0`.
- [x] `Lecture Notes Exercise 61`
  - Source: Lecture Notes Chapter 5, Section 5.4, immediately after Example 24.
  - Covered by exact title `\begin{exerciseblock}[Lecture Notes Exercise 61]`.
  - Content: direct epsilon-delta proof of
    `lim_{x -> 0} (x^2-4)/(x-1) = 4`, with explicit denominator control and no
    use of limit laws.
- [x] `Homework 9 Problem 1`
  - Source: `build/extracted/MATH1090_HW9.txt`, Problem 1.
  - Covered by exact title `\begin{exerciseblock}[Homework 9 Problem 1]`.
  - Content: epsilon-N proof of `lim_{n -> infinity} n^2/4^n = 0`, using an
    induction estimate `n^2 <= 2^n` for `n >= 4`.
- [x] `Homework 9 Problem 2`
  - Source: `build/extracted/MATH1090_HW9.txt`, Problem 2.
  - Covered by exact title `\begin{exerciseblock}[Homework 9 Problem 2]`.
  - Content: identifies `L=0` and proves
    `lim_{x -> 0} x/(1+x) = 0` by controlling the denominator with
    `delta <= 1/2`.

## Supporting Lecture Notes Coverage

- Sequence limit recap and the epsilon-N definition.
- Function limit definition on an open interval with the point removed.
- The reason for the condition `0 < |x-a|`.
- Worked examples for a linear function, a constant function, and a function
  with a removable hole.
- Negation of the epsilon-delta definition.
- Sum, product, and quotient limit laws, including proof strategy and the role
  of boundedness near the limiting point.
- Sequential Characterization as a method for proving existence or
  nonexistence of limits.
- Continuity as the condition `lim_{x -> a} f(x) = f(a)`.

## Source Ambiguity

- Lecture Notes Example 24 is internally inconsistent in the extracted text.
  The displayed computation uses
  `lim_{x -> 0} (x^2-4)/(x-1) = 4`, and the quotient-law calculation also
  depends on denominator `x-1`. A later extracted line appears to say
  `lim_{x -> 0} (x^2-4)/(x-2) = 4`; that statement would have value `2`, not
  `4`, if read literally. The chapter therefore treats Exercise 61 as the
  direct epsilon-delta proof of the limit with denominator `x-1`.
- Lecture Notes Exercise 59 says `f : R\{0} -> R` and then includes the phrase
  `for x > 0` after `f(x)=sin(1/x)`. The chapter uses positive sequences
  approaching `0`, so the nonexistence proof is valid even under the narrower
  right-side wording visible in the extraction.

## Authoring Decisions

- The corrupted Chapter 5 file was replaced from scratch with UTF-8 Chinese
  prose and English mathematical terms.
- Each required exercise has a discoverable `exerciseblock` title, followed by
  non-empty `solution` and `explanation` environments.
- Explanations emphasize epsilon-N, epsilon-delta, nonexistence, denominator
  control, and limit-law pitfalls.
- Homework 9 Problems 3 and 4 are intentionally excluded from this chapter
  because the requested coverage only names Problems 1 and 2.
