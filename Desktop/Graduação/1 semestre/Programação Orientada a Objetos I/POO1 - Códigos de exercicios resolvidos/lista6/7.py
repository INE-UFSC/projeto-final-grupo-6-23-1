soma = 0
cont= 0
notamaior= 0

def calculo (soma , cont):
    media= soma/cont
    
    return media

for i in range(5):
    nota= float(input('Escreva uma nota = '))
    soma = soma + nota
    cont= cont + 1

    if i == 0:
        notamaior = nota
        
    if i>0:
        if nota > notamaior:
            notamaior = nota
    
if notamaior >=5.75:
    print('Você Está Aprovado E Sua Nota É: {}'.format(notamaior))
    
elif 5.75 >=notamaior >=2.75:
    print('Você Está Recuperação E Sua Nota É: {}'.format(notamaior))
    
else:
    print('Você Está Reprovado E Sua Nota É: {}'.format(notamaior))
    
resultado = calculo(soma , cont)
print('A maior nota é {}'.format(notamaior))
print('A media é {}'.format(resultado))
    
    