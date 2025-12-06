#!/usr/bin/env python3
"""
Advent of Code 2025 day 06
"""

from pathlib import Path
from rich import print


def read_input_file(input_path: Path) -> list[list[str]]:
    with input_path.open() as input_file:
        input_list = [
            list(filter(None, (e.strip() for e in l.strip().split(" "))))
            for l in input_file
        ]

    return input_list


def day_06(input_path: Path) -> int:
    input_list = read_input_file(input_path)
    result_list: list[int] = [int(i) for i in input_list[0]]

    for line in input_list[1:-1]:
        for i, num in enumerate(line):
            match input_list[-1][i]:
                case "+":
                    result_list[i] += int(num)
                case "*":
                    result_list[i] *= int(num)

    return sum(result_list)


def main():
    target = 4277556
    result = day_06(Path("test_input"))
    print(
        f"The sum of all results from test input is {result}, target is {target}, diff {result - target}"
    )
    print(f"The sum of all results from real input is {day_06(Path('input'))}")


if __name__ == "__main__":
    main()
