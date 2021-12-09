# file handling

from functools import total_ordering
from os import path, replace
import numpy as np
from collections import deque

file_path = path.relpath("day_9/input9.txt")

file = open(file_path, 'r')
lines = file.readlines()

numbers = []
for line in lines:
    numbers.append(line.replace("\n", ""))
    
#------------------part1-------------------
num_rows = len(numbers)
num_cols = len(numbers[0])

matrix = np.zeros((num_rows, num_cols))

for i, line in enumerate(numbers):
    for j, digit in enumerate(line):
        matrix[i][j] = digit

low_points = []
low_point_cooridnates = []

for i in range(num_rows):
    for j in range(num_cols):

        element = matrix[i][j]

        neighbours = []

        if j != 0:
            neighbours.append(matrix[i][j-1])
        if j != (num_cols -1):
            neighbours.append(matrix[i][j+1])
        if i != 0:
            neighbours.append(matrix[i-1][j])
        if i != (num_rows -1):
            neighbours.append(matrix[i+1][j])
        
        if all(i > element for i in neighbours):
            low_points.append(int(element))
            low_point_cooridnates.append((i,j))

total = 0
for point in low_points:
    total += (point + 1)

#print(total)
print(low_point_cooridnates)

#------------------part2-------------------

move_row = [0, 0, -1, 1]
move_col = [-1, 1, 0, 0]

def can_fill(matrix, row, col):

    return 0 <= row < num_rows and 0 <= col < num_cols and matrix[row][col] < 9

def flood_fill(matrix, row, col, replacement):

    queue = deque()
    queue.append((row, col))

    if matrix[row][col] == replacement:
        return

    while queue:
        i, j = queue.popleft()
        matrix[i][j] = replacement

        for k in range(len(move_row)):
            if can_fill(matrix, i + move_row[k], j + move_col[k]):
                queue.append((i + move_row[k], j + move_col[k]))
    

bassins = []
replacement = 11
replacements = []

for point in low_point_cooridnates:
    flood_fill(matrix, point[0], point[1], replacement)
    print(matrix)
    print("\n")

    replacements.append(replacement)
    replacement += 11

for r in replacements:
    occurrences = np.count_nonzero(matrix == r)
    bassins.append(occurrences)

descending = sorted(bassins, reverse=True)

bassin_sum = descending[0] * descending[1] * descending[2]

print(bassin_sum)


    




    

    

        