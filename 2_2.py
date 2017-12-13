import numpy as np

inputArray = np.loadtxt('2_2_input.txt')

total=0
currentRow=0


for i in range(0,inputArray.shape[1]-1):
    checkingElement=inputArray[currentRow, i] #pulls elements of row in order
    for j in range(0, inputArray.shape[1]-1):
        compareElement=inputArray[currentRow, j]
        #print (checkingElement, compareElement)
        if (checkingElement%compareElement)==0 or (compareElement%checkingElement)== 0: #checks each element against other elements in row
            if j!=i:
                total+= max(checkingElement,compareElement)/min(checkingElement,compareElement)
                currentRow+=1
                print (currentRow)
                print (total)

