"""
Advent of Code 2025
"""

from pathlib import Path
from rich import print


def read_input_file(input_path: Path) -> list[list[int]]:
    with input_path.open() as input_file:
        input_list = [list(int(i) for i in l.strip().split(",")) for l in input_file]

    return input_list


def day_08(input_path: Path, connections: int) -> int:
    input_list = read_input_file(input_path)

    print(input_list)

    return 0


def main():
    connections = 10
    result = day_08(Path("test_input"), connections)
    target = 40
    print(f"The product of curcuit lengths in test input is {result}, target is {target}, diff is {result - target}")

    connections = 1000
    result = day_08(Path("input"), connections)
    print(f"The product of curcuit lengths in real input is {result}")


if __name__ == "__main__":
    main()
