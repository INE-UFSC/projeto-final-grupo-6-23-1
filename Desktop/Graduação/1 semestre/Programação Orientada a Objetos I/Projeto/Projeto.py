from Classes import Veiculos
from Classes import Carros
from Classes import Motos

ListaCarros = []
ListaMotos = []
IDmoto = 0
IDCarro = 0
vendas = 0
vendasmotos = 0
vendascarros = 0
v = Veiculos('','','') #Criei para conseguir imprimir o texto(para polimorfismo)
while True:   
    print('<-=-=-=-=-=-=-=-=-=-=-=-=-=-=-MENU-=-=-=-=-=-=-=-=-=-=-=-=-=-=>')
    print('1 - Cadastrar Veiculo')
    print('2 - Alterar Veiculo')
    print('3 - Consultar Veiculo|Adicionar venda')
    print('4 - Excluir Veiculo')
    print('<-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=->')
    escolha = str(input('Escolha uma das opções acima: '))
    
    if escolha == '1':
        print('Qual veiculo você deseja cadastrar? [Carro|Moto]')
        esc = str(input('Sua escolha:')).upper()
        if esc == 'MOTO':
            nome = str(input('Qual o nome do modelo: '))
            cor = str(input('Qual a cor: '))
            preço = str(input('Qual o preço: '))
            IDmoto += 1
            print(f'ID da moto: {IDmoto}') 
            m = Motos('','','','')
            m.setIDmoto(str(IDmoto))
            m.setNome(nome)
            m.setCor(cor)
            m.setPreço(preço)
         
            ListaMotos.append(m)
            
        elif esc == 'CARRO':
            nome = str(input('Qual o nome do modelo: '))
            cor = str(input('Qual a cor: '))
            preço = str(input('Qual o preço: '))
            IDCarro += 1
            print(f'ID do carro: {IDCarro}')
            c = Carros('','','','')
            c.setIDCarros(str(IDCarro))
            c.setNome(nome)
            c.setCor(cor)
            c.setPreço(preço)
                       
            ListaCarros.append(c)
        
        else:
            pass
        
    elif escolha == '2':
        decisão = str(input('Qual veiculo você pretende alterar: [Carro|Moto]')).upper()
        if decisão == 'CARRO':
           idcarro = str(input('Qual o ID do carro: '))
           flag = False
           for i in ListaCarros:
               if idcarro == i.getIDCarros():
                   nome = str(input('Digite o novo nome deste modelo: '))
                   cor = str(input('Digite a nova cor deste modelo: '))
                   preço = int(input('Digite o novo preço: '))
                   
                   i.setNome(nome)
                   i.setCor(cor)
                   i.setPreço(preço)
                   flag = True
           if flag == False:
               print('Não será possível alterar pois o id não foi encontrado')
        
        elif decisão == 'MOTO':
           idmoto = str(input('Qual o ID da moto: '))
           flag = False
           for i in ListaMotos:
               if idmoto == i.getIDmoto():
                   nome = str(input('Digite o novo nome deste modelo: '))
                   cor = str(input('Digite a nova cor deste modelo: '))
                   preço = int(input('Digite o novo preço: '))
                   
                   i.setNome(nome)
                   i.setCor(cor)
                   i.setPreço(preço)
                   flag = True
           if flag == False:
               print('Não será possível alterar pois o id não foi encontrado')
               
        else:
            pass
        
    elif escolha == '3':
        decida = str(input('Qual veiculo você pretende consultar: [Carro|Moto] ')).upper()
        if decida == 'CARRO':
            print('<-=-=-=-=-=-=-=-=-=-=-=-=-=-Formas de consulta=-=-=-=-=-=-=-=-=-=-=-=-=-=-=->')
            print('1 - Consultar pelo nome do modelo')
            print('2 - Consultar pelo ID')
            consulta = int(input('Escolha uma das acimas: '))
            if consulta == 1:
                digite_o_nome = str(input('Digite o nome do modelo: '))
                flag = False
                for i in ListaCarros:
                    if digite_o_nome == i.getNome():
                        print('<-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-Informações do veiculo-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=->')
                        print('Nome do modelo:', i.getNome())
                        print('Cor do modelo:', i.getCor())
                        print('Preço do modelo:', i.getPreço())
                        print('Id do modelo:', i.getIDCarros())
                        print('<-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=>')
                        flag = True
                        comprar = str(input('Deseja comprar este veiculo: [S|N]')).upper()
                        if comprar == 'S':
                            vendas += 1
                            vendascarros += 1
                            c.__str__(vendascarros)
                            v.__str__(vendas)
                        elif comprar == 'N':
                            print('Ok, compra não realizada')
                            
                        else:
                            pass                            
                                                
                if flag == False:
                    print('Não há esse nome cadastrado')
                                       
            if consulta == 2:
                digite_o_idcarros = str(input('Digite o id do modelo: '))
                flag = False
                for i in ListaCarros:
                    if digite_o_idcarros == i.getIDCarros():
                        print('<-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-Informações do veiculo-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=->')
                        print('Nome do modelo:', i.getNome())
                        print('Cor do modelo:', i.getCor())
                        print('Preço do modelo:', i.getPreço())
                        print('Id do modelo:', i.getIDCarros())
                        print('<-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=>')
                        flag = True
                        comprar = str(input('Deseja comprar este veiculo: [S|N]')).upper()
                        if comprar == 'S':
                            vendas += 1
                            vendascarros += 1 
                            c.__str__(vendascarros)
                            v.__str__(vendas)
                            
                        elif comprar == 'N':
                            print('Ok, compra não realizada')
                            
                        else:
                            pass                
                if flag == False:
                    print('Não há esse id cadastrado')
            else:
                pass
            
        if decida == 'MOTO':
            print('<-=-=-=-=-=-=-=-=-=-=-=-=-=-Formas de consulta=-=-=-=-=-=-=-=-=-=-=-=-=-=-=->')
            print('1 - Consultar pelo nome do modelo:')
            print('2 - Consultar pelo ID:')
            
            cons = int(input('Escolha uma das acimas: '))
            if cons == 1:
                digite_nome = str(input('Digite o nome do modelo: '))
                flag = False
                for i in ListaMotos:
                    if digite_nome == i.getNome():
                        print('<-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-Informações do veiculo-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=->')
                        print('Nome do modelo: ', i.getNome())
                        print('Cor do modelo: ', i.getCor())
                        print('Preço do modelo: ', i.getPreço())
                        print('Id do modelo: ', i.getIDmoto())
                        print('<-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=>')
                        flag = True
                        comprar = str(input('Deseja comprar este veiculo: [S|N]')).upper()
                        if comprar == 'S':
                            vendas += 1
                            vendasmotos += 1
                            m.__str__(vendasmotos)
                            v.__str__(vendas)
                        elif comprar == 'N':
                            print('Ok, compra não realizada')
                            
                        else:
                            pass
                if flag == False:
                    print('Não há esse nome cadastrado')

            if cons == 2:
                digite_o_idc = str(input('Digite o id do modelo: '))
                flag = False
                for i in ListaMotos:
                    if digite_o_idc == i.getIDmoto():
                        print('Nome do modelo:', i.getNome())
                        print('Cor do modelo:', i.getCor())
                        print('Preço do modelo:', i.getPreço())
                        print('Id do modelo:', i.getIDmoto())
                        flag = True
                        comprar = str(input('Deseja comprar este veiculo: [S|N]')).upper()
                        if comprar == 'S':
                            vendas += 1
                            vendasmotos += 1
                            m.__str__(vendasmotos)
                            v.__str__(vendas)
                        elif comprar == 'N':
                            print('Ok, compra não realizada')
                            
                        else:
                            pass                
                    
                if flag == False:
                    print('Não há esse id cadastrado')
            else:
                pass
            
        else:
            pass
                        
    elif escolha == '4':
        flag = False
        veiculo_selecionado = str(input('Qual veiculo você deseja selecionar para excluir: [Carro|Moto]')).upper()
        if veiculo_selecionado == 'CARRO':
            id_exc_carro = str(input('Qual id do carro:'))
            for i,j in enumerate(ListaCarros):
                if id_exc_carro == j.getIDCarros():
                    ListaCarros.pop(i)
                    flag = True
            if flag == False:    
                print('Não foi possível excluir pois esse id não está cadastrado')
                
        if veiculo_selecionado == 'MOTO':
            id_exc_moto = str(input('Qual o id da moto:'))
            
            for e,r in enumerate(ListaMotos):
                if id_exc_moto == r.getIDmoto():
                    ListaMotos.pop(e)           
                    
                    flag = True
            if flag == False:
                print('Não foi possível excluir pois esse id não está cadastrado')
        else:
            pass    
        
    else:
        pass