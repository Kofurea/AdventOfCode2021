# Part 1

import re
from functools import reduce

class BingoCard:
    def __init__(self, input_grid):
        self.grid = input_grid
        self.bingo = False # for part 2

with open('Day04_input.txt', 'r') as file:
    input_file = [line.strip() for line in file]

# Setup Bingo Cards
called_numbers = list(map(lambda n: int(n), input_file[0].split(',')))
bingo_cards = []
card_num = -1

for i in range(len(input_file)):
    if i == 0:
        counter = 0
    else:
        counter += 1
        if counter == 1:
            card = []
        else:
            card.append([input_file[i]])
            if len(card) == 5:
                counter = 0
                bingo_cards.append(BingoCard(card))

for card in range(len(bingo_cards)):
    for row in range(len(bingo_cards[card].grid)):
        bingo_cards[card].grid[row][0] = list(map(lambda n: int(n), re.split(" +", bingo_cards[card].grid[row][0])))
        bingo_cards[card].grid[row] = bingo_cards[card].grid[row][0]

def run_bingo(bingo_boards, list_of_numbers, firstlast):
    if firstlast != "first" and firstlast != "last":
        raise ValueError

    bingo = False

    winning_board = []
    winning_number = 0
    boards_with_bingo = 0

    for number in range(len(list_of_numbers)):
        if not bingo:
            for card in range(len(bingo_boards)):
                for row in range(len(bingo_boards[card].grid)):
                    # Add new number to the card
                    if bingo_boards[card].bingo == False:
                        for digit in range(len(bingo_boards[card].grid[row])):
                            if bingo_boards[card].grid[row][digit] == list_of_numbers[number]:
                                bingo_boards[card].grid[row][digit] = 'X'

                # Check for the first bingo
                if firstlast == "first":
                    if not bingo:
                        columns = list(map(list, zip(*bingo_boards[card].grid)))
                        for column in range(len(columns)):
                            if columns[column].count('X') == 5:
                                bingo = True
                        for row in range(len(bingo_boards[card].grid)):
                            if bingo_boards[card].grid[row].count('X') == 5:
                                bingo = True
                        if bingo:
                            winning_number = list_of_numbers[number]
                            winning_board = bingo_boards[card].grid

                # Check for the last bingo
                if firstlast == "last":
                    if bingo_boards[card].bingo == False:
                        columns = list(map(list, zip(*bingo_boards[card].grid)))
                        for column in range(len(columns)):
                            if columns[column].count('X') == 5:
                                bingo_boards[card].bingo = True
                        for row in range(len(bingo_boards[card].grid)):
                            if bingo_boards[card].grid[row].count('X') == 5:
                                bingo_boards[card].bingo = True
                        if bingo_boards[card].bingo == True:
                            boards_with_bingo += 1
                            if boards_with_bingo == len(bingo_boards):
                                winning_number = list_of_numbers[number]
                                winning_board = bingo_boards[card].grid



    return winning_number, winning_board

number, board = run_bingo(bingo_cards, called_numbers, "first")

frmt = "{:>3}"*len(board[0])

print("The board:\n", frmt.format(*board[0]), "\n",
      frmt.format(*board[1]), "\n",
      frmt.format(*board[2]), "\n",
      frmt.format(*board[3]), "\n",
      frmt.format(*board[4]))
print("Last called number:", number)
print("The answer to part 1 is:",
      reduce(lambda l,r: l+r, filter(lambda n: type(n) is int,
                                     [item for sublist in board for item in sublist])) * number)

print("\n \n \n")

number, board = run_bingo(bingo_cards, called_numbers, "last")

print("The board:\n", frmt.format(*board[0]), "\n",
      frmt.format(*board[1]), "\n",
      frmt.format(*board[2]), "\n",
      frmt.format(*board[3]), "\n",
      frmt.format(*board[4]))
print("Last called number:", number)
print("The answer to part 2 is:",
      reduce(lambda l,r: l+r, filter(lambda n: type(n) is int,
                                     [item for sublist in board for item in sublist])) * number)
