import re
inputFile = open('input.txt', 'r' )

commandList = []
line = inputFile.readline()

while line:
    try:
        commandList.append(line)
    except:
        print("something went wrong injesting ", line)
        pass
    line = inputFile.readline().rstrip()


def part1(cmd:list):
    bearing = 'E'
    EW = 0 # + is east, - is west
    NS = 0 # + is north, - is south
    for elem in cmd:
        tokens = re.split('(\d+)',elem)
        instruction = tokens[0]
        if(instruction == 'F'):
            instruction = bearing
        magnitude = int(tokens[1])

        if(instruction == 'N'):
            NS += magnitude
        elif(instruction == 'S'):
            NS -= magnitude
        elif(instruction == 'E'):
            EW += magnitude
        elif(instruction == 'W'):
            EW -= magnitude
        elif(instruction in ['L','R']):
            bearing = turn(bearing, instruction, magnitude)
    return(abs(NS) + abs(EW))

def part2(cmd:list):
    shipBearing = 'E'
    wayYBearing = 'N'
    wayXBearing = 'E'
    #ship coordinates
    EWB = 0
    NSB = 0
    #waypoint coordinates
    EWW = 10
    NSW = 1
    for elem in cmd:
        tokens = re.split('(\d+)',elem)
        instruction = tokens[0]
        magnitude = int(tokens[1])

        if(instruction == 'N'):
            NSW += magnitude
            if(NSW > 0):
                wayYBearing = 'N'
        elif(instruction == 'S'):
            NSW -= magnitude
            if(NSW < 0):
                wayYBearing = 'S'
        elif(instruction == 'E'):
            EWW += magnitude
            if(EWW > 0):
                wayXBearing = 'E'
        elif(instruction == 'W'):
            EWW -= magnitude
            if(EWW < 0):
                wayXBearing = 'W'
        elif(instruction == 'F'):
            EWB += (EWW * magnitude)
            NSB += (NSW * magnitude)
        elif(instruction in ['L','R']):
            wayXBearing = turn(wayXBearing, instruction, magnitude)
            wayYBearing = turn(wayYBearing, instruction, magnitude)
            if(wayXBearing in ['N','S']): #rotated an odd number of cardinals, flip waypoint XY to reflect this
                #flip Bearings
                temp = wayYBearing
                wayYBearing = wayXBearing
                wayXBearing = temp
                #flipCoordinates
                temp = NSW 
                NSW = EWW
                EWW = temp
                #signCoordinates
                if(wayXBearing == 'W'):
                    EWW = (abs(EWW) * -1)
                else:
                    EWW = abs(EWW)
                if(wayYBearing == 'S'):
                    NSW = (abs(NSW) * -1)
                else:
                    NSW = abs(NSW)
            else: #rotated an even number of cardinals
                NSW *= -1
                EWW *= -1

    return(abs(NSB) + abs(EWB))    
        

def turn(currentBearing, direction, degree):
    cardinals = {
        'E' : 0,
        'S' : 1,
        'W' : 2,
        'N' : 3
    }
    carVals = list(cardinals.values())
    carKeys = list(cardinals.keys())

    current = cardinals[currentBearing]
    magnitude = degree / 90

    if(direction == 'L'):
        magnitude *= -1
        current += 4

    current += magnitude

    return(carKeys[carVals.index(current % 4)])



print("After following all directions, Manhattan distance is : ", part1(commandList))
print("After following all directions with Waypoint, Manhattan distance is ", part2(commandList))
#Test turning
#print("E, Left 90 : ", turnShip('E', 'L', 90))
#print("N, Right 180 : ", turnShip('N', 'R', 180))
#print("S, Left 270 : ", turnShip('S', 'L', 270))