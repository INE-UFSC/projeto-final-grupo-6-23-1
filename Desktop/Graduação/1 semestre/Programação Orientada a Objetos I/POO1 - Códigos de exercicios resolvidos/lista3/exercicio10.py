#exercicio10

soma= 0

for n in range(5):
    aluno= str(input(' Qual o seu nome?'))
    nota= float(input('Qual a sua nota?'))
    
    if n==0:
        notamaior= nota
        notamenor= nota
        soma= soma + nota
        nomemaior= aluno
    else:
        if nota > notamaior:
            notamaior = nota
            nomemaior= aluno
            
        if  nota < notamenor:
            notamenor = nota
            
        soma= soma + nota
    
media= soma/5
print('Média da turma = ', media)
print('Nome do aluno com nota mais alta = ', nomemaior, 'nota do aluno', notamaior)

if notamaior >= 5.75:
    print('Aprovado')
elif (nota >=2.75) and (nota < 5.75):
    print('Recuperação')
else:
    print('Reprovado')