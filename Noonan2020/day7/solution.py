import re

inputFile = open('input.txt', 'r' )

line = inputFile.readline().strip()

rulesList = []
rulesListNumberless = []
currentRules = []
currentRulesNumberless = []
index = 0

while line:
    try:
        tokens = line.split("contain")   
        name = tokens[0]
        contents = tokens[1].split(",")    
        currentRules.append(name)
        for c in contents :
            cn = []
            c = c.strip().strip(".")
            cn.append(name.rstrip('s '))
            clNumberless = re.split("[1-9] ", c)
            cl = re.split("([1-9] )", c)
            for l in cl:
                currentRules.append(l)
            for l in clNumberless:
                cn.append(l.rstrip().rstrip('s'))

            for n in cn:
                currentRulesNumberless.append(n)

        #for r in currentRules:
        #    print(r)
        #rulesList.append(currentRules[:])
        #rulesList.append((currentRules, currentRules[0]))
        #rulesList[index] = []
        #rulesList[index].append(currentRules)
        #rulesList[index] = currentRules
        #rulesList.append([currentRules])
        #Why is this so hard?
        rulesList.append(list(currentRules))
        rulesListNumberless.append(list(currentRulesNumberless))
        
    except:
        pass
    index += 1
    currentRules = []
    currentRulesNumberless = []
    line = inputFile.readline().rstrip()

rulesList.sort(key = len)
rulesListNumberless.sort(key = len)

def canFit(bagName, rules):
    allowedContainers = set([bagName.rstrip('s')])
    matches = []
    numRules = len(rules)
    exhausted = 0
    found = 0
    index = 0
    while not exhausted:
        for cont in allowedContainers:
            try :
                if cont in rules[index][1:] :
                    matches.append(rules[index][0])
            except :
                print("Problem with ", rules[index])
                pass
        
        for match in matches:
            if (match not in allowedContainers):
                allowedContainers.add(match)
                found += 1 
        
        index += 1
        matches = []
        if (index >= numRules): #roll back to the beginning of the list, we're done if we found nothing this iteration
            if(found == 0):
                exhausted = 1
            found = 0
            index = 0
    
    return (len(allowedContainers) - 1) #dont count the bag you're trying to find holders for

def holds(bagName, capacity ,rules):
    bagNames = []
    bagCapacities = []
    numPattern = re.compile("[1-9] ")
    conversion = ""

    for bag in rules:
        if bag[0].rstrip() == bagName:
            for r in bag[1:] :
                if(r != ""):
                    if(r == "no other bags"):
                        conversion = r
                        break
                    elif(numPattern.match(r)):
                        bagCapacities.append(int(r.rstrip()))
                    else:
                        bagNames.append(r)
            break
    if(conversion == "no other bags"):
        return 1
    else:
        return 1 + holds()   
    conversion = ""

storeBag = "shiny gold bags"

#print("You could carry a ",storeBag, " in " ,canFit(storeBag,rulesListNumberless), " ways")
print("A ", storeBag, " can hold ", (holds(storeBag, rulesList) -1)) #dont count the outermost bag

#for i in rulesList:
#    print(i)