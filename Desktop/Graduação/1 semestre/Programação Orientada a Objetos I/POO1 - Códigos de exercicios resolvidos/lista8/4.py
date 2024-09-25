listaX = []

k = int(input('Digite um numero para "k" = '))
n= int(input('Quantos numeros você deseja ler?'))

for i in range(n):
    numeros = int( input('Qual numero você deseja adicionar a lista = '))
    listaX.append (numeros)
    
novalista = []
for i in range(n):
    novalista.append (listaX[i]*k)
    
    
print(novalista)