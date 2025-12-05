#!/usr/bin/env python3
"""
Advent of Code 2025 day 04
"""

from pathlib import Path

from rich import print


def read_input_file(input_path: Path) -> list[str]:

    with input_path.open() as input_file:
        output_list = [l.strip() for l in input_file]

    return output_list


def day_04(input_path: Path) -> int:

    input_list = read_input_file(input_path)
    max_roles = 3
    accessible_roles = 0

    for i, row in enumerate(input_list):
        for j, space in enumerate(row):
            if space == "@":
                adjacent_spaces = []
                for adjacent_row in input_list[
                    max(0, i - 1) : min(len(input_list), i + 2)
                ]:
                    adjacent_spaces.append(
                        adjacent_row[max(0, j - 1) : min(len(adjacent_row), j + 2)]
                    )
                if sum(r.count("@") for r in adjacent_spaces) <= max_roles + 1:
                    accessible_roles += 1

    return accessible_roles


def main():
    target = 13
    result = day_04(Path("test_input"))
    print(
        f"The number of accessable roles in test input are {result}, target is {target}, diff {result-target}"
    )
    print(f"The number of accessable roles in real input are {day_04(Path('input'))}")


if __name__ == "__main__":
    main()
