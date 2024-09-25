dic ={}
lista = []

def contaehd(lista):
    
    contehd = 0
    for i in range(len(lista)):
        if lista[i]['sigla'] == 'ehd':
            contehd += 1
    
    return contehd
    
def contaepr(lista):
    contepr = 0
    for i in range(len(lista)):
        if lista[i]['sigla'] == 'epr':
            contepr += 1
            
    return contepr

def containtrusos(lista):
    contintrusos = 0
    for i in range(len(lista)):
        if lista[i]['sigla'] != 'epr':
            if lista[i]['sigla'] != 'ehd':
                contintrusos +=1
            
    return contintrusos

n = int(input('Quantos alunos: '))

for i in range(n):
    dic['matricula'] = int(input('Digite sua matricula: '))
    dic['sigla'] = str(input('Qual a sigla do curso: '))
    lista.append(dic.copy())
    
print(lista)

intrusos = containtrusos(lista)
ehd = contaehd(lista)
epr = contaepr(lista)

print('O numero de alunos intrusos é:',intrusos)
print('O numero de alunos do curso de engenharia hidrica é: ',ehd)
print('O numero de alunos do curso de engenharia de produção é: ', epr)


    
    
    