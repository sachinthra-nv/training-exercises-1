# =================================================================================================
# This program is written by Sachinthra N V.
# This code reads a yaml file and adds imagepullpolicy according the cases given.
__author__ = "Sachinthra N V"
__copyright__ = "Copyright 2022(C) - This belongs to HPE - Sachinthra N V"
__version__ = "1.0"
# =================================================================================================
# module for regular expression
import re

class FindEditAddTags:
    def __init__(self, totalLen, lines, debugMode, searchTag, addTag, addedTagValue):
        # currLineIndex has the current line number and lines will have all the lines for the input file.
        self.currLineIndex = 0
        self.lines = lines
        self.debugMode = debugMode
        self.searchTag = searchTag
        self.addTag = addTag
        self.addedTagValue = addedTagValue

    def printIfDebugOn(self, *msg, end="\n"):
        if self.debugMode:
           print(*msg, end=end)
        
    # this function will find the image tags and calls the findNextTag. This will loop through every 
    # lines and find the image tag is available or not. if available it will find the front space and 
    # call the findNextTag function.
  
    def findTags(self): 
        # for line in lines:
        # totalLen = len(lines)
        # for i in range(0,len(self.lines)):
        while self.currLineIndex < len(self.lines):
            # print(line)
            # print(file1.readline())
            # findNextTag(file1)
            # break
            # if re.search(self.searchTag, line):
            # print(self.currLineIndex," - ",len(self.lines))
            # print(self.lines[self.currLineIndex])
            if self.searchTag in self.lines[self.currLineIndex]:
                # print("Found a Line With Image Tag: ",self.lines[self.currLineIndex],end="")
                self.printIfDebugOn("Found a Line With " + self.searchTag + " Tag in Line No.:",self.currLineIndex,end="")
                fSpace = self.findFrontSpace(self.lines[self.currLineIndex])
                # print(line.find(self.searchTag))
                if self.isImageTagLink():
                    self.printIfDebugOn("\n"," "*4,"- This tag has a Link",end="")
                    self.findNextTag(fSpace)
                self.printIfDebugOn("  --> Done\n")
            self.currLineIndex+=1
        return self.lines

    # this will return the no of front spaces in the string passed to it.
    def findFrontSpace(self, s):
        return len(s) - len(s.lstrip())

    # This function will finf the next tage to the current line by calculating the front spaces.
    # So, this will run a while loop until it find a string which has less or equal front spaces to the previous tag
    # if it find a string which has equal front spaces the we can conclude that it the next tag to the image tag.
    def findNextTag(self, fSpace):
        self.currLineIndex += 1
        line = self.lines[self.currLineIndex]
        while self.findFrontSpace(line) > fSpace:
            self.currLineIndex+=1
            line = self.lines[self.currLineIndex]
        # print("Next Tag: ",line)
        self.printIfDebugOn("\n"," "*4,"- Next Tag:",self.currLineIndex,end="")
        self.matchNextTag(fSpace)
        
    # if current line has imagePullPolicy then get the value of it and check if it is a imagePullPolicy 
    # or not. Then it calls the case functions accordingly
    def matchNextTag(self, fSpace):
        line = self.lines[self.currLineIndex]
        
        if self.addTag in line:
            if fSpace == self.findFrontSpace(line):
                self.printIfDebugOn("\n"," "*4,"- It is a "+self.addTag+" tag",end="")
                if line.strip() == self.addTag:
                    self.printIfDebugOn("\n"," "*4,"It has sub tags",end="")
                    self.changeValueOfTagCase1()
                else: 
                    self.checkChangeValueCase3()
               # print(line, end="")
            else:
                self.insertTagCase2()
        else:
            self.insertTagCase2()

    # case 1
    #   if imagePullPolicy has someother child tag del it and put ifNotPresent
    def changeValueOfTagCase1(self):
        fSp = self.findFrontSpace(self.lines[self.currLineIndex])
        #  IfNotPresent
        self.lines[self.currLineIndex] = self.lines[self.currLineIndex][0:len(self.lines[self.currLineIndex])-1] + " "+self.addedTagValue+"\n"
        self.currLineIndex+=1
        line = self.lines[self.currLineIndex]
        # print(line)
        while fSp < self.findFrontSpace(line):
            # print(line, end="hi")
            # i+=1
            # line = self.lines[i]
            self.lines.pop(self.currLineIndex)
            line = self.lines[self.currLineIndex]
        self.currLineIndex -= 1
        

    # case 2
    #   if imagePullPolicy not present then add imagePullPolicy line.
    def insertTagCase2(self):
        offset = self.findFrontSpace(self.lines[self.currLineIndex-1])
        val = ' '*offset + self.addTag + " "+self.addedTagValue+"\n"
        self.lines.insert(self.currLineIndex, val) 


    # case 3
    # if imagePullPolicy does not have IfNotPresent add the line.
    def checkChangeValueCase3(self):
        line = self.lines[self.currLineIndex]
        if "IfNotPresent" not in line:
            self.printIfDebugOn("\n"," "*4,"- Tag "+self.addTag+" does not have "+self.addedTagValue+"", end="")
            self.lines.pop(self.currLineIndex)
            self.insertTagCase2()
        else:
            self.printIfDebugOn("\n"," "*4,"- Tag "+self.addTag+" have IfNotPresent",end="")

    # This function checks ifthe given string is a link or not.
    def isImageTagLink(self):
        s = self.lines[self.currLineIndex]
        st = s[self.findFrontSpace(s)+7:]
        # print("\n",st)
        if re.match('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d{4,5}', st) != None:
            # print(True)
            return True
        else:
            return False
        # return True        