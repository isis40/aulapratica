nome = input('Qual o seu nome?\n- ')
idade = int(input('Qual sua idade?\n- '))
if(nome == 'Vinicius'):
    print('Seja bem vindo! Vinicius!')
elif(idade<18):
    print('Você é menor de idade!')
elif(idade>100):
    print('Desculpe você possivelmente não existe!')