# file handling

from os import path

file_path = path.relpath("day_6/input6.txt")

fish_numbers = []

with open(file_path, "r") as filestream:
    for line in filestream:
        fish_numbers.append(line.split(","))

#print(fish_numbers)

# a fish class
class LanternFish():
    def __init__(self, day_count, is_new):
        self.day_count = day_count
        self.reproduce = False
        self.is_new = is_new
        
    def next_day(self):

        if self.day_count == 0:
           self.reproduce = True
           self.day_count = 6
        
        elif self.is_new:
            self.is_new = False
        
        else:
            self.reproduce = False
            self.day_count -= 1
   

#------------------part1-------------------

# not very efficient
def fish_swarm1(days):

    fish_list = []
    for number in fish_numbers[0]:
        fish_list.append(LanternFish(int(number), False))

    #print("Initial state: " + str(fish_list) + "\n")

    for _ in range(1, days + 1):
        for fish in fish_list:
            fish.next_day()
            if fish.reproduce:
                fish_list.append(LanternFish(8, True))
        
        nums = []
        for fish in fish_list:
            nums.append(fish.day_count)
        
        #print("After " + str(i) + " days: " + str(nums) + "\n")

    return len(fish_list)

print(fish_swarm1(80))

#------------------part2-------------------

# only keep track of the fish ages instead of counting the fish
def fish_swarm2(days):

    input = open(file_path).read()
    
    age_table = [input.count(str(i)) for i in range(0,9)]
    
    for _ in range(days):
        age_table = age_table[1:] + age_table[:1]
        age_table[6] += age_table[8]
    
    return sum(age_table)

print(fish_swarm2(256))