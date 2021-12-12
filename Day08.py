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

def decode(clues):
    letter_to_position = {"a":[], "b":[], "c":[], "d":[], "e":[], "f":[], "g":[]}
    # Retrieve the positions in the number 1
    num_one = [char for char in [clue for clue in clues if len(clue) == 2][0]]
    # Retrieve the positions in the number 7
    num_seven = [char for char in [clue for clue in clues if len(clue) == 3][0]]
    # Assing position "a" by subtracting 1 from 7
    letter_to_position[list(set(num_seven) ^ set(num_one))[0]] = 'a'
    # Retrieve position "b" and "d" by subtracting 1 from 4
    pos_bd = list(set([char for char in [clue for clue in clues if len(clue) == 4][0]]) ^ set(num_one))
    # Retrieve position "b" and "e" by looking at the length 5 digits and finding which occur only once
    len_five = [char for char in "".join([clue for clue in clues if len(clue) == 5])]
    pos_be = []
    for char in set(len_five):
        if len_five.count(char) == 1:
            pos_be.extend(char)
    # Find b by looking for the overlap of the two subtractions
    letter_to_position[list(set(pos_be)&set(pos_bd))[0]] = 'b'
    # And by extend find what the other characters of these subtractions mean
    letter_to_position[list(set(pos_bd) ^ (set(pos_be) & set(pos_bd)))[0]] = 'd'
    letter_to_position[list(set(pos_be) ^ (set(pos_be) & set(pos_bd)))[0]] = 'e'
    # Counting the length 5 for items that occur 3 times, and then removing 'a' and 'd', gives us 'g'
    for char in set(len_five):
        if len_five.count(char) == 3:
            if letter_to_position[char] == []:
                letter_to_position[char] = 'g'
    # Count for 9 occurrances, assing that 'f', and give the other letter of the number one 'c'
    for char in set("".join(clues)):
        if list("".join(clues)).count(char) == 9:
            letter_to_position[char] = 'f'
            letter_to_position[list(set(char) ^ set(num_one))[0]] = 'c'

    # Now we have a dict that can input any 'coded' segment, and return the real segment
    return letter_to_position

def decypher(decoder, code):
    number_lookup = [
        [1, 2, 3, 5, 6, 7],  # 0
        [3, 6],  # 1
        [1, 3, 4, 5, 7],  # 2
        [1, 3, 4, 6, 7],  # 3
        [2, 3, 4, 6],  # 4
        [1, 2, 4, 6, 7],  # 5
        [1, 2, 4, 5, 6, 7],  # 6
        [1, 3, 5],  # 7
        [1, 2, 3, 4, 5, 6, 7, 8],  # 8
        [1, 2, 3, 4, 5, 7, 8]  # 9
    ]

    value = 0

    return value

answers = []

for line, _ in enumerate(list_of_clues):
    decoding_dict = decode(line)
    answers.append(decypher(decoding_dict, list_of_questions[line]))

print("The answer to part 2 is:", decoding_dict)

end = time.time()

print("The elapsed time is:", end-start)