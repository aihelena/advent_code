import numpy as np

inputArray = np.loadtxt('2_2_input.txt')

total=0 #running sum of quotients
currentRow=0

while currentRow < inputArray.shape[0]: #for each row in the array
    for i in range(0,inputArray.shape[1]):
        sortedRow= sorted(inputArray[currentRow], reverse=True)
        checkingElement=sortedRow[i] #pulls elements of row in decreasing order
        for j in range(1, inputArray.shape[1]):
            compareElement=sortedRow[j]
            if (checkingElement%compareElement)==0: #checks each element against other elements in row
                if j!=i: #not dividing something by itself
                    total+= checkingElement/compareElement
                    currentRow+=1
                    print (currentRow)
                    print (total)
                

