# file handling

from os import path
import numpy as np

file_path = path.relpath("day_8/example8.txt")

file = open(file_path, 'r')
lines = file.readlines()


#------------------part1-------------------

outputs = []

for line in lines:
    sp = line.split("|")
    outputs.append(sp[1].strip())

def count_unique(digit_list):

    unique_counter = 0

    for digits in digit_list:
        digit = digits.split(" ")

        for d in digit:
            if len(d) == 2 or len(d)== 3 or len(d) == 4 or len(d) == 7:
                unique_counter += 1
    
    return unique_counter

#print(count_unique(outputs))

#------------------part2-------------------

def arePermutation(str1, str2):
     
    # Get lengths of both strings
    n1 = len(str1)
    n2 = len(str2)
 
    # If length of both strings is not same,
    # then they cannot be Permutation
    if (n1 != n2):
        return False
 
    # Sort both strings
    a = sorted(str1)
    str1 = " ".join(a)
    b = sorted(str2)
    str2 = " ".join(b)
 
    # Compare sorted strings
    for i in range(0, n1, 1):
        if (str1[i] != str2[i]):
            return False
 
    return True

def remove_used(used, list):

    for ele in used:
            list.remove(ele)
    
    return list


def get_digits(input_list):

    for line in input_list:
        sp = line.split("|")
        input = sp[0].strip().split(" ")
        output = sp[1].strip().split(" ")

        str_1 = ""
        str_4 = ""
        str_7 = ""
        str_8 = ""
        str_9 = ""
        str_0 = ""

        for num in input:
            
            if len(num) == 2:
                str_1 = num
            elif len(num) == 3:
                str_7 = num
            elif len(num) == 4:
                str_4 = num
            elif len(num) == 7:
                str_8 = num


        to_remove = [str_1, str_4, str_7, str_8]
        rest = remove_used(to_remove, input)
       
            
        for n in rest:
            if len(n) == len(str_8)-1:
                for l in str_4:
                    if not l in n:
                        str_0 = n


        rest = remove_used([str_0], rest)
            
        for n in rest:
            if len(n) == len(str_8)-1:
                for l in str_1:
                    if not l in n:
                        str_9 = n
        
        rest = remove_used([str_9], rest)

        print(rest)  
            
get_digits(lines)

                


