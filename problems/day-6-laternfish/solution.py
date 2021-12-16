# Advent of Code 2021
# Day 6: Part 1 and Part 2
# Author: Nico Van den Hooff

import numpy as np
from collections import Counter


def read_data(path):
    with open(path, "r") as f:
        data = f.read()

    laternfish = np.array(data.split(","), dtype=int)

    return laternfish


def latern_fish_growth(laternfish, days, timer=8):
    """Models latern fish growth and returns number of fish after n days"""
    tracker = Counter()

    for i in range(timer + 1):
        tracker[i] = 0

    # starting values of each latern fish
    for i in laternfish:
        tracker[i] += 1

    for day in range(days):

        # new fish to be born
        new_fish = tracker[0]

        # shift fish one day up as day passes
        for i in range(timer + 1):
            tracker[i] = tracker[i + 1]

        # reset fish that spawned a new fish and add spawned fish
        tracker[timer - 2] += new_fish
        tracker[timer] += new_fish

    total_latern_fish = sum(tracker.values())

    return total_latern_fish


def part_1(laternfish, days=80):
    solution1 = latern_fish_growth(laternfish, days)

    return solution1


def part_2(laternfish, days=256):
    solution2 = latern_fish_growth(laternfish, days)

    return solution2


def main(path):
    data = read_data(path)
    solution1 = part_1(data)
    solution2 = part_2(data)

    print(f"Part 1 Solution: {solution1}")
    print(f"Part 2 Solution: {solution2}")


if __name__ == "__main__":
    path = "problems/day-6-laternfish/input.txt"
    main(path)
