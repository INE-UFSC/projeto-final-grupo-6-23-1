lista = []
maior = 0
segundomaior = 0

while True:
    
    n = int(input('Escreva o numero de casos de teste : '))
    for i in range(n):
        pont_suspeito = int(input(f'O quão suspeita a pessoa {i+1} é:'))
        
        if i == 0:
            maior = pont_suspeito
        
        if i == 1:
            if pont_suspeito > maior:
                segundomaior = maior
                maior = pont_suspeito
            else:
                segundomaior = pont_suspeito
            
        if i > 1:
            if pont_suspeito >= maior:
               segundomaior = maior
               maior = pont_suspeito
            
            if pont_suspeito < maior and pont_suspeito > segundomaior:
               segundomaior = pont_suspeito
        lista.append(pont_suspeito)
    print(segundomaior)
    
        
        
    print(lista)
    lista.clear()
    continuação = str(input('Deseja continuar? [S/N]'))
    if continuação == 'S':
        pass
        
    else:
        break
        
    
    



