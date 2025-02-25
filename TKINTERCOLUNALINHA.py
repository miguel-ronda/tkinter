from tkinter import*
i=Tk()
i.title("Programa Financeiro")
i.geometry('980x720+250+30')


lb1=Label(i,text="login",bg="yellow")
#componente .grid serve tambem para posicionar utiliANDO INDICATIVO DE LINHA (ROW) E COLUNA (COLUMN).
lb1.grid(row=2,column=2)


lb2=Label(i,text="senha",bg="red")
lb2.grid(row=1,column=25)

ed1=Entry(i)
ed1.grid(row=1,column=2)

ed2=Entry(i)
ed2.grid(row=2,column=2)

bt1 = Button(i,text="login")
bt1.grid(row=2,column=4)


i.mainloop()