notaf1 = int(input('Digite a primeira nota: '))
notaf2 = int(input('Digite a segunda nota: '))
notaf3 = int(input('Digite a terceira nota: '))
nota_final = notaf1>=7 and notaf2>=7 and notaf3>=7
if(nota_final==True):
    print('o aluno passou de ano!')
else:
    print('o aluno reprovou de ano!')