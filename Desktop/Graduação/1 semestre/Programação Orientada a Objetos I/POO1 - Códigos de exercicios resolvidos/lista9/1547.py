lista = []

qtd_teste = int(input('Escreva o numero de casos de teste: '))
maisproximo = 0

for i in range(qtd_teste):
    n_alunos = int(input('Escreva o numero de alunos que irão dar palpites: '))
    n_secreto = int(input('Qual o numero secreto: '))
    for j in range(n_alunos):
        numeros = int(input('Quais os numeros ditos pelos respectivos alunos: '))
        
        if j == 0:
            maisproximo = numeros
            posicao = j
                
        else:
            if numeros == n_secreto:
                maisproximo = numeros
                posicao =j
                
            if maisproximo > numeros > n_secreto:
                maisproximo = numeros
                posicao = j
            
            if maisproximo < numeros < n_secreto:
                maisproximo = numeros
                posicao = j
            if maisproximo < n_secreto < numeros:
                if n_secreto - maisproximo > numeros - n_secreto:
                    maisproximo = numeros
                    posicao = j
                if n_secreto - maisproximo < numeros - n_secreto:
                    maisproximo = maisproximo
                    posicao = j
            if maisproximo > n_secreto > numeros:
                if maisproximo - n_secreto > n_secreto - numeros:
                    maisproximo = numeros
                    posicao = j
                if maisproximo - n_secreto < n_secreto - numeros:
                    maisproximo = maisproximo
                    posicao = j
    print(f'O numero mais proximo do numero secreto é o: {maisproximo} na posição {j}')
                


