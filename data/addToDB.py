import sqlite3
import sys
def imporT(File):
    with open(File) as f:
        lines = list(f)
        for i in lines:
            print("[info]   "+i)
            addToDataBase(i.split(";"))
    input("finished")


def addToDataBase(data):
    con = sqlite3.connect("mostlyUsed.db")
    cur = con.cursor()
    cur.execute("INSERT INTO popular(ID,text,md5,lenght,lowerCase,upperCase,numbers) Values("+
                str(data[0])+",'"+str(data[1])+"','"
                    +str(data[2])+"',"+str(data[3])+","
                    +str(data[4])+","+str(data[5])+","+str(data[6])+");")
    con.commit()
    cur.fetchall()
            
    

if __name__=="__main__":
    imporT("pass.txt")
else:
    
