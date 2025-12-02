#!/usr/bin/env python3
"""
Day 01 on the Advent of Code
"""

from pathlib import Path


def read_file(input_path: Path) -> list[str]:
    with input_path.open() as input_file:
        lines = [line.strip() for line in input_file]

    return lines


def main():
    input_list = read_file(Path("input"))

    lock = list(range(100))

    step = 50
    counter = 0
    for order in input_list:
        direction = order[0]
        number = int(order[1:])

        match direction:
            case "L":
                steps = -1 * number
            case "R":
                steps = number

        step = lock[(step + steps) % len(lock)]

        if step == 0:
            counter += 1

    print(f"The searched number is {counter}")


if __name__ == "__main__":
    main()
