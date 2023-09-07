import random as rd
# funções
def menu():
    print('-Calculadora-')
    num1 = int(input('Digite um número:\n- '))
    return num1

def somar(num1):
    num2 = int(input('Digite o valor a somar com o primeiro número:\n- '))
    resultado = num1 + num2
    return num2, resultado


def subtrair(num1):
    num2 = int(input('Digite o valor a subtrair com o primeiro número:\n- '))
    resultado = num1 - num2
    return num2, resultado


def dividir(num1):
    num2 = int(input('Digite o valor a dividir com o primeiro número:\n- '))
    resultado = num1 / num2
    return num2, resultado


def multiplicar(num1):
    num2 = int(input('Digite o valor a multiplicar com o primeiro número:\n- '))
    resultado = num1 * num2
    return num2, resultado


# principal
num_fechamento = rd.randint(1, 100)
num1 = rd.randint(1, 100)
while (num_fechamento != num1):
    print('O número aleátorio é {}, faça-o chegar em {}'.format(num1, num_fechamento))
    x = int(input('Digite o que Deseja fazer:\n'
                  '1-Somar\n'
                  '2-Subtrair\n'
                  '3-Dividir\n'
                  '4-Multiplicar\n- '))
    if (x == 1):
        num2, resultado = somar(num1)
        print('O resultado de {} + {} = {}'.format(num1, num2, resultado))
        num1 = resultado
    elif (x == 2):
        num2, resultado = subtrair(num1)
        print('O resultado de {} - {} = {}'.format(num1, num2, resultado))
        num1 = resultado
    elif (x == 3):
        num2, resultado = dividir(num1)
        print('O resultado de {} ÷ {} = {}'.format(num1, num2, resultado))
        num1 = resultado
    elif (x == 4):
        num2, resultado = dividir(num1)
        print('O resultado de {} x {} = {}'.format(num1, num2, resultado))
        num1 = resultado
    else:
        print('\033[1;31mDigite uma das opções!\033[m')
        continue
print('\033[1;32mVocê Ganhou!, fechando o programa...\033[m')