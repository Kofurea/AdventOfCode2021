import time
import numpy as np

start = time.time()

class LineSegment():
    def __init__(self, x1_i, y1_i, x2_i, y2_i):
        self.x1 = x1_i
        self.y1 = y1_i
        self.x2 = x2_i
        self.y2 = y2_i
        self.part1 = False

    def make_line(self):
        if self.x1 == self.x2 or self.y1 == self.y2:
            self.part1 = True
            self.x_line = list(range(min([self.x1,self.x2]), max([self.x1,self.x2])))
            self.y_line = list(range(min([self.y1,self.y2]), max([self.y1,self.y2])))
            if self.x_line == []:
                self.x_line = [ self.x1 for _, _ in enumerate(self.y_line)]
            else:
                self.y_line = [ self.y1 for _, _ in enumerate(self.x_line)]
            self.coordinates = np.array(list(zip(self.x_line, self.y_line)))
        else:
            pass

class Radar():
    def __init__(self):
        self.grid = [ [ 0 for _ in range(1000) ] for _ in range(1000) ]

# Open the file
with open('Day05_input.txt', 'r') as file:
    input_file = [line.strip().split() for line in file]

# Clean the data
for row, _ in enumerate(input_file):
    input_file[row][2] = int(input_file[row][2].split(',')[0]), int(input_file[row][2].split(',')[1])
    del input_file[row][1]
    input_file[row][0] = int(input_file[row][0].split(',')[0]), int(input_file[row][0].split(',')[1])
    input_file[row] = [ item for sublist in input_file[row] for item in sublist ]

# Put the data in LineSegment classes

list_of_linesegments = []

for row, _ in enumerate(input_file):
    list_of_linesegments.append(LineSegment(input_file[row][0],
                                            input_file[row][1],
                                            input_file[row][2],
                                            input_file[row][3]))
    list_of_linesegments[row].make_line()

# Prepare the list for part 1

part1_linesegments = []

for row, _ in enumerate(list_of_linesegments):
    if list_of_linesegments[row].part1 == True:
        part1_linesegments.append(list_of_linesegments[row])

# Create a grid and get to plotting

screen = Radar()

for row, _ in enumerate(part1_linesegments):
    for x_y, _ in enumerate(part1_linesegments[row].coordinates):
        screen.grid[part1_linesegments[row].coordinates[x_y][0]][part1_linesegments[row].coordinates[x_y][1]] += 1

crosses = 0

for row, _ in enumerate(screen.grid):
    for item, _ in enumerate(screen.grid[row]):
        if screen.grid[row][item] > 1:
            crosses += 1

print(crosses)

end = time.time()
print("Time elapsed:", end-start)