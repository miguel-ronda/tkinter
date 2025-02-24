from tkinter import*

#CRIANDO UMA FUNCAO PARA CLIQUE NO BOTAO
def bt_click():
    # o label que usa proprieda text recebera a mensagem "trocou o texto"
    lb['text']="trocou o texto"
    #esse print abaixo exibe o texto a tela do console.
    print("o botao foi clicado!")

def bt_clikar():
    #esse print exibe o texto digitado na caixa de texto e exibe na label da tela
    print(ed.get())
    lb["text"]=ed.get()
        #i (instanciar) recebe o objeto tk 
    i =Tk()
    #gerar titulo  na janela 
    i.title('programa financeiro')
    i.geometry('980x720+250=30')
    i["bg"]= "green" 

    #i.wm_iconbitmap('icone.ico')

    lb= Label(i,text = 'nome do usuario')
    lb.place(x=100,y=100)

    bt= Button(i,width='20',text='ok',command=bt_click)
    bt.place(x=230,y=100)
    #o codihgo abaixo cria um botao e posiciona
    bt = Button(i,width="20",text='capturar',command=bt_clikar)
    bt.place(x=230,y=190) 

    #O CODIGO ABAIXO CRIA A CAIXA DE TEXTO PARA DIGITAR ALGO DENTRO
    ed= Entry(i)
    ed.place (x=230,y=150)

    i.mainloop()
