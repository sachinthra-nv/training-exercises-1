import re

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
                # print("Found a Line With Image Tag: ",self.lines[self.index],end="")
                print("Found a Line With Image Tag in Line No.",self.index,end="")
                fSpace = self.findFrontSpace(self.lines[self.index])
                # print(line.find("image:"))
                if self.isImageTagLink():
                    print("\n"," "*4,"- This tag has a Link",end="")
                    self.findNextTag(fSpace)
                print("  --> Done\n")
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
        # print("Next Tag: ",line)
        print("\n"," "*4,"- Next Tag:",self.index,end="")
        self.matchNextTag()
        
    # Matching the next tag and if it has imagePullPolicy then get the value of it
    def matchNextTag(self, tag="imagePullPolicy:"):
        line = self.lines[self.index]
        if tag in line:
            print("\n"," "*4,"- It is a imagePullPolicy tag",end="")
            if line.strip() == tag:
                print("\n"," "*4,"It has sub tags",end="")
                self.changeValueOfTagCase1()
            else: 
                self.checkChangeValueCase3()
            # print(line, end="")
        else:
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
            # print(line, end="hi")
            # i+=1
            # line = self.lines[i]
            self.lines.pop(self.index)
            line = self.lines[self.index]
        self.index -= 1
        

    # case 2
    #   if imagePullPolicy not present
    def insertTagCase2(self):
        offset = self.findFrontSpace(self.lines[self.index-1])
        val = ' '*offset + "imagePullPolicy: IfNotPresent\n"
        self.lines.insert(self.index, val) 


    # case 3
    # if imagePullPolicy does not have IfNotPresent
    def checkChangeValueCase3(self):
        line = self.lines[self.index]
        if "IfNotPresent" not in line:
            print("\n"," "*4,"- Tag imagePullPolicy does not have IfNotPresent", end="")
            self.lines.pop(self.index)
            self.insertTagCase2()
        else:
            print("\n"," "*4,"- Tag imagePullPolicy have IfNotPresent",end="")

    def isImageTagLink(self):
        s = self.lines[self.index]
        st = s[self.findFrontSpace(s)+7:]
        # print("\n",st)
        if re.match('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d{4,5}', st) != None:
            # print(True)
            return True
        else:
            return False
        # return True


        