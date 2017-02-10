__author__ = 'Marcin'
import lib.utils.PrintInfo
class InputBox():
    attributes={}
    def __init__(self,attribues):
        self.attributes = attribues

    def getAttributes(self):
        return self.attributes

    def changeAttributes(self,key,value):
        None

class Form():
    attributes={}
    inputBoxes=[]
    isforLogin=False
    def __init__(self,attributes):
        self.attributes=attributes

    def countInputBoxes(self):
        return len(self.inputBoxes)

    def isforLogin(self):
        return False

    def getAttributes(self):
        return self.attributes()

    def changeAttribute(self,key,value):
        None

    def addInputBox(self,inputBox):
        v = InputBox(inputBox)
        self.inputBoxes.append(v)

    def addInputBoxes(self,inputBoxes):
        for i in inputBoxes:
            self.addInputBox(i)

