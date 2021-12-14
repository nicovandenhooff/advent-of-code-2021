# Advent of Code 2021
# Day 3: Part 1 and Part 2
# Author: Nico Van den Hooff


import numpy as np


def read_data(path):
    with open(path, "r") as f:
        data = f.read().splitlines()

    return data


def part_1(data):

    # split the binary digits into a 2D matrix
    digits = np.array([[int(d) for d in binary] for binary in data])

    # get gamma and epsilon based on digit counts in each row
    gamma = np.array(digits.sum(axis=0) > (len(data) / 2), dtype=int)
    epsilon = np.array(digits.sum(axis=0) <= (len(data) / 2), dtype=int)

    # join digits together
    gamma = "".join(gamma.astype(str).tolist())
    epsilon = "".join(epsilon.astype(str).tolist())

    # convert to decimal from binary and solve
    solution1 = int(gamma, 2) * int(epsilon, 2)

    return solution1


def get_rating(data, type):

    # vector of binary numbers
    binaries = np.array([int(d) for d in data]).reshape(-1, 1)

    # maxtrix of individual binary digits
    digits = np.array([[int(d) for d in binary] for binary in data])

    count = 0

    # continuing pruning digits until we are left with one
    while digits.shape[0] != 1:

        # current column to count 0s and 1s for
        column = digits[:, count].reshape(-1, 1)

        # based on the rating filter binary numbers that we want
        if type == "oxygen":
            if (np.sum(column == 1)) >= np.sum((column == 0)):
                digits = np.where(column == 1, digits, 0)
            else:
                digits = np.where(column == 0, digits, 0)

        # co2 rating swaps the two where clauses, the rest is the same
        else:
            if (np.sum(column == 1)) >= np.sum((column == 0)):
                digits = np.where(column == 0, digits, 0)
            else:
                digits = np.where(column == 1, digits, 0)

        # remove zero values
        digits = digits[~np.all(digits == 0, axis=1)]

        count += 1

    # get binary rating and convert to decimal
    rating = int("".join(digits.flatten().astype(str).tolist()), 2)

    return rating


def part_2(data):

    oxygen = get_rating(data, "oxygen")
    co2 = get_rating(data, "co2")
    solution2 = oxygen * co2

    return solution2


def main(path):
    data = read_data(path)
    solution1 = part_1(data)
    solution2 = part_2(data)

    print(f"Part 1 Solution: {solution1}")
    print(f"Part 2 Solution: {solution2}")


if __name__ == "__main__":
    path = "problems/day-3-binary-diagnostic/input.txt"
    main(path)
