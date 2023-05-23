inicial = int(input('Qual o inicio da contagem?'))
final =  int(input('Qual o valor deseja encerrar a contagem?'))
x = inicial
while(x <=final):
    if(x % 2 ==0):
        print(x)
    x = x + 1