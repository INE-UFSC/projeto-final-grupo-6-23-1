#exercicio3

for n in range(0,5):
    aluno= str(input('Qual o seu nome?'))
    media= int(input('Qual sua média geral?'))
    mensalidade= int(input('Qual sua mensalidade?'))
    
    if n==0:
        alunomais = aluno
        mediamais = media
        mensalidademais = mensalidade
    else:
        if media > mediamais:
            mediamais = media
            alunomais= aluno
            mensalidademais = mensalidade
    
print('aluno com nota mais alta:', alunomais)
print('aluno com media mais alta:', mediamais)
print('mensalidade do aluno com media mais alta', mensalidademais)
print('Desconto', mensalidademais *0.7)