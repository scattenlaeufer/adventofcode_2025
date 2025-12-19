#!/usr/bin/env python3
"""
Advent of Code 2025 day 09
"""


from pathlib import Path
from rich import print


def read_input_file(input_path: Path) -> list[tuple[int, ...]]:
    with input_path.open() as input_file:
        input_list = [l.strip() for l in input_file]

    return [tuple(int(c) for c in p.split(",")) for p in input_list]


def day_09(input_path: Path) -> int:
    input_list = read_input_file(input_path)

    return 0


def main():
    result = day_09(Path("test_input"))
    target = 50
    print(
        f"The largest area in test input is {result}, target is {target}, diff is {result-target}"
    )
    print(f"The largest area in test input is {day_09(Path('input'))}")


if __name__ == "__main__":
    main()
