__author__ = 'Marcin'
import lib.core.form

def parseForm(data):
    lib.utils.PrintInfo.printInfo("<found form>")
    tmp = data.split("<")
    at={}
    Attrib = parseAttributes(tmp[0])
    inputs=[]
    for i in tmp:
        v = i.split(" ")
        if(v[0]=="input"):
            ret = parseFormInputBox(i)
            inputs.append(ret)
    f = lib.core.form.Form(Attrib)
    f.addInputBoxes(inputs)
    return f

def parseFormInputBox(data):
    attributes = parseAttributes(data)
    vName=None
    if("name" in attributes):vName = attributes["name"]
    else:vName="Not set"
    lib.utils.PrintInfo.printInfo("<found input> ",attributes["type"]," varliable Name:",vName)
    return attributes

def parseAttributes(data):
    tmp = data.split(" ")
    Attributes = {}
    for i in tmp[1:]:
        i = i.split("=")
        try:
            #lib.utils.PrintInfo.printInfo("Attribute Name:",i[0]," Value:",i[1])
            if(str(i[0]).strip().lower()=="method"):
                lib.utils.PrintInfo.printInfo("method:["+i[1]+"]")
            elif(str(i[0]).strip().lower()=="action"):
                lib.utils.PrintInfo.printInfo("url:["+i[1]+"]")
            Attributes.update({str(i[0]):str(i[1])})
        except Exception:break
    return Attributes
