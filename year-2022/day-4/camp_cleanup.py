with open("ids.txt") as id_list:
    
    complete_overlapped = 0
    partially_overlapped = 0
   
    for id_line in id_list:
        row_instruction = id_line.strip().split(",") 

        instruction1 = row_instruction[0].split("-")
        instruction2 = row_instruction[1].split("-")

        ids1 = []
        ids2 = []

        for number in range(int(instruction1[0]), int(instruction1[1])+1):
            ids1.append(number)
            
        for number in range(int(instruction2[0]), int(instruction2[1])+1):
            ids2.append(number)
        
        if all(number in ids1 for number in ids2) or all(number in ids2 for number in ids1):
            complete_overlapped += 1
        
        if any(number in ids1 for number in ids2) or all(number in ids2 for number in ids1):
            partially_overlapped += 1
        
    print(complete_overlapped, partially_overlapped)    
