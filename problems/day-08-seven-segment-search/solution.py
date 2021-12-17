# Advent of Code 2021
# Day 8: Part 1 and Part 2
# Author: Nico Van den Hooff


def read_data(path):
    inputs = []
    outputs = []

    with open(path, "r") as f:
        data = f.read().splitlines()

    # split inputs and outputs
    for i, string in enumerate(data):
        data[i] = string.split(" | ")

    # create lists of inputs and outputs
    for sequence in data:
        inputs.append(sequence[0].split())
        outputs.append(sequence[1].split())

    return inputs, outputs


def part_1(outputs):
    counts = 0
    uniques = {2, 3, 4, 7}

    for sequences in outputs:
        for sequence in sequences:
            if len(sequence) in uniques:
                counts += 1

    return counts


def part_2(inputs, outputs):
    pass


def main(path):
    inputs, outputs = read_data(path)
    solution1 = part_1(outputs)
    # solution2 = part_2(data)

    print(f"Part 1 Solution: {solution1}")
    # print(f"Part 2 Solution: {solution2}")


if __name__ == "__main__":
    path = "problems/day-8-seven-segment-search/input.txt"
    main(path)
