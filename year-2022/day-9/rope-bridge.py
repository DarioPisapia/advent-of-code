with open('./year-2022/day-9/steps.txt') as steps_file:
    steps_line = steps_file.readlines()

    positions = []
    tail = [0, 0]
    head = [0, 0]
    pl = []


    for line in steps_line:
        
        steps = line.strip().split(' ')
        
        #head_movements
        for step in range(0, int(steps[1])):
            if steps[0] == 'R':
                head[0] += 1
                #check tail and eventual movement
                if head[0] - tail[0] > 1 or head[0] - tail[0] < -1:
                    tail[0] += 1
                    if head[1] != tail[1]:
                        tail[1] = head[1]

            if steps[0] == 'L':
                head[0] -= 1
                #check tail and eventual movement
                if head[0] - tail[0] > 1 or head[0] - tail[0] < - 1 :
                    tail[0] -= 1
                    if head[1] != tail[1]:
                        tail[1] = head[1]
                   
            if steps[0] == 'U':
                head[1] += 1
                #check tail and eventual movement
                if head[1] - tail[1] > 1 or head[1] - tail[1] < -1:
                    tail[1] += 1
                    if head[0] != tail[0]:
                        tail[0] = head[0]

            if steps[0] == 'D':
                head[1] -= 1
                #check tail and eventual movement
                if head[1] - tail[1] > 1 or head[1] - tail[1] < -1:
                    tail[1] -= 1
                    if head[0] != tail[0]:
                        tail[0] = head[0]

            nx = str(tail[0])
            ny = str(tail[1])
            np = nx+" "+ ny
            if np not in pl:
                pl.append(np)  

            
   
    print(len(pl))