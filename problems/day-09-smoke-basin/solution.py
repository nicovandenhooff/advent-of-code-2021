# Advent of Code 2021
# Day 9: Part 1 and Part 2
# Author: Nico Van den Hooff

import numpy as np


def read_data(path):
    with open(path, "r") as f:
        data = f.read().splitlines()

    array = np.array([[int(d) for d in digits] for digits in data])

    # pad edge of array with highest value
    # this makes solutions much easier
    array = np.pad(array, (1, 1), constant_values=9)

    return array


def get_path(i, j, array, visited, basin):
    """Recursively get a basin path"""

    # mark as visited and append to basin
    if visited[i][j] == 0:
        basin.append(array[i][j])
        visited[i][j] = 1

    # move up and visit if appropriate
    if visited[i - 1][j] != 1:
        visited[i - 1][j] == 1
        get_path(i - 1, j, array, visited, basin)

    # move down and visit if appropriate
    if visited[i + 1][j] != 1:
        visited[i + 1][j] == 1
        get_path(i + 1, j, array, visited, basin)

    # move right and visit if appropriate
    if visited[i][j + 1] != 1:
        visited[i][j + 1] == 1
        get_path(i, j + 1, array, visited, basin)

    # move left and visit if appropriate
    if visited[i][j - 1] != 1:
        visited[i][j - 1] == 1
        get_path(i, j - 1, array, visited, basin)


def part_1(array):

    nrows, ncols = array.shape

    # to track where the low points are
    low_points = np.zeros_like(array)

    for i in range(1, nrows - 1):
        for j in range(1, ncols - 1):
            # skip 9s for efficiency boost
            if array[i][j] == 9:
                continue
            # mark low points as applicable
            if (
                min(
                    array[i - 1][j],
                    array[i + 1][j],
                    array[i][j - 1],
                    array[i][j + 1],
                    array[i][j],
                )
                == array[i][j]
            ):
                low_points[i][j] = 1

    solution1 = np.sum(np.where(low_points == 1, low_points + array, 0))

    return low_points, solution1


def part_2(array, low_points):

    totals = []

    # indicies of our low points
    row_idx, col_idx = np.where(low_points == 1)

    # array to track where we have visited during a basin path search
    visited = np.where(array == 9, 1, 0)

    # get the total of each basin path and sum it
    for i, j in zip(row_idx, col_idx):
        basin = []
        get_path(i, j, array, visited, basin)
        totals.append(len(basin))

    totals.sort(reverse=True)
    solution2 = totals[0] * totals[1] * totals[2]

    return solution2


def main(path):
    array = read_data(path)
    low_points, solution1 = part_1(array)
    solution2 = part_2(array, low_points)

    print(f"Part 1 Solution: {solution1}")
    print(f"Part 2 Solution: {solution2}")


if __name__ == "__main__":
    path = "problems/day-9-smoke-basin/input.txt"
    main(path)
