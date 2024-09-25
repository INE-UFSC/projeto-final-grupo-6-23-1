futebol = {'André', 'João', 'Lucas', 'Isabela'}
natacao = {'Julia', 'Pedro', 'Ramon', 'Raquel'}
volei = {'Eric', 'Luiz', 'André'} 
basquete = {'Luiz', 'Jacó', 'Mauro'}
total = set()

print('Olá seja bem vindo(a)!! Qual opção abaixo você gostaria :')
print('1 - Mostrar a relação de alunos matriculados por modalidade: Futebol, Basquete, Natação e Vôlei .')
print('2 - Matricula de novos alunos .')
print('3 - Analisar a possibilidade do desconto .')
print('4 - Verificação de numero total de alunos por modalidades e numero total no centro de treinamento .')
while True:
    escolha = int(input('Escolha sua opção : '))
    
    while escolha > 4 or escolha < 0:
        escolha = int(input('Escolha sua opção : '))
    
    if escolha == 1:
        print('Na modalidade futebol estão matriculados(as) : ', futebol) 
        print('Na modalidade natacao estão matriculados(as) : ', natacao)
        print('Na modalidade volei estão matriculados(as) : ', volei)
        print('Na modalidade basquete estão matriculados(as) :', basquete)
        
    if escolha == 2:
        n= str(input('Insira o seu nome :'))
        modalidade = str(input('Em qual das quatro modalidades(Futebol, Natação, Volei, Basquete) você deseja matricular-se?'))
        if modalidade == 'Futebol':
            futebol.add(n)
            
        elif modalidade == 'Natação':
            natacao.add(n)
            
        elif modalidade == 'Volêi':
            volei.add(n)
            
        elif modalidade == 'Basquete' :
            basquete.add(n)

    if escolha == 3:
        print (futebol.intersection(natacao))
        print (futebol.intersection(volei))
        print (futebol.intersection(basquete))
        print (natacao.intersection(volei))
        print (natacao.intersection(basquete))
        print (volei.intersection(basquete))
               
    if escolha == 4:
       
        total = futebol.union(natacao, volei, basquete)
        print(f'O numero de alunos matriculados em futebol é: {len(futebol)}')
        print(f'O numero de alunos matriculados em volei é: {len(volei)}')
        print(f'O numero de alunos matriculados em basquete é:{len(basquete)}')
        print(f'O numero de alunos matriculados em natacao é: {len(natacao)}')
        print(f'O numero total de alunos matriculados é :{len(total)}')

