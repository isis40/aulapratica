#Função que cria a vizualização do Menu
def Menu():
    print('*********************Cardápio*********************')
    print('| Código |       Descrição          |  Valor  |')
    print('|  100   |     Cachorro Quente      |   9,00  |')
    print('|  101   |  Cachorro Quente Duplo   |  11,00  |')
    print('|  102   |          X-Egg           |  12,00  |')
    print('|  103   |         X-Salada         |  12,00  |')
    print('|  104   |         X-Bacon          |  14,00  |')
    print('|  105   |         X-Tudo           |  17,00  |')
    print('|  200   |    Refrigerante Lata     |   5,00  |')
    print('|  201   |        Chá Gelado        |   4,00  |')


# programa principal
print('Bem-vindo(a) a lanchonete da Isis Paiva de Sousa Lima')
preco = 0.00
while True:
    Menu()
    cod = int(input('Digite o Código do produto:\n- '))
    if (cod == 100):
        print('Você pediu um Cachorro Quente no valor de R$9,00')
        preco += 9.00
    elif (cod == 101):
        print('Você pediu um Cachorro Quente Duplo no valor de R$11,00')
        preco += 11.00
    elif (cod == 102):
        print('Você pediu um X-Egg no valor de R$12,00')
        preco += 12.00
    elif (cod == 103):
        print('Você pediu um X-Salada no valor de R$12,00')
        preco += 12.00
    elif (cod == 104):
        print('Você pediu um X-Bacon no valor de R$14,00')
        preco += 14.00
    elif (cod == 105):
        print('Você pediu um X-Tudo no valor de R$17,00')
        preco += 17.00
    elif (cod == 200):
        print('Você pediu um Refrigerante Lata no valor de R$5,00')
        preco += 5.00
    elif (cod == 201):
        print('Você pediu um Chá Gelado no valor de R$4,00')
        preco += 4.00
    else:
        print('opção inválida')
        continue
    opcao = int(input('Deseja pedir mais alguma coisa?\n1 - Sim\n0 - Não\n- '))
    if(opcao==1):
        continue
    elif(opcao==0):
        print('o total a ser pago será {:.2f}R$'.format(preco))
        print('Saindo do programa...')
        break
    else:
        print('Digite uma das opções')
        continue

