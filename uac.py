import tkinter as tk
from tkinter import *
import sqlite3
import urllib.request
import uacfuncs
from tkinter import messagebox

main = tk.Tk()
#SQLite3 Initialization
conn = sqlite3.connect('uacData')
c = conn.cursor()
t = ('Maharashtra',)
sqlpull = c.execute("SELECT totalInfected,newInfected,deceased,newDeceased FROM cases WHERE region='Maharashtra'")
results = sqlpull.fetchall()
for rows in results:
    totalInfected = rows[0]
    newInfected = rows[1]
    deceased = rows[2]
    newDeceased = rows[3]

#Download Data


#Tkinter Initiatilization & basic formatting

main.title("Project UAC - Detailed Coronavirus(SARS-CoV-2) Metrics")
main.geometry("600x400")
#Label
topLabel = Label(main, text="Maharashtra COVID Cases",pady=20) #Top Title Label
topLabel.pack(side="top")


#Total Infected
dataMHTotalInfectedStatic = Label(main, text="Total Infected")
dataMHTotalInfected = Label(main, text=totalInfected)
dataMHTotalInfectedStatic.pack(side="top")
dataMHTotalInfected.pack(side="top")

#Padding
padding1 = Label(main, pady=5)
padding1.pack(side="top")

#Infected in last 24 hours
dataMHNewInfectedStatic = Label(main, text="Infected in last 24 hours")
dataMHNewInfected = Label(main, text=newInfected)
dataMHNewInfectedStatic.pack(side="top")
dataMHNewInfected.pack(side="top")

#Padding
padding2 = Label(main, pady=5)
padding2.pack(side="top")

#Total Deceased
dataMHTotalDeceasedStatic = Label(main, text="Total Deceased")
dataMHTotalDeceased = Label(main, text=deceased)
dataMHTotalDeceasedStatic.pack(side="top")
dataMHTotalDeceased.pack(side="top")

#Padding
padding1 = Label(main, pady=5)
padding1.pack(side="top")

#Deceased in last 24 hours
dataMHNewDeceasedStatic = Label(main, text="Deceased in last 24 hours")
dataMHNewDeceased = Label(main, text=newDeceased)
dataMHNewDeceasedStatic.pack(side="top")
dataMHNewDeceased.pack(side="top")

#Padding
padding1 = Label(main, pady=5)
padding1.pack(side="top")

#Download data
downloadDatabutton = Button(main, text="Download Data", command=lambda: uacfuncs.core.download())
downloadDatabutton.pack(padx=105, side="left")


#convert json data into sqlite
convertData = Button(main, text="Convert Data", command=lambda: uacfuncs.core.convert())
convertData.pack(padx=50, side="left")



#SQLite closes
conn.commit()
conn.close()
#Final mainloop call
mainloop()