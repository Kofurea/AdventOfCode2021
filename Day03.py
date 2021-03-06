# Part 1

import time

start = time.time()

def power_calc(gamma, epsilon):
    power = gamma * epsilon
    return power

def list_to_dec(binary_input):
    str_bin = ""
    for element in binary_input:
        str_bin += element
    answer = int(str_bin, 2)
    return answer

def reverse_the_binary(binary_input):
    new_binary = []
    for element in binary_input:
        if element == '0':
            new_binary.append('1')
        elif element == '1':
            new_binary.append('0')
        else:
            raise ValueError
    return new_binary


def analyse_input(file, type):
    if type != "gamma" and type != "epsilon":
        raise ValueError

    binary = []

    for digit in range(len(file[0])):
        count_0, count_1 = 0, 0
        for row in range(len(file)):
            if file[row][digit] == '0':
                count_0 += 1
            elif file[row][digit] == '1':
                count_1 += 1
            else:
                raise ValueError
        if count_0 > count_1:
            binary.append('0')
        elif count_0 < count_1:
            binary.append('1')
        else:
            raise ValueError

    if type == "epsilon":
        binary = reverse_the_binary(binary)

    return list_to_dec(binary)

def day03():
    print("Day 3")
    with open('Day03_input.txt', 'r') as file:
        input_file = [line.strip() for line in file]

    gamma_answer = analyse_input(input_file, "gamma")
    epsilon_answer = analyse_input(input_file, "epsilon")

    print("The answer to part 1 is: ", power_calc(gamma_answer, epsilon_answer))

    # Part 2

    def life_support_rating_calc(oxygen_generator_rating, CO2_scrubber_rating):
        answer = oxygen_generator_rating * CO2_scrubber_rating
        return answer

    def reduction(input_list, type):
        if type == "oxygen":
            keep_ox = "1"
        elif type == "CO2":
            keep_co = "0"
        else:
            raise ValueError

        keep = ""

        new_list = list(filter(lambda x: x.startswith(keep), input_list)).copy()

        for digit, _ in enumerate(input_list[0]):
            nth_digit = []
            for row, _ in enumerate(new_list):
                nth_digit.append(new_list[row][digit])
            if type == "oxygen":
                if nth_digit.count('1') > nth_digit.count('0'):
                    keep += '1'
                elif nth_digit.count('1') < nth_digit.count('0'):
                    keep += '0'
                else:
                    keep += keep_ox
            else:
                if nth_digit.count('1') < nth_digit.count('0'):
                    keep += '1'
                elif nth_digit.count('1') > nth_digit.count('0'):
                    keep += '0'
                else:
                    keep_co

            new_list = list(filter(lambda x: x.startswith(keep), new_list))

            if len(new_list) == 1:
                return new_list

        return new_list

    oxygen = reduction(input_file, "oxygen")
    CO2 = reduction(input_file, "CO2")
    print("The answer to part 2 is: ", life_support_rating_calc(int(oxygen[0], 2), int(CO2[0], 2)))

    end = time.time()
    print("Elapsed time:", end-start, "\n")