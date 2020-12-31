inputFile = open('input.txt', 'r' )

allInts = []

line = inputFile.readline()

while line:
    try:
        allInts.append(int(line))
    except:
        pass
    
    line = inputFile.readline().rstrip()

def findInvalid(intList) :
    intWindow = intList[0:25]
    index = 25
    while index < len(intList):
        valid = 0
        cursor = intList[index]
        for i in intWindow :
            if (cursor - i) in intWindow:
                valid = 1
                intWindow.append(cursor)
                del intWindow[0]
                break #no need to finish this loop
        if not valid :
            return cursor, index
        else :
            index += 1
    return -1, -1

def findWeakness(intList, target):
    contiguous = []
    index = 0
    while index < len(intList):
        cursor = intList[index]
        contiguous.append(cursor)
        
        while sum(contiguous) > target :
            del contiguous[0]

        if sum(contiguous) == target :
            #print(contiguous)
            #print(contiguous[-1])
            #print(target)
            #print(sum(contiguous))
            return (min(contiguous) + max(contiguous))
        index += 1

    return -1 #something when wrong

inv, ind = findInvalid(allInts)

print("The first invalid entry in the list is ", inv, " occuring at ", ind)
print("The encryption weakness is ", findWeakness(allInts, inv))