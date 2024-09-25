def novogod (lista):
    for i in range(n):
        if i == 0:
            maiorpoder = lista[i]['poder']
            novogodofor  = lista[i]['nome']
        
        if i > 0:
            if lista[i]['poder'] > maiorpoder:
                maiorpoder = lista[i]['poder']
                novogodofor = lista[i]['nome']
            elif lista[i]['poder'] < maiorpoder:
                pass
            
            elif lista[i]['poder'] == maiorpoder:
                if novogodofor > lista[i]['nome']:
                    novogodofor = lista[i]['nome']
                    
                elif novogodofor ==  lista[i]['nome']:
                    print('Empate')
                    
            
    return novogodofor
#André Thiago Pfleger (22200345) Questão 1



dic = {}
lista = []
maiorpoder = 0


n = int(input('Quantos candidatos: '))

for i in range(n):
    dic['nome'] = str(input('Digite o nome: '))
    dic['poder'] = int(input('Qual o poder: '))
    lista.append(dic.copy())
    
print(lista)

#escolha do novo godofor

        
a = novogod (lista)

print('Resultado Oficial:', a , 'será o novo Godofor')
        
         
            
    
