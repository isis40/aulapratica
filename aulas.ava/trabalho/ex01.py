#inicio do programa
print('Bem-vindo(a) a Loja da Isis Paiva de Sousa Lima')
#variaveis a serem guardadas e digitadas pelo usuário
valorProduto = float(input('Digite o Valor do Produto:\n- '))
quantidadeProduto = float(input('Digite a Quantidade do Produto:\n- '))
valorsemdesc = valorProduto * quantidadeProduto #calcula o preço total
print('O valor total sem desconto é: {:.2f}R$.'.format(valorsemdesc))
#estrutura condicional que determina o tamanho do desconto e imprime na tela com o valor em reais
if(quantidadeProduto <= 9):
    print('O valor total com desconto é: {:.2f}R$ (desconto 0%).'.format(valorsemdesc))
elif(quantidadeProduto >= 10 or quantidadeProduto <= 99):
    print('O valor total com desconto é: {:.2f}R$ (desconto 5%).'.format(valorsemdesc - (valorsemdesc * 5 / 100)))
elif(quantidadeProduto >= 100 or quantidadeProduto <= 999):
    print('O valor total com desconto é: {:.2f}R$ (desconto 10%).'.format(valorsemdesc - (valorsemdesc * 10 / 100)))
elif(quantidadeProduto >= 1000):
    print('O valor total com desconto é: {:.2f}R$ (desconto 15%).'.format(valorsemdesc - (valorsemdesc * 15 / 100)))
else:
    print('Digite um valor positivo, fechando o programa...')
