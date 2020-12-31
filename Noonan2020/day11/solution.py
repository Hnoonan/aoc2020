inputFile = open('input.txt', 'r' )

seatMap = []
line = inputFile.readline()

while line:
    try:
        seatMap.append(list(line))
    except:
        pass
    
    line = inputFile.readline().rstrip()

#Indexes from 0
mapHeight = len(seatMap) -1
mapWidth = len(seatMap[0]) -1

def resetMap():
    yindex = 0
    xindex = 0
    while yindex <= mapHeight:
        while xindex < mapWidth:
            if seatMap[yindex][xindex] == '#' :
                seatMap[yindex][xindex] = 'L'
            xindex += 1
        yindex +=1
        xindex = 0

def part1():
    changed = -1 #unreachable val as placeholder
    while changed != 0 :
        changed = flipSeats(4,0)
        if (changed == 0) :
            totalSeats = 0
            for elem in seatMap:
                totalSeats += elem.count('#')
            return totalSeats

def part2():
    changed = -1
    while changed != 0 :
        changed = flipSeats(5,1)
        if (changed == 0) :
            totalSeats = 0
            for elem in seatMap:
                totalSeats += elem.count('#')
            return totalSeats

def flipSeats(threshold:int, mode:int):
    yindex = 0
    xindex = 0
    flipYs = []
    flipXs = []
    while yindex <= mapHeight:
        while xindex < mapWidth:
            cursor = seatMap[yindex][xindex]
            if(mode == 0):
                if( cursor == '#' and getAdj(xindex, yindex) >= threshold):
                    flipYs.append(yindex)
                    flipXs.append(xindex)
                elif( cursor == 'L' and getAdj(xindex, yindex) == 0):
                    flipYs.append(yindex)
                    flipXs.append(xindex)
            elif(mode == 1):
                if( cursor == '#' and getAdjExt(xindex, yindex) >= threshold):
                    flipYs.append(yindex)
                    flipXs.append(xindex)
                elif( cursor == 'L' and getAdjExt(xindex, yindex) == 0):
                    flipYs.append(yindex)
                    flipXs.append(xindex)
            xindex += 1
        xindex = 0
        yindex += 1
    
    #perform flips
    flipindex = 0
    changeCount = len(flipYs)
    while flipindex <  changeCount:
        cursor = seatMap[flipYs[flipindex]][flipXs[flipindex]]
        if(cursor == 'L'):
            seatMap[flipYs[flipindex]][flipXs[flipindex]] = '#'
        if(cursor == '#'):
            seatMap[flipYs[flipindex]][flipXs[flipindex]] = 'L'
        flipindex += 1
    return changeCount

def getAdj(x:int, y:int):
    adjacencies = []

    if(x-1 >= 0):
        adjacencies.append(seatMap[y][x-1])
    if(x+1 < mapWidth):
        adjacencies.append(seatMap[y][x+1])
    if(y-1 >= 0):
        adjacencies.append(seatMap[y-1][x])
    if(y+1 <= mapHeight):
        adjacencies.append(seatMap[y+1][x])
    if(x-1 >= 0 and y-1 >= 0):
        adjacencies.append(seatMap[y-1][x-1])
    if(x-1 >= 0 and y+1 <= mapHeight):
        adjacencies.append(seatMap[y+1][x-1])
    if(x+1 < mapWidth and y-1 >= 0):
        adjacencies.append(seatMap[y-1][x+1])
    if(x+1 < mapWidth and y+1 <= mapHeight):
        #print(y+1 , " || ", x+1)
        adjacencies.append(seatMap[y+1][x+1])
    return adjacencies.count('#')

def getAdjExt(x:int, y:int):
    adjacencies = []
    hits = ['#','L']
    matched = False
    scan = 1
    while not matched :
        if(x-scan < 0):
            #out of bounds
            adjacencies.append('.')
            matched = True
        elif(seatMap[y][x-scan] in hits):
            adjacencies.append(seatMap[y][x-scan])
            matched = True
        scan += 1
    matched = False
    scan = 1
    while not matched:
        if(x+scan >= mapWidth):
            adjacencies.append('.')
            matched = True
        elif(seatMap[y][x+scan] in hits):
            adjacencies.append(seatMap[y][x+scan])
            matched = True
        scan += 1
    matched = False
    scan = 1
    while not matched:
        if(y-scan < 0):
            adjacencies.append('.')
            matched = True
        elif(seatMap[y-scan][x] in hits):
            adjacencies.append(seatMap[y-scan][x])
            matched = True
        scan += 1
    matched = False
    scan = 1
    while not matched:
        if(y+scan > mapHeight):
            adjacencies.append('.')
            matched = True
        elif(seatMap[y+scan][x] in hits):
            adjacencies.append(seatMap[y+scan][x])
            matched = True
        scan += 1
    matched = False
    scan = 1
    while not matched:
        if((x-scan < 0) or (y-scan < 0)):
            adjacencies.append('.')
            matched = True
        elif(seatMap[y-scan][x-scan] in hits):
            adjacencies.append(seatMap[y-scan][x-scan])
            matched = True
        scan += 1
    matched = False
    scan = 1
    while not matched:
        if((x-scan < 0) or (y+scan > mapHeight)):
            adjacencies.append('.')
            matched = True
        elif(seatMap[y+scan][x-scan] in hits):
            adjacencies.append(seatMap[y+scan][x-scan])
            matched = True
        scan += 1
    matched = False
    scan = 1
    while not matched:
        if((x+scan >= mapWidth) or (y-scan < 0)):
            adjacencies.append('.')
            matched = True
        elif(seatMap[y-scan][x+scan] in hits):
            adjacencies.append(seatMap[y-scan][x+scan])
            matched = True
        scan += 1
    matched = False
    scan = 1
    while not matched:
        if((x+scan >= mapWidth) or (y+scan > mapHeight)):
            adjacencies.append('.')
            matched = True
        elif(seatMap[y+scan][x+scan] in hits):
            adjacencies.append(seatMap[y+scan][x+scan])
            matched = True
        scan += 1
    matched = False
    scan = 1
    return adjacencies.count('#')

print("After settling out, there are :", part1(), " occupied seats")
resetMap()
print("With new visibility rules, there are :", part2(), " occupied seats")

#flipSeats()
#for elem in seatMap:
#   print(elem)