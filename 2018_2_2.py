#advent of code 2018, day 2, part 2

inputList = []
puzzleInput = open('2018_2_1.txt', 'r') #bring in input

for line in puzzleInput:
    inputList.append(str(line.strip())) #split into a list and strip spaces


#i want to see how many characters differ between the current string
#and every other string

for currID in inputList: #for each item in the list
#compare it to every other item on the list
    for compareID in inputList:
        #string of common characters
        currentContender = ''
    #for every row of the two lists zip together:
        for currentLetter,compareLetter in zip(currID, compareID):
            if currentLetter==compareLetter:
    #append it to currentContender
                currentContender = currentContender+currentLetter
    #once you're done making currentContender, find the ones that are one off
        if len(currentContender)==len(currID)-1:
            print(currentContender)
        
      
#return leaderBoard
