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


def day_05_02(input_path: Path) -> int:
    input_list = read_input_file(input_path)

    fresh_ranges = []

    range_limit_list = [[int(i) for i in r.split("-")] for r in input_list[0]]
    range_limit_list.sort(key=lambda r: r[0])

    for range_limits in range_limit_list:
        done = False
        for id_range in fresh_ranges:
            if range_limits[1] <= id_range[1]:
                done = True
                break
            if (
                id_range[0] <= range_limits[0] <= id_range[1]
                and range_limits[1] > id_range[1]
            ):
                id_range[1] = range_limits[1]
                done = True
                break

        if not done:
            fresh_ranges.append(range_limits)
            fresh_ranges.sort(key=lambda r: r[0])

    return sum(r[1] - r[0] + 1 for r in fresh_ranges)


def main():
    target = 3
    result = day_05(Path("test_input"))
    print(
        f"the number of fresh ingredients in test input are {result}, target is {target}, diff {result - target}"
    )
    print(f"the number of fresh ingredients in real input are {day_05(Path('input'))}")
    target = 14
    result = day_05_02(Path("test_input"))
    print(
        f"the total number of fresh ingredients IDs in test input are {result}, target is {target}, diff {result - target}"
    )
    result = day_05_02(Path("input"))
    print(f"the total number of fresh ingredients IDs in real input are {result}")


if __name__ == "__main__":
    main()
