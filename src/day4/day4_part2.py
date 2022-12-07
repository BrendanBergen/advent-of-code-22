class Range:
    def __init__(self, stringRange):
        self.min, self.max = stringRange.rsplit("-")
        self.min = int(self.min)
        self.max = int(self.max)

    def length(self):
        return (self.max - self.min)

groups = []
totalOverlap = 0

#read the file 
with open('input.txt','r') as f:
    for line in f:
        firstPart, secondPart = line.rsplit(",")
        secondPart = secondPart.rstrip()
      
        rOne = Range(firstPart)
        rTwo = Range(secondPart)

        #find the cases that do not overlap
        if(rOne.min < rTwo.min and rOne.max < rTwo.min):
            totalOverlap += 0
        elif(rOne.min > rTwo.max and rOne.max > rTwo.max):
            totalOverlap += 0
        else:
            totalOverlap += 1
                  
  
print("total overlap is ", totalOverlap)
            
