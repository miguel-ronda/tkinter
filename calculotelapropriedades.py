from tkinter import*

def bt_soma():
    #codigo abaixo para validar a entrada apenas de numeros
 if(str(ed1.get())).isnumeric()and str(ed2.get()).isnumeric():
     num1 = int(ed1.get())
     num2 = int(ed2.get())
     lb["text"] = num1 + num2 
    #se valorees nao forem numericos imprime a mensagem abaixo:
     lb["text"] = num1 = num2 
     lb["bg"] = "#00FA9A"
 else:
    lb ["text"] = "valores sao invalidos"
    lb["bg"] = "red"
def bt_sub():
    if(str(ed1.get())).isnumeric()and str(ed2.get()).isnumeric():
     num1 = int(ed1.get())
     num2 = int(ed2.get())
     lb["text"] = num1 - num2 

     lb["text"] = num1 = num2 
     lb["bg"] = "#00FA9A"
    else:
     lb ["text"] = "valores sao invalidos"
     lb["bg"] = "red"

def bt_multi():
    if(str(ed1.get())).isnumeric()and str(ed2.get()).isnumeric():
     num1 = int(ed1.get())
     num2 = int(ed2.get())
    lb["text"] = num1 * num2 
    

          
def bt_div():
    if(str(ed1.get())).isnumeric()and str(ed2.get()).isnumeric():
     num1 = int(ed1.get())
     num2 = int(ed2.get())
    lb["text"] = num1 / num2 

            

i=Tk()
i.title("Programa Financeiro")
i.geometry('980x720+250+30')

lb=Label(i,text="0")
lb.place(x=230,y=200)

bt=Button(i,width="20",text="soma",command=bt_soma)
bt.place(x=230,y=260)

bt=Button(i,width="20",text="subtracao",command=bt_sub)
bt.place(x=230,y=290)

bt=Button(i,width="20",text="multiplicacao",command=bt_multi)
bt.place(x=230,y=320)

bt=Button(i,width="20",text="divisao",command=bt_div)
bt.place(x=230,y=350)

ed1 = Entry(i)
ed1.place(x=230,y=150)

ed2 = Entry(i)
ed2.place(x=230,y=180)

lb2=Label(i,text='miguel do amaral paes ronda')
lb2.place(x=230,y=125)


i.mainloop()
    