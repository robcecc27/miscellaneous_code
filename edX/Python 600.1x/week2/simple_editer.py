# -*- coding: utf-8 -*-
"""
Created on Sat Sep 15 12:01:43 2018

@author: Rob
"""

import tkinter as tk

root = tk.Tk()
root.title('Tkinker Window, Written in Python 3.6')
frame1 = tk.Frame(root, width=900, height=250, background="bisque")
frame2 = tk.Frame(root, width=450, height = 100, background="#b22222")

frame1.pack(fill=None, expand=False)
frame2.place(relx=.5, rely=.5, anchor="c")

root.mainloop()




var = tkinter.StringVar()
entry = tkinter.Entry(root, textvariable=var)
entry.focus_set()
entry.pack()
var.set(root.title())
def changeTitle(): root.title(var.get())
tkinter.Button(root, text="Change Title", command=changeTitle).pack()
tkinter.mainloop()

from tkinter import *

def msg():
    print('hello stdout...')
    
top = Frame()
top.pack()
Label(top, text='Hello World').pack(side=TOP)
widget = Button(top, text='press', command=msg)
widget.pack(side=BOTTOM)
top.mainloop()
