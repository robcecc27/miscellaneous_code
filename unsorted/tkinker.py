#!/usr/bin/python

from Tkinter import *

root = Tk()
root.title("Factor")

num=int(input("enter a number "))
factors=[]
for i in range(1,num+1):
    if num%i==0:
       factors.append(i)

print ("Factors of {} = {}".format(num,factors))



def Button3():
	text_contents = text.get()
	listbox.insert(END, text_contents)
	text.delete(0,END)

button3 = Button(root, text="Factor", command = Button3)

text = Entry(root)

scrollbar = Scrollbar(root, orient=VERTICAL)
listbox = Listbox(root, yscrollcommand=scrollbar.set)
scrollbar.configure(command=listbox.yview)

text.pack()
button3.pack()
listbox.pack()
scrollbar.pack()

root.mainloop()
