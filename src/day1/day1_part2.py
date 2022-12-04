elves = []
currentElf = 0

with open('input.txt','r') as f:
    for line in f:
        if line == '\n':
            elves.append(currentElf)
            currentElf = 0
            
        else:
            currentElf += int(line)
            
elves.sort(reverse=True)

print("Max elf is ", elves[0])
print("Next elf is ", elves[1])
print("Third elf is ", elves[2])

totalCal = elves[0] + elves[1] + elves[2]

print ("Total is ", totalCal)

            
            
    
