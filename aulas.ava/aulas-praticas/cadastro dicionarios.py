cadastro = {'nome': [], 'sexo': [], 'ano': []}

while True:
    terminar = input('Deseja cadastar uma pessoa? [S/N]\n- ')
    if terminar.upper() in 'N':
        break
    if terminar.upper() not in 'S':
        print('Digite S para SIM ou N para NÃO')
        continue

    nome = input('Qual seu nome?\n- ')
    sexo = input('Qual seu sexo? [M/F]\n- ')
    ano = int(input('Qual seu ano de nascimento?\n- '))
    cadastro['nome'].append(nome)
    cadastro['sexo'].append(sexo.upper())
    cadastro['ano'].append(ano)

print(cadastro)