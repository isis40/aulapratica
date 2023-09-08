import PySimpleGUI as sg
#tema
sg.theme('REDDIT')
#layout
layout_l = [[sg.Text('Digite algo, seu texto aparecerá aqui:'),sg.T(size=(20,0),font=('bold'),key='Texto1')],
          [sg.Image(source='icone.png',key='-ICONE-')],
          [sg.In(key='-INPUT-')],
          [sg.Button('Confirmar',key='-CONFIRMAR-'),sg.Button('Sair',key='-SAIR-'),
           [sg.Text('Some dois números:',size=(16,0),font=('bold'),key='Texto2'), sg.In(key='-INPUT1-',size=(5,1),pad=(1,1)), sg.T('+',size=(1,1),pad=(1,1)),sg.In(key='-INPUT2-',size=(5,1),pad=(1,1)),
            sg.Text('='),sg.T(font=('bold'),key='-RESPOSTA-')]]
]

janela = sg.Window('Isinha-Projeto',layout_l)

#loop
while True:
  eventos, valores = janela.read()
  print(eventos, valores)
  if eventos == sg.WIN_CLOSED or eventos == '-SAIR-':
   break
  if eventos == '-CONFIRMAR-':
   janela['Texto1'].update(valores['-INPUT-'])
   num1 = int(valores['-INPUT1-'])
   num2 = int(valores['-INPUT2-'])
   resposta = num1 + num2
   janela['-RESPOSTA-'].update(resposta)


janela.close()