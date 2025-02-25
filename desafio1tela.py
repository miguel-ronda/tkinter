from tkinter import*
i=Tk()
i.title("Programa Financeiro")
i.geometry('980x720+250+30')

#componente .grid serve tambem para posicionar utiliANDO INDICATIVO DE LINHA (ROW) E COLUNA (COLUMN).
'''lb1=Label(i,text="login",bg="yellow")
lb1.place(x=1130,y=100)

lb2=Label(i,text="senha",bg="red")
lb2.place(x=1130,y=150)

ed1=Entry(i)
ed1.place(x=1130,y=80)

ed2=Entry(i)
ed2.place(x=1130,y=130)

bt1 = Button(i,text="login")
bt1.place(x=950,y=950)
'''



#o codigo abaixo faz correcao das posicos das label, caias de texto e botao
lb1=Label(i,text="LOGIN",bg="yellow")
lb1.grid(row=1,column=1)

lb2=Label(i,text="SENHA",bg="red")
lb2.grid(row=2,column=1)

ed1=Entry(i)
ed1.grid(row=1,column=2)

ed2=Entry(i)
ed2.grid(row=2,column=2)

bt1 = Button(i,text="login")
bt1.grid(row=3,column=1)












i.mainloop()