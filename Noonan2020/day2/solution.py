inputFile = open('input.txt', 'r' )

intList = []
line = inputFile.readline()
validPasswords = 0
invalidPasswords = 0
index = 0
while line:
    index += 1
    try:
        tokens = line.split(":") #produces [Rules][password]
        password = tokens[1].lstrip().rstrip()

        rules = tokens[0].split() #produces [#-#][letter]
        letter = rules[1].lstrip().rstrip()
        counts = rules[0].split("-") #produces [min][max]
        
        letterMin = int(counts[0])
        letterMax = int(counts[1])

        #occurance = password.count(letter)
        #if occurance <= letterMax and occurance >= letterMin:
        #    validPasswords += 1
        #else:
        #    print(letterMin, " - ",letterMax,"  ",letter, " |  ", password, "  | ",occurance)
        #    invalidPasswords += 1
        if(password[letterMin-1] == letter and password[letterMax-1] != letter) or (password[letterMin-1] != letter and password[letterMax-1] == letter):
            validPasswords += 1
        else:
            print(letterMin, " - ",letterMax,"  ",letter, " |  ", password, "  | ")
            invalidPasswords += 1

        line = inputFile.readline().rstrip()


    except Exception as e:
        print("AHHHHHHHH!  ",e, "  at ", index)
        pass

print("There are : ", validPasswords, " valid passwords in the list - ", invalidPasswords)