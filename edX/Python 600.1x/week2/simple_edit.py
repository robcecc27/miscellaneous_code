# -*- coding: utf-8 -*-
"""
Created on Sat Sep 15 11:58:01 2018

@author: Rob
"""


# Example (Hello, World):
import tkinter
from tkinter.constants import *
tk = tkinter.Tk()
frame = tkinter.Frame(tk, relief=RIDGE, borderwidth=2)
frame.pack(fill=BOTH,expand=1)
label = tkinter.Label(frame, text="Hello, World")
label.pack(fill=X, expand=1)
button = tkinter.Button(frame,text="Exit",command=tk.destroy)
button.pack(side=BOTTOM)
tk.mainloop()


import tkinter
root = tkinter.Tk()
var = tkinter.StringVar()
entry = tkinter.Entry(root, textvariable=var)
entry.focus_set()
entry.pack()
var.set(root.title())
def changeTitle(): root.title(var.get())
tkinter.Button(root, text="Change Title", command=changeTitle).pack()
tkinter.mainloop()
