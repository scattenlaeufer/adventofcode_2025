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

    print(input_list)

    return 0


def main():
    target = 13
    result = day_04(Path("test_input"))
    print(
        f"The number of accessable roles in test input are {result}, target is {target}, diff {result-target}"
    )
    # print(f"The number of accessable roles in real input are {day_04(Path('input'))}")


if __name__ == "__main__":
    main()
