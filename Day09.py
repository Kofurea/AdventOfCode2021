# Part 1
import time
import numpy as np

def day09():
    print("Day 9")
    start = time.time()
    with open('Day09_input.txt', 'r') as file:
        input_file = [list(line.strip()) for line in file]

    heights = []

    for index_row, row in enumerate(input_file):
        for index_column, column in enumerate(input_file[index_row]):
            # If it is the first column
            if index_column == 0:
                # If its smaller than the horizontally adjacent numbers
                if column < input_file[index_row][index_column+1]:
                    # If it is the first row
                    if index_row == 0:
                        if column < input_file[index_row+1][index_column]:
                            heights.append(int(column)+1)
                    # If it is the last row
                    elif index_row == len(input_file)-1:
                        if column < input_file[index_row-1][index_column]:
                            heights.append(int(column)+1)
                    # If it is any other row
                    else:
                        if column < input_file[index_row+1][index_column] and column < input_file[index_row-1][index_column] :
                            heights.append(int(column)+1)
            # If it is the last column
            elif index_column == len(input_file[index_row])-1:
                # If its smaller than the horizontally adjacent numbers
                if column < input_file[index_row][index_column-1]:
                    # If it is the first row
                    if index_row == 0:
                        if column < input_file[index_row+1][index_column]:
                            heights.append(int(column)+1)
                    # If it is the last row
                    elif index_row == len(input_file)-1:
                        if column < input_file[index_row-1][index_column]:
                            heights.append(int(column)+1)
                    else:
                    # If it is any other row
                        if column < input_file[index_row+1][index_column] and column < input_file[index_row-1][index_column] :
                            heights.append(int(column)+1)
            # If its any other column
            else:
                # If its smaller than the horizontally adjacent numbers
                if column < input_file[index_row][index_column-1] and column < input_file[index_row][index_column+1]:
                    # If it is the first row
                    if index_row == 0:
                        if column < input_file[index_row+1][index_column]:
                            heights.append(int(column)+1)
                    # If it is in the last row
                    elif index_row == len(input_file)-1:
                        if column < input_file[index_row-1][index_column]:
                            heights.append(int(column)+1)
                    # If it is any other row
                    else:
                        if column < input_file[index_row+1][index_column] and column < input_file[index_row-1][index_column] :
                            heights.append(int(column)+1)

    print("The answer to part 1 is:", sum(heights))

    # Part 2

    # Make a masking grid to mark
    masking_grid = np.zeros((len(input_file[0]), len(input_file))).astype(int)

    # Mark all nines as 'walls' on the masking grid
    for index_row, row in enumerate(input_file):
        for index_column, column in enumerate(input_file[index_row]):
            if column == '9':
                masking_grid[index_row][index_column] = 9

    size_of_sinks = []
    size_of_sinks_index = 0

    def bleed_nodes(row, column):
        # 9 is a wall, 1 is "testing", 2 is "has been tested"
        any_neighbors = True
        while any_neighbors == True:
            # For every 1, we will check if all neighbors have been checked (aka not 0)
            for index_row, row in enumerate(masking_grid):
                for index_column, column in enumerate(masking_grid[index_row]):
                    # If we need to test this one
                    if column == 1:
                        # Turn the column into "has been tested"
                        masking_grid[index_row][index_column] = 2
                        # Check horizontal neighbors
                        # If it is the first element
                        if index_column == 0:
                            if masking_grid[index_row][index_column+1] == 0:
                                masking_grid[index_row][index_column+1] = 1
                        # If it is the last element
                        elif index_column == len(masking_grid)-1:
                            if masking_grid[index_row][index_column-1] == 0:
                                masking_grid[index_row][index_column-1] = 1
                        # If it is any other element
                        else:
                            if masking_grid[index_row][index_column+1] == 0:
                                masking_grid[index_row][index_column+1] = 1
                            if masking_grid[index_row][index_column-1] == 0:
                                masking_grid[index_row][index_column-1] = 1
                        # Check vertical neighbors
                        # If it is the first element
                        if index_row == 0:
                            if masking_grid[index_row+1][index_column] == 0:
                                masking_grid[index_row+1][index_column] = 1
                        # If it is the last element
                        elif index_row == len(masking_grid)-1:
                            if masking_grid[index_row-1][index_column] == 0:
                                masking_grid[index_row-1][index_column] = 1
                        # If it is any other element
                        else:
                            if masking_grid[index_row+1][index_column] == 0:
                                masking_grid[index_row+1][index_column] = 1
                            if masking_grid[index_row-1][index_column] == 0:
                                masking_grid[index_row-1][index_column] = 1

            # Check if we tried all neighbors, count_1 is "number of nodes that have to be tested"
            count_1 = 0
            for index_row, row in enumerate(masking_grid):
                for index_column, column in enumerate(masking_grid[index_row]):
                    if masking_grid[index_row][index_column] == 1:
                        count_1 += 1

            # If all neighbors are tried, break the loop
            if count_1 == 0:
                # Count the size of the sink
                count_2 = 0
                for index_row, row in enumerate(masking_grid):
                    for index_column, column in enumerate(masking_grid[index_row]):
                        if masking_grid[index_row][index_column] == 2:
                            count_2 += 1

                # Break the loop
                any_neighbors = False

        for index_row, row in enumerate(masking_grid):
            for index_column, column in enumerate(masking_grid[index_row]):
                if masking_grid[index_row][index_column] == 2:
                    masking_grid[index_row][index_column] = 9

        return count_2

    for index_row, row in enumerate(input_file):
        list_of_sink_nodes = []
        for index_column, column in enumerate(input_file[index_row]):
            # Check the masking grid
            if masking_grid[index_row][index_column] == 0:
                masking_grid[index_row][index_column] = 1
                masking_grid[index_row][index_column] = 1
                size_of_sinks.append(bleed_nodes(index_row, index_column))
            else:
                pass

    size_of_sinks = sorted(size_of_sinks, reverse=True)[:3]

    print("The answer to part 2 is:", size_of_sinks[0] * size_of_sinks[1] * size_of_sinks[2])

    end = time.time()

    print("The elapsed time is:", end-start)