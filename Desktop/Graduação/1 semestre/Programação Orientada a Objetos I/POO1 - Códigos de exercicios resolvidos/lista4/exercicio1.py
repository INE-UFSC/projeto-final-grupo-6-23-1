#exercicio1

lista = []
dic = {}
maior = 0

for z in range(3):
    dic[input('Digite o nome do candidato a Godofor: ')] = int(input('Digite o numero do poder do Godofor: '))

    lista.append(dic.copy())

for i in range(len(lista)):
    for e in dic.values():
        if i == 0:
            
            if e > 0:
                maior = e
        
        if i> 0:
            if e > maior:
                maior = e
        
print(maior)






    
        