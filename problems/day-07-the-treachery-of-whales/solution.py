# Advent of Code 2021
# Day 7: Part 1 and Part 2
# Author: Nico Van den Hooff


def read_data(path):
    with open(path, "r") as f:
        data = f.read()

    data = data.split(",")
    data = [int(i) for i in data]

    return data


def get_fuel_cost(data, method):
    """Calculates minimum fuel cost of all horizontal movements for crabs"""
    # key: starting position, value: # of crabs in each
    start = dict()

    # key: ending position, value: total cost to move there
    end = dict()

    min_start = min(data)
    max_start = max(data)

    # sets up position dictionaries
    for i in range(min_start, max_start + 1):
        start[i] = 0
        end[i] = 0

    # initializes start positions with # of crabs in each
    for i in data:
        start[i] += 1

    # calculates the cost of moving to each horizontal position
    for end_position in end.keys():
        for start_position, total_crabs in start.items():
            if method == "horizontal":
                # part 1 is a constant cost for steps
                step_cost = abs(start_position - end_position)
                end[end_position] += step_cost * total_crabs
            if method == "cumulative":
                # part 2 is a cumulative cost for steps
                steps = abs(start_position - end_position)
                step_cost = (steps * (steps + 1)) // 2
                end[end_position] += step_cost * total_crabs

    minimum_fuel_cost = min(end.values())

    return minimum_fuel_cost


def part_1(start, method="horizontal"):
    solution1 = get_fuel_cost(start, method)
    return solution1


def part_2(start, method="cumulative"):
    solution2 = get_fuel_cost(start, method)
    return solution2


def main(path):
    data = read_data(path)
    solution1 = part_1(data)
    solution2 = part_2(data)

    print(f"Part 1 Solution: {solution1}")
    print(f"Part 2 Solution: {solution2}")


if __name__ == "__main__":
    path = "problems/day-7-the-treachery-of-whales/input.txt"
    main(path)
