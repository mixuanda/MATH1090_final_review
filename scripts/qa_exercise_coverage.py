#!/usr/bin/env python3
"""Repository QA for MATH1090 final-review exercise coverage.

The test is intentionally text-based. It does not prove mathematical
correctness, but it enforces that every required exercise has a named entry,
a solution block, and a separate explanation block.
"""

from __future__ import annotations

import re
import sys
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TEX_FILES = [
    ROOT / "main.tex",
    ROOT / "tex" / "chapter01_logic.tex",
    ROOT / "tex" / "chapter02_sets_functions_relations.tex",
    ROOT / "tex" / "chapter03_integers_rationals.tex",
    ROOT / "tex" / "chapter04_reals_dedekind.tex",
    ROOT / "tex" / "chapter05_limits_continuity.tex",
    ROOT / "tex" / "chapter06_big_sets.tex",
    ROOT / "tex" / "chapter07_structure.tex",
    ROOT / "tex" / "midterm_review.tex",
]

BANNED_PHRASES = [
    "易得",
    "显然",
    "顯然",
    "不难看出",
    "不難看出",
    "容易看出",
    "很容易得到",
    "obvious",
    "obviously",
    "clearly",
    "trivial",
    "trivially",
    "straightforward",
    "it is easy to see",
]

# Characters repeatedly produced by the earlier mojibake regression. Proper
# Chinese mathematical prose should not contain these rare garbage tokens.
SUSPECT_MOJIBAKE_CHARS = set(
    "韸鍮镴䑆鯴阇鿙崹鮲帉俕霬䫟幀鯵鉀鶵崀韺麯䳿䇮鮤幯䜟鈖嵍鯍霉䔀"
)


@dataclass(frozen=True)
class ExpectedItem:
    item_id: str
    aliases: tuple[str, ...]


def lecture_items() -> list[ExpectedItem]:
    return [
        ExpectedItem(
            item_id=f"ln-exercise-{number:02d}",
            aliases=(
                f"Lecture Notes Exercise {number}",
                f"Lecture Note Exercise {number}",
                f"LN Exercise {number}",
            ),
        )
        for number in range(1, 73)
    ]


def worksheet_items() -> list[ExpectedItem]:
    counts = {
        "1": 9,
        "3": 5,
        "4": 3,
        "5": 4,
        "6": 4,
        "7": 5,
        "8": 4,
        "10": 5,
    }
    items: list[ExpectedItem] = []
    for worksheet, count in counts.items():
        for number in range(1, count + 1):
            items.append(
                ExpectedItem(
                    item_id=f"worksheet-{worksheet}-exercise-{number}",
                    aliases=(
                        f"Worksheet {worksheet} Exercise {number}",
                        f"Worksheet {worksheet}, Exercise {number}",
                    ),
                )
            )
    return items


def homework_items() -> list[ExpectedItem]:
    counts = {
        "1": 6,
        "2": 4,
        "3": 4,
        "4": 5,
        "5": 4,
        "6": 5,
        "7": 4,
        "8": 4,
        "9": 4,
    }
    items: list[ExpectedItem] = []
    for homework, count in counts.items():
        for number in range(1, count + 1):
            items.append(
                ExpectedItem(
                    item_id=f"homework-{homework}-problem-{number}",
                    aliases=(
                        f"Homework {homework} Problem {number}",
                        f"Homework {homework} Question {number}",
                        f"Homework {homework} Q{number}",
                        f"HW{homework} Problem {number}",
                        f"HW{homework} Question {number}",
                        f"HW{homework} Q{number}",
                    ),
                )
            )
    return items


def midterm_items() -> list[ExpectedItem]:
    return [
        ExpectedItem(
            item_id=f"midterm-problem-{number}",
            aliases=(
                f"Midterm Problem {number}",
                f"Midterm Review Problem {number}",
            ),
        )
        for number in range(1, 8)
    ]


EXPECTED_ITEMS = (
    lecture_items()
    + worksheet_items()
    + homework_items()
    + midterm_items()
)


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def line_number(text: str, index: int) -> int:
    return text.count("\n", 0, index) + 1


EXERCISE_BLOCK_RE = re.compile(
    r"\\begin\{exerciseblock\}(?:\[(?P<title>[^\]]*)\])?",
    flags=re.DOTALL,
)


def find_alias_matches(text: str, item: ExpectedItem) -> list[re.Match[str]]:
    matches: list[re.Match[str]] = []
    for match in EXERCISE_BLOCK_RE.finditer(text):
        title = match.group("title") or ""
        for alias in item.aliases:
            pattern = r"(?<![A-Za-z0-9])" + re.escape(alias) + r"(?![A-Za-z0-9])"
            if re.search(pattern, title, flags=re.IGNORECASE):
                matches.append(match)
                break
    return matches


UNIT_BOUNDARY_RE = re.compile(
    r"\\begin\{exerciseblock\}\[|\\chapter\{|\\section\{|\\subsection\{"
)


def item_unit(text: str, start: int) -> str:
    boundaries = [
        match.start()
        for match in UNIT_BOUNDARY_RE.finditer(text, pos=start + 1)
    ]
    end = min(boundaries) if boundaries else len(text)
    return text[start:end]


def environment_content(unit: str, environment: str) -> str | None:
    match = re.search(
        rf"\\begin\{{{re.escape(environment)}\}}(.*?)\\end\{{{re.escape(environment)}\}}",
        unit,
        flags=re.DOTALL,
    )
    if not match:
        return None
    content = re.sub(r"%.*", "", match.group(1))
    content = re.sub(r"\\[A-Za-z]+\*?(?:\[[^\]]*\])?(?:\{[^{}]*\})?", "", content)
    content = re.sub(r"\s+", " ", content).strip()
    return content


def nonempty_environment(unit: str, environment: str, min_length: int) -> bool:
    content = environment_content(unit, environment)
    return content is not None and len(content) >= min_length


def check_items(text: str) -> list[str]:
    failures: list[str] = []
    for item in EXPECTED_ITEMS:
        matches = find_alias_matches(text, item)
        if not matches:
            failures.append(f"missing item: {item.item_id}")
            continue
        if len(matches) > 1:
            lines = ", ".join(str(line_number(text, match.start())) for match in matches)
            failures.append(f"duplicate item: {item.item_id} at lines {lines}")
        match = matches[0]
        unit = item_unit(text, match.start())
        if not nonempty_environment(unit, "solution", min_length=80):
            failures.append(f"missing or too short solution: {item.item_id}")
        if not nonempty_environment(unit, "explanation", min_length=120):
            failures.append(f"missing or too short explanation: {item.item_id}")
    return failures


def check_explanation_repetition(text: str) -> list[str]:
    failures: list[str] = []
    explanations: dict[str, list[str]] = {}
    for match in EXERCISE_BLOCK_RE.finditer(text):
        title = match.group("title") or "(untitled)"
        unit = item_unit(text, match.start())
        content = environment_content(unit, "explanation")
        if content is None:
            continue
        normalized = re.sub(r"\s+", " ", content).strip()
        explanations.setdefault(normalized, []).append(title)

    for titles in explanations.values():
        if len(titles) >= 3:
            shown = ", ".join(titles[:5])
            if len(titles) > 5:
                shown += f", ... {len(titles) - 5} more"
            failures.append(
                "repeated explanation block used for multiple items: " + shown
            )
    return failures


def check_style(files: list[tuple[Path, str]]) -> list[str]:
    failures: list[str] = []
    for path, text in files:
        rel = path.relative_to(ROOT)
        lower_text = text.lower()
        for phrase in BANNED_PHRASES:
            idx = lower_text.find(phrase.lower())
            if idx != -1:
                failures.append(
                    f"banned phrase `{phrase}` in {rel}:{line_number(text, idx)}"
                )
        for idx, char in enumerate(text):
            if char in SUSPECT_MOJIBAKE_CHARS:
                failures.append(
                    f"suspect mojibake `{char}` in {rel}:{line_number(text, idx)}"
                )
                break
    return failures


def check_font_shell(files_by_name: dict[str, str]) -> list[str]:
    failures: list[str] = []
    main = files_by_name.get("main.tex", "")
    preamble = files_by_name.get("tex/preamble.tex", "")
    if "fontset=none" not in main:
        failures.append("main.tex must use ctex fontset=none")
    for command in ("setCJKmainfont", "setCJKsansfont", "setCJKmonofont"):
        if command not in preamble:
            failures.append(f"tex/preamble.tex must define \\{command}")
    return failures


def main() -> int:
    tex_files = [(path, read_text(path)) for path in TEX_FILES if path.exists()]
    preamble = ROOT / "tex" / "preamble.tex"
    files_for_style = tex_files + [(preamble, read_text(preamble))]
    combined = "\n".join(text for _, text in tex_files)
    files_by_name = {
        str(path.relative_to(ROOT)): text for path, text in files_for_style
    }

    failures = []
    failures.extend(check_items(combined))
    failures.extend(check_explanation_repetition(combined))
    failures.extend(check_style(files_for_style))
    failures.extend(check_font_shell(files_by_name))

    print(f"expected exercise items: {len(EXPECTED_ITEMS)}")
    print(f"checked tex files: {len(tex_files)}")
    if failures:
        print(f"QA FAILED: {len(failures)} issue(s)")
        for failure in failures[:250]:
            print(f"- {failure}")
        if len(failures) > 250:
            print(f"- ... {len(failures) - 250} more issue(s)")
        return 1

    print("QA PASSED: every expected exercise item has solution and explanation blocks")
    return 0


if __name__ == "__main__":
    sys.exit(main())
