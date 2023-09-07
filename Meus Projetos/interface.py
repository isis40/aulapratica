import tkinter.messagebox
from tkinter import *
def aviso():
    texto_funçao = 'Você foi avisado\n- '
    print(texto_funçao)
    texto_aviso['text'] = texto_funçao
#tkinter
janela = Tk()
janela.title('App Padrão')
janela.geometry('854x480')

menu = Menu(janela)
menu

texto = Label(janela, text='Teste')
texto.grid(column=0,row=0,padx=10,pady=10)

texto2 = Label(janela, text='Teste2')
texto2.grid(column=1,row=0,padx=10,pady=10)

botao = Button(janela,text='Aperte',command=aviso)
botao.grid(column=0,row=1,padx=10,pady=10)

texto_aviso = Label(janela, text='')
texto_aviso.grid(column=0,row=2,padx=10,pady=10)
janela.mainloop()
#----------------------------