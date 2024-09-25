#1150

X = int(input("Qual o valor de x= "))
Z = int(input("Qual o valor de z= "))

while Z <= X:
    Z = int(input("Qual o valor de Z= "))

contador = 0
soma = 0

while soma <= Z:
    soma = soma + (X + contador)
    contador += 1
    
print("Quantos inteiros= {}".format(contador))