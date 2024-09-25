contadorC=0
contadorR=0
contadorS=0


casosdeteste= int(input('digite um numero para casos de teste ='))

for n in range(casosdeteste):
    quantidade= input(' digite o que foi testado=').split()

    quant = int(quantidade[0])
    tipo = quantidade[1]
    
    if tipo == "C":
        contadorC += quant
        
    elif tipo == "R":
        contadorR += quant
        
    elif tipo == "S":
        contadorS += quant

total = contadorS+ contadorR + contadorC

print( "TOTAL DE COBAIAS=", (total))
print( "TOTAL DE RATOS=", (contadorR))
print( "TOTAL DE COELHOS=", (contadorC))
print( "TOTAL DE SAPOS=", (contadorS))
print( "PERCENTUAL DE RATOS= %.2f"% (contadorR*100/total))
print( "PERCENTUAL DE COELHOS= %.2f"% (contadorC*100/total))
print( "PERCENTUAL DE SAPOS= %.2f"% (contadorS*100/ total))
       
       
