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
        
        #CASE 1 total overlap: check for same length and same min
        if(rOne.length() == rTwo.length() and rOne.min == rTwo.min):
            totalOverlap += 1
    
        #CASE 2 one range of shorter length in the other
        if(rOne.length() < rTwo.length()):
            if(rTwo.min <= rOne.min and rTwo.max >= rOne.max):
                totalOverlap += 1

        elif(rOne.length() > rTwo.length()):
            if(rOne.min <= rTwo.min and rOne.max >= rTwo.max):
                totalOverlap += 1
                  
  
print("total overlap is ", totalOverlap)
            
