import tkinter.ttk
from tkinter import *
from tkinter import ttk

root = Tk()


class Funcoes():
    def limpa_tela(self):
        self.codigo_entry.delete(0, END)


class Application(Funcoes):
    def __init__(self):
        self.root = root
        self.tela()
        self.frames()
        self.widgets_frame1()
        self.lista_frame2()
        root.mainloop()

    def tela(self):
        self.root.title('Cadastro de Clientes')
        self.root.configure(background='#282a36')
        self.root.geometry('720x576')
        self.root.resizable(True, True)
        self.root.maxsize(width=1920, height=1080)
        self.root.minsize(width=500, height=400)

    def frames(self):
        self.frame_1 = Frame(self.root, bd=4, bg='#dfe3ee',
                             highlightbackground='#759fe6', highlightthickness=3)
        self.frame_1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.46)

        self.frame_2 = Frame(self.root, bd=4, bg='#dfe3ee',
                             highlightbackground='#759fe6', highlightthickness=3)
        self.frame_2.place(relx=0.02, rely=0.5, relwidth=0.96, relheight=0.46)

    @staticmethod
    def widgets_frame1(self):
        # limpar
        self.bt_limpar = Button(self.frame_1, text='Limpar', bd=2, bg='#99DBF5', fg='white',
                                font=('calibri', 8, 'bold'), command=self.limpa_tela())
        self.bt_limpar.place(relx=0.2, rely=0.1, relwidth=0.1, relheight=0.15)
        # buscar
        self.bt_buscar = Button(self.frame_1, text='Buscar', bd=2, bg='#99DBF5', fg='white',
                                font=('calibri', 8, 'bold'))
        self.bt_buscar.place(relx=0.3, rely=0.1, relwidth=0.1, relheight=0.15)
        # novo
        self.bt_novo = Button(self.frame_1, text='Novo', bd=2, bg='#99DBF5', fg='white', font=('calibri', 8, 'bold'))
        self.bt_novo.place(relx=0.53, rely=0.1, relwidth=0.1, relheight=0.15)
        # alterar
        self.bt_alterar = Button(self.frame_1, text='Alterar', bd=2, bg='#99DBF5', fg='white',
                                 font=('calibri', 8, 'bold'))
        self.bt_alterar.place(relx=0.63, rely=0.1, relwidth=0.1, relheight=0.15)
        # apagar
        self.bt_apagar = Button(self.frame_1, text='Apagar', bd=2, bg='#99DBF5', fg='white',
                                font=('calibri', 8, 'bold'))
        self.bt_apagar.place(relx=0.73, rely=0.1, relwidth=0.1, relheight=0.15)

        # label_codigo
        self.lb_codigo = Label(self.frame_1, text='Código', bg='#dfe3ee', fg='#9AC5F4', font=('calibri', 14, 'bold'))
        self.lb_codigo.place(relx=0.05, rely=0.05, relwidth=0.08)

        self.codigo_entry = Entry(self.frame_1, font=('calibri', 8, 'bold'))
        self.codigo_entry.place(relx=0.05, rely=0.15, relwidth=0.08)

        # label_nome
        self.lb_nome = Label(self.frame_1, text='Nome', bg='#dfe3ee', fg='#9AC5F4', font=('calibri', 14, 'bold'))
        self.lb_nome.place(relx=0.05, rely=0.40, relwidth=0.08)

        self.nome_entry = Entry(self.frame_1, font=('calibri', 8, 'bold'))
        self.nome_entry.place(relx=0.05, rely=0.50, relwidth=0.60)

        # label_telefone
        self.lb_telefone = Label(self.frame_1, text='Telefone', bg='#dfe3ee', fg='#9AC5F4',
                                 font=('calibri', 14, 'bold'))
        self.lb_telefone.place(relx=0.05, rely=0.65, relwidth=0.1)

        self.telefone_entry = Entry(self.frame_1, font=('calibri', 8, 'bold'))
        self.telefone_entry.place(relx=0.05, rely=0.75, relwidth=0.40)

        # label_cidade
        self.lbcidade = Label(self.frame_1, text='Cidade', bg='#dfe3ee', fg='#9AC5F4', font=('calibri', 14, 'bold'))
        self.lbcidade.place(relx=0.5, rely=0.65, relwidth=0.08)

        self.cidade_entry = Entry(self.frame_1, font=('calibri', 8, 'bold'))
        self.cidade_entry.place(relx=0.5, rely=0.75, relwidth=0.40)

    def lista_frame2(self):
        self.listaClientes = ttk.Treeview(self.frame_2, height=3, columns=('col1', 'col2', 'col3', 'col4'))
        self.listaClientes.heading('#0', text='')
        self.listaClientes.heading('#1', text='Código')
        self.listaClientes.heading('#2', text='Nome')
        self.listaClientes.heading('#3', text='Telefone')
        self.listaClientes.heading('#4', text='Cidade')

        self.listaClientes.column('#0', width=1, stretch=NO)
        self.listaClientes.column('#1', width=50)
        self.listaClientes.column('#2', width=200)
        self.listaClientes.column('#3', width=125)
        self.listaClientes.column('#4', width=125)

        self.listaClientes.place(relx=0.01, rely=0.1, relwidth=0.95, relheight=0.85)

        self.scrollLista = Scrollbar(self.frame_2, orient='vertical')
        self.listaClientes.configure(yscrollcommand=self.scrollLista.set)
        self.scrollLista.place(relx=0.96, rely=0.1, relwidth=0.04, relheight=0.85)


Application()
