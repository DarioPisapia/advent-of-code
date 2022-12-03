
#create the value table
letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
value_temp = 1
value_table = {}
for letter in letters:
    value_table[letter] = value_temp
    value_temp += 1

#utilities temp variables
group_count = 0
group_pack = []

#results
sum1 = 0
sum2 = 0

with open('day-3.txt') as rucksacks:
    for rucks in rucksacks:
        ruck = rucks.strip()

        #firts part
        half = len(ruck)//2
        ruck1 = ruck[0:half]
        ruck2 = ruck[half:]
        for letter in ruck1:
            if letter in ruck2:
                sum1 += value_table[letter]
                break
        
        #second part  
        group_pack.append(ruck)
        group_count += 1
        if group_count == 3:
            for letter in group_pack[0]:
                if letter in group_pack[1] and letter in group_pack[2]:
                    sum2 += value_table[letter]
                    group_pack = []
                    group_count = 0
                    break
            
print(sum1, sum2)
