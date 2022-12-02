def first_part ():

    with open('strategy.txt') as strategy:
   
        total_points = 0
        
        for line in strategy:
            round = line.strip()
            if round[2] == 'X':
                total_points += 1
                if round[0] == "A":
                    total_points += 3
                if round[0] == "C":
                    total_points += 6
            
            if round[2] == 'Y':
                total_points += 2
                if round[0] == "B":
                    total_points += 3
                if round[0] == "A":
                    total_points += 6

            if round[2] == 'Z':
                total_points += 3
                if round[0] == "C":
                    total_points += 3
                if round[0] == "B":
                    total_points += 6

        print(total_points)

def second_part():
     with open('strategy.txt') as strategy:
        total_points = 0
        
        for line in strategy:
            round = line.strip()

            if round[0] == "A":
                if round[2] == "X":
                    total_points += 3
                if round[2] == "Y":
                    total_points += 4
                if round[2] == "Z":
                    total_points += 8
            
            if round[0] == "B":
                if round[2] == "X":
                    total_points += 1
                if round[2] == "Y":
                    total_points += 5
                if round[2] == "Z":
                    total_points += 9
            
            if round[0] == "C":
                if round[2] == "X":
                    total_points += 2
                if round[2] == "Y":
                    total_points += 6
                if round[2] == "Z":
                    total_points += 7
                    
        print(total_points)

first_part()
second_part()
