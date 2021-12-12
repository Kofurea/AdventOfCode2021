# Part 1

import re
import time

start = time.time()

input_file_split = []

with open('Day08_input.txt', 'r') as file:
    input_file = [line.strip() for line in file]
    for line, _ in enumerate(input_file):
        num_strings = re.findall(r'-?[A-Za-z]+', input_file[line])
        input_file_split.append([str(num_str) for num_str in num_strings])

# Split the list into clues to analyse, and questions to answer
list_of_clues = []
list_of_questions = []

for _, line in enumerate(input_file_split):
    list_of_clues.append(line[:10])
    list_of_questions.append(line[10:])

# Flatten the list
part1_list = [item for sublist in list_of_questions for item in sublist]

# Count the number of unique lengths
count_unique = 0

for _, item in enumerate(part1_list):
    if len(item) == 2: # The number 1
        count_unique += 1
    if len(item) == 3: # The number 7
        count_unique += 1
    if len(item) == 4: # The number 4
        count_unique += 1
    if len(item) == 7: # The number 8
        count_unique += 1

print("The answer to part 1 is:", count_unique)

# Part 2

for row, line in enumerate(list_of_clues):
    number = []
    for _, item in enumerate(line):
        if len(item) == 2:
            number.append('1')
        elif len(item) == 4:
            number.append('4')
        elif len(item) == 3:
            number.append('7')
        elif len(item) == 7:
            number.append('8')
        elif len(item) == 5:
            for _, clue in enumerate(line):
                if len(clue) == 2:
                    two = clue
                    if len(set(clue) & set(item)) == 2:
                        number.append('3')
            for _, clue in enumerate(line):
                if len(clue) == 4:
                    disp24 = set(clue) & set(two)
                    print(set(item), set(disp24), set(item) & set(disp24), len(set(item)&set(disp24)))
                    if len(set(disp24) & set(clue)) == 2:
                       number.append('5')
                    else:
                        number.append('2')
        elif len(item) == 6:
            for _, clue in enumerate(line):
                if len(clue) == 2:
                    two = clue
            for _, clue in enumerate(line):
                if len(clue) == 4:
                    disp24 = set(clue) & set(two)
            if len(set(item) & set(disp24)) != 2:
                number.append('0')
            else:
                if len(set(item) & set(two)) == 2:
                    number.append('9')
                else:
                    number.append('6')

        else:
            raise ValueError
    print(number)
    pause