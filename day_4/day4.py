# file handling

from os import path

file_path_nums = path.relpath("day_4/input4_2.txt")
file_path_bingo = path.relpath("day_4/input4_1.txt")

file_nums = open(file_path_nums, 'r')
lines = file_nums.readlines()

numbers = lines[0].split(",")
numbers = list(map(int, numbers))
numbers2 = numbers

file_bingo = open(file_path_bingo, 'r')
lines = file_bingo.readlines()

# make the bingo cards

class BingoCard():
    
    def __init__(self, number_rows):
        self.number_rows = number_rows
        self.marked = []
        self.has_bingo = False

        
    def mark_number(self, number):
        for row in self.number_rows:
            if number in row:
                self.marked.append(number)
    
    def rows_to_cols(self):
        return list(map(list, zip(*self.number_rows)))
             
    def check_bingo(self):
        for row in self.number_rows:
            bingo = all(item in self.marked for item in row)

            if bingo:
                return True   
        
        cols = self.rows_to_cols()

        for row in cols:
            bingo = all(item in self.marked for item in row)

            if bingo:
                return True  
        
        return False
   
    def calc_sum(self):
        sum = 0
        for row in self.number_rows:
            for num in row:
                if not num in self.marked:
                    sum += num
        
        return sum
        
# break list into smaller lists
def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

lines = [value for value in lines if value != "\n"]

card_list = list(chunks(lines, 5))

bingo_cards = []

for entry in card_list:
    card_lines = []
    
    for line in entry:
        l = line.replace("\n", "")
        split = l.split(" ")
        card_line = []

        for num in split:
            if num != "":
                card_line.append(int(num))
        
        card_lines.append(card_line)
    
    card = BingoCard(card_lines)
    bingo_cards.append(card)

bingo_cards2 = bingo_cards

#------------------part1-------------------

def play_bingo():
    for number in numbers:
        for card in bingo_cards:
            card.mark_number(number)
            bingo = card.check_bingo()

            if bingo:
                return (card.calc_sum()) * number

print(play_bingo())
                
#------------------part2-------------------

def last_bingo():
    last_bingo = None
    last_number = None

    for number in numbers2:
         for card in bingo_cards2:
            
            if not card.has_bingo:
                card.mark_number(number)
            bingo = card.check_bingo()

            if bingo and not card.has_bingo:
                last_bingo = card
                card.has_bingo = True
                last_number = number

    return (last_bingo.calc_sum()) * last_number

print(last_bingo())


    

        




    


        
