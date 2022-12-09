with open('./year-2022/day-9/steps.txt') as steps_file:
    steps_line = steps_file.readlines()

    positions = []
    rope = [[0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0]]
    for line in steps_line:
        
        steps = line.strip().split(' ')
        
        #head_movements
        for step in range(0, int(steps[1])):
            if steps[0] == 'R':
                    rope[0][0] += 1
            if steps[0] == 'L':
                    rope[0][0] -= 1
            if steps[0] == 'U':
                    rope[0][1] += 1
            if steps[0] == 'D':
                    rope[0][1] -= 1

            for n in range(0, len(rope)-1):
                #same y
                if rope[n][1] == rope[n+1][1]:
                    if abs(rope[n][0] - rope[n+1][0]) > 1:
                        if rope[n][0] > rope[n+1][0]:
                            rope[n+1][0] +=1
                        else:
                            rope[n+1][0] -=1
              
                #same x (write in different way, but like same y)
                if rope[n][0] == rope[n+1][0]:
                    if rope[n][1] - rope[n+1][1] > 1:
                        rope[n+1][1] +=1
                    if rope[n][1] - rope[n+1][1] < -1:
                        rope[n+1][1] -=1
                
                #both different
                if rope[n][1] != rope[n+1][1] and rope[n][0] != rope[n+1][0]:
                    if abs(rope[n][0] - rope[n+1][0]) > 1  or abs(rope[n][1] - rope[n+1][1]) > 1:
                        #x movement
                        rope[n+1][0] = rope[n+1][0]+1 if rope[n][0] > rope[n+1][0] else rope[n+1][0]-1
                        #y movement
                        rope[n+1][1] = rope[n+1][1] + 1 if rope[n][1] > rope[n+1][1] else rope[n+1][1]-1
                  
            nex = str(rope[9][0])
            ney = str(rope[9][1])
            nep = nex+", "+ ney
            if nep not in positions:
                positions.append(nep) 
       
    print(len(positions))