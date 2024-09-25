class Veiculos:
    def __init__(self,nome,cor,preço):
        self.nome = nome
        self.cor = cor
        self.preço = preço
        
    def getNome(self):
        return self.nome
    
    def setNome(self,nome):
        self.nome = nome
        
    def getCor(self):
        return self.cor
        
    def setCor(self,cor):    
        self.cor = cor
        
    def getPreço(self):
        return self.preço
    
    def setPreço(self, preço):
        self.preço = preço   
    
    def __str__(self, vendas):
        print('O numero total de vendas é:', vendas)
    
class Carros(Veiculos):
    def __init__(self,nome,cor,preço,IDCarros):
        super().__init__(nome,cor,preço)
        self.IDCarros = IDCarros
    
    def getIDCarros (self):
        return self.IDCarros
    
    def setIDCarros (self, IDCarros):
        self.IDCarros = IDCarros
    
    def __str__(self, vendascarros):
        print('O número de carros vendidos foram:', vendascarros )

class Motos(Veiculos):
    def __init__(self,nome,cor,preço,IDmoto):
        super().__init__(nome,cor,preço)
        self.IDmoto = IDmoto
    
    def getIDmoto (self):
        return self.IDmoto
    
    def setIDmoto (self, IDmoto):
        self.IDmoto = IDmoto

    def __str__(self, vendasmotos):
        print('o número de motos vendidas foram:', vendasmotos)
    