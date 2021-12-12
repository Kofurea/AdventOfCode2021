import time
import numpy as np

start = time.time()

with open('Day06_input.txt', 'r') as file:
    input_file = [line.strip() for line in file]
    initial_fish = list(map(int, input_file[0].split(',')))

fishcount = list(np.zeros(9, dtype=int))

for _, fish in enumerate(initial_fish):
    fishcount[fish] += 1

for tick in range(80):
    new_count = list(np.zeros(9, dtype=int))
    for count, _ in enumerate(fishcount):
        if count != 0:
            new_count[count-1] += fishcount[count]
        else:
            new_count[6] += fishcount[count]
            new_count[8] += fishcount[count]
    fishcount = new_count

print("The answer to part 1 is:", sum(fishcount))

with open('Day06_input.txt', 'r') as file:
    input_file = [line.strip() for line in file]
    initial_fish = list(map(int, input_file[0].split(',')))

fishcount = list(np.zeros(9, dtype=int))

for _, fish in enumerate(initial_fish):
    fishcount[fish] += 1

for tick in range(256):
    new_count = list(np.zeros(9, dtype='int64'))
    for count, _ in enumerate(fishcount):
        if count != 0:
            new_count[count-1] += fishcount[count]
        else:
            new_count[6] += fishcount[count]
            new_count[8] += fishcount[count]
    fishcount = new_count

print("The answer to part 2 is:", sum(fishcount))

end = time.time()

print("The elapsed time is:", end-start)