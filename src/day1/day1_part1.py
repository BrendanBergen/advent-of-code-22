maxElf = 0
currentElf = 0

with open('input.txt','r') as f:
    for line in f:
      #  print(line,end='')
        if line == '\n':
            print('new elf')
            if currentElf > maxElf:
      #          print('new max elf! ', currentElf)
                maxElf = currentElf
            currentElf = 0
        else:
            currentElf += int(line)

print("Max elf is ", maxElf)
            
            
    
