#COLUMN 1: A for Rock, B for Paper, and C for Scissors
#COLUMN 2: X for Rock, Y for Paper, and Z for Scissors
#RULES: Rock > Scissor, Scissor > Paper, Paper > Rock
#SCORING: Rock = 1, Paper = 2, Scissor = 3, Loss = 0, Tie = 3, Win = 6

#function to calculate round outcome
def calcOutcome(oppPlay,youPlay):
    if(oppPlay == youPlay):
        return 'T'
    if(oppPlay == 'A' and youPlay == 'C'):
        return 'L'
    if(oppPlay == 'B' and youPlay == 'A'):
        return 'L'
    if(oppPlay == 'C' and youPlay == 'B'):
        return 'L'
    else:
        return 'W'
       
#function to calculate round score
def calcScore(outcome,eventType):
    totalScore = 0
    if(outcome == 'W'):
        totalScore = 6
    elif(outcome == 'T'):
        totalScore = 3

    if(eventType == 'A'): #Rock
        totalScore += 1
    elif(eventType == 'B'): #Paper
        totalScore += 2
    else: #Scissors
        totalScore += 3

    return totalScore


rounds = []
totalScore = 0

#read the file into a list of lists
with open('input.txt','r') as f:
    for line in f:
            if(line[2] == 'X'):
                rounds.append([line[0],'A'])
            elif(line[2] == 'Y'):
                rounds.append([line[0],'B'])
            else:
                rounds.append([line[0],'C'])

for r in rounds:
    outCome = calcOutcome(r[0],r[1])
  #  print("Round ",r," outcome is ", outCome)
    score = calcScore(outCome,r[1])
  #  print("Round score is ", score)
    totalScore += score
   
print("Total score is ", totalScore)   
