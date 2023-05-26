def fatorial(num=0):
    fat = 1
    if num == 0:
        return fat
    for i in range(1,num+1,1):
        fat*=i
    return fat

x= int(input('Digite um valor para calcular o fatorial:\n- '))
print('{}! = {}'.format(x,fatorial(x)))