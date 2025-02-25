from tkinter import*

i=Tk()
i.title("Programa Financeiro")
i.geometry('980x720+250+30')

lb1 = Label(i,text="label 1",bg="yellow")
lb1.place(x=230,y=200) 

lb2 = Label(i,text="label 1",bg="pink")
lb1.place(x=230,y=200) 

lb3 = Label(i,text="label 1",bg="green")
lb1.place(x=230,y=200) 

lb4 = Label(i,text="label 1",bg="red")
lb1.place(x=230,y=200) 

#lb1.pack()
#lb2.pack()
#lb3.pack()
#lb4.pack()

# os codigos sao abaixo e responsavel em posicionar o label nas extremidades da interface
#lb1.pack(side="top")
#lb2.pack(side="left")
#lb3.pack(side="right")
#lb4.pack(side="bottom")


lb1.pack(side="left")
lb2.pack(side="left")
lb3.pack()
lb4.pack()




i.mainloop()