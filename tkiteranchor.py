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


#O CODGIO ABAIXO POSICIONA CADA LABEL EM LUGARES DIFEERENTES
#APOS TESTAR CIMENTE A LINHA DO LB1 ATE O LB4

lb1.pack(side=LEFT)
lb2.pack(side="left")
lb3.pack(anchor="w")#sempre que nao usar a opcao SIDE,ele smepre sera topo
#lb4.pack(anchor="w")



#lb4.pack(side=BOTTOM,anchor="sw")


lb4.pack(anchor="e")
i.mainloop()