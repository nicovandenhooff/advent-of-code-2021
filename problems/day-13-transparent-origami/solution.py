# Advent of Code 2021
# Day 13: Part 1 and Part 2
# Author: Nico Van den Hooff

import numpy as np


def read_data(path):
    with open(path, "r") as f:
        data = f.read().splitlines()

    split = data.index("")

    # creates a list of lists with (x, y) coordinates at each index
    coords, folds = data[:split], data[split + 1 :]
    coords = [[int(i) for i in coord.split(",")] for coord in coords]

    max_x, max_y = 0, 0

    for coord in coords:
        if coord[0] > max_x:
            max_x = coord[0]

        if coord[1] > max_y:
            max_y = coord[1]

    # create list of folds with (direction, line) at each index
    for i, fold in enumerate(folds):
        fold = fold.split("fold along ")[1]
        line = int(fold.split("=")[1])

        if fold.split("=")[0] == "x":
            direction = "horizontal"
        else:
            direction = "vertical"

        folds[i] = (direction, line)

    # creates "paper" which is an array of zeros
    paper = np.zeros((max_y + 1, max_x + 1))

    # marks paper with 1s to represent dots
    for coord in coords:
        x, y = coord[1], coord[0]
        paper[x, y] = 1

    return folds, paper


def fold_paper(paper, direction, line):
    """Folds a piece of transparent paper in a given direction"""

    if direction == "vertical":
        top = paper[:line]
        bottom = paper[line+1:]
        return top + np.flipud(bottom)

    if direction == "horizontal":
        left = paper[:, :line]
        right = paper[:, line+1:]
        return left + np.fliplr(right)


def get_visible_dots(paper):
    """Gets the number of visible dots on a transparent piece of paper"""
    visible_dots = np.where(paper != 0, 1, 0)
    return np.sum(visible_dots)


def get_letters(paper):
    """Gets the final letters after all folds are completed"""
    return "\n".join("".join(str(cell) for cell in row) for row in paper)


def part_1(folds, paper):
    # part 1 we only do the first fold
    direction = folds[0][0]
    line = folds[0][1]
    result = fold_paper(paper, direction, line)

    solution1 = get_visible_dots(result)

    return solution1


def part_2(folds, paper):
    result = paper.copy()

    # part 2 we do all the folds
    for fold in folds:
        result = fold_paper(result, fold[0], fold[1])

    solution2 = get_letters(np.where(result != 0, 1, "."))

    return solution2


def main(path):
    folds, paper = read_data(path)
    solution1 = part_1(folds, paper)
    solution2 = part_2(folds, paper)

    print(f"Part 1 Solution: {solution1}")
    print(f"Part 2 Solution:\n{solution2}")


if __name__ == "__main__":
    path = "problems/day-13-transparent-origami/input.txt"
    main(path)
