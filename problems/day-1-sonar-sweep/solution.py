# Advent of Code 2021
# Day 1: Part 1 and Part 2
# Author: Nico Van den Hooff


import numpy as np
from numpy.lib.stride_tricks import sliding_window_view


def read_data(path):
    with open(path, "r") as f:
        data = f.read().splitlines()

    return data


def part_1(data):

    # convert data to numpy array
    day = np.array([int(num) for num in data])

    # next day values to compare
    next_day = np.append(day[0], day[0:-1])

    # sum boolean trues where there was an increase
    solution1 = np.sum(day - next_day > 0)

    return solution1


def part_2(data):

    # create 3 day sliding windows, values only
    windows = sliding_window_view(np.array([int(num) for num in data]), 3)

    # sum to create aggregate window values
    windows_sum = windows.sum(axis=1)

    # next day values to compare
    windows_sum_next = np.append(windows_sum[0], windows_sum[0:-1])

    # sum boolean trues where there was an increase
    solution2 = np.sum(windows_sum - windows_sum_next > 0)

    return solution2


def main(path):
    data = read_data(path)
    solution1 = part_1(data)
    solution2 = part_2(data)

    print(f"Part 1 Solution: {solution1}")
    print(f"Part 2 Solution: {solution2}")


if __name__ == "__main__":
    path = "problems/day-1-sonar-sweep/input.txt"
    main(path)
