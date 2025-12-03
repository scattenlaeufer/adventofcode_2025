#!/usr/bin/env python3
"""
Day 01 on the Advent of Code
"""

from pathlib import Path


def read_file(input_path: Path) -> list[str]:
    with input_path.open() as input_file:
        lines = [line.strip() for line in input_file]

    return lines


def directive(order: str, step: int, lock: int = 100) -> (int, int):
    direction = order[0]
    number = int(order[1:])

    counter_diff = 0

    print(f"old_{step=}")

    match direction:
        case "L":
            steps = -1 * number
        case "R":
            steps = number

    new_step = step + steps
    if steps < 0:
        new_step = step+steps
        if new_step < 0 and step != 0:
            counter_diff += 1
    counter_diff += int(abs(new_step) / lock)
    # print(counter, step, steps, new_step, (step + steps) % lock)

    print(f"{steps=}")

    step = (step + steps) % lock

    print(f"new_{step=}")

    return step, counter_diff


def day_01(input_path: Path) -> int:
    input_list = read_file(input_path)

    # lock = list(range(100))
    lock = 100

    step = 50
    counter = 0
    for order in input_list:
        print("================")
        print(f"old_{counter=}")
        print(f"{order=}")

        step, counter_diff = directive(order, step)
        print(f"{counter_diff=}")

        counter += counter_diff

        print(f"new_{counter=}")
    return counter


def main():
    print(f"The searched test number is {day_01(Path('test_input'))}")
    print(f"The searched number is {day_01(Path('input'))}")


if __name__ == "__main__":
    main()
