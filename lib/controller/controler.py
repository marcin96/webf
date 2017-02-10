__author__ = 'Marcin'
import threading
import lib.utils.Commands
from lib.utils.scan import Scan
from lib.utils.attack import attack
commands={}
class MissionControl():
    def __init__(self,file):
        self.file=file

    def loadCommands(self):
        global commands
        commands = lib.utils.Commands.Commander.LoadCommands(file=self.file)

    def execute(self,command):
        self.loadCommands()
        for i in commands:
            if(i.Name==command.split(" ")[0]):
                globals()[i.method](command)
def Scan(*Attr):
    lib.utils.scan.Scan(Attr)

def Attack(Attr):
    url = str(Attr).split("-url ")[1].split(" ")[0].strip()
    user= str(Attr).split("-user ")[1].split(" ")[0].strip()
    userVariable = str(Attr).split("-vU ")[1].split(" ")[0].strip()
    passwordvariable = str(Attr).split("-p ")[1].split(" ")[0].strip()
    destiny = str(Attr).split("-d " )[1].split(" ")[0].strip()
    technique = str(Attr).split("-t ")[1].split(" ")[0].strip()
    tech = str(Attr).split("-l ")[1].split(" ")[0].strip()
    lib.utils.attack.attack(url,destiny,user,userVariable,passwordvariable,technique,tech)

class Mission(threading.Thread):
    def __init__(self,method):
        None