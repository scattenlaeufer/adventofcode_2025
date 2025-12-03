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
        for id_int in range(start, end + 1):
            found = False
            id_str = str(id_int)
            for i in range(1, len(id_str)):
                if found:
                    continue
                id_split = [id_str[j : j + i] for j in range(0, len(id_str), i)]
                if all(id_split[0] == s for s in id_split):
                    id_sum += id_int
                    found = True

    return id_sum


def main():
    target = 4174379265
    result = day_02(Path("test_input"))
    print(
        f"The sum of invalid IDs from test input is {result}, should be {target}, diff is {result - target}"
    )
    print(f"The sum of invalid IDs from real input is {day_02(Path('input'))}")


if __name__ == "__main__":
    main()
