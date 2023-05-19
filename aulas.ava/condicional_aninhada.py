maça = 2.30
laranja = 3.60
banana = 1.85
res  = int(input('Qual fruta você deseja?\n1.Maçã: \n2.laranja: \n3.banana:\n- '))
unidades = int(input('Quantas unidades?\n- '))
if(res == 1):
    print('o valor para {} unidades de maçã, será: {:.2f}RS'.format(unidades,(maça*unidades)))
elif(res == 2):
    print('o valor para {} unidades de laranja, será: {:.2f}RS'.format(unidades, (laranja * unidades)))
elif(res == 3):
    print('o valor para {} unidades de banana, será: {:.2f}RS'.format(unidades, (banana * unidades)))
else:
    print('Você precisa escolher um dos valores!')