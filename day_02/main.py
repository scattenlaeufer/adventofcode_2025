#!/usr/bin/env python3
"""
Advent of Code 2025 Day 02
"""


from pathlib import Path

from rich import print


def read_input_file(input_path: Path) -> list[list[int]]:
    with input_path.open() as input_file:
        input_str = input_file.read().strip()

    return [[int(i) for i in r.split("-")] for r in input_str.split(",")]

def day_02(input_path: Path) -> int:
    input_list = read_input_file(input_path)

    id_sum = 0

    for start, end in input_list:
        for i in range(start, end+1):
            i_str = str(i)
            if len(i_str) % 2 == 0:
                if i_str[:int(len(i_str)/2)] == i_str[int(len(i_str)/2):]:
                    id_sum += i

    return id_sum


def main():
    print(f"The sum of invalid IDs from test input is {day_02(Path('test_input'))}")
    print(f"The sum of invalid IDs from real input is {day_02(Path('input'))}")


if __name__ == "__main__":
    main()
