import time
import statistics

def day10():
    # Part 1
    print("Day 10")
    start = time.time()
    with open('Day10_input.txt', 'r') as file:
        input_file = [list(line.strip()) for line in file]

    # Testing based on example
    #input_file = ['[({(<(())[]>[[{[]{<()<>>','[(()[<>])]({[<{<<[]>>(','{([(<{}[<>[]}>{[]{[(<()>','(((({<>}<{<{<>}{[]{[]{}','[[<[([]))<([[{}[[()]]]','[{[{({}]{}}([{[{{{}}([]','{<[[]]>}<{[{[{[]{()[[[]','[<(<(<(<{}))><([]([]()','{([([[(<>()){}]>(<<{{','<{([{{}}[<[[[<>{}]]]>[]]']

    scoring = {')':3, ']':57, '}':1197, '>':25137}
    closers = {')':'(', ']':'[', '}':'{', '>':'<'}

    score = 0
    corrupted_lines = []

    for line_index, line in enumerate(input_file):
        list_of_opened_syntaxes = []
        for _, char in enumerate(line):
            if char in closers.keys():
                # If the closing character doesn't match the most recent opener, we have a corruption
                if list_of_opened_syntaxes[-1] == closers[char]:
                    del list_of_opened_syntaxes[-1]
                else:
                    score += scoring[char]
                    corrupted_lines.append(line_index)
                    break
            else:
                list_of_opened_syntaxes.append(char)

    print("The answer to part 1 is:", score)

    # Make the file without corruption
    part2_input = []
    for line_index, line in enumerate(input_file):
        if line_index not in corrupted_lines:
            part2_input.append(line)

    scoring = {'(':1, '[':2, '{':3, '<':4}
    score = []

    for line_index, line in enumerate(part2_input):
        list_of_opened_syntaxes = []
        internal_score = 0
        for char_index, char in enumerate(line):
            # Closing chars
            if char in closers.keys():
                if list_of_opened_syntaxes[-1] == closers[char]:
                    del list_of_opened_syntaxes[-1]
            else:
                list_of_opened_syntaxes.append(char)
            if char_index == len(line)-1:
                for _, missing_char in enumerate(list_of_opened_syntaxes[::-1]):
                    internal_score = internal_score*5
                    internal_score += scoring[missing_char]
                score.append(internal_score)

    score.sort()

    print("The answer to part 2 is:", statistics.median(score))

    end = time.time()

    print("The elapsed time is:", end-start)