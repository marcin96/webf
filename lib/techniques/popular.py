import sqlite3
import data
def PopularPassword():
    con = sqlite3.connect("D:\\webf\\data\\mostlyUsed.db")
    cur = con.cursor()
    cur.execute("SELECT text FROM popular")
    passwords = cur.fetchall()
    return passwords