inputFile = open('input.txt', 'r' )

line = inputFile.readline()
affirmatives = set([])
allAffirmatives = set([])
totalYes = 0
totalAllYes = 0
firstInBlock = 1

while line:
    try:
        if line == "\n" :
            totalYes += len(affirmatives)
            totalAllYes += len(allAffirmatives)
            affirmatives.clear()
            allAffirmatives.clear()
            firstInBlock = 1
        else :
            tokens = list(line.strip())
            for t in tokens:
                affirmatives.add(t)
            if(firstInBlock): #The base set from which we will remove answers not shared by other group members
                for t in tokens:
                    allAffirmatives.add(t)
            else :
                for ans in affirmatives:
                    if ans not in tokens:
                        allAffirmatives.discard(ans)
            firstInBlock = 0

    except:
        pass
    line = inputFile.readline()

totalYes += len(affirmatives) #last block
totalAllYes += len(allAffirmatives)

print("Total affirmative answers : ", totalYes)
print("Total affirmatives from all group members : ", totalAllYes)