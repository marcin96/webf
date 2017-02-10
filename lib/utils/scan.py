__author__ = 'Marcin'
import lib.core.crawler


def Scan(attributes):
    victim="None"
    for i in range(len(attributes)):
        print(attributes[0][i])
        if(str(attributes[0][i])=="-v"):
            victim=attributes[0][i+1]
    print(victim)
    getSiteswithForms(victim)

def getSiteswithForms(url):
    if("http" in url or "https" in url):
        return lib.core.crawler.ScanF(url)
    return None

#getSiteswithForms("http://marcin96.pythonanywhere.com")