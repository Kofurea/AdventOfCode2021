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

number_lookup = [
    [1, 2, 3, 5, 6, 7],         # 0
    [3, 6],                     # 1
    [1, 3, 4, 5, 7],            # 2
    [1, 3, 4, 6, 7],            # 3
    [2, 3, 4, 6],               # 4
    [1, 2, 4, 6, 7],            # 5
    [1, 2, 4, 5, 6, 7],         # 6
    [1, 3, 5],                  # 7
    [1, 2, 3, 4, 5, 6, 7, 8],   # 8
    [1, 2, 3, 4, 5, 7, 8]       # 9
]

answer = 0

for row, line in enumerate(list_of_clues):
    # Numbers are each section of the 7-segment display, top-to-bottom, left-to-right
    decode = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0}
    # Find the number 1
    one = [x for x in line if len(x) == 2]
    # The number 7 gives us decode 1
    seven = [x for x in line if len(x) == 3]
    decode[1] = seven[0].replace(one[0][0], '').replace(one[0][1], '')
    # Of the numbers in one, decode 3 occurs
    flat_line = [x for x in [item for sublist in line for item in sublist] if x == one[0][0]]
    if len(flat_line) == 8:
        decode[3] = one[0][0]
        decode[6] = one[0][1]
    else:
        decode[3] = one[0][1]
        decode[6] = one[0][0]
    # The number 4 gives us decode 2 and 4 (unspecified)
    four = [x for x in line if len(x) == 4]
    decode2decode4 = four[0].replace(one[0][0], '').replace(one[0][1], '')
    # The common set between all 5 lengths are digit 1, 4 and 7 (unspecified). Combined with the last this gives us decode 2, 4 and 7. The last decode is 5
    decodefivewithout147 = [x for x in
                            [x.replace(list(set([x for x in [item for sublist in [x for x in line if len(x) == 5] for item in sublist]
                                                 if [item for sublist in [x for x in line if len(x) == 5] for item in sublist].count(x) == 3]))[0], '')
                                 .replace(list(set([x for x in [item for sublist in [x for x in line if len(x) == 5] for item in sublist]
                                                    if [item for sublist in [x for x in line if len(x) == 5] for item in sublist].count(x) == 3]))[1], '')
                                 .replace(list(set([x for x in [item for sublist in [x for x in line if len(x) == 5] for item in sublist]
                                                    if [item for sublist in [x for x in line if len(x) == 5] for item in sublist].count(x) == 3]))[2], '')
                             for x in [item for sublist in [x for x in line if len(x) == 5] for item in sublist]] if x != '']
    decode[2] = [x for x in list(set(decodefivewithout147))
                 if x != one[0][0] and x != one[0][1] and x != four[0][0] and x != four[0][1] and x != four[0][2] and x != four[0][3]][0]
    decode[5] = [x for x in list(set(decodefivewithout147))
                 if x != one[0][0] and x != one[0][1] and x != decode[2]][0]
    decode[4] = [x for x in four[0]
                 if x != decode[2] and x != decode[3] and x != decode[5] and x != decode[6]][0]
    decode[7] = [x for x in list(set([item for sublist in line for item in sublist]))
                 if x != decode[1] and x != decode[2] and  x != decode[3] and  x != decode[4] and  x != decode[5] and  x != decode[6]][0]
    invert_decode = {v: k for k, v in decode.items()}

    for item in list_of_questions[row]:
        code = []
        combined_number = []
        for _, letter in enumerate(item):
            code.append(invert_decode[letter])
        for index, item in enumerate(number_lookup):
            if [item for item in code if item not in number_lookup[index]] == []:
                combined_number.append(str(index))
        answer += int("".join(combined_number))

print("The answer to part 2 is:", answer)

end = time.time()

print("The elapsed time is:", end-start)