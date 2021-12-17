# Advent of Code 2021
# Day 5: Part 1 and Part 2
# Author: Nico Van den Hooff

import numpy as np
from collections import Counter


def read_data(path):
    with open(path, "r") as f:
        data = f.read().splitlines()

    for i, coords in enumerate(data):
        coords = coords.replace(",", " ").replace(" -> ", " ").split(" ")
        data[i] = [int(num) for num in coords]

    return data


def get_slope(coords):
    """Calculates the slope of a line from two coordinates"""
    x1, y1, x2, y2 = coords[0], coords[1], coords[2], coords[3]

    if x1 == x2:
        # vertical line
        return np.nan
    if y1 == y2:
        # horizontal line
        return 0
    else:
        # diagonal line
        return (y2 - y1) / (x2 - x1)


def get_intercept(coords, m):
    """Calculates the intercept of a line from coordinates and slope"""
    x, y = coords[0], coords[1]
    b = y - m * x
    return b


def get_points(coords, m, b=None, diagonal=False):
    """Returns all discrete points on a line"""
    points = []
    x1, y1, x2, y2 = coords[0], coords[1], coords[2], coords[3]

    # vertical line
    if m is np.nan:
        # bottom to top
        y = min(y1, y2)
        while y <= max(y1, y2):
            points.append((x1, y))
            y += 1

    # horizontal line
    elif m == 0:
        # left to right
        x = min(x1, x2)
        while x <= max(x1, x2):
            points.append((x, y1))
            x += 1

    else:
        # diagonal line
        if diagonal:
            x = x1
            y = y1

            if x1 < x2:
                # left to right
                while x <= x2:
                    points.append((x, y))
                    x += 1
                    y = m * x + b
            else:
                # right to left
                while x >= x2:
                    points.append((x, y))
                    x -= 1
                    y = m * x + b
        else:
            return None

    return points


def add_points(points, tracker):
    """Adds a tuple(s) of points to a Counter"""
    if points is None:
        return

    for point in points:
        tracker[point] += 1


def count_overlap(tracker):
    """Counts the total points with multiple overlaps"""
    total = 0

    for _, value in tracker.items():
        if value > 1:
            total += 1

    return total


def part_1(data):
    tracker = Counter()

    for coords in data:
        m = get_slope(coords)
        points = get_points(coords, m)
        add_points(points, tracker)

    solution1 = count_overlap(tracker)

    return solution1


def part_2(data):
    tracker = Counter()

    for coords in data:
        m = get_slope(coords)
        b = get_intercept(coords, m)
        points = get_points(coords, m, b, diagonal=True)
        add_points(points, tracker)

    solution2 = count_overlap(tracker)

    return solution2


def main(path):
    data = read_data(path)
    solution1 = part_1(data)
    solution2 = part_2(data)

    print(f"Part 1 Solution: {solution1}")
    print(f"Part 2 Solution: {solution2}")


if __name__ == "__main__":
    path = "problems/day-5-hydrothermal-venture/input.txt"
    main(path)
