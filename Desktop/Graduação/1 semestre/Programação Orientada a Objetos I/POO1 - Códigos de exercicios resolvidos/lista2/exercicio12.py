#exercicio 12

d= int(input('Dia que registrou o preço da ação da NlogNintendo= '))
i= int(input('Preço inicial registrado na NlogNintendo= '))
x= int(input('Variação diária do preço da ação= '))
f= int(input('Numero de dias que deve prever= '))

# Número de dia impar
if (d % 2) == 1:
    # Número de dias que quero prever impar
    if (f % 2) == 1:
        print(i + x)
    # Número de dias que quero prever par
    else:
        print(i)

# Número de dia par
else:
    # Número de dias que quero prever impar
    if (f % 2) == 1:
        print(i - x)
    # Número de dias que quero prever par   
    else:
        print(i)