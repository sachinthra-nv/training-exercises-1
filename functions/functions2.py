# import re



def findTags(tag, file1): 
    for line in file1:
        # print(file1.readline())
        # findNextTag(file1)
        # break
        # if re.search("image:", line):
        if "image:" in line:
            print(line,end="")
            fSpace = findFrontSpace(line)
            # print(line.find("image:"))
            findNextTag(file1, fSpace)

def findFrontSpace(s):
    return len(s) - len(s.lstrip())

def findNextTag(file1, fSpace):
    line = file1.readline()
    while findFrontSpace(line) > fSpace:
        line = file1.readline()
    print(line)
    matchNextTag(line, file1)
    
# Matching the next tag and if it has imagePullPolicy then get the value of it
def matchNextTag(line, file1, tag="imagePullPolicy:"):
    if tag in line:
        print(line)
        changeValueOfTag(line, file1)
    else:
        print(False)

# case 1
#   if imagePullPolicy has someother child tag del it and put  ifNotPresent
def changeValueOfTag(line, file1):
    fSp = findFrontSpace(line)
    line = file1.readline()
    print(line)
    while fSp > findFrontSpace(line):
        file1.seek(len(line))
        # print(line.replace(line,""))
        line = file1.readline()
        # break
    print(file1.readline())




