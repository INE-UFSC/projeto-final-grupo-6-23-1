#Exer3 - URI 1150 Ultrapassando Z

def ultrapassandoZ(x, y):
    cont = 0
    som = 0
    while y > som:
        som = som + x
        x = x + 1
        cont = cont + 1
    print(cont)


#programa principal
x = int(input("x:"))
while True:
    y = int(input("y:"))
    if y > x:
        break 
    else:
        print("Digite o valor de y novamente.")

ultrapassandoZ(x,y)
print("Fim.")