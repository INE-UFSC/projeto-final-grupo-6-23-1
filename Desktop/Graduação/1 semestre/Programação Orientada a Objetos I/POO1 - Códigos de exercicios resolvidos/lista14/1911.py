dicionario = {}
cont = 0

while True:
    
    n_test = int(input('Digite o numero de casos de teste: '))
    if n_test == 0:
        break
    else:
        for i in range(n_test):
            n_alunos = int(input('Qual o numero de alunos na turma: '))
            dicionarios = []
            for c in range(n_alunos):
                dicionarioaluno = {}
                dicionarioaluno['nome'] = input('Digite o nome do aluno: ')
                dicionarioaluno['assinatura'] = str(input('Assine aqui: '))
                dicionarios.append(dicionarioaluno)
            
            contassinaturas = 0
            for dicionarioaluno in dicionarios:
                conterro = 0
                for i in range(len(dicionarioaluno['nome'])):
                    if dicionarioaluno['nome'][i] != dicionarioaluno['assinatura'][i]:
                        conterro += 1
                    if conterro == 2:
                        contassinaturas += 1
                        break
            
            print(contassinaturas)

    
    
    
    
    