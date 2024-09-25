lista = list()
lista2 = list()

soma= 0

n = int(input(" Escreva o numero de células no tabuleiro = "))

#cria a lista
for i in range(n):
    minas = int(input( "Digite se há ou não há bombas nessa posição :"))
    lista.append(minas)
print(lista)
'''
if i == 0:
    if minas > 0:
        soma = soma + minas
           
if i > 0:
    if minas > 0 :
        soma = (0 + minas) + soma[i-1]
        soma[i-1] = soma + minas
        
    lista2.append(soma)

print(lista2)
'''




