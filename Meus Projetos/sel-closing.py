import PySimpleGUI as sg
#tema
sg.theme('Reddit')
#layout
janela_layout = [[sg.Text('Janela Persistente')],
          [sg.In(key='input: ')],
          [sg.B('Confirmar'),sg.Exit('Sair')]]
#janela
janela = sg.Window('Janela que se mantém aberta', janela_layout)
while True:
    evento, valores = janela.read()
    print(evento, valores)
    if evento == sg.WIN_CLOSED or evento == 'Sair':
        break
    if valores['input: '] == '10':
        print('a')

janela.close()