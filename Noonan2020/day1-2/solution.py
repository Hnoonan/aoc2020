inputFile = open('input.txt', 'r' )

intList = []
line = inputFile.readline()

while line:
    line = inputFile.readline().rstrip()
    try:
        x = int(line)
        intList.append(int(line))
    except:
        pass

for elem in intList:
    val = elem
    for elem2 in intList:
        #print((2020-(val + elem2))) 
        if((2020-(val + elem2)) in intList):
            print(val * elem2 * (2020-(val + elem2)))