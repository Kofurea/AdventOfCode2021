import time
import numpy as np

def day11():
    start = time.time()
    # Part 1
    with open('Day11_input.txt', 'r') as file:
        input_file = [list(line.strip()) for line in file]

    # Input file for testing
    testing = False
    if testing:
        input_file = []
        for item in [5483143223,2745854711,5264556173,6141336146,6357385478,4167524645,2176841721,6882881134,4846848554,5283751526]:
            input_file.append(list(str(item)))

    # Turn the strings into ints
    for row, _ in enumerate(input_file):
        input_file[row] = [int(i) for i in input_file[row]]

    flashes = []
    part2_answer = 0
    halt_simulation = False

    # For every step
    for step in range(1,1001):
        flashes_this_step = 0
        # Make a copy
        # First, increase the energy level of each octopus by 1
        for row, _ in enumerate(input_file):
            for column, _ in enumerate(input_file[row]):
                input_file[row][column] += 1
        # Let the octopi flash
        new_flashers = True
        while new_flashers:
            if halt_simulation == False:
                for row, _ in enumerate(input_file):
                    for column, value in enumerate(input_file[row]):
                        if value > 9:
                            flashes_this_step += 1
                            input_file[row][column] = 0
                            # And then chain the flashes
                            for neighbor in [[row-1, column-1], [row-1, column], [row-1, column+1], [row, column-1], [row, column+1], [row+1, column-1], [row+1, column], [row+1, column+1]]:
                                try:
                                    if input_file[neighbor[0]][neighbor[1]] > 0 and input_file[neighbor[0]][neighbor[1]] <= 9 and neighbor[0] != -1 and neighbor[1] != -1:
                                        input_file[neighbor[0]][neighbor[1]] += 1
                                except:
                                    pass

                # Check if there are any new flashers
                any9s = False
                for row, _ in enumerate(input_file):
                    for column, _ in enumerate(input_file[row]):
                        if input_file[row][column] > 9:
                            any9s = True

                if flashes_this_step == 100:
                    part2_answer = step
                    halt_simulation = True
                    new_flashers = False

                if not any9s:
                    new_flashers = False
                    flashes.append(flashes_this_step)
            else:
                new_flashers = False
    print("The answer to part 1 is:", sum(flashes))

    print("The answer to part 2 is:", part2_answer)

    end = time.time()

    print("The elapsed time is:", end-start)