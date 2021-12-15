# Advent of Code 2021
# Day 6: Part 1 and Part 2
# Author: Nico Van den Hooff

import numpy as np


def read_data(path):
    with open(path, "r") as f:
        data = f.read()

    laternfish = np.array(data.split(","), dtype=int)

    return laternfish


def part_1(laternfish, days=80):

    total_new_fish = 0

    while days > 0:
        # add new fish from previous day
        new_fish = np.full(total_new_fish, 8)

        # reset fish that just spawned a new fish
        laternfish = np.where(laternfish == 0, 7, laternfish)

        # day goes by
        days -= 1
        laternfish -= 1

        # add new fish
        laternfish = np.append(laternfish, new_fish)

        # calcualte new fish for next day
        total_new_fish = laternfish.shape[0] - np.count_nonzero(laternfish)

    solution1 = len(laternfish)

    return solution1


def part_2(data):
    pass


def main(path):
    data = read_data(path)
    solution1 = part_1(data)
    # solution2 = part_2(data)

    print(f"Part 1 Solution: {solution1}")
    # print(f"Part 2 Solution: {solution2}")


if __name__ == "__main__":
    path = "problems/day-6-laternfish/input.txt"
    main(path)
