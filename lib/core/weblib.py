__author__ = 'Marcin'
import requests
import lib.utils.PrintInfo
richtig =["<Response [200]>","<Response [201]>","<Response [202]>"]

def SendFormGET_with_Proxy(url,datas,proxies):
    if(requests.get(url,params=datas,proxies=proxies)in richtig):
        lib.utils.PrintInfo.printInfo("Right credentials:>",datas)
        return True

def SendFormPOST_with_Proxy(url,datas,proxies):
    if(requests.post(url,data=datas,proxies=proxies) in richtig):
        lib.utils.PrintInfo.printInfo("Right credentials:>",datas)
        return True

def SendFromPOST(anmeldurl,admurl,datas):
    client = requests.session()
    client.get(anmeldurl)
    csrf = client.cookies['csrftoken']
    payload={"user":datas["user"],"password":datas["password"],"csrfmiddlewaretoken":csrf}
    header ={"X-CSRFToken":csrf,"Referer":anmeldurl}
    ret = client.post(admurl,data=payload,allow_redirects=True,headers=header)
    client.cookies.clear()
    ret.connection.close()
    if("200" in ret):
        lib.utils.PrintInfo.printInfo("Right credentials:>",datas)
        return True
    else:return ret

def SendFormGET(url,datas):
    if(requests.get(url,params=datas)in richtig):
        lib.utils.PrintInfo.printInfo("Right credentials:>",datas)
        return True
