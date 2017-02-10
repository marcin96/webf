__author__ = 'Marcin'
import urllib.request
import lib.parse.FormParse

class element:
    def __init__(self,name,attrb,elements):
        None

class Parser():
    data=""
    def __init__(self):
        None

    def setData(self,data):
        self.data=data

    def parse(self,tag):
        tmp = str(self.data).split("<"+tag)
        ElementV=[]
        for i in tmp[1:]:
            ElementV.append(str(i.split("</"+tag)[0]))
        return ElementV



    def ParseTag(self,TagName):
        data = self.parse(tag=TagName)

    def ParseLinks(self):
        links=[]
        data = self.parse(tag="a")
        for i in data:
            if("href" in i):
                links.append(i.split("=")[1].replace('"',"").split(">")[0])
        return links

    def ParseFormulars(self):
        forms = list()
        data = self.parse(tag="form")
        for i in data:
            ret = lib.parse.FormParse.parseForm(i)
            forms.append(ret)
        return forms

    def parseAttributes(self,data):
        tmp = data.split("=")
        attributes={}
        for i in range(len(tmp)):
            attributes.pop({tmp[i]:tmp[i+1]})
            i+=2

    def parseInputBoxes(self,data):
        tmp = data.split("<")
        inputs=[]
        for i in range(len(tmp)):
            if(i==tmp[i]=="input"):
                inputs.append(tmp[i])
        return inputs

def test():
    p = Parser()
    s = urllib.request.urlopen("http://marcin96.pythonanywhere.com")#http://marcin96.pythonanywhere.com/Anmelden
    d = s.read()
    p.setData(d)
    lib.utils.PrintInfo.printInfo(p.ParseLinks())
    #lib.utils.PrintInfo.printInfo(p.ParseFormulars()[0].countInputBoxes())
