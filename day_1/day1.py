# file handling

from os import path

file_path = path.relpath("day_1/day1_input1.txt")

file = open(file_path, 'r')
lines = file.readlines()

numbers = []

for line in lines:
    num = line.replace("\n", "")
    num = int(num)
    numbers.append(num)

#------------------part1-------------------

increased = 0

for idx, number in enumerate(numbers):
    if idx == 0:
        continue

    elif number > numbers[idx - 1]:
        increased += 1

print(increased)

#------------------part2-------------------

window_prev = 0
inc_counter = 0

for i in range(len(numbers)-2):
    
    window = numbers[i] + numbers[i + 1] + numbers[i + 2]
    
    if i == 0:
        pass

    elif window > window_prev:
        inc_counter += 1
    
    window_prev = window

print(inc_counter)
