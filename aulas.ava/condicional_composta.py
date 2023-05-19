#resolver agora descobre se um número inteiro digitado é par ou é ímpar.
valor1 = int(input('Digite o valor: '))

if(valor1 % 2 == 0):
    print('o número: {}. é par!'.format(valor1))
else:
    print('o número: {}. é impar!'.format(valor1))