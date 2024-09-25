lista = []
somapar = 0
somadiagonal = 0
soma_acimadiagonal = 0
soma_ultima = 0
menornumero = 0
cont = 0
n = int(input('Quais as dimensôes da matriz: '))

for i in range(n):
    listafinal = []
    for j in range(n):
       number = int(input(f'Escreva um numero para a posição {i},{j} : '))
       
       #para a escolha 1 a seguir:
       
       if number % 2 == 0:
           somapar += 1
       
       #para a escolha 2 a seguir:
           
       if i ==j:
           somadiagonal = number + somadiagonal
           med = somadiagonal / n
        
       #para a escolha 4 a seguir:
       
       if i : # i qualquer
           if j + 1: #j seguinte
             soma_acimadiagonal = soma_acimadiagonal + number
             cont += 1
             mediaacima = soma_acimadiagonal / cont
       
       #para a escolha 5 a seguir:
             
       if i == 0:
           if j == n:
               soma_ultima = soma_ultima + number
               
       if i > 0:
           if j == n:
               soma_ultima = soma_ultima + number
               
       
               
       #para a escolha 6 a seguir:
       
       if i == 0:
           if j == 0:
               menornumero = number
               
           if j > 0:
               if number < menornumero:
                   menornumero = number
           
       listafinal.append(number)
       
    lista.append(listafinal)

for i in range(0,n):
    for j in range(0,n):
        print(f'[{lista[i][j]:^5}]',end=" ")
    print()
       
print('Escolha uma das 6 possibilidades abaixo: ')
print('1 - Mostrar a soma de todos os elementos pares da matriz')
print('2 - Mostrar a média dos elementos da diagonal principal')
print('3 - Mostrar o produto dos elementos da diagonal secundária')
print('4 - Mostrar a média dos elementos acima da diagonal principal')
print('5 - Mostrar a soma dos elementos da última coluna da matriz')
print('6 - Mostrar o menor valor da primeira linha da matriz')

escolha = int(input('Escolha a sua opção: '))

if escolha == 1:
    print(somapar)
    
if escolha == 2:
    print(med)

if escolha == 3:
    print()

if escolha == 4:
    print(mediaacima)
    
if escolha == 5:
    print(soma_ultima)
    
if escolha == 6:
    print(menornumero)