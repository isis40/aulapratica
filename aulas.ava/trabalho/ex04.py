def menu(x=0):
    x = int(input('Escolha a opção Desejada:\n1-Cadastrar Peças\n2-Consultar Peças\n3-Remover Peças\n4-Sair\n- '))
    return x


def cadastrarPeca(codigo=1):
    cod = codigo
    nome = ''
    fabricante = ''
    valor = 0
    for i in range(0, cod):
        nome = input('Digite o nome da peça:\n- ')
        fabricante = input('Digite o fabricante da peça:\n- ')
        valor = float(input('Digite o valor da peça:\n- '))
    cod += 1
    return nome, fabricante, valor


# Programa Principal
print('Bem-vindo(a) ao controle de estoque da ISIS PAIVA DE SOUSA LIMA')
while True:
    peca = {'Nome': [], 'Fabricante': [], 'Valor': []}
    lista = []
    x = menu()
    contador = 0
    if (x == 1):
        peca['Nome', 'Fabricante', 'Valor'].append(cadastrarPeca())
    elif (x == 2):
        print(peca)
    elif (x == 3):
        print(x)
    elif (x == 4):
        print('Saindo do Programa...')
        break
    print(peca)
