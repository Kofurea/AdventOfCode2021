import time
import numpy as np

def day13():
    start = time.time()
    # Part 1
    with open('Day13_input.txt') as file:
        input_file = [line.strip().split(',') for line in file]

    # Split the file into instructions and dots
    dots = []
    instructions = []
    for item in input_file:
        if len(item) == 2:
            dots.append([int(item[0]), int(item[1])])
        else:
            if item != ['']:
                instructions.append(item[0].replace('fold along ', '').split('='))

    testing = False
    if testing:
        dots = [[6,10], [0,14], [9,10], [0,3], [10,4], [4,11],
                [6,0], [6,12], [4,1], [0,13], [10,12], [3,4],
                [3,0], [8,4], [1,10], [2,14], [8,10], [9,0]]
        instructions = [['y', '7'], ['x', '5']]

    # Find paper size
    x_y_size = [0,0]
    for _, coordinate in enumerate(dots):
        if coordinate[0] > x_y_size[0]:
            x_y_size[0] = coordinate[0]
        if coordinate[1] > x_y_size[1]:
            x_y_size[1] = coordinate[1]

    # Create the paper and populate it
    paper = np.zeros((x_y_size[0]+1, x_y_size[1]+1), dtype=int)
    for _, dot in enumerate(dots):
        paper[dot[0]][dot[1]] += 1
    # For some reason we have to transpose this paper
    paper = np.rot90(np.fliplr(paper))

    instruction_count = 0
    for _, instruction in enumerate(instructions):
        instruction_count += 1
        if instruction[0] == 'x':
            new_paper = paper[:,:int(instruction[1])]
            fold = np.fliplr(paper[:,int(instruction[1])+1:])
            for line_index, line in enumerate(fold):
                new_paper[line_index] += line
            paper = new_paper
            if instruction_count == 1:
                part_1_answer = np.count_nonzero(paper)
        if instruction[0] == 'y':
            new_paper = paper[:int(instruction[1])]
            fold = np.flipud(paper[int(instruction[1])+1:])
            for line_index, line in enumerate(fold):
                new_paper[line_index] += line
            paper = new_paper
            if instruction_count == 1:
                part_1_answer = np.count_nonzero(paper)

    print("The answer to part 1 is:", part_1_answer)

    print("The answer to part 2 is:")
    for line_index, line in enumerate(paper):
        print_line = []
        for item_index, item in enumerate(line):
            if item == 0:
                print_line.append("  ")
            else:
                if len(str(item)) == 1:
                    print_line.append(" " + str(item))
                else:
                    print_line.append(str(item))
        print(print_line)

    end = time.time()

    print("The elapsed time is:", end-start)