# file handling

from os import path

file_path = path.relpath("day_3/input3.txt")

file = open(file_path, 'r')
lines = file.readlines()

bits = []

for line in lines:
    bits.append(line.replace("\n", ""))


#------------------part1-------------------


counts = [0] * len(bits[0])

for b in bits:
    for i in range(len(b)):
        if b[i] == '1':
            counts[i] += 1

    gamma = "".join(('1' if v > len(bits) / 2 else '0') for v in counts)
    epsilon = "".join(('0' if v > len(bits) / 2 else '1') for v in counts)

print(int(gamma,2) * int(epsilon,2))

    
#------------------part2-------------------

def part2(list, counter, is_most):
    idx1 = []
    idx0 = []

    for i, b in enumerate(list):
        if b[counter] == '1':
            idx1.append(i)
        else:
            idx0.append(i)
    
    print(idx1)
    
    if is_most:
        if len(idx1) < len(idx0):
            for i in reversed(idx1):
                del list[i]

        else:
            for i in reversed(idx0):
                del list[i]
    
    else:
        if len(idx1) < len(idx0):
            for i in reversed(idx0):
                del list[i]
        
        else:
            for i in reversed(idx1):
                del list[i]
    
    return list


oxygen_generator = bits.copy()
co2 = bits.copy()

for i in range(len(bits[0])):

    if len(oxygen_generator) == 1:
        break

    oxygen_generator = part2(oxygen_generator, i, True)


for i in range(len(bits[0])):

    if len(co2) == 1:
        break

    co2 = part2(co2, i, False)
    
    
print(int(oxygen_generator[0],2) * int(co2[0],2))
