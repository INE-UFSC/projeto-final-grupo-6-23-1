#1437

atualizacaolado= 'Norte'

lados= str(input('Para quais lados você deseja virar? ')).split()

for i in range(len(lados)):
    
    if atualizacaolado == 'Oeste' and lados[i] == 'D':
        atualizacaolado = 'Norte'
        
    elif atualizacaolado == 'Oeste' and lados[i] == 'E':
        atualizacaolado = 'Sul'
        
    elif atualizacaolado == 'Leste' and lados[i] == 'D':
        atualizacaolado = 'Sul'
        
    elif atualizacaolado == 'Leste' and lados[i] == 'E':
        atualizacaolado = 'Norte'
        
    elif atualizacaolado == 'Norte' and lados[i] == 'E':
        atualizacaolado = 'Oeste'
        
    elif atualizacaolado == 'Norte' and lados[i] == 'D':
        atualizacaolado = 'Leste'
        
    elif atualizacaolado == 'Sul' and lados[i] == 'E':
        atualizacaolado = 'Oeste'
        
    elif atualizacaolado == 'Sul' and lados[i] == 'D':
        atualizacaolado = 'Leste'
    
print(atualizacaolado)