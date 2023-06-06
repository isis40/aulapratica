import json
cod = 0
lista_peca  = []
peca = {'Nome': [], 'Fabricante': [], 'Valor': [], 'Codigo': []}
def menu(x=0):
    x = int(input('Escolha a opção Desejada:\n1-Cadastrar Peças\n2-Consultar Peças\n3-Remover Peças\n4-Sair\n- '))
    return x

def cadastrarPeca(codigo = 0):
    global lista_peca
    global cod
    global peca
    nome = input('Digite o nome da peça:\n- ')
    fabricante = input('Digite o fabricante da peça:\n- ')
    valor = float(input('Digite o valor da peça:\n- '))
    cod += 1
    lista_peca.append(peca.copy())
    return nome,valor,fabricante
    cod += 1
def consultarPeca():
    global cod
    global peca
    print('Digite o que deseja consultar:')
    opcao = int(input('1- Todas as peças\n2- Peças por Código\n3- Peças por fabricante\n- '))
    if (opcao == 1):
        for i, j in peca.items():
            print('{} = {}'.format(i, j))
    elif (opcao == 2):
        codi = input('Qual o código deseja procurar?\n- ')
        for peca in lista_peca:
            if peca['Codigo'] == codi:
                for i, j in peca.items():
                    print('{} = {}'.format(i, j))
    elif (opcao == 3):
        print('2')
    else:
        print('Digite uma das opções')

def removerPeca():
    global peca
    remove = int(input('Qual peça deseja remover?'))

# Programa Principal
print('Bem-vindo(a) ao controle de estoque da ISIS PAIVA DE SOUSA LIMA')

while True:
    x = menu()
    contador = 0
    if (x == 1):
        dados = cadastrarPeca()
        peca['Nome'].append(dados[0])
        peca['Fabricante'].append(dados[1])
        peca['Valor'].append(dados[2])
        peca['Codigo'].append(dados[3])
    elif (x == 2):
        consultarPeca()
    elif (x == 3):
        print(x)
    elif (x == 4):
        print('Saindo do Programa...')
        break

