#O exercício a seguir lê dois valores numéricos inteiros e compara se o primeiro é maior do que osegundo, utilizando uma condicional simples. Caso seja (resultado verdadeiro), ele imprime na tela a
#mensagem informando que o primeiro valor digitado é maior do que o segundo.

valor1 = int(input('Digite o primeiro valor: '))
valor2 = int(input('Digite o segundo valor: '))

if(valor1 > valor2):
    print('o primeiro valor: {}, é maior que o segundo valor: {}.'.format(valor1, valor2))