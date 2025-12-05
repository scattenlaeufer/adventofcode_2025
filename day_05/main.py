#!/usr/bin/env python3
"""
Advent of Code 2025 day 05
"""

from pathlib import Path
from rich import print


def read_input_file(input_path: Path) -> list[list[str]]:

    with input_path.open() as input_file:
        input_list = [l.strip() for l in input_file]

    processed_list = []
    current_part = []

    for line in input_list:
        if not line:
            processed_list.append(current_part)
            current_part = []
            continue
        current_part.append(line)
    processed_list.append(current_part)
    return processed_list


def day_05(input_path: Path) -> int:
    input_list = read_input_file(input_path)
    ids_fresh = 0

    id_range_list = []
    for range_str in input_list[0]:
        range_limits = range_str.split("-")
        id_range_list.append(range(int(range_limits[0]), int(range_limits[1]) + 1))

    for id_str in input_list[1]:
        for id_range in id_range_list:
            if int(id_str) in id_range:
                ids_fresh += 1
                break

    return ids_fresh


def main():
    target = 3
    result = day_05(Path("test_input"))
    print(
        f"the number of fresh ingredients IDs in test input are {result}, target is {target}, diff {result - target}"
    )
    print(
        f"the number of fresh ingredients IDs in test input are {day_05(Path('input'))}"
    )


if __name__ == "__main__":
    main()
