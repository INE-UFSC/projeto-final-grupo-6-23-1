#exercicio 3

peso= float(input( 'qual seu peso?'))
altura= float(input( 'qual sua altura?'))
imc= peso/ (altura*altura)

if imc <18.5:
    print('Abaixo de 18,5 – abaixo do peso')
if 18.5<imc<25:
    print('Entre 18.5 e 25 – peso ideal')
if 25<imc<30:
    print('Entre 25 e 30 - sobrepeso')
if 30<imc<40:
    print('Entre 30 e 40 - obesidade')
if imc>40:
    print('Acima de 40 - obesidade mórbida')
    
print(imc)
    
    


print( peso)
print(altura)


