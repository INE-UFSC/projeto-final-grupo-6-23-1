soma = 0
cont = 0
soma2 = 0
cont2 = 0
soma3 = 0
cont3 = 0

n= str(input('Escreva o nome do primeiro aluno: '))
j= str(input('Escreva o nome do segundo aluno: '))
f= str(input('Escreva o nome do terceiro aluno:'))

matriz=[[n,0,0,0],[j,0,0,0],[f,0,0,0]]

for l in range(0,3):
    for c in range(1,4):
        matriz[l][c]= int(input(f'Digite uma nota para posição [{l},{c}]: '))
        if l == 0:
            cont = cont + 1
            soma = soma + matriz[l][c]
            media = soma / cont
            
        if l == 1:
            cont2 = cont2 + 1
            soma2 = soma2 + matriz[l][c]
            media2 = soma2 / cont2
            
        if l == 2:
            cont3 = cont3 + 1
            soma3 = soma3 + matriz[l][c]
            media3 = soma3 / cont3
        
print('Muito bem!!! Tudo prenchido com sucesso =D')
print('Agora qual resultado você gostaria de conferir?')
print('Se você gostaria de conferir a media de cada aluno, digite "1", caso deseje consultar alguma nota parcial digite "2":')
print(matriz)

escolha = int(input('Digite o que você gostaria de escolher: '))
if escolha == 1:
    
    print(media)
    print(media2)
    print(media3)

if escolha == 2:
    posL = int(input('Digite a linha que você deseja consultar: '))
    posC = int(input('Digite a coluna que você deseja consultar: '))
    l = posL - 1  
    c = posC - 1

    print(matriz[l][c])