lista = []

n = int(input('Digite a altura do pulo do sapo: '))
canos = int(input('Digite a quantidade de canos: '))
att_altura = 0
att_erro = 0

for i in range(canos):
    altura = int(input('Escreva a altura dos respectivos canos: '))
    lista.append(altura)
    
    if i == 0:
        if -n<= altura <= n:
            att_altura = altura
            
        else:
            att_erro = 1
            
    if i > 0:
        if att_altura + n == altura:
            att_altura = altura
            
        elif att_altura - n == altura:
            att_altura = altura
            
        elif att_altura + n < altura :
            att_erro = 1
            
        elif att_altura - altura > altura :
            att_erro = 1
            
        elif att_altura - altura < altura :
            att_altura = altura
            
        elif att_altura + n > altura:
            att_altura = altura
         
        if att_erro == 1:
            break
    
if att_erro == 0:
    print('YOU WIN!!!')
    
elif att_erro == 1:
    print('GAME OVER!!!')
    
print(lista)
