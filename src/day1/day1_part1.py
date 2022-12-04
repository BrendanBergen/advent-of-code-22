maxElf = 0
currentElf = 0

with open('input.txt','r') as f:
    for line in f:
        if line == '\n':
            if currentElf > maxElf:
                maxElf = currentElf
            currentElf = 0
        else:
            currentElf += int(line)

print("Max elf is ", maxElf)
            
            
    
