#2418
soma = 0

for n in range(5):
    num = float(input('digite a nota = '))
    while num<5:
        print('Numero indisponivel')
    
    if n== 0:
        maiornota = num
        menornota = num
    
        
    if num>maiornota:
        maiornota = num
        
    if num<menornota:
        menornota = num
        
        
    soma = soma+ num

soma = soma - maiornota - menornota
media = soma/3
print("Soma = ", soma)
print('media = ', media )
        
    
        
    
        
