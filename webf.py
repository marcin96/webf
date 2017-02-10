__author__="Marcin"
import sys
import os
import logging
from lib.parse.CommandParse import parse
from lib.controller import controler
from lib.core.webfExcpetions import webfException
from lib.controller.controler import MissionControl
import urllib.request
import lib.utils.PrintInfo
import socket
import platform

prompt="[webf] "
failText="Something went wrong please look at the logs."
multithreading=True
Proxy = None
missionControl=None

def checkInternetConnection():
    try:
        urllib.request.urlopen("http://www.google.com")
        lib.utils.PrintInfo.printInfo("[ok] connected to the internet")
        return True
    except:
        lib.utils.PrintInfo.printInfo("[fail] not connected to the internet")
        return False

def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    lib.utils.PrintInfo.printInfo("[ok] Ip == '"+s.getsockname()[0]+"'")
    return True

def checkProcessorPower():
    lib.utils.PrintInfo.printInfo("[ok] "+platform.processor())
    return True

def checkRamSize():
    return True

def checkInternetSpeed():
    return True

def loadConf():
    return True

def checkSystem():
    lib.utils.PrintInfo.printInfo("[ok] "+platform.system())
    return True

def printStartText():
    lib.utils.PrintInfo.printInfo("welcome to webf")
    print(open("startText.txt").read())
    return True

def LoadCommands():
    missionControl.loadCommands()

def load():
    global missionControl
    missionControl = MissionControl("xml/commands.xml")
    rets=[]
    rets.append(printStartText())
    rets.append(checkSystem())
    rets.append(checkInternetConnection())
    rets.append(get_ip_address())
    rets.append(checkProcessorPower())
    rets.append(checkRamSize())
    rets.append(checkInternetSpeed())
    rets.append(loadConf())
    rets.append(LoadCommands())
    if False in rets:
        return False
    return True

if __name__=="__main__":
    os.system("title webf")
    if(load()):
        lib.utils.PrintInfo.printInfo("Successfully loaded webf .)\n")
        while(True):
            try:
                inp = input(prompt)
                c = parse(inp)
                missionControl.execute(inp)
            except webfException:
                lib.utils.PrintInfo.printInfo("Syntax Error")
    else:
        lib.utils.PrintInfo.printInfo(failText)