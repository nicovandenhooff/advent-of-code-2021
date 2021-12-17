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

        # append the last board
        bingo_boards.append(np.array(matrix, dtype=int))

    # theres a space in the input file that needs to be removed here...
    bingo_boards.pop(0)

    return numbers, bingo_boards


def mark_board(board, number):
    """Marks a bingo board for a number that was called"""
    return np.where(board == number, -1, board)


def check_win(board, index):
    """Checks a bingo board to see if it is a winner"""
    row_winner = np.all(board[index, :] == -1)
    column_winner = np.all(board[:, index] == -1)

    return row_winner or column_winner


def get_score(board, number):
    """Gets the final score for a bingo board"""
    return np.sum(np.where(board == -1, 0, board)) * number


def part_1(numbers, bingo_boards):

    count = 0
    win = False

    while not win:
        # draw the next number
        current_num = numbers[count]

        for i in range(len(bingo_boards)):
            # mark the boards
            bingo_boards[i] = mark_board(bingo_boards[i], current_num)

            for j in range(len(bingo_boards[i])):
                if check_win(bingo_boards[i], j):
                    win = True
                    winner = bingo_boards[i]
                    break

            if win:
                break

        count += 1

    solution1 = get_score(winner, current_num)

    return solution1


def part_2(numbers, bingo_boards):

    count = 0
    winners = np.zeros(len(bingo_boards))

    while sum(winners) < len(bingo_boards):
        # draw the next number
        current_num = numbers[count]

        for i in range(len(bingo_boards)):
            # mark the boards
            bingo_boards[i] = mark_board(bingo_boards[i], current_num)

            for j in range(len(bingo_boards[i])):
                if check_win(bingo_boards[i], j):
                    # keep track of boards as they win
                    if winners[i] == 0:
                        winners[i] = 1
                    else:
                        continue

                # get the last winner board index
                if sum(winners) == len(bingo_boards) - 1:
                    last_winner_idx = int(np.where(winners == 0)[0])

        count += 1

    last_winner = bingo_boards[last_winner_idx]
    solution2 = get_score(last_winner, current_num)

    return solution2


def main(path):
    numbers, bingo_boards = read_data(path)
    solution1 = part_1(numbers, bingo_boards)
    solution2 = part_2(numbers, bingo_boards)

    print(f"Part 1 Solution: {solution1}")
    print(f"Part 2 Solution: {solution2}")


if __name__ == "__main__":
    path = "problems/day-4-giant-squid/input.txt"
    main(path)
