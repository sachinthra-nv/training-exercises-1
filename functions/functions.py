# import re

class MyYaml:
    def __init__(self, totalLen, lines):
        self.index = 0
        self.lines = lines
        

    def findTags(self, tag): 
        # for line in lines:
        # totalLen = len(lines)
        # for i in range(0,len(self.lines)):
        while self.index < len(self.lines):
            # print(line)
            # print(file1.readline())
            # findNextTag(file1)
            # break
            # if re.search("image:", line):
            # print(self.index," - ",len(self.lines))
            # print(self.lines[self.index])
            if "image:" in self.lines[self.index]:
                print(self.lines[self.index],end="")
                fSpace = self.findFrontSpace(self.lines[self.index])
                # print(line.find("image:"))
                self.findNextTag(fSpace)
            self.index+=1
        return self.lines

    def findFrontSpace(self, s):
        return len(s) - len(s.lstrip())

    def findNextTag(self, fSpace):
        self.index += 1
        line = self.lines[self.index]
        while self.findFrontSpace(line) > fSpace:
            self.index+=1
            line = self.lines[self.index]
        print(line)
        self.matchNextTag()
        
    # Matching the next tag and if it has imagePullPolicy then get the value of it
    def matchNextTag(self, tag="imagePullPolicy:"):
        line = self.lines[self.index]
        if tag in line:
            if line.strip() == tag:
                print("ooh ic")
                self.changeValueOfTagCase1()
            else: 
                print("No Changes")
            print(line, end="")
        else:
            print(False)
            self.insertTagCase2()

    # case 1
    #   if imagePullPolicy has someother child tag del it and put  ifNotPresent
    def changeValueOfTagCase1(self):
        fSp = self.findFrontSpace(self.lines[self.index])
        #  IfNotPresent
        self.lines[self.index] = self.lines[self.index][0:len(self.lines[self.index])-1] + " IfNotPresent\n"
        self.index+=1
        line = self.lines[self.index]
        # print(line)
        while fSp < self.findFrontSpace(line):
            print(line, end="")
            # i+=1
            # line = self.lines[i]
            self.lines.pop(self.index)
            line = self.lines[self.index]
            # self.totalLen -= 1

    # case 2
    #   if imagePullPolicy has someother child tag del it and put  ifNotPresent
    def insertTagCase2(self):
        offset = self.findFrontSpace(self.lines[self.index-1])
        val = ' '*offset + "imagePullPolicy: IfNotPresent\n"
        self.lines.insert(self.index, val) 



