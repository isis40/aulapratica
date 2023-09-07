renda = int(input('Digite o valor da renda mensal liquida: \n-'))
valor_financiamento = int(input('Digite o valor do financiamento: \n-'))
renda_porcetagem = renda/5
if valor_financiamento < renda_porcetagem:
    print('valor do financiamento liberado')
else:
    print('valor do financiamento ultrapassado')