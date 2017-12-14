import numpy as np

puzzleInput=347991

spiralLayer=1
smallerSquare=1

#find the largest squared odd number within puzzle input
while smallerSquare**2 <puzzleInput:
    smallerSquare+=2
    spiralLayer+=1
sideLength=smallerSquare-1 #length of sides on current layer
smallerSquare-=2
#print (smallerSquare)
#print ("spirallayer=", spiralLayer)

#find wrap distance
inputWrap=puzzleInput-smallerSquare**2
#print("sideLength=", sideLength)
#print("inputWrap=", inputWrap)

#if input is at the middle of a side, that's the shortest path
if inputWrap==sideLength/2:
    pathDistance=spiralLayer-1
#otherwise, distance along a side
#from that shortest path determines final distance    
else:
    distancefromCenter=abs((inputWrap%sideLength)-sideLength/2)
    #print("DistancefromCenter=", distancefromCenter)
    pathDistance=(spiralLayer-1)+distancefromCenter

print (pathDistance)
