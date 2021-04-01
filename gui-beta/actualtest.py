#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 6.0.1
#  in conjunction with Tcl version 8.6
#    Mar 06, 2021 11:38:23 AM IST  platform: Linux

import sys
import sqlite3
import json

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import firsttest_support


def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Toplevel1 (root)
    firsttest_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_Toplevel1(root, *args, **kwargs)' .'''
    global w, w_win, root
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    firsttest_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None




class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        conn = sqlite3.connect('uacDataDB')
        c = conn.cursor()
        t = ('Maharashtra',)
        sqlpull = c.execute("SELECT totalInfected,newInfected,deceased,newDeceased FROM cases WHERE region='Maharashtra'")
        results = sqlpull.fetchall()
        for rows in results:
            totalInfected = rows[0]
            newInfected = rows[1]
            deceased = rows[2]
            newDeceased = rows[3]
            aTotalInfected = rows[0]
            aInfected = rows[1]
            aDeceased = rows[2]
            aNewDeceased = rows[3]

        #TotalIndiaCase
        fp = open('data.json')
        fr = json.load(fp)
        totalIndiaActive = fr['activeCases']
        totalIndiaInfected = fr['totalCases']
        totalIndiaNewInfected = fr['activeCasesNew']
        top.geometry("648x434+546+357")
        top.minsize(1, 1)
        top.maxsize(1905, 1050)
        top.resizable(1,  1)
        top.title("Project UAC")
        top.configure(highlightcolor="black")

        self.Frame1 = tk.Frame(top)
        self.Frame1.place(relx=0.0, rely=0.0, relheight=1.0, relwidth=1.0)
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief="groove")

        self.Frame2 = tk.Frame(self.Frame1)
        self.Frame2.place(relx=0.015, rely=0.092, relheight=0.341
                , relwidth=0.458)
        self.Frame2.configure(relief='groove')
        self.Frame2.configure(borderwidth="2")
        self.Frame2.configure(relief="groove")

        self.Label1 = tk.Label(self.Frame2)
        self.Label1.place(relx=0.256, rely=0.068, height=20, width=150)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(text='''Maharashtra Cases''')

        self.Label3 = tk.Label(self.Frame2)
        self.Label3.place(relx=0.034, rely=0.27, height=20, width=118)
        self.Label3.configure(activebackground="#f9f9f9")
        self.Label3.configure(text='''Total Infected -''')

        self.Label4 = tk.Label(self.Frame2)
        self.Label4.place(relx=0.034, rely=0.473, height=20, width=183)
        self.Label4.configure(activebackground="#f9f9f9")
        self.Label4.configure(text='''Infected in last 24 hours -''')

        self.Label5 = tk.Label(self.Frame2)
        self.Label5.place(relx=0.034, rely=0.676, height=20, width=107)
        self.Label5.configure(activebackground="#f9f9f9")
        self.Label5.configure(text='''Total Deceased -''')

        self.Label11 = tk.Label(self.Frame2)
        self.Label11.place(relx=0.805, rely=0.27, height=21, width=50)
        self.Label11.configure(activebackground="#f9f9f9")
        self.Label11.configure(text=totalInfected)

        self.Label12 = tk.Label(self.Frame2)
        self.Label12.place(relx=0.842, rely=0.473, height=21, width=39)
        self.Label12.configure(activebackground="#f9f9f9")
        self.Label12.configure(text=newInfected)

        self.Label13 = tk.Label(self.Frame2)
        self.Label13.place(relx=0.842, rely=0.676, height=21, width=39)
        self.Label13.configure(activebackground="#f9f9f9")
        self.Label13.configure(text=deceased)

        self.Frame3 = tk.Frame(self.Frame1)
        self.Frame3.place(relx=0.5, rely=0.09, relheight=0.343, relwidth=0.475)
        self.Frame3.configure(relief='groove')
        self.Frame3.configure(borderwidth="2")
        self.Frame3.configure(relief="groove")

        self.Label2 = tk.Label(self.Frame3)
        self.Label2.place(relx=0.282, rely=0.067, height=20, width=171)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(text='''Overall Cases in India''')

        self.Total_Infected = tk.Label(self.Frame3)
        self.Total_Infected.place(relx=0.065, rely=0.268, height=21, width=129)
        self.Total_Infected.configure(activebackground="#f9f9f9")
        self.Total_Infected.configure(text='''Total Infected -''')

        self.Label6 = tk.Label(self.Frame3)
        self.Label6.place(relx=0.097, rely=0.47, height=21, width=179)
        self.Label6.configure(activebackground="#f9f9f9")
        self.Label6.configure(text='''Infected in last 24 hours -''')

        self.Label7 = tk.Label(self.Frame3)
        self.Label7.place(relx=0.065, rely=0.671, height=21, width=119)
        self.Label7.configure(activebackground="#f9f9f9")
        self.Label7.configure(text='''Active Cases -''')

        self.Label8 = tk.Label(self.Frame3)
        self.Label8.place(relx=0.747, rely=0.268, height=21, width=75)
        self.Label8.configure(activebackground="#f9f9f9")
        self.Label8.configure(text=totalIndiaInfected)

        self.Label9 = tk.Label(self.Frame3)
        self.Label9.place(relx=0.747, rely=0.47, height=21, width=59)
        self.Label9.configure(activebackground="#f9f9f9")
        self.Label9.configure(text=totalIndiaNewInfected)

        self.Label10 = tk.Label(self.Frame3)
        self.Label10.place(relx=0.747, rely=0.671, height=21, width=59)
        self.Label10.configure(activebackground="#f9f9f9")
        self.Label10.configure(text=totalIndiaActive)

        self.Frame4 = tk.Frame(self.Frame1)
        self.Frame4.place(relx=0.509, rely=0.461, relheight=0.5, relwidth=0.466)
        self.Frame4.configure(relief='groove')
        self.Frame4.configure(borderwidth="2")
        self.Frame4.configure(relief="groove")


        self.Frame5 = tk.Frame(self.Frame1)
        self.Frame5.place(relx=0.015, rely=0.461, relheight=0.495
                , relwidth=0.471)
        self.Frame5.configure(relief='groove')
        self.Frame5.configure(borderwidth="2")
        self.Frame5.configure(relief="groove")

        self.Entry1 = tk.Entry(self.Frame5)
        self.Entry1.place(relx=0.492, rely=0.093, height=33, relwidth=0.348)
        self.Entry1.configure(background="white")
        self.Entry1.configure(font="TkFixedFont")

        

        self.Label14 = tk.Label(self.Frame4)
        self.Label14.place(relx=0.066, rely=0.138, height=21, width=99)
        self.Label14.configure(text='''Active Cases -''')
        
        self.Button1 = tk.Button(self.Frame5)
        self.Button1.place(relx=0.328, rely=0.465, height=31, width=71)
        self.Button1.configure(text='''Button''')


        self.menubar = tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

        self.sub_menu = tk.Menu(top,
                tearoff=0)
        self.menubar.add_cascade(menu=self.sub_menu,
                label="Update")
        self.sub_menu.add_command(
                label="Download Data", command=lambda: firsttest_support.download())
        self.sub_menu.add_command(
                label="Upload Data", command=lambda: firsttest_support.convert())
        conn.commit()
        conn.close()
if __name__ == '__main__':
    vp_start_gui()





