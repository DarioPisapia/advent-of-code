with open('./year-2022/day-7/system.txt') as commandfile:
    commands = commandfile.readlines()

    tree ={'start':0}
    current = 'start'
    path=['start']
    folders = ['start']

    for command in commands:
        com = command.strip().split(" ")

        if com[1]=='cd' and com[2] == '/':
            path=['start']
            current='start'
        if com[1]=='cd' and com[2]=='..':
            if len(path) == 2:
                path.pop()
                current='start'
            if len(path) == 1:
                current='start'
            else:
                path.pop()
                current=path[-1]
        
        if com[1]=='cd' and com[2]!='..' and com[2]!='/':
            current += com[2]
            path.append(current)
         

        if com[0]=='dir':
            word = current+com[1]
            tree[word]=0
            folders.append(word)
        if com[0].isdigit():
            tree[com[1]]=0
            for key in path:
                tree[key] += int(com[0])

sum = 0
for folder in folders:
    if tree[folder] < 100000:
        sum += tree[folder]

#second part
space_to_clean = tree['start'] - 40000000 

sorted_tree = sorted(tree.items(), key=lambda x:x[1])

minimum_folder_to_remove = 0

for n in sorted_tree:
    if tree[n[0]] > space_to_clean:
        minimum_folder_to_remove += tree[n[0]]
        break
    
print(sum, minimum_folder_to_remove)
 
