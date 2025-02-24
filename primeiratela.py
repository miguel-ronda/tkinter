#comando abaixo importa tudo da bliblioteca que e necessaria 
#para a  criacao de telas.(ASTERISCO sgnifica tudo)
from tkinter import *
#i (intanciar) recebe o objeto Tk 
i = Tk()
#gerar titulo da janela 
i.title('programa financeiro')

# proriedade que alterea o tamanho da janela (980 x 720)
# e distancia da diretia e topo da tela (250X30)
i.geometry('980x720+250+30')

#propriedades graficas , cor de fundo da tela (bg) ou (background)
# nao pode passae o i com ponto! DEVE SER  i[]
i["bg"] = "red"

#CRIA O INCONE NA JANELA, VOCE DEVE TER A IMAGEM NO MESMO LOCAL DO CODIGO.
#i.wm_iconbitmap('icone.ico')

#cria um label e posiciona (place) ele em relacao a tela
lb = Label(i,text='nome do usuario')
lb.place(x=100,y=100)

#cria um botao e posiciona (place) elçe  em relacao ao label.
bt = Button(i,width='20',text='ok')
bt.place(x=230,y=100)

#gera a janela grafica
i.mainloop()