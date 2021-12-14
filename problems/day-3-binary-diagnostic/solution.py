# Advent of Code 2021
# Day 2: Part 1 and Part 2
# Author: Nico Van den Hooff


import numpy as np


def read_data(path):
    with open(path, "r") as f:
        data = f.read().splitlines()

    return data


def part_1(data):

    # split the binary digits into a 2D matrix
    digits = np.array([[int(d) for d in binary] for binary in data])

    # gamma value is where there are more 1s in each matrix column
    gamma = np.array(digits.sum(axis=0) > (len(data) / 2), dtype=int)

    epsilon = np.array(digits.sum(axis=0) <= (len(data) / 2), dtype=int)

    gamma = "".join(gamma.astype(str).tolist())
    epsilon = "".join(epsilon.astype(str).tolist())

    return int(gamma, 2) * int(epsilon, 2)


# def part_2():


def main(path):
    data = read_data(path)
    solution1 = part_1(data)
    # solution2 = part_2()

    print(f"Part 1 Solution: {solution1}")
    # print(f"Part 2 Solution: {solution2}")


if __name__ == "__main__":
    path = "problems/day-3-binary-diagnostic/input.txt"
    main(path)
