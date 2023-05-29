def menu(x=0):
    x = int(input('Escolha a opção Desejada:\n1-Cadastrar Peças\n2-Consultar Peças\n3-Remover Peças\n4-Sair\n- '))
    return x


def cadastrarPeca(codigo=0):
    global cod
    nome = input('Digite o nome da peça:\n- ')
    fabricante = input('Digite o fabricante da peça:\n- ')
    valor = float(input('Digite o valor da peça:\n- '))
    cod += 1
    return nome, fabricante, valor , cod

def consultarPeca(codi=0):
    global cod
    global peca
    print('Digite o que deseja consultar:')
    opcao = input('1- Todas as peças\n2- Peças por Código\n3- Peças por fabricante\n- ')
    if (opcao==1):
        for i, j in peca.items():
            print('{} = {}'.format(i, j))
    elif(opcao==2):
        print('2')
    elif(opcao==3):
        print('3')
    else:
        print('Digite uma das opções')

# Programa Principal
print('Bem-vindo(a) ao controle de estoque da ISIS PAIVA DE SOUSA LIMA')
cod = 0
peca = {'Nome': [], 'Fabricante': [], 'Valor': [], 'Código': []}
while True:
    x = menu()
    contador = 0
    if (x == 1):
        dados = cadastrarPeca()
        peca['Nome'].append(dados[0])
        peca['Fabricante'].append(dados[1])
        peca['Valor'].append(dados[2])
        peca['Código'].append(dados[3])
    elif (x == 2):
        consultarPeca()
    elif (x == 3):
        print(x)
    elif (x == 4):
        print('Saindo do Programa...')
        break

