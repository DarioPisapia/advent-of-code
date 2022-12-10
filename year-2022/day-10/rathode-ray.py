cycle = 1
X = 1
strength = 0

display = ""
crt = 0

def check_cycle():
    global strength
    if (cycle-20)%40 == 0 and cycle < 221:
        strength += cycle*X

def draw_display():
    global display
    global crt
    global X
    if crt in range(X-1, X+2):
        display += "#"
    else:
        display += "."
    if crt%40 == 0:
        display += "\n"
        crt = 0
        
with open('./year-2022/day-10/commands.txt') as commands_file:
    commands = commands_file.readlines()
    
    for line in commands:
        command = line.strip().split(" ")
        
        if command[0] == "noop":
            check_cycle()
            draw_display()
            cycle += 1
            crt += 1
        
        if command[0] == 'addx':
            check_cycle()
            draw_display()
            cycle += 1
            crt += 1
            check_cycle()
            draw_display()
            cycle += 1
            crt += 1
            X += int(command[1])

print(strength)
print(display)
