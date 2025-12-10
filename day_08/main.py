"""
Advent of Code 2025
"""

from math import sqrt, prod
from pathlib import Path
from rich import print


def read_input_file(input_path: Path) -> list[list[int]]:
    with input_path.open() as input_file:
        input_list = [list(int(i) for i in l.strip().split(",")) for l in input_file]

    return input_list


def day_08(input_path: Path, connections_max: int, prod_num: int) -> int:
    input_list = read_input_file(input_path)

    distance_list = []

    for i, point_a in enumerate(input_list[:-1]):
        for point_b in input_list[i+1:]:
            distance = sqrt(sum((a - b) ** 2 for a, b in zip(point_a, point_b)))
            distance_list.append((distance, point_a, point_b))

    distance_list.sort(key=lambda p: p[0])

    curcuits = [[[distance_list[0][1], distance_list[0][2]]]]
    connections = 0

    for i, (distance, point_a, point_b) in enumerate(distance_list[1:]):
        if connections >= connections_max:
            break
        connection_in_curcuit = False
        for curcuit in curcuits:
            points_in_curcuit = [p for c in curcuit for p in c]
            if (point_a in points_in_curcuit and not point_b in points_in_curcuit) or (
                not point_a in points_in_curcuit and point_b in points_in_curcuit
            ):
                curcuit.append([point_a, point_b])
                connections += 1
                connection_in_curcuit = True
                break
            if point_a in points_in_curcuit and point_b in points_in_curcuit:
                connection_in_curcuit = True
                break
        if not connection_in_curcuit:
            curcuits.append([[point_a, point_b]])
            connections += 1

    curcuits.sort(reverse=True, key=len)

    points_in_curcuits = []
    for curcuit in curcuits:
        points_in_curcuit = [curcuit[0][0]]
        for point in [p for c in curcuit for p in c][1:]:
            if point in points_in_curcuit:
                continue
            points_in_curcuit.append(point)
        points_in_curcuits.append(points_in_curcuit)

    points_in_curcuits.sort(reverse=True, key=len)

    return prod(len(c) for c in points_in_curcuits[:prod_num])


def main():
    connections = 10
    result = day_08(Path("test_input"), connections, 3)
    target = 40
    print(
        f"The product of curcuit lengths in test input is {result}, target is {target}, diff is {result - target}"
    )

    connections = 1000
    result = day_08(Path("input"), connections, 3)
    print(f"The product of curcuit lengths in real input is {result}")
    print(f"{result > 8280=}")


if __name__ == "__main__":
    main()
