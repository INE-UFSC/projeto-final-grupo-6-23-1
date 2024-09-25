#exercicio10

a= int(input('Qual a pontuação do competidor a?'))
b= int(input('Qual a pontuação do competidor b?'))
c= int(input('Qual a pontuação do competidor c?'))

if (a>b) and( b> c):
    print(b)
elif (b>a) and (a>c):
    print(a)
elif (c>a)and(a>b):
    print(a)
elif (c>b)and(b>a):
    print(b)
elif (a>c)and(c>b):
    print(c)
elif (b>c)and (c>a):
    print(c)
    
