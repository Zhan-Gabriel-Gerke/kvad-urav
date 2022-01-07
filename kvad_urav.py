from tkinter import *
from math import *
import matplotlib.pyplot as plt
import numpy as np
global a,b,c
def lahenda():
    if (a.get()!="" and b.get()!="" and c.get()!=""):
        a_=float(a.get())
        b_=float(b.get())
        c_=float(c.get())
        D=b_*b_-4*a_*c_
        if D>0:
            x1_=round((-1*b_+sqrt(D))/(2*a_),2)
            x2_=round((-1*b_-sqrt(D))*(2*a_),2)
            t=f"X1={x1_}, \nX2={x2_}"
            graf=True
        elif D==0:
            x1_round((-1*b_)/(2*a_),2)
            t=f"X1={x1_}"
            graf=True
        else:
            t="Нет корней"
            graf=False
        otv.configure(text=f"D={D}\n{t}")
        a.configure(bg="lightblue")
        b.configure(bg="lightblue")
        c.configure(bg="lightblue")
    else:
        if a.get()=="":
            a.configure(bg="red")
        if b.get()=="":
            b.configure(bg="red")
        if c.get()=="":
            c.configure(bg="red")
    return graf,D,t
def graafik():
    flag,D,t=lahenda()
    if flag==True:
        a_=int(a.get())
        b_=int(b.get())
        c_=int(c.get())
        x0=(-b_)/(2*a_)
        y0=a_*x0*x0+b_*x0+c_
        x = np.arange(x0-10, x0+10, 0.5)
        y=a_*x*x+b_*x+c_
        fig = plt.figure()
        plt.plot(x, y,"b:o", x0, y0,"g-d")
        plt.title("Квадратное уравнение")
        plt.ylabel("y")
        plt.xlabel("x")
        plt.grid(True)
        plt.show()
        text=f"вершина параболы({x0},{y0})"
    else:
        text=f"график нет возможности построить"
    otv.configure(text=f"D={D}\n{t}\n{text}")
def veel():
    pass
aken=Tk()
aken.title("Решение квадратного уравнения")
aken.geometry("800x300")
lk=Label(aken,text="Решение квадратного уравнения",font="Arial 20", fg="green",bg="lightblue")
lk.pack()
otv=Label(aken,text="Решение", height=4,width=60,bg="yellow")
otv.pack(side=BOTTOM)
a=Entry(aken,font="Arial 20", fg="green",bg="lightblue",width=3)
a.pack(side=LEFT)
x2=Label(aken,text="x**2+",font="Alial 20", fg="green", padx=10)
x2.pack(side=LEFT)
b=Entry(aken,font="Arial 20", fg="green",bg="lightblue",width=3)
b.pack(side=LEFT)
x=Label(aken,text="x+",font="Arial 20", fg="green")
x.pack(side=LEFT)
c=Entry(aken,font="Arial 20", fg="green",bg="lightblue",width=3)
c.pack(side=LEFT)
ghj=Label(aken,text="=0",font="Arial 20", fg="green")
ghj.pack(side=LEFT)
bnt=Button(aken,text="Решить",font="Arial 20",bg="green",command=lahenda)
bnt.pack(side=LEFT)
bui_g=Button(aken,text="График", font="Arial 20",bg="green",command=graafik)
bui_g.pack(side=LEFT)
kit=Radiobutton(aken,text="Кит",font="Arial 20",bg="blue")
kit.pack()
zont=Radiobutton(aken,text="Зонтик",font="Arial 20",bg="blue")
zont.pack()
babo4=Radiobutton(aken,text="Бабочка",font="Arial 20",bg="blue")
babo4.pack()
aken.mainloop()