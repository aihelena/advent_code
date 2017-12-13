puzzleInput=

total=0 #running total of sums

strungInput=str(puzzleInput) #splits input into digits
listedInput=[int(x) for x in strungInput] #adds digits to a list

previousDigit=listedInput[-1] #populates last digit first
currentDigit=listedInput[0]

if currentDigit==previousDigit: #checks first and last digits
		total+=currentDigit
		previousDigit=currentDigit
else:
    	previousDigit=currentDigit
    	
for i in range(1,len(listedInput)): #checks subsequent digit against previous
		currentDigit=listedInput[i]
		if currentDigit==previousDigit:
				total+=currentDigit
				previousDigit=currentDigit
		else: 
				previousDigit=currentDigit
print total
