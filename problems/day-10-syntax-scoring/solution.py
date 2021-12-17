# Advent of Code 2021
# Day 10: Part 1 and Part 2
# Author: Nico Van den Hooff

from collections import Counter


def read_data(path):
    with open(path, "r") as f:
        data = f.read().splitlines()

    # convert data to set, makes deleting corrupted lines efficient in part 2
    data = set(data)

    return data


def get_brackets():
    """Gets problem information as it relates to the brackets used in syntax"""
    # starting brackets
    opening = {"(", "[", "{", "<"}

    # maps starting brackets to ending brackets
    legal_opening = {"(": ")", "[": "]", "{": "}", "<": ">"}

    # maps ending brackets to starting brackets
    legal_closing = {")": "(", "]": "[", "}": "{", ">": "<"}

    return opening, legal_opening, legal_closing


def get_points(problem):
    """Gets the point values for part 1 (corrupted) or part 2 (incomplete)"""
    if problem == "corrupted":
        return {")": 3, "]": 57, "}": 1197, ">": 25137}
    elif problem == "incomplete":
        return {")": 1, "]": 2, "}": 3, ">": 4}


def calc_corrupted_score(illegals, points):
    """Calculates the score for problematic brackets in corrupted chunks (part 1)"""
    score = 0

    for char, count in illegals.items():
        score += points[char] * count

    return score


def calc_incomplete_score(fixes, points):
    """Calculates the score for fixing incomplete chunks (part 2)"""
    scores = []

    for fix in fixes:
        score = 0

        for i in reversed(range(len(fix))):
            score *= 5
            current = fix[i]
            score += points[current]

        scores.append(score)

    scores.sort()
    score = scores[len(scores) // 2]

    return score


def solve(problem, chunks):
    """Solves the corrupted or incomplete chunk problem"""
    opening, legal_opening, legal_closing = get_brackets()

    # we need different data structures for part 1 and 2
    if problem == "corrupted":
        illegals = Counter()
        corrupted = set()
    elif problem == "incomplete":
        fixes = []

    for chunk in chunks:
        # stack tracks the opening brackets
        stack = []

        # push the first bracket onto the stack
        stack.append(chunk[0])

        for char in chunk[1:]:
            # push opening brackets onto stack
            if char in opening:
                stack.append(char)
            else:
                top = len(stack) - 1

                # pop opening bracket if legal closing bracket encounted
                if legal_closing[char] == stack[top]:
                    stack.pop()
                else:
                    if problem == "corrupted":
                        illegals[char] += 1
                        corrupted.add(chunk)
                        # end here since we stop at first illegal closing bracket
                        break

        if problem == "incomplete":
            # create a list of closing brackets to fix an incomplete chunk
            for i, char in enumerate(stack):
                stack[i] = legal_opening[char]

            fixes.append(stack)

    if problem == "corrupted":
        return illegals, corrupted
    elif problem == "incomplete":
        return fixes


def part_1(data, problem="corrupted"):
    points = get_points(problem)
    illegals, corrupted = solve(problem, data)
    solution1 = calc_corrupted_score(illegals, points)

    return corrupted, solution1


def part_2(data, corrupted, problem="incomplete"):
    # remove corrupted chunks
    incomplete = data - corrupted

    points = get_points(problem)
    fixes = solve(problem, incomplete)
    solution2 = calc_incomplete_score(fixes, points)

    return solution2


def main(path):
    data = read_data(path)
    corrupted, solution1 = part_1(data)
    solution2 = part_2(data, corrupted)

    print(f"Part 1 Solution: {solution1}")
    print(f"Part 2 Solution: {solution2}")


if __name__ == "__main__":
    path = "problems/day-10-syntax-scoring/input.txt"
    main(path)
