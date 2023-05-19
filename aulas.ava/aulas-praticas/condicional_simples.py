#ex01 se idade maior que 60 escreva voce tem d ireito aos beneficios
idade = int(input('Qual sua idade?\n- '))
if(idade>60):
    print('você tem direitos aos beneficios')
else:
    print('você não tem direito')
#ex02 se dano é maior que 10 e escudo é igual a 0, escreva  voce esta morto
dano =  int(input('Qual o dano?\n- '))
escudo = int(input('Qual o escudo?\n- '))
escudo =  (escudo-dano)
if(dano>10 and escudo <= 0):
    print('Você está morto!')
else:
    print('Você está vivo!')
#ex03 Se pelo menos uma das variaveis booleanas norte, sul, leste, oeste resultarem em true escreva= voce escapou
if(norte or sul or oeste or leste):
    print('Você escapou!')