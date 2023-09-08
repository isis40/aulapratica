import PySimpleGUI as sg
#tema
sg.theme('Reddit')
#layout
layout = [[sg.T('Seu texto digitado aparecerá aqui:'),sg.T(size=(15,1),key='OUTPUT')],
          [sg.In(key='INPUT')],
          [sg.B('Atualizar'),sg.B('Sair')]]
janela = sg.Window('Padrão 2B', layout)
#loop
while True:
    eventos, valores = janela.read()
    print(eventos,valores)
    if eventos == sg.WIN_CLOSED  or eventos== 'Sair':
        break
    if eventos == 'Atualizar':
        janela['OUTPUT'].update(valores['INPUT'])
janela.close()