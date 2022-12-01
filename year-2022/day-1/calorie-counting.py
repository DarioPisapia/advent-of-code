
def calories ():
    sums = []
    tempsum = 0

    with open('counting.txt') as f:
        for line in f:
            l = line.strip()
            if l != "":
                tempsum += int(l)
            else:
                sums.append(tempsum)
                tempsum = 0
              
    sums.sort(reverse=True)
    best = sums[0]
    best3 = sums[0] + sums[1] + sums[2]
    print(f"The best elf (but we don't like elfs) is carrying: {best}\nThe sum of the best 3 (we like them even less) are: {best3}")
calories()