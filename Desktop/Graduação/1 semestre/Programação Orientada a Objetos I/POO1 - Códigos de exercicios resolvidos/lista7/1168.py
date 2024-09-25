soma = 0
n= int(input('Quantos casos de teste você deseja realizar?'))

for i in range(n):
    
    soma = 0
    
    numero= input('Qual numero você deseja montar com os leds?').split()
    
    for j in range(len(numero)):
    
        if int(numero[j]) == 1:
            soma = soma + 2
            
        elif int(numero[j]) == 2:
            soma = soma + 5
            
        elif int(numero[j]) == 3:
            soma = soma + 5
            
        elif int(numero[j]) == 4:
            soma = soma + 4
            
        elif int(numero[j]) == 5:
            soma = soma + 5
            
        elif int(numero[j]) == 6:
            soma = soma + 6
            
        elif int(numero[j]) == 7:
            soma = soma + 3
            
        elif int(numero[j]) == 8:
            soma = soma + 7
            
        elif int(numero[j]) == 9:
            soma = soma + 6
            
        elif int(numero[j]) == 0:
            soma = soma + 6
            
    print(soma, 'Leds')
        
        
        
        
        
        
        
        
        
        
    