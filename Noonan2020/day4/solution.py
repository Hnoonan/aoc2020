import re

class Passport:
    byr = ""
    iyr = ""
    eyr = ""
    hgt = ""
    hcl = ""
    ecl = ""
    pid = ""
    cid = ""
    validEyeColors = {"amb","blu","brn","gry","grn","hzl","oth"}

    def __init__(self,tokens):
        try:
            self.byr = tokens[tokens.index("byr") + 1]
            self.iyr = tokens[tokens.index("iyr") + 1]
            self.eyr = tokens[tokens.index("eyr") + 1]
            self.hgt = tokens[tokens.index("hgt") + 1]
            self.hcl = tokens[tokens.index("hcl") + 1]
            self.ecl = tokens[tokens.index("ecl") + 1]
            self.pid = tokens[tokens.index("pid") + 1]
            self.cid = tokens[tokens.index("cid") + 1]
        except:
            pass
    
    def printFields(self):
        print(self.byr)
        print(self.iyr)
        print(self.eyr)
        print(self.hgt)
        print(self.hcl)
        print(self.ecl)
        print(self.pid)
        print(self.cid)
    
    def validateFields(self):
        if(self.byr == "" or self.iyr == "" or self.eyr =="" or self.hgt =="" or self.hcl == "" or self.ecl == "" or self.pid == ""):
            return 0 #Missing required fields
        else:
            return 1

    def validatePassport(self):

        if(self.validateFields() != 1):
            print("bad fields")
            return 0
        if(int(self.byr) < 1920 or int(self.byr) > 2002):
            print("byr failed ", self.byr)
            return 0
        if(int(self.iyr) < 2010 or int(self.iyr) > 2020):
            print("iyr failed ", self.iyr)
            return 0
        if(int(self.eyr) < 2020 or int(self.eyr) > 2030):
            print("eyr failed ", self.eyr)
            return 0
        try:
            height = re.split('(\d+)',self.hgt)
            if(height[2] != "cm" and height[2] != "in"):
                print("wrong label ", height[0], " ",height[1]," ",height[2], "   || ", self.hgt)
                return 0
            if(height[2] == "cm" and (int(height[1]) < 150 or int(height[1]) > 192)):
                print("cm failed ", height[1], " ",height[2])
                return 0
            elif(height[2] == "in" and (int(height[1]) < 59 or int(height[1]) > 76)):
                print("in failed ", height[0], " ",height[1])
                return 0
        except Exception as e:
            print("Height split broke for ", self.hgt, "   ", e)
            return 0
        
        hcPattern = re.compile("#([a-f]|[0-9]){6}")
        if(not hcPattern.match(self.hcl)):
            print("bad HCL ", self.hcl)
            return 0
        if(not self.ecl in self.validEyeColors):
            print("bad ECL ", self.ecl)
            return 0
        pidPattern = re.compile("[0-9]{9}")
        if(not pidPattern.match(self.pid)):
            print("bad PID ", self.pid)
            return 0
        
        return 1
        

inputFile = open('input.txt', 'r' )

line = inputFile.readline()
currentPassport = []
validPassports = 0
totalPassports = 0

while line:
    try:
        if line == "\n" :
            newPass = Passport(currentPassport)
            totalPassports += 1
            validPassports += newPass.validatePassport()
            currentPassport = [] #Reset the current passport
        else :
            newTokens = re.split(' |:|\n', line)
            for s in newTokens:
                s.lstrip().rstrip()
                currentPassport.append(s)
    except:
        pass
    line = inputFile.readline()

newPass = Passport(currentPassport) #check the last row
validPassports += newPass.validatePassport()
totalPassports += 1

 

print("Found ", validPassports, " valid passports of ", totalPassports)


