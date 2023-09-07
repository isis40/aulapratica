from PySimpleGUI import PySimpleGUI as sg
#Layout
sg.theme('Reddit')
layout = [
    [sg.Text('Usuário'),sg.Input(key='usuario',size=(19,1))],
    [sg.Text('Senha'),sg.Input(key='senha',password_char='*',size=(20,1))],
    [sg.Checkbox('Salvar login')],
    [sg.Button('Entrar')]
]
#Janela
janela = sg.Window('Teste',layout)
#Ler os eventos
while True:
    eventos, valores = janela.read()
    if eventos == sg.WIN_CLOSED:
        break
    if eventos == 'Entrar':
        if valores['usuario'] == 'isis' and valores ['senha'] == '123':
            sg.popup('Usuário correto, seja bem-vinda! ', valores['usuario'])
