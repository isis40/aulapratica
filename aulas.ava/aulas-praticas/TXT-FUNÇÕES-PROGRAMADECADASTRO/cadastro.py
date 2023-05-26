def validar(pergunta, num1,num2):
    x = int(input(pergunta))
    while((x<num1)or(x>num2)):
        x=int(input(pergunta))
    return x
def criaArquivo(nomeArquivo):
    try:
        a = open(nomeArquivo,'wt+')
        a.close()
    except:
        print('ERROR NA CRIAÇÃO DO ARQUIVO')
    else:
        print('Arquivo {} foi criado com sucesso!\n'.format(nomeArquivo))
def existeArquivo(nomeArquivo):
    try:
        a = open(nomeArquivo,'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True
def cadastrarJogo(nomeArquivo,nomeJogo,nomeVideogame):
    try:
        a = open(nomeArquivo, 'at')
    except:
        print('Erro ao abrir o arquivo')
    else:
        a.write('{};{}\n'.format(nomeJogo,nomeVideogame))
    finally:
        a.close()
def listarArquivo(nomeArquivo):
    try:
        a = open(nomeArquivo, 'rt')
    except:
        print('ERRO AO LER O ARQUIVO')
    else:
        print(a.read())
    finally:
        a.close()


#programa principal
arquivo  = 'jogos.txt'
if(existeArquivo(arquivo)):
    print('Arquivo Localizado!')
else:
    print('Arquivo Inexistente')
    criaArquivo(arquivo)

while True:
    print('MENU')
    print('1- Cadastrar')
    print('2- Listar')
    print('3- Sair')

    op  = validar('Digite uma opção\n- ',1 ,3)
    if (op==1):
        nomeJogo= input('Nome do jogo:\n- ')
        nomeVideogame= input('Nome do VideoGame:\n- ')
        cadastrarJogo(arquivo,nomeJogo,nomeVideogame)
    elif(op==2):
        listarArquivo(arquivo)
        print('Fechando o programa...')
        break