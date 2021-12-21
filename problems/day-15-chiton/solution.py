# Advent of Code 2021
# Day 15: Part 1 and Part 2
# Author: Nico Van den Hooff

import numpy as np


def read_data(path):
    with open(path, "r") as f:
        data = f.read().splitlines()

    data = [[i for i in number.split()] for number in data]
    data = [[int(i) for i in line[0]] for line in data]

    array = np.array(data, dtype=float)

    return array


def minimum_path_sum(array):
    """DP algo to calc min path sum from top left to bottom right

    Note: In part 2 you can move in any direction so this will not work...

    """
    rows, cols = array.shape
    padded = np.pad(array, 1, constant_values=np.inf)
    cheapest_path = padded.copy()

    for i in reversed(range(1, rows + 1)):
        for j in reversed(range(1, cols + 1)):
            if cheapest_path[i + 1, j] == np.inf and cheapest_path[i, j + 1] == np.inf:
                continue
            else:
                cheapest_path[i, j] += min(
                    cheapest_path[i + 1, j], cheapest_path[i, j + 1]
                )

    return cheapest_path[1, 1] - padded[1, 1]


def get_next_portion(array):
    """Helper function to build each portion of the full cave"""
    return np.where(array + 1 > 9, 1, array + 1)


def get_full_cave(array):
    """Expands the input to create the full cave"""
    portions = dict.fromkeys([1, 2, 3, 4, 5, 6, 7, 8, 9])
    portions[1] = array

    for key in range(2, 10):
        portions[key] = get_next_portion(portions[key - 1])

    full_cave = np.vstack(
        [
            np.hstack(
                [portions[1], portions[2], portions[3], portions[4], portions[5]]
            ),
            np.hstack(
                [portions[2], portions[3], portions[4], portions[5], portions[6]]
            ),
            np.hstack(
                [portions[3], portions[4], portions[5], portions[6], portions[7]]
            ),
            np.hstack(
                [portions[4], portions[5], portions[6], portions[7], portions[8]]
            ),
            np.hstack(
                [portions[5], portions[6], portions[7], portions[8], portions[9]]
            ),
        ],
    )

    return full_cave


def part_1(array):
    solution1 = minimum_path_sum(array)

    return solution1


def part_2(array):
    pass


def main(path):
    array = read_data(path)
    solution1 = part_1(array)

    # TODO: fix part 2 to be a search problem rather than a DP problem
    # solution2 = part_2(array)

    print(f"Part 1 Solution: {solution1}")
    # print(f"Part 2 Solution: {solution2}")


if __name__ == "__main__":
    path = "problems/day-15-chiton/input.txt"
    main(path)
