#!/usr/bin/env python3
"""
Advent of Code 2025
"""

from pathlib import Path
from rich import print


def read_input_file(input_path: Path) -> list[str]:
    with input_path.open() as input_file:
        input_list = [l.strip() for l in input_file]

    return input_list


def find_path(
    i: int, line: list[str], input_list: list[str], gone_paths: set[str]
) -> int:
    line_str = f"{i} {''.join(line)}"
    if i == len(input_list) - 1:
        # print(len(gone_paths), line_str)
        return 1

    if line_str in gone_paths:
        return 1

    # print(i, line)
    gone_paths.add(line_str)
    print(gone_paths, len(gone_paths))
    next_lines: list[list[str]] = []

    for j, c in enumerate(line):
        if c in ["|", "S"]:
            next_line = input_list[i + 1]
            if next_line[j] == "^":
                next_line_l = list(next_line)
                next_line_l[j - 1] = "|"
                next_line_r = list(next_line)
                next_line_r[j + 1] = "|"
                next_lines += [next_line_l, next_line_r]
            else:
                next_line_s = list(next_line)
                next_line_s[j] = "|"
                next_lines.append(next_line_s)

    # print(next_lines)
    return sum(find_path(i + 1, l, input_list, gone_paths) for l in next_lines)


def day_07(input_path: Path) -> int:
    input_list = read_input_file(input_path)

    return find_path(0, list(input_list[0]), input_list, set())


def main():
    target = 40
    result = day_07(Path("test_input"))
    print(
        f"The number of splits in test input is {result}, target is {target}, diff is {result - target}"
    )
    # result = day_07(Path("input"))
    # print(f"The number of splits in real input is {result}")
    # print(f"{result > 140=}")
    # print(f"{result > 1668=}")


if __name__ == "__main__":
    main()
