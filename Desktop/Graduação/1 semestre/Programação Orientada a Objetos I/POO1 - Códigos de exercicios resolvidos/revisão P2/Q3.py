#André Thiago Pfleger (22200345) Questão 3

lista = []

while True:

    n = int(input('Qual o tamanho da colunas: '))
    m = int(input('Qual o tamanho de linhas: '))

    if n == 0:
        break
    
    if m == 0:
        break
    
    else:
        for linha in range(n):   
            listafinal = []
            for coluna in range(m):
                one_zero = int(input(f'Indique se há pão de queijo nessa posição{linha},{coluna}: '))
                
                if one_zero == 1:
                    one_zero = 9
                listafinal.append(one_zero)
                
            lista.append(listafinal)                    
    
        for linha in range(n):    
            for coluna in range(m):
                if one_zero == 0:   
                
                    if linha == 0:
                        if coluna == 0:
                            
                            if lista[linha][coluna+1] == 9:
                                lista[linha][coluna] += 1
                                
                            if lista[linha+1][coluna] == 9:
                                lista[linha][coluna] += 1
                                
                        if m > coluna > 0 :
                            if lista[linha+1][coluna] == 9: 
                                lista[linha][coluna] += 1
                            
                            if lista[linha][coluna+1] == 9:
                                lista[linha][coluna] += 1
                                
                            if lista[linha][coluna-1] == 9:
                                lista[linha][coluna] += 1
                        
                            if lista[linha-1][coluna] == 9:
                                lista[linha][coluna] += 1 
                        
                        if coluna == m-1:
                            
                            if lista[linha-1][coluna] == 9:
                                lista[linha][coluna] +=1
                            if lista[linha][coluna-1] == 9:
                                lista[linha][coluna] += 1  

                    if linha > 0:
                        if coluna == 0:
                            
                            if lista[linha-1][coluna] == 9:  
                                lista[linha][coluna] += 1
                                
                            if lista[linha+1][coluna] == 9:
                                lista[linha][coluna] += 1
                                    
                            if lista[linha][coluna+1] == 9:
                                lista[linha][coluna] += 1
                                
                        if m > coluna > 0:
                            if lista[linha+1][coluna] == 9: 
                                lista[linha][coluna] += 1
                                
                            if lista[linha][coluna+1] == 9:
                                lista[linha][coluna] += 1
                                
                            if lista[linha-1][coluna] == 9:
                                lista[linha][coluna] += 1
                                
                            if lista[linha-1][coluna] == 9:
                                lista[linha][coluna] += 1
                                
                            if lista[linha][coluna-1] == 9:
                                lista[linha][coluna] += 1
                                
                    if linha == n-1:
                         
                        if coluna == 0:
                            if lista[linha-1][coluna] == 9: 
                                lista[linha][coluna] += 1
                                
                            if lista[linha][coluna+1] == 9:
                                lista[linha][coluna] += 1
                                
                        if m > coluna > 0:
                            if lista[linha+1][coluna] == 9:
                                lista[linha][coluna] += 1
                            
                            if lista[linha][coluna+1] == 9:
                                lista[linha][coluna] += 1
                                 
                            if lista[linha][coluna-1] == 9:
                                lista[linha][coluna] += 1
                    
            for linha in range(n):
                for coluna in range(m):
                     print(f'[{lista[linha][coluna]:^5}]',end=" ")
            print(lista)
                    

