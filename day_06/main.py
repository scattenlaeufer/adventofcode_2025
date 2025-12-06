#!/usr/bin/env python3
"""
Advent of Code 2025 day 06
"""

import math
from pathlib import Path
from rich import print


def read_input_file(input_path: Path) -> list[str]:
    with input_path.open() as input_file:
        input_list = [l.strip("\n") for l in input_file]

    return input_list


def day_06(input_path: Path) -> int:
    input_list = read_input_file(input_path)

    operator_list = list(filter(None, (o.strip() for o in input_list[-1].split(" "))))

    separator_positions: list[int | None] = list(range(len(input_list[0])))
    for line in input_list:
        for i, c in enumerate(line):
            if not c == " ":
                separator_positions[i] = None
    separator_positions = list(filter(None, separator_positions))

    number_list: list[list[int | str]] = [[]] * len(operator_list)

    for line in input_list[0:-1]:
        for i, (l, h) in enumerate(
            zip([0] + separator_positions, separator_positions + [-1])
        ):
            if h == -1:
                num_str = line[l + 1 :]
            elif l == 0:
                num_str = line[l:h]
            else:
                num_str = line[l + 1 : h]

            if not number_list[i]:
                number_list[i] = [""] * len(num_str)

            for n, c in enumerate(num_str):
                number_list[i][n] += c

    number_list = [[int(n.strip()) for n in l if isinstance(n, str)] for l in number_list]

    result_list: list[int] = []

    for operator, numbers in zip(operator_list, number_list):
        match operator:
            case "+":
                result_list.append(sum(numbers))
            case "*":
                result_list.append(math.prod(numbers))

    return sum(result_list)


def main():
    target = 3263827
    result = day_06(Path("test_input"))
    print(
        f"The sum of all results from test input is {result}, target is {target}, diff {result - target}"
    )
    print(f"The sum of all results from real input is {day_06(Path('input'))}")


if __name__ == "__main__":
    main()
