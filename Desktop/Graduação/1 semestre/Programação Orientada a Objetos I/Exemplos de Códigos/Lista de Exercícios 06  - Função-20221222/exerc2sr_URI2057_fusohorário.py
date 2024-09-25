#Exercício 02  - URI 2057
#sem o uso de return

def fuso(s,t,f):
    horario = s+t+f
    if horario > 24:
        print(horario-24)
    elif horario<0:
        print(horario+24)
    else:
        print(horario)
        
#programa principal    
result = False
while (result == False):
    s, t, f = input('Digite a hora de saída, o tempo de viagem e o fuso horário do destino com relação a origem: ').split()
    s = int(s)
    t = int(t)
    f = int(f)
    if 0<=s<=23 and 1<=t<=12 and -5<=f<=5:
        fuso(s,t,f)
        result = True
    else:
        result = False
        
            
            


