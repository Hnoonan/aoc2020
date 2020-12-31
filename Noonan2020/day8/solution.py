inputFile = open('input.txt', 'r' )

line = inputFile.readline()

instructions = []

while line:
    try:
        currentInstruction = line.split()
        instructions.append(currentInstruction)
    except:
        pass
    line = inputFile.readline().rstrip()

def part1(instructions):
    
    visitedInstructions = []
    looped = 0
    accTotal = 0
    cursorIndex = 0
    cursor = instructions[cursorIndex]

    while not looped:
        try:
            #note the index of the instruction we are executing
            visitedInstructions.append(cursorIndex)

            #Split instruction
            command = cursor[0]
            arg = int(cursor[1])

            #print(cursor[1], " --- ", arg)

            #Execute instruction
            if command == "acc":
                cursorIndex += 1
                accTotal += arg
            elif command == "nop":
                cursorIndex += 1
            elif command == "jmp":
                cursorIndex += arg

            #print(cursorIndex)
            #Advance instruction
            #print("index advance to ", cursorIndex, "With accumulator ", accTotal)
            #verify we have not already executed this instruction
            if cursorIndex in visitedInstructions :
                looped = 1
                return accTotal, False
            if cursorIndex >= len(instructions) :
                #Should mean terminated properly??
                return accTotal, True
            cursor = instructions[cursorIndex]        
        except:
            print("Failed at ", cursorIndex)
            pass

def part2(instructions):
    index = 0
    while index <= len(instructions):
        if "nop" in instructions[index]:
            #print(instructions[index])
            instructions[index] = [item.replace("nop", "jmp") for item in instructions[index]]
            #print(instructions[index])
            acc, state = part1(instructions)
            if state == True :
                return acc
            else :
                instructions[index] = [item.replace("jmp", "nop") for item in instructions[index]]
        elif "jmp" in instructions[index]:
            instructions[index] = [item.replace("jmp", "nop") for item in instructions[index]]
            acc, state = part1(instructions)
            if state == True :
                return acc
            else :
                instructions[index] = [item.replace("nop", "jmp") for item in instructions[index]]
        #advance index
        index += 1



acc, state = part1(instructions)
print("At the first repeated instruction the accumulator is", acc)
print("Properly executing, the accumulator ends at ", part2(instructions))