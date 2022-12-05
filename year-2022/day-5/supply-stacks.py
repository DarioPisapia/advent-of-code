stacks = [
    ["B", "W", "N"],
    ["L", "Z", "S", "P", "T", "D", "M", "B"],
    ["Q", "H", "Z", "W", "R"],
    ["W", "D", "V", "J", "Z", "R"],
    ["S", "H", "M", "B"],
    ["L", "G", "N", "J", "H", "V", "P", "B"],
    ["J", "Q", "Z", "F", "H", "D", "L", "S"],
    ["W", "F", "S", "J", "G", "Q", "B"],
    ["Z", "W", "M", "S", "C", "D", "J"]
    ]

def crane9000():
    with open('movements.txt') as movement_list:
        for movement_instruction in movement_list:
            movement = movement_instruction.strip().split(' ')

            n_crate = int(movement[1])
            from_stack = int(movement[3])-1
            to_stack = int(movement[5])-1

            while n_crate > 0:
                stacks[to_stack].append(stacks[from_stack][-1])
                stacks[from_stack].pop()
                n_crate -= 1

def crane9001():
     with open('movements.txt') as movement_list:
        for movement_instruction in movement_list:
            movement = movement_instruction.strip().split(' ')

            n_crate = int(movement[1])
            from_stack = int(movement[3])-1
            to_stack = int(movement[5])-1

            stacks[to_stack].extend(stacks[from_stack][-n_crate:])
            
            del stacks[from_stack][-n_crate:]

crane = ""      
while crane != "9000" and crane != "9001":
    crane = input("Write here which crane you are using (9000 or 9001):")
    if crane == "9000":
        crane9000()
    elif crane == "9001":
        crane9001()
    else:
        print("Giovane non fare il furbo! Scrivi il numero giusto")

top_crates = ""     
for stack in stacks:
    top_crates += stack[-1]

print(top_crates)