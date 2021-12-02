# file handling

from os import path

file_path = path.relpath("day_2/input2.txt")

file = open(file_path, 'r')
lines = file.readlines()

#------------------part1-------------------

horizontal = 0
depth = 0

for line in lines:
    splitted = line.split(" ")

    direction = splitted[0]
    amount = int(splitted[1].replace("\n", ""))

    if direction == "forward":
        horizontal += amount
    
    elif direction == "down":
        depth += amount
    
    elif direction == "up":
        depth -= amount

print(horizontal * depth)

#------------------part2-------------------

horizontal = 0
depth = 0
aim = 0

for line in lines:
    splitted = line.split(" ")

    direction = splitted[0]
    amount = int(splitted[1].replace("\n", ""))

    if direction == "forward":
        horizontal += amount
        depth += (aim*amount)
    
    elif direction == "down":
        aim += amount
    
    elif direction == "up":
        aim -= amount

print(horizontal * depth)


    