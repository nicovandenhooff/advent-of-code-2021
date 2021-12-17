# Advent of Code 2021
# Day 11: Part 1 and Part 2
# Author: Nico Van den Hooff

import numpy as np


def read_data(path):
    with open(path, "r") as f:
        data = f.read().splitlines()

    data = [[int(i) for i in numbers] for numbers in data]
    data = np.array(data, dtype=float)

    return data


def flash_cycle(array, flashed, mode, flashes=None):
    """Completes a single dumbo octopus flash cycle"""
    # energy level increases by 1
    array += 1

    # determine which octopus will flash
    flash = np.where((array > 9) & (array != np.inf), 1, 0)

    while np.sum(flash) > 0:
        # indicies of octopuses that will flash
        frow, fcol = np.where(flash == 1)

        for i, j in zip(frow, fcol):
            if mode == "steps":
                flashes += 1

            # update neighbours of octopus that flashes
            grid = array[i - 1 : i + 2, j - 1 : j + 2]
            grid = np.where(grid > 9, grid, grid + 1)
            array[i - 1 : i + 2, j - 1 : j + 2] = grid

            # mark flash as complete
            flash[i, j] = 0

            # update flash tracker array to prevent another flash from same octopus
            flashed[i, j] = 1

        # next round of octopus that will flash
        flash = np.where((array > 9) & (array != np.inf) & (flashed != 1), 1, 0)

    if mode == "steps":
        # part 1 tracks number of flashes
        return array, flashes
    elif mode == "simultaneously":
        # part 2 continues occuring til all octopus flash together
        return array


def part_1(data, steps=100, mode="steps"):
    flashes = 0
    array = np.pad(data, pad_width=1, constant_values=np.inf)

    for _ in range(steps):
        # reset array that tracks if an octopus flashed already this cycle
        flashed = np.zeros_like(array)

        # perform the flash cycle for this step and update number of flashes
        array, flashes = flash_cycle(array, flashed, mode, flashes)

        # resent octopus that flashed to zero energy
        array = np.where(array == 10, 0, array)

    return flashes


def part_2(data, mode="simultaneously"):
    steps = 0
    total_octopuses = data.size
    array = np.pad(data, pad_width=1, constant_values=np.inf)

    # we need to initialize flashed array here for part 2 so that
    # the while loop triggers
    flashed = np.zeros_like(array)

    while np.sum(flashed) != total_octopuses:
        # reset array that tracks if an octopus flashed already this cycle
        flashed = np.zeros_like(array)

        # perform the flash cycle for this step
        array = flash_cycle(array, flashed, mode)

        # resent octopus that flashed to zero energy
        array = np.where(array == 10, 0, array)
        steps += 1

    return steps


def main(path):
    data = read_data(path)
    solution1 = part_1(data)
    solution2 = part_2(data)

    print(f"Part 1 Solution: {solution1}")
    print(f"Part 2 Solution: {solution2}")


if __name__ == "__main__":
    path = "problems/day-11-dumbo-octopus/input.txt"
    main(path)
