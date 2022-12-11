import re

n_monkey = 0
monkeys = []

#creating the array on initial monkeys from the file given
with open('./year-2022/day-11/monkeys.txt') as file:
    file_lines = file.readlines()
    
    for ln in file_lines:
        line = ln
        line = re.sub('[:,=]','',line)
        line = line.strip().split()
        
        if line == [] : continue
        
        if line[0] == 'Monkey':
            n_monkey = int(line[1])
            monkeys.append(
                {
                    'items': [],
                    'operation': [],
                    'test': 0,
                    'action': [0, 0],
                    'inspected_items': 0
                }
            )
        
        if line[0] == 'Starting':
            for n in line[2:]:
                monkeys[n_monkey]['items'].append(int(n))
             
        if line[0] == 'Operation': 
            for op in line[2:]:
                monkeys[n_monkey]['operation'].append(op)  

        if line[0] == 'Test': monkeys[n_monkey]['test'] = int(line[-1])

        if line[1] == 'true': monkeys[n_monkey]['action'][0] = int(line[-1])
        
        if line[1] == 'false': monkeys[n_monkey]['action'][1] = int(line[-1])


for rounds in range(1000):
    for n in range(0, 8):
        test_true_target = monkeys[n]['action'][0] 
        test_false_target = monkeys[n]['action'][1]
        nu = len(monkeys[n]['items'])

        monkeys[n]['inspected_items'] += nu
        operator = monkeys[n]['operation'][1]
        for num in range(nu):
            item = monkeys[n]['items'][-1]
            #operator = monkeys[n]['operation'][1]
            item2= item if monkeys[n]['operation'][-1] == 'old' else int(monkeys[n]['operation'][-1])

            worry_level = item+item2 if operator=='+' else item*item2
            
            if worry_level%monkeys[n]['test'] == 0:
                monkeys[test_true_target]['items'].append(worry_level)
            else:
                monkeys[test_false_target]['items'].append(worry_level)
            
            #monkeys[n]['inspected_items'] += 1
            monkeys[n]['items'].pop()


inspections = []
for n in range(len(monkeys)):
    inspections.append(monkeys[n]['inspected_items'])

inspections.sort(reverse=True)

print(inspections[0]*inspections[1])