#advent of code 2018 day 1 part 2#


inputList = ['+3', '+3', '+4', '-2', '-4']
##puzzleInput = open('2018_1_1.txt', 'r')
##
##for line in puzzleInput:
##    inputList.append(str(line.strip()))
##    
#initiate current frequency#
    
currentFreq = 0
freqList = set([0])
duplicates = False

#while there are no duplicates
##Iterate over the list
##after each operation, append the new frequency
##and check if there's a duplicate in the list of frequencies

while duplicates == False:
    for i in range(0,len(inputList)):
        if inputList[i][0]== '+':
            currentFreq+=int(inputList[i][1:])
            if currentFreq in freqList:
                duplicates = True
                print (currentFreq)
            
        else:
            currentFreq-=int(inputList[i][1:])
            if currentFreq in freqList:
                duplicates = True
                print (currentFreq)

        freqList.add(currentFreq)


