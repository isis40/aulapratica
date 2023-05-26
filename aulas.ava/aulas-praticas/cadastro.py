def validar(programa1 = 0,programa2 = 0, resposta=0):
    while(resposta != 3):
        if(resposta == 1):
            programa1,
            resposta=int(input('Selecione uma das opções\n- '))
        elif(resposta ==2):
            programa2
            resposta=int(input('selecione uma das opções\n- '))
        else:
            print('Digite uma das opções!\n- ')
            resposta = int(input())
    print('Saindo do programa...')
    return resposta

def cadastrar(nome,plataforma):

x = validar(1,2,int(input('Digite um numero\n- ')))