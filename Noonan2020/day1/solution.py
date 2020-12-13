inputFile = open('input.txt', 'r' )

intList = [0]
line = inputFile.readline()

while line:
    line = inputFile.readline().rstrip()
    try:
        x = int(line)
        intList.append(int(line))
    except:
        pass

for elem in intList:
    if( (2020 - elem) in intList):
        print(elem * (2020- elem))
        break