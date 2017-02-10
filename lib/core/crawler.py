import urllib.request
from lib.parse.WebsiteParse import Parser
import urllib.request
import lib.utils.PrintInfo
WebsitewithForm=[]

def getWebsiteCode(url):
    return urllib.request.urlopen(url).read()

def ScanForForms(url,data):
    p = Parser()
    p.setData(data)
    urls = p.ParseLinks()
    lib.utils.PrintInfo.printInfo(urls)
    Urls=[]
    for u in urls:
        if("http" in u):
            Urls.append(u)
        else:
            v = str(url)+u
            Urls.append(v)
    lib.utils.PrintInfo.printInfo(Urls)
    for i in Urls:
        lib.utils.PrintInfo.printInfo("Search in:",i)
        p.setData(getWebsiteCode(i))
        forms=p.ParseFormulars()
        if(len(forms)>0):
            WebsitewithForm.append(i)
    return WebsitewithForm

def ScanForLoginForms(url):
    None

def getAllurls(urls,url,idx):
    if(idx==0):
        p = Parser()
        p.setData(getWebsiteCode(url))
        urls.append(p.ParseLinks())
    else:
        p = Parser()
        p.setData(getWebsiteCode(urls[idx]))
        if(p.ParseLinks()==None):return urls
        urls.append(p.ParseLinks())
        idx+=1
        getAllurls(urls,urls,idx)




def ScanF(url):
    return ScanForForms(url,getWebsiteCode(url))


lib.utils.PrintInfo.printInfo(getAllurls([],"http://marcin96.pythonanywhere.com",0))