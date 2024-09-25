#calculo

def printQuadrante(x,y):

    if (x>0) and (y>0):
        print('primeiro')
    
    elif (x<0) and (y>0):
        print('Segundo')
        
    elif (x<0) and (y<0):
        print('Terceiro')
        
    elif (x>0) and (y<0):
        print('Quarto')

while True:
    #leitura
                
    x= int(input('escreva um valor para x='))
    y= int(input('escreva um valor para y='))
    
    if x==0 or y==0:
        break
    
    #chamando a funçao

    printQuadrante(x,y)
