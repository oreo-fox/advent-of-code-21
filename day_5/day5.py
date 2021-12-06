# file handling

from os import path
import numpy as np

file_path = path.relpath("day_5/example.txt")

file = open(file_path, 'r')
lines = file.readlines()

#------------------part1-------------------



matrix = np.zeros((1000,1000))

for line in lines:
    split = line.split("->")
    xy1 = split[0].split(",")
    xy2 = split[1].split(",")

    x1 = int(xy1[0])
    y1 = int(xy1[1])

    x2 = int(xy2[0])
    y2 = int(xy2[1])

    #print(str(x1) + " " + str(y1))
    #print(str(x2) + " " + str(y2))

    if x1 == x2:
        if y1 > y2:
            for i in range(y2,y1 + 1):
                matrix[i][x1] += 1
        
        elif y1 < y2:
            for i in range(y1,y2 + 1):
                matrix[i][x1] += 1
        else:
            matrix[y1][x1] += 1

    elif y1 == y2:
        if x1 > x2:
            for i in range(x2,x1 + 1):
                matrix[y1][i] += 1
        
        elif x1 < x2:
            for i in range(x1,x2 + 1):
                matrix[y1][i] += 1
        else:
            matrix[y1][x1] += 1

#print (matrix)

counter = 0

for x in matrix:
  for y in x:
    if y > 1:
        counter += 1

print(counter)


#------------------part2-------------------
#TODO Fix part2

"""

matrix2 = np.zeros((10,10))

for line in lines:
    split = line.split("->")
    xy1 = split[0].split(",")
    xy2 = split[1].split(",")

    x1 = int(xy1[0])
    y1 = int(xy1[1])

    x2 = int(xy2[0])
    y2 = int(xy2[1])

    if x1 == x2:
        if y1 > y2:
            for i in range(y2,y1 + 1):
                matrix2[i][x1] += 1
        
        elif y1 < y2:
            for i in range(y1,y2 + 1):
                matrix2[i][x1] += 1
        else:
            matrix2[y1][x1] += 1
    
    elif y1 == y2:
        if x1 > x2:
            for i in range(x2,x1 + 1):
                matrix2[y1][i] += 1
        
        elif x1 < x2:
            for i in range(x1,x2 + 1):
                matrix2[y1][i] += 1
        else:
            matrix2[y1][x1] += 1
    
   

print (matrix2)

"""