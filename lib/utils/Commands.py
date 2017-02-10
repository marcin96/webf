__author__ = 'Marcin'
from xml.dom import minidom
import lib.utils.PrintInfo

class Attribut():
    Name=""
    required=False
    usage=""
    alternative=""
    def __init__(self,Name,required,usage,alternative):
        self.Name=str(Name).strip()
        self.required=required
        self.usage=str(usage).strip()

class command():
    Name=""
    Alternatives=[]
    Attributes=[]
    method=""
    info=""
    def __init__(self,Name,Alternatives,Atributes,method,info):
        self.Name=str(Name).strip()
        self.Alternatives=Alternatives
        self.Attributes=Atributes
        self.method=str(method).strip()
        self.info=str(info).strip()

    def prpi(self):
        print(self.Name,self.method,self.info)
        for i in self.Attributes:
            print("Attributes: ",i.Name,i.required,i.usage)

class Commander():
    file=""
    Commands={}
    def __init__(self,file):
        self.file = file

    @staticmethod
    def LoadCommands(file):
        xmldoc = minidom.parse(file)
        itemlist = xmldoc.getElementsByTagName('command')
        Commands=[]
        for i in itemlist:
            alternatives=[]
            attributes=[]
            vName="";vMethod="";vInfo=""
            for w in i.childNodes:
                if(w.nodeName=="name"):
                    vName=w.firstChild.data
                elif(w.nodeName=="method"):
                    try:
                        vMethod = w.firstChild.nodeValue
                    except:vMethod=""
                elif(w.nodeName=="info"):
                    vInfo=w.firstChild.data
                elif(w.nodeName=="alternative"):
                    alternatives.append(w.firstChild.data)
                elif(w.nodeName=="attribute"):
                    aName=None;required=None;usage=None;alternative=None
                    for t in w.childNodes:
                        if(t.nodeName=="name"):
                            aName=t.firstChild.data
                        elif(t.nodeName=="required"):
                            required=t.firstChild.data
                        elif(t.nodeName=="usage"):
                            usage=t.firstChild.data
                        elif(t.nodeName=="alternative"):
                            alternative=t.nodeValue
                    attributes.append(Attribut(aName,required,usage,alternative))
            Commands.append(command(Name=vName,Alternatives=alternatives,Atributes=attributes,method=vMethod,info=vInfo))
        #lib.utils.PrintInfo.printInfo("Command lenght:",len(Commands))
        return Commands

Commander.LoadCommands("D:/webf/xml/commands.xml")