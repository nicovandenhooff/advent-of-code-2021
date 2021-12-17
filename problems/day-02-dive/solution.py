# Advent of Code 2021
# Day 2: Part 1 and Part 2
# Author: Nico Van den Hooff


import numpy as np


def read_data(path):
    with open(path, "r") as f:
        data = f.read().splitlines()

    return data


def part_1(data):

    # array of movement values (integers)
    movement = np.array([int(d[-1]) for d in data])

    # list of movement directions (strings)
    directions = [d[:-2] for d in data]

    # array of depth movements, 0 if not a depth movement
    depths = np.array(
        [-1 if y == "up" else "1" if y == "down" else 0 for y in directions], dtype=int
    )

    # array of horizontal movements, 0 if not a horzontal movement
    horizontals = np.array([1 if x == "forward" else 0 for x in directions], dtype=int)

    final_depth = np.sum(movement * depths)
    final_horizontal = np.sum(movement * horizontals)

    solution1 = final_horizontal * final_depth

    return movement, depths, horizontals, final_horizontal, solution1


def part_2(movement, depths, horizontals, final_horizontal):

    # aim is simply a cumsum of old depth values * movement values
    # remember old depth values are 0 if it is a horizontal movement
    aim = np.cumsum(depths * movement)

    # actual and final depth movements based on new information
    actual_depths = horizontals * aim
    final_depth = np.sum(movement * actual_depths)

    solution2 = final_horizontal * final_depth

    return solution2


def main(path):
    data = read_data(path)
    movement, depths, horizontals, final_horizontal, solution1 = part_1(data)
    solution2 = part_2(movement, depths, horizontals, final_horizontal)

    print(f"Part 1 Solution: {solution1}")
    print(f"Part 2 Solution: {solution2}")


if __name__ == "__main__":
    path = "problems/day-2-dive/input.txt"
    main(path)
