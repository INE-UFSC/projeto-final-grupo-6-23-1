dic = {}
lista = []

def informações():

    while True:
        print('============>>MENU<<============')

        print('1)	Cadastrar usuário)')
        print('2)	Imprimir dados (pesquisar pelo nome)')
        print('3)	Imprimir dados (todos os usuários)')
        print('4)	Encerrar o programa')
        print(32*'=')

        escolha = int(input('Escolha uma das opções acima: '))

        if escolha == 1:
            dic['nome'] = str(input('Digite o nome: ')).upper()
            dic['ano de nascimento'] = 2022 - int(input('Qual seu ano de nascimento: '))
            dic['carteira de trabalho'] =  int(input('Quantos anos possui de carteira de trabalho: '))
            
            if dic['carteira de trabalho'] > 0:
                dic['ano da contratação'] = int(input('Qual o ano da sua contratação: '))
                dic['salario'] = int(input('Qual seu salário atual: '))
                dic['idade que vai se aposentar'] = dic['ano da contratação'] + 35
                
            if dic['carteira de trabalho'] == 0:
                dic['ano da contratação'] = print('Não possui ano de contratação')
                dic['salario'] = print('Não possui salário')
                dic['idade que vai se aposentar'] = print('Indefinida a idade que irá se aposentar')
            
            lista.append(dic.copy())
            
            print('Usuário Cadastrado com sucesso! Operação Finalizada.')
        
        if escolha == 2:
            user = str(input('Qual usuário você gostaria de imprimir os dados: ')).upper()
            
            for i in range(len(lista)):
                
            
                if dic['nome'] == user:
                    print(dic)
                    
                else:
                    print('Usuário não cadastrado.')
            
        if escolha == 3:
            print('Segue abaixo as informações relacionadas a todos os usuários: ')
            print(lista)
            
        if escolha == 4:
            break
