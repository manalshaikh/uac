import urllib
import sqlite3
import json

#Tkinter initalization

class core:
    def download():
        url = urllib.request.urlopen("https://api.apify.com/v2/key-value-stores/toDWvRj1JpTXiM8FF/records/LATEST?disableRedirect=true")
        s = url.read()
        fileopen = open("data.json", 'wb')
        fileopen.write(s)
        fileopen.close()
        print("The data has been downloaded and saved as data.json in your directory.")
    def convert():
        conn = sqlite3.connect('uacData')
        c = conn.cursor()

        #Table creation if not exists
        c.execute('CREATE TABLE IF NOT EXISTS cases(region text, totalInfected integer, newInfected integer, recovered integer, newRecovered integer, deceased integer, newDeceased integer)')

        #Convert Json in SQLite
        jd = json.load(open('data.json'))
        for n in jd['regionData']:
            c.execute("INSERT INTO cases VALUES(?, ?, ?, ?, ?, ?, ?)", [n['region'], n['totalInfected'], n['newInfected'], n['recovered'], n['newRecovered'], n['deceased'], n['newDeceased']])
        print("The data has been uploaded.")
        #Committing and closing after queries
        conn.commit()
        conn.close()