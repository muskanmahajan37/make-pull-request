# !/usr/bin/python3
from tkinter import *
top = Tk()
top.geometry("400x250")
# creating label
uname = Label(top, text="Username").place(x=30, y=50)
# creating label
password = Label(top, text="Password").place(x=30, y=90)
# creating label
proffession = Label(top, text="Proffession").place(x=30, y=120)
sbmitbtn = Button(top, text="Submit", activebackground="pink", activeforeground="blue").place(x=30, y=150)
e1 = Entry(top, width=20).place(x=100, y=50)
e2 = Entry(top, width=20).place(x=100, y=90)
e3 = Entry(top, width=20).place(x=100, y=130)
top.mainloop()



