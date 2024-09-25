#exercicio 15

horainicial= int(input( 'qual a hora inicial do jogo?'))
minutoinicial= int(input( 'qual o minuto inicial do jogo?'))
horafinal= int(input('qual a hora final do jogo?'))
minutofinal= int(input( 'qual o minuto final do jogo?'))

if(horafinal > horainicial):
    if(minutofinal >= minutoinicial):
        print(horafinal - horainicial, 'horas')
        print(minutofinal - minutoinicial, 'minutos')
    
    elif(minutofinal < minutoinicial):
        print(horafinal - horainicial - 1, 'horas')
        print(minutofinal - minutoinicial +60, 'minutos')

elif(horafinal < horainicial):
    if( minutofinal >= minutoinicial):
        print(horafinal - horainicial + 24, 'horas')
        print(minutofinal - minutoinicial -60, 'minutos')
        
    elif( minutofinal < minutoinicial):
        print(horafinal - horainicial, 'horas')
        print(minutofinal - minutoinicial, 'minutos')
        
elif (horafinal == horainicial) and (minutoinicial == minutofinal):
        print('24 horas')