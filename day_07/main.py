#!/usr/bin/env python3
"""
Advent of Code 2025
"""

from pathlib import Path
from rich import print


def read_input_file(input_path: Path) -> list[list[str]]:
    with input_path.open() as input_file:
        input_list = [list(l.strip()) for l in input_file]

    return input_list


def day_07(input_path: Path) -> int:
    input_list = read_input_file(input_path)

    num_splits = 0

    for i, line in enumerate(input_list[:-1]):
        for j, c in enumerate(line):
            if c in  ["S", "|"]:
                if input_list[i+1][j] == "^":
                    input_list[i+1][j-1] = "|"
                    input_list[i+1][j+1] = "|"
                    num_splits += 1
                else:
                    input_list[i+1][j] = "|"

    return num_splits


def main():
    target = 21
    result = day_07(Path("test_input"))
    print(
        f"The number of splits in test input is {result}, target is {target}, diff is {result - target}"
    )
    print(f"The number of splits in real input is {day_07(Path('input'))}")


if __name__ == "__main__":
    main()
