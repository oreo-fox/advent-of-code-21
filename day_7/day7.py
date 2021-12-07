# file handling
from os import path

file_path = path.relpath("day_7/input7.txt")

positions = []

with open(file_path, "r") as filestream:
    for line in filestream:
        positions.append(line.split(","))

positions = list(map(int,positions[0]))

#------------------part1-------------------

def fuel1(list):
    distances = []

    for pos in list:
        distance = 0
        for other_pos in list:
            d = pos - other_pos
            distance += abs(d)
        
        distances.append(distance)

    print(min(distances))

#fuel1(positions)

#------------------part2-------------------

# very unefficient, takes like 30 seconds to calculate but whatever...

def fuel2(crab_list):

    distances = []

    for pos in range(min(crab_list), max(crab_list)):
        distance = 0
        for other_pos in crab_list:
            d = abs(pos - other_pos) + 1

            add_fuel = 0
            if d > 1:
                for i in range(d):
                    add_fuel += i

            distance += add_fuel

        distances.append(distance)

    print(min(distances))

fuel2(positions)