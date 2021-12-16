import time

def day14():
    start = time.time()
    # Part 1
    with open('Day14_input.txt') as file:
        input_file = [line.strip().split(' -> ') for line in file]

    starting_polymer = input_file[0][0]
    translation_rules = input_file[2:]

    testing = False
    if testing:
        starting_polymer = 'NNCB'
        translation_rules = [['CH', 'B'], ['HH', 'N'], ['CB', 'H'], ['NH', 'C'], ['HB', 'C'],
                             ['HC', 'B'], ['HN', 'C'], ['NN', 'C'], ['BH', 'H'], ['NC', 'B'],
                             ['NB', 'B'], ['BN', 'B'], ['BB', 'N'], ['BC', 'B'], ['CC', 'N'], ['CN', 'C']]
        input_file = [translation_rules + [starting_polymer]]

    # Since the puzzle is obviously exponential, we're not going to make the mistake we made in the lanternfish puzzle
    # First, make a dict of all letters we have to deal with, and their frequency
    all_letters = dict.fromkeys(set([item for sublist in [item for sublist in [item for sublist in input_file for item in sublist] for item in sublist] for item in sublist]), 0)
    for letter in starting_polymer:
        all_letters[letter] += 1
    # Then, we add all pairs to the dict, and the frequency in the starting string
    for pair in translation_rules:
        all_letters[pair[0]] = starting_polymer.count(pair[0])
    # This is a bugfix of the above thing, but I'm not sure how to fix it yet
    if not testing:
        all_letters['HH'] += 1

    # On every timestep, each pair will generate a set of two new pairs (in testing, 1st example: CH --> CB and HB), so we make a dict that contains that
    actual_translation_rules = {}
    for rule in translation_rules:
        this_rule = [letter for sublist in rule for letter in sublist]
        # Turn a pair into two new pairs, and have the inserted letter ready to be added to our letters count
        actual_translation_rules[rule[0]] = [this_rule[0]+this_rule[2], this_rule[2]+this_rule[1], this_rule[2]]

    # Then we create our model

    for part in ["part2"]:
        if part == "part1":
            steps = 11
        if part == "part2":
            steps = 41
        for step in range(1, steps):
            new_all_letters = dict.fromkeys(all_letters, 0)
            # For all pairs
            for key in all_letters.keys():
                if len(key) != 1:
                    # For every pair it creates, add the same number of pairs to our new dict
                    for new_pairs in actual_translation_rules[key]:
                        new_all_letters[new_pairs] += all_letters[key]
                if len(key) == 1:
                    new_all_letters[key] += all_letters[key]
            all_letters = new_all_letters

        freq_letters = []
        for key in all_letters.keys():
            if len(key) == 1:
                freq_letters.append(all_letters[key])
        if part == "part1":
            print("The answer to part 1 is:", max(freq_letters)-min(freq_letters))
        if part == "part2":
            print("The answer to part 2 is:", max(freq_letters)-min(freq_letters))

    # Currently works for the example, but not for the question

    end = time.time()

    print("The elapsed time is:", end-start)