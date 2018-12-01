#advent of code 2018 day 1#

inputList = []
puzzleInput = open('2018_1_1.txt', 'r')

for line in puzzleInput:
    inputList.append(str(line.strip()))
    
#initiate current frequency#
    
currentFreq = 0

##for every item in the list length
##see if it's positive
##    add everything after the first character to puzzle input
##    else
##    subtract everything after the first character from puzzle input
##
##    return current frequency

for i in range(0,len(inputList)):
    if inputList[i][0]== '+':
        currentFreq+=int(inputList[i][1:])
    else:
        currentFreq-=int(inputList[i][1:])

print (currentFreq)
