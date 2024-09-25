#exercicio7
somaIdade = 0
n= int(input('digite o numero de pessoas='))
for i in range(n):
    idade= int(input('escreva a sua idade?'))
    somaIdade = somaIdade + idade
    
media= somaIdade/n

if (media<=25):
    print('Jovem')  
elif (media<= 60):
    print('Adulto')
else:
    print('Idoso')
        
    


