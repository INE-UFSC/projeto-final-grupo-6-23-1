pessoa = {}

pessoa['nome'] = str(input('Qual seu nome: '))
pessoa['idade'] = int(input('Qual o ano de nascimento: '))
pessoa['carteira de trabalho'] = int(input('Quantos anos de trabalho: '))

if pessoa['idade'] > 0:
    print('Sua idade é: ', 2022 - pessoa['idade'])
    
if pessoa['carteira de trabalho'] != 0:
    pessoa['ano que foi contratado'] = int(input('Qual o ano da sua contratação: '))
    pessoa['salario'] = int(input('Qual seu salário: '))
    print('Será possível se aposentar a partir de: ', pessoa['ano que foi contratado'] + 35)
    










print('PESQUISE AQUI: ')
print('1 - Cadastrar usuário')
print('2 - Imprimir dados (pesquisar pelo nome)')
print('3 - Imprimir dados (todos os usuários)')
print('4 - Encerrar o programa')

print(100*'-')

escolha = int(input('Escolha uma das acimas: '))

    
    
 
 
 
if escolha == 2:
    for v in pessoa.values():
        nome = str(input('digite um nome: '))
        if nome == v:
            break
            print(v)
        
        
        
 
 
 
 
 
 