
with open('./year-2022/day-8/tree-grid.txt') as grid_file:
    grid_lines = grid_file.readlines()
    
    matrix = []
    visible = 0
    score = 0

    #creates a list of lists (lines)
    for tree_line in grid_lines:
        trees = tree_line.strip()
        line = list(trees)
        lnum = []
        for n in line:
            lnum.append(int(n))
        matrix.append(lnum)
    
    #creates a list of lists (columns)
    columns = []
    for n in range(0, len(matrix[0])):
        col = []
        for line in matrix:
            col.append(int(line[n]))
        columns.append(col)
    
    #main cycle
    for l in range(1, len(matrix)-1):
        line = matrix[l]
        index = matrix.index(line)
        
        for tree in range(1, len(line)-1): 
            
            #the tree
            tr = line[tree] 

            #building the lists of tree in the four directions
            left = []
            right = []
            for n in range(0, tree):
                left.append(line[n])
            for n2 in range(tree+1, len(line)):
                right.append(line[n2])
            top = []
            bottom= []
            for n in range(0, index):
                top.append(columns[tree][n])
            for n in range(index+1, len(matrix)):
                bottom.append(columns[tree][n]) 

            t = max(top)      
            b = max(bottom)
            l = max(left)
            r = max(right)
        
            if tr > l or tr > r or tr > t or tr > b:
                visible += 1

            #second part
            top.reverse()     
            left.reverse()
            
            tv = 0
            bv = 0
            lv = 0
            rv = 0

            for tree in top:
                tv += 1
                if tree >= tr:
                    break
            for tree in bottom:
                bv += 1
                if tree >= tr:
                    break
            for tree in left:
                lv += 1
                if tree >= tr:
                    break
            for tree in right:
                rv += 1
                if tree >= tr:
                    break

            result = tv*bv*lv*rv
            if result > score:
                score = result           
    print(visible+99+99+97+97, score)
