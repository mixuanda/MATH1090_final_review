# MATH1090 Final Exam Review Notes

This repository contains a LaTeX textbook-style final review note for CUHK MATH1090/1098 Introduction to Set Theory.

The review is written in Chinese prose with mathematical technical terms kept in English. The main source spine is `reference/MATH1090_Lecture_Notes_Apr18.pdf`; worksheets, homework, the midterm solution, `Elementary Set Theory`, and `Naive Set Theory` are used for exercises and background.

## Build

Use XeLaTeX:

```bash
latexmk -xelatex -interaction=nonstopmode -halt-on-error main.tex
```

The output is `main.pdf`.

## Repository Scope

The `reference/` directory and generated extraction files under `build/` are local source material and are intentionally ignored by Git. The Overleaf-facing tracked files are the authored LaTeX source, documentation, and final compiled PDF.
