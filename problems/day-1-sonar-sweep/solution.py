# Advent of Code 2021
# Day 1: Part 1 and Part 2
# Author: Nico Van den Hooff


import numpy as np
from numpy.lib.stride_tricks import sliding_window_view


def read_data(path):
    with open(path, "r") as f:
        data = f.read().split("\n")

    return data


def part_1(data):
    day = np.array([int(num) for num in data])
    next_day = np.append(day[0], day[0:-1])

    return np.sum(day - next_day > 0)


def part_2(data):
    windows = sliding_window_view(np.array([int(num) for num in data]), 3)
    windows_sum = windows.sum(axis=1)
    windows_sum_next = np.append(windows_sum[0], windows_sum[0:-1])

    return np.sum(windows_sum - windows_sum_next > 0)


def main(path):
    data = read_data(path)
    solution1 = part_1(data)
    solution2 = part_2(data)

    print(f"Part 1 Solution: {solution1}")
    print(f"Part 2 Solution: {solution2}")


if __name__ == "__main__":
    path = "problems/day-1-sonar-sweep/input.txt"
    main(path)
