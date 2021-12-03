# Part 1

import re

input_split = []

with open('Day02_input.txt', 'r') as file:
    input_file = [line.strip() for line in file]

for i in range(len(input_file)):
    input_split.append(re.findall('(\d+|[A-Za-z]+)', input_file[i]))

class Submarine():
    horizontal = 0
    depth = 0
    aim = 0 # For part 2

submarine = Submarine()

for i in range(len(input_split)):
    if input_split[i][0] == 'forward':
        submarine.horizontal += int(input_split[i][1])
    elif input_split[i][0] == 'up':
        submarine.depth -= int(input_split[i][1])
    elif input_split[i][0] == 'down':
        submarine.depth += int(input_split[i][1])

print("Answer part 1: ", submarine.horizontal * submarine.depth)

# Part 2

submarine = Submarine()

for i in range(len(input_split)):
    if input_split[i][0] == 'forward':
        submarine.horizontal += int(input_split[i][1])
        submarine.depth += submarine.aim * int(input_split[i][1])
    elif input_split[i][0] == 'up':
        submarine.aim -= int(input_split[i][1])
    elif input_split[i][0] == 'down':
        submarine.aim += int(input_split[i][1])

print("Answer part 2: " + str(submarine.horizontal * submarine.depth))