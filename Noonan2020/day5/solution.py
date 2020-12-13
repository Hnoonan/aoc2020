inputFile = open('input.txt', 'r' )

line = inputFile.readline()
#line = "BBFFFFBRLL"
maxSeatID = 0
seatIDs = []

while line:
    try:
        row = 0
        col = 0

        cursorIndex = 0
        minRow = 0
        maxRow = 127
        while cursorIndex < 7: #first 7 chars determine row
            if(line[cursorIndex] == "F"):
                maxRow = (maxRow - (int(((maxRow-minRow) / 2)+.9))) ##Round up to carve out
            elif(line[cursorIndex] == "B"):
                minRow = (minRow + (int(((maxRow-minRow) / 2.0)+.9))) ##Round up to carve out
            cursorIndex += 1
        if(minRow == maxRow):
            row = minRow
        else :
            print("Something went wrong getting the row for ", line)
        
        minCol = 0
        maxCol = 7
        while cursorIndex < 10: #Last 3 are column
            if(line[cursorIndex] == "L"):
                maxCol = (maxCol - (int(((maxCol - minCol) / 2.0)+.9)))
            elif(line[cursorIndex] == "R"):
                minCol = (minCol + (int(((maxCol - minCol) / 2.0)+.9)))
            cursorIndex += 1
        if(minCol == maxCol):
            col = maxCol
        else :
            print("Something went wrong getting the column for ", line) 
        
        seatId = (row * 8) + col
        maxSeatID = max(seatId, maxSeatID)
        seatIDs.append(seatId)
    except:
        pass
    line = inputFile.readline().rstrip()

seatIDs.sort()
gaps = []
lastSid = seatIDs[0]
for sid in seatIDs[1:]:
    if sid != lastSid + 1 :
        gaps.append (lastSid+1)
    lastSid = sid

for g in gaps:
    print("Your seat should be : ", g)
print("Max Seat ID is : ", maxSeatID)