
def mannaggiaglielfi(num):
    with open('./year-2022/day-6/signal.txt') as signal_file:
        signal = signal_file.readline()

        char_4 = []
        char_count = 0
        for char in signal:
            if char_count < num:
                char_4.append(char)
                char_count += 1
            else:
                char_count += 1
                char_4.append(char)
                char_4.pop(0)
                compare_set = set(char_4)    
                if len(char_4) == len(compare_set):
                    print(char_4, compare_set)
                    return char_count
               
print(f"The first packet starts at {mannaggiaglielfi(4)}, the first message starts at {mannaggiaglielfi(14)} ")
