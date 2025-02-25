from tkinter import*
i=Tk()
i.title("Programa Financeiro")
i.geometry('980x720+250+30')

#componente .grid serve tambem para posicionar utiliANDO INDICATIVO DE LINHA (ROW) E COLUNA (COLUMN).
lb1=Label(i,text="login",bg="yellow")
lb1.place(x=1130,y=100)

lb2=Label(i,text="senha",bg="red")
lb2.place(x=1130,y=150)

ed1=Entry(i)
ed1.place(x=1,y=2)

ed2=Entry(i)
ed2.place(x=2,y=2)

bt1 = Button(i,text="login")
bt1.place(x=465,y=500)


i.mainloop()