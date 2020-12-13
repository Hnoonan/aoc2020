inputFile = open('input.txt', 'r' )

line = inputFile.readline().rstrip()
stringList = []

index = 0

while line:
    index += 1
    try:
        stringList.append(line)
        #print(line)
        line = inputFile.readline().rstrip()

    except Exception as e:
        print("AHHHHHHHH!  ",e, "  at ", index)
        pass

def treeHitter(xrate:int, yrate:int, map):
    width = len(map[0])
    xIndex = 0
    yAdvance = yrate #We always start on the first line
    xRate = xrate
    yRate = yrate
    trees = 0
    
    counter = 0
    for row in map:
        if(yAdvance == yRate):
            if(row[xIndex] == "#"):
                trees += 1
            xIndex = ((xIndex + xRate) % width)
            yAdvance = 1
        else:
            yAdvance += 1
    return trees

print("1-1 Hits " ,treeHitter(1,1,stringList) , " trees")
print("3-1 Hits " ,treeHitter(3,1,stringList) , " trees")
print("5-1 Hits " ,treeHitter(5,1,stringList) , " trees")
print("7-1 Hits " ,treeHitter(7,1,stringList) , " trees")
print("1-2 Hits " ,treeHitter(1,2,stringList) , " trees")

x = (treeHitter(1,1,stringList))
k = (treeHitter(3,1,stringList))
y = (treeHitter(5,1,stringList))
j = (treeHitter(7,1,stringList))
z = (treeHitter(1,2,stringList))

print(x*k*y*j*z)
