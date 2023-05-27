#Função que pergunta altura, comprimento, largura. Valida os dados e calcula o volume depois condicionalmente retorna o valor
def dimensoesObjeto(x=0):
    try:
        valor =  0
        altura = float(input('Digite a altura do objeto em centimetros:\n- '))
        comprimento = float(input('Digite agora o comprimento do objeto em centimetros:\n- '))
        largura = float(input('Digite agora a largura do objeto em centimetros:\n- '))
        volume = largura*comprimento*altura
    except ValueError:
        print('Digite um valor númerico!')

    if (volume < 1000):
        valor = 10
    elif (1000 <= volume < 10000):
        valor = 20
    elif (10000 <= volume < 30000):
        valor = 30
    elif(30000 <= volume < 100000):
        valor = 50
    elif(volume>=100000):
        print('valor não aceito')
    return valor

#Função que pergunta o peso do objeto em quilos, valida e atraves de condição determina o peso e retorna
def pesoOjeto(x=0):
    multiplicador = 0
    try:
        peso = float(input('Qual o peso do objeto em KG?\n- '))
    except ValueError:
        print('Digite um valor númerico!')

    if(peso <= 0.1):
        multiplicador = 1
    elif(0.1 <= peso < 1):
        multiplicador = 1.5
    elif(1 <= peso < 10):
        multiplicador =  2
    elif(10 <= peso < 30):
        multiplicador = 3
    elif(peso >= 30):
        print('Valor não aceito')
    return multiplicador

#Função que pergunta a rota do objeto desejada, condicionalmente define o multiplicador e retorna
def rotaObjeto(x= 0):
    mult = 0
    rota = input('Selecione uma das rotas:\nRS- Rio de Janeiro até São Paulo.\nBS- Brasília até São Paulo.\nBR- Brasília até Rio de Janeiro.\n- ')
    if(rota=='RS'):
        mult = 1
    elif(rota=='BS'):
        mult = 1.2
    elif(rota=='BR'):
        mult = 1.5
    else:
        print('Digite uma das opções!')
    return mult


#programa principal
print('Bemvindo(a) a Companhia de Logistica Isis Paiva de Sousa Lima')
try:
    a = dimensoesObjeto()
    b = pesoOjeto()
    c = rotaObjeto()
    ValorTotal = a * b * c
    print('Total a pagar(R$): {:.2f}. (dimensões: {}R$ * peso: {} * rota: {}.)'.format(ValorTotal,a,b,c))
except:
    print('Preencha os Dados Corretamente!')
