#1
notas = []
soma = 0
maiornota= -1
menornota = 11

for i in range(3):
     
        notas.append(int(input('Digite a nota do aluno=')))
            
        soma = soma + notas[i]
        if maiornota < notas[i]:
            maiornota = notas[i]
            
        if menornota > notas[i]:
            menornota = notas[i]  

media= soma/3
print('As notas do aluno são: {}'.format(notas))
#print('A média do aluno é: {:.2f}'.format(media))
print('A média do aluno é: {}'.format(round(media, 2)))
print('A maior nota é : {}'.format(maiornota))
print('A menor nota é : {}'.format(menornota))
print('A diferença entre as notas é : {}'.format(maiornota - menornota))