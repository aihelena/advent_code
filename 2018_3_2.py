#advent of code 2018, day 3, part 1


inputList = []
puzzleInput = open('2018_3.txt', 'r') #bring in input

for line in puzzleInput:
    inputList.append(str(line.strip())) #split into a list and strip spaces


#making a class for claims and their attributes

class Claim:
    def __init__(self, claim):
        claim = claim.split(' ')
        
        self.elf = claim[0][1:]
        self.x = int(claim[2][:-1].split(',')[0])
        self.y = int(claim[2][:-1].split(',')[1])
        self.width = int(claim[3].split('x')[0])
        self.height = int(claim[3].split('x')[1])
        
fabric = [[0 for x in range(1000)]for y in range(1000)]
listOfClaims = []
#for each claim in the list
for aClaim in inputList:
#make it an instance of a Claim
    #listofClaims.append(Claim(currentClaim))
    currentClaim = Claim(aClaim)
    #print(currentClaim.__dict__)
#for fabric column index starting at x and going until width
    for i in range (currentClaim.x,currentClaim.x+currentClaim.width):
#for fabric row index starting at y and going until height
        for j in range(currentClaim.y, currentClaim.y+currentClaim.height):
#if that array position exists
            if fabric[j][i]!=0:
#add 1
                if fabric[j][i]>=2:
                    pass
                else:
                    fabric[j][i]+=1
#else
            else:
#make that array position 1
                fabric[j][i]=1
#to find the one that doesn't overlap
#now that you have a mapped fabric,
                
for aClaim in inputList:
#make it an instance of a Claim
    #listofClaims.append(Claim(currentClaim))
    currentClaim = Claim(aClaim)
    status = True
    #print(currentClaim.__dict__)
#for fabric column index starting at x and going until width
    for i in range (currentClaim.x,currentClaim.x+currentClaim.width):
#for fabric row index starting at y and going until height
        for j in range(currentClaim.y, currentClaim.y+currentClaim.height):
#if any of the values in its area are not 1
            if fabric[j][i]!=1:
                #disqualify it
                status=False
#if, in the end, it's not disqualified yet, it's the one!
    if status:
        print(currentClaim.elf)
