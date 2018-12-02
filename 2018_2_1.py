#advent of code 2018, day 2, part 1

inputList = []
puzzleInput = open('2018_2_1.txt', 'r') #bring in input

for line in puzzleInput:
    inputList.append(str(line.strip())) #split into a list and strip spaces

#counters for 2 and 3
twoCount=0
threeCount=0


for i in range(0,len(inputList)): #for each item in the list
    currID=inputList[i]
    #and count the letters for each letters in the set
    letterCounts = dict((letter, currID.count(letter))for letter in set(currID))
        
#if counts include 2 and 3, they both get one
    if 2 in letterCounts.values() and 3 in letterCounts.values():
        twoCount+=1
        threeCount +=1
    #otherwise if it's 2 or 3, increase accordingly
    elif 2 in letterCounts.values():
        twoCount+=1
    elif 3 in letterCounts.values():
        threeCount+=1

print (twoCount*threeCount)
