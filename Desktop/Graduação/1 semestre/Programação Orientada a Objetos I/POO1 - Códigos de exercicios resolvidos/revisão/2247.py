n= int(input('Digite o numero de testes = '))

soma= 0

for i in range(n):
    
    z= int(input('Quanto deseja depositar para zezinho?'))
    j= int(input('Quanto deseja depositar para joaozinho?'))

    
    if n==1:
        if z>j:
            print(z-j)
        
        elif z<j:
            print(z-j)
        
        elif z==j:
            print(0)
        
            soma= soma + z 
            
    if n>1:
        
        if z>j:
            print(z-j)
        
        elif z<j:
            print(z-j)
        
        elif z==j:
            print(0)
            
            soma= soma + z 
    
print(soma)
            

        
    
    
            
            
    
        
    
        
    
        
        
        
    
        
    
    
