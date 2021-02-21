import tkinter
from tkinter import *
import json

#Tkinter Initiatilization & basic formatting
main = Tk()
main.title("Project UAC - Detailed Coronavirus(SARS-CoV-2) Metrics")
main.geometry("600x300")
#Label
topLabel = Label(main, text="Maharashtra COVID Cases",pady=20) #Top Title Label
topLabel.pack(side="top")

#JSon work
data = json.load(open('data.json'))
json_dump = json.dumps(data)
dict_json = json.loads(json_dump)

#Total Infected
dataMHTotalInfectedStatic = Label(main, text="Total Infected")
dataMHTotalInfected = Label(main, text=dict_json['regionData'][20]['totalInfected'])
dataMHTotalInfectedStatic.pack(side="top")
dataMHTotalInfected.pack(side="top")

#Padding
padding1 = Label(main, pady=5)
padding1.pack(side="top")

#Infected in last 24 hours
dataMHNewInfectedStatic = Label(main, text="Infected in last 24 hours")
dataMHNewInfected = Label(main, text=dict_json['regionData'][20]['newInfected'])
dataMHNewInfectedStatic.pack(side="top")
dataMHNewInfected.pack(side="top")

#Final mainloop call
# topLabelText.pack(side="top") 
mainloop()