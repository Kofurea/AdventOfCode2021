import time
import numpy as np

def day11():
    start = time.time()
    # Part 1
    with open('Day11_input.txt', 'r') as file:
        input_file = [list(line.strip()) for line in file]

    # Input file for testing
    testing = True
    if testing:
        input_file = []
        for item in [5483143223,2745854711,5264556173,6141336146,6357385478,4167524645,2176841721,6882881134,4846848554,5283751526]:
            input_file.append(list(str(item)))

    # Turn the strings into ints
    for row, _ in enumerate(input_file):
        input_file[row] = [int(i) for i in input_file[row]]

    # Create an empty masking layer
    mask = np.zeros((100,100), dtype=int)
    print(mask)

    for step in range(1,101):
        # First, increase the energy level of each octopus by 1
        for row, _ in enumerate(input_file):
            for column, _ in enumerate(input_file):
                input_file[row][column] += 1
        # Then

    end = time.time()

    print("The elapsed time is:", end-start)