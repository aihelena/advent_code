puzzleInput=
total=0 #running total sum
strungInput=str(puzzleInput)#turns input into digits
listedInput=[int(x) for x in strungInput]

#split list of digits in half
firstHalf=listedInput[0:len(listedInput)/2]
secondHalf=listedInput[len(listedInput)/2:len(listedInput)]

#check each digit with corresponding one in second half
for i in range(0,len(listedInput)/2):
		if firstHalf[i]==secondHalf[i]:
				total+=firstHalf[i]*2
print total
