teste= int(input('Quantos testes você deseja realizar?'))
for i in range(teste):
    conta= str(input('Digite um numero, uma letra e um numero =')).split()
    
    primeiro = conta[0]
    segundo = conta [1]
    terceiro = conta [2]
    
    primeiro = int(primeiro)
    
    terceiro = int(terceiro)
    
    if primeiro == terceiro:
        print( primeiro * terceiro)
    elif segundo == segundo.upper() and primeiro != terceiro:
        print(terceiro - primeiro)
    elif segundo == segundo.lower() and primeiro != terceiro:
        print(primeiro + terceiro) 

    
    
    
    