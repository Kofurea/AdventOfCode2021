# Part 1

with open('Day01_input.txt', 'r') as file:
    input_file = [int(line.strip()) for line in file]

increased = 0

for i in range(len(input_file)):
    if i != 0:
        if input_file[i-1] < input_file[i]:
            increased += 1

#print(increased)

# Part 2

increased_2 = 0

for i in range(len(input_file)-3):
    first = input_file[i]
    second =  input_file[i+3]
    if second > first:
        increased_2 += 1

print(increased_2)