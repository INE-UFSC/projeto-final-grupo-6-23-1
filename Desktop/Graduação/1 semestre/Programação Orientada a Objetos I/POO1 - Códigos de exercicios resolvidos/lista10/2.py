EmpresaCOCA = {'Raul','Ivonei','João','Rony','Isabella','Juliana','Ralf'}
EmpresaCOLA = {'Filipe','Gustavo','Júlia','Ivonei','Isabella','Raul','Teodoro'}


print('1 - Mostrar (imprimir na tela) a relação de clientes cadastrados por empresa.')
print('2 - Cadastro de novos clientes em qualquer das modalidades')
print('3 - Verificação se existem clientes já cadastrados nas 2 empresas. E quais são estes clientes.')
print('4 - Numero de clientes')
print(143*'-')

escolha = int(input('Escreva qual a sua opção : '))

if escolha == 1:
    print('Na empresaCOCA estão cadastrados:', empresaCOCA)
    print('Na empresaCOLA estão cadastrados:', empresaCOLA)
    
if escolha == 2:
    nome= str(input('Qual seu nome? '))
    empresa= str(input('Qual empresa você gostaria de ser cadastrado : '))
    
    if empresa == 'EmpresaCOCA':
        EmpresaCOCA.add(nome)
    
    elif empresa == 'EmpresaCOLA':
        EmpresaCOLA.add(nome)
        
    elif empresa == 'Ambas':
        EmpresaCOCA.add(nome)
        EmpresaCOLA.add(nome)
        
if escolha == 3:
    print('Os clientes que estão cadastrados nas duas empresas são: ',EmpresaCOCA.intersection(EmpresaCOLA))
    

if escolha == 4:
    print('Os clientes cadastrados na EmpresaCOCA são: ', len(EmpresaCOCA))
    print('Os clientes cadastrados na EmpresaCOLA são: ', len(EmpresaCOLA))
    print('Clientes já pertencentes a ambas as empresas são: ', len(EmpresaCOCA.union(EmpresaCOLA)))
    print('O numero totais de clientes na Empresa é : ', len(EmpresaCOCA.union(EmpresaCOLA) + EmpresaCOCA.intersection(EmpresaCOLA)))