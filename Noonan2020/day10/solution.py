inputFile = open('input.txt', 'r' )

adapterList = []
line = inputFile.readline()

while line:
    try:
        adapterList.append(int(line))
    except:
        pass
    
    line = inputFile.readline().rstrip()

adapterList.append(max(adapterList) + 3)

def part1(alist:list):
    alist.sort()
    diffList = []
    lastVal = 0
    for adapter in alist : 
        currentVal = adapter
        diffList.append(currentVal - lastVal)
        lastVal = adapter

    return(diffList.count(1) * diffList.count(3))

def part2(alist:list):
    alist.sort()
    solutionSet = {0:1}
    for adapter in alist :
        solutionSet[adapter] = 0
        if (adapter-1) in solutionSet:
            solutionSet[adapter] += solutionSet[adapter-1]
        if (adapter-2) in solutionSet:
            solutionSet[adapter] += solutionSet[adapter-2]
        if (adapter-3) in solutionSet:
            solutionSet[adapter] += solutionSet[adapter-3]
    
    return(solutionSet[max(alist)])

print("Differences multiplied comes out to : ", part1(adapterList))
print("There are ", part2(adapterList), " working permutations")