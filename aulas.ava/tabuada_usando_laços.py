#tabuada de 2 while
tabuada = 1
while(tabuada <= 10):
    print('tabuada do {}:'.format(tabuada))
    i=1
    while(i<=10):
        print('{} x {} = {}'.format(tabuada,i,(tabuada*i)))
        i += 1
    tabuada += 1
###############################################################################################
tabuada de 2 for
for i in range(1,11):
    print('tabuada do {}:'.format(i))
    for j in range(1, 11):
        print('{} x {} = {}'.format(i,j,(i*j)))
###############################################################################################
#tabuada while e for
tabuada = 1
while(tabuada <=10):
    print('tabuada do {}'.format(tabuada))
    for i in range(1,11):
        print('{} x {} = {}'.format(tabuada,i,(tabuada*i)))
    tabuada +=1