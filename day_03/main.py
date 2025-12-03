#!/usr/bin/env python3
"""
Advent of Code day 03
"""

from pathlib import Path
from rich import print


def read_input_file(input_path: Path) -> list[str]:
    with input_path.open() as input_file:
        return [l.strip() for l in input_file]


def day_03(input_path: Path) -> int:
    input_list = read_input_file(input_path)
    jolt_sum = 0

    for line in input_list:
        jolt_max = 0
        for i in range(0, len(line) - 1):
            for j in range(i + 1, len(line)):
                jolt_max = max(jolt_max, int(line[i] + line[j]))
        jolt_sum += jolt_max

    return jolt_sum


def main():
    target = 357
    result = day_03(Path("test_input"))
    print(
        f"The sum of joltage from test input is {result}, target is {target}, diff is {result - target}"
    )
    print(f"The sum of joltage from real input is {day_03(Path('input'))}")


if __name__ == "__main__":
    main()
