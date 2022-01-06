from tkinter import*
aken=Tk()
aken.title("Решение квадратного уравнения")
aken.geometry("900x900")
nup=Label(aken,text="Решение квадратного уравнения",height=1,width=30,font="Arial 20",fg="green",bg="lightblue",relief=GROOVE)
txt=Entry(aken,width=5,font="Arial 20",fg="green",bg="lightblue",justify=CENTER)
x=Label(aken,text="X**2",height=1,width=4,font="Arial 15",fg="green",bg="white",relief=GROOVE)
reh=Button(aken,text="Решение",font="Arial 20",fg="black",bg="green",height=2,width=10,relief=GROOVE)





















reh.pack(side=RIGHT)
x.pack(side=LEFT)
txt.pack(side=LEFT)
nup.pack()
aken.mainloop()