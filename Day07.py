# Part 1

import re
import time

def day07():
    print("Day 7")
    start = time.time()

    with open('Day07_input.txt', 'r') as file:
        input_file = [line.strip() for line in file]
        num_strings = re.findall(r'-?[0-9]+', input_file[0])
        input_file = [int(num_str) for num_str in num_strings]

    fuel_spend = []

    for value in range(min(input_file), max(input_file)):
        fuel_spend.append(sum([abs(crab-value) for crab in input_file]))

    print("The answer to part 1 is:", min(fuel_spend))

    fuel_spend = []
    list_of_travelcosts = []

    for value in range(0, max(input_file)+1):
        list_of_travelcosts.append(sum(range(1, abs(value)+1)))

    for value in range(min(input_file), max(input_file)):
        fuel = []
        for _, crab in enumerate(input_file):
            fuel.append(list_of_travelcosts[abs(crab-value)])
        fuel_spend.append(sum(fuel))

    print("The answer to part 2 is:", min(fuel_spend))

    end = time.time()

    print("Time elapsed:", end-start, "\n")