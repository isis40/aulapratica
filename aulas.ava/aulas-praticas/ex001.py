lado1 = float(input('Digite um lado do triangulo:\n- '))
lado2 = float(input('Digite outro lado do triangulo:\n- '))
lado3 = float(input('Digite outro lado diferente do triangulo:\n- '))
if(lado1 and lado2 and  lado3):
    print('é um triangulo isoceles')
elif(lado1 or lado2 or lado3):
    print('é um triangulo escaleno')
else:
    print('é um triangulo isósceles')

