# advent of code 2018, day 4

from datetime import datetime

inputList = []
puzzleInput = open('2018_4.txt', 'r')  # bring in input

for eachLine in puzzleInput:
    inputList.append(str(eachLine.strip()))  # split into a list and strip spaces

dictofRecords = dict()

for line in inputList:
    # take out and parse the time
    onlyTime = datetime.strptime(line.split(']')[0][1:], "%Y-%m-%d %H:%M")  # notEnya
    # make the rest of it the record
    record = line.split('] ')[1]
    # create a dictionary entry with key time and value record
    dictofRecords[onlyTime]=record

allGuardTimes = dict()
sleepBegins = 0
sleepEnds = 0
isAsleep = False
#sort by time, and for each time:
for time in sorted(dictofRecords.keys()):
    # setting current record equal to value of the current time
    record = dictofRecords[time]
    if 'Guard' in record:
        if isAsleep:
            for i in range(sleepBegins,59):
                guardTime[i]=guardTime.get(i,0)+1
        #extract the number by splitting on the octothorpe and then the spaces
        guardNo = record.split('#')[1].split(' ')[0]

        if guardNo not in allGuardTimes:
            allGuardTimes[guardNo] = dict()
        guardTime = allGuardTimes[guardNo]
    if 'falls' in record:
        isAsleep = True
        sleepBegins = time.minute
    if 'wake' in record:
        isAsleep = False
        sleepEnds = time.minute
        #for the specific minute between begin and end of sleep
        for i in range(sleepBegins,sleepEnds):
            # add 1 to the value at the key of the specific minute, and make it 0 if it hasn't appeared yet
            guardTime[i] = guardTime.get(i,0)+1

topAsleepGuard = 0
topTimeSlept = 0
topMinSlept = 0
gdSleepyhead = 0
sleepyTimes = 0
sleepyheadMinute = 0

for Guard,times in allGuardTimes.items():
    minMostAsleep = -1
    for m,t in times.items():
        #track each guard's top slept minute
        if t > times.get(minMostAsleep,0):
            #print(m)
            minMostAsleep = m
    #print('Guard: {} total time sleep: {} most minute: {}'.format(Guard,sum(times.values()),minMostAsleep))
    #if this guard is the most minutes total slept so far, add their values to the leaderboard
    if sum(times.values())>topTimeSlept:
        topTimeSlept = sum(times.values())
        topAsleepGuard = Guard
        topMinSlept = minMostAsleep

    #ignore guards that don't fall asleep
    try:
        # find the guard that sleeps the most for any minute
        if sleepyTimes < max(times.values()):
            sleepyTimes = max(times.values())
            gdSleepyhead = Guard
            sleepyheadMinute = minMostAsleep
    except:
        pass
print('Guard: {} total time sleep: {} most minute: {}'.format(topAsleepGuard, topTimeSlept, topMinSlept))
print(int(topAsleepGuard)*int(topMinSlept))
print(int(gdSleepyhead)*int(sleepyheadMinute))
# currentRecord = Record(aRecord)
# sortedRecord = inputList.sort(key = lambda x:

# if the first word is guard
# make a list named the guard if it doesn't exist yet
# while the first word in the next line is wakes or falls
# if it's falls
# append the minutes between falls and the minutes on wake of the next line to the guard's list
# go to the next line

# Find the minute that appears most in each guard's list and add that as a dictionary entry under that guard's ID
# return the highest entry multiplied by that ID
