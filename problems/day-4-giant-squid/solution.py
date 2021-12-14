# Advent of Code 2021
# Day 4: Part 1 and Part 2
# Author: Nico Van den Hooff


import numpy as np


def read_data(path):

    with open(path, "r") as f:
        lines = []
        matrix = []
        bingo_boards = []

        # bingo numbers
        numbers = [int(num) for num in f.readline().split(",")]

        # read individual bingo board lines
        for line in f.readlines():
            lines.append(line.split("\n"))

        # remove trailing "" from lines
        lines = [array[:-1] if array[-1] == "" else array for array in lines]

        # split each board line into numbers
        for row in range(len(lines)):
            lines[row] = lines[row][0].split()

        # create each bingo board
        for row in lines:

            # adds boards to list of boards when seperator encountered
            if not row or row[0] == "":
                bingo_boards.append(np.array(matrix, dtype=int))
                matrix = []

            # otherwise continues creating current board
            else:
                matrix.append(row)

    # theres a space in the input file that needs to be removed here...
    bingo_boards.pop(0)

    return numbers, bingo_boards


def check_win(board, index):
    row_winner = np.all(board[index, :] == -1)
    column_winner = np.all(board[:, index] == -1)

    return row_winner or column_winner


def part_1(numbers, bingo_boards):
    win = False

    while not win:
        # draw number
        current_num = numbers.pop(0)

        for i in range(len(bingo_boards)):
            # mark current number in each board as -1
            bingo_boards[i] = np.where(
                bingo_boards[i] == current_num, -1, bingo_boards[i]
            )

            for j in range(len(bingo_boards[i])):
                # check for a winner
                if check_win(bingo_boards[i], j):
                    win = True
                    winner = bingo_boards[i]
                    break

            if win:
                break

    # score is sum of unmarked numbers
    score = np.sum(np.where(winner == -1, 0, winner))
    solution1 = current_num * score

    return solution1


def part_2(data):
    pass


def main(path):
    numbers, bingo_boards = read_data(path)
    solution1 = part_1(numbers, bingo_boards)
    # solution2 = part_2(data)

    print(f"Part 1 Solution: {solution1}")
    # print(f"Part 2 Solution: {solution2}")


if __name__ == "__main__":
    path = "problems/day-4-giant-squid/input.txt"
    main(path)
