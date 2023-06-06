#VARIAVEIS
listapecas = []
codigo = 0
#FUNÇÕES
def cadastraPeca(codigo): #Função que cadastra peça
    print('Cadastra pecas')
    print('Codigo da Peça: {}'.format(codigo))
    nome = input('Digite o Nome da peca:\n- ')
    fabricante = input('Digite o Fabricante da peca:\n- ')
    valor = int(input('Digite o Valor(R$) da peca:\n- '))
    dict_peca = {'codigo':codigo,
                 'nome':nome,
                 'fabricante': fabricante,
                 'valor':valor}
    listapecas.append(dict_peca.copy())
def consultaPeca(): #Função que consulta peça
    print('Consulta pecas')
    while True:
        opcao = input('Escolha a opção  desejada:\n''1-Consultar Todas Peças\n''2-Consultar Peças por código\n''3-Consultar peça por fabricante\n''4-Sair\n- ')
        if opcao == '1':
            print('Consultar todos')
            for i in listapecas:#percorre toda lista e printa
                for j,k in i.items():
                    print('{}: {}'.format(j,k))
        elif opcao == '2':
            print('Consultar por codigo')
            cod = int(input('Digite o código desejado:\n- '))
            for i in listapecas: #percorre toda a lista porém printa somente o codigo desejado
                if  i['codigo'] == cod:
                    for key,value in i.items():
                        print('{}: {}'.format(key,value))
        elif opcao == '3':
            print('consultar por fabricante')
            fab = input('Digite o fabricante desejado:\n- ')
            for i in listapecas: #percorre toda a lista porém printa somente o fabricante desejado
                if i['fabricante'] == fab:
                    for key, value in i.items():
                        print('{}: {}'.format(key, value))
        elif opcao == '4':
            return #volta para o main
        else:
            print('Digite uma das opções!')
            continue
def removerPeca():
    print('Remover peças')
    valorinput = int(input('Entre com o codigo que deseja remover:\n- '))
    for produto in listapecas: #percorre toda a lista e modifica somente o codigo desejado
        if produto['codigo'] == valorinput:
            listapecas.remove(produto)
            print('Produto Removido!')

#PROGRAMA PRINCIPAL
print('Bem-vindo(a) ao Controle de Estoque da ISIS PAIVA DE SOUSA LIMA')
while True:#while que mantem o usuario no menu até que seja desejada a saida
    opcao= input('Escolha a opção  desejada:\n''1-Cadastrar Peça\n''2-Consultar Peça(s)\n''3-Remover Peça\n''4-Sair\n- ')
    if opcao=='1':
        codigo = codigo+1
        cadastraPeca(codigo)
    elif opcao=='2':
        consultaPeca()
    elif opcao=='3':
        removerPeca()
    elif opcao=='4':
        print('Finalizando programa....')
        break #finaliza o loop e encerra o programa
    else:
        print('Digite uma das opções!')
        continue
