#exercicio4
contPar=0
contImpar=0

for i in range(5):
    numero= int(input('escreva um numero inteiro='))
    if numero%2==0:
        contPar = contPar+1
    else:
        contImpar = contImpar+1
    
print("quantidade de numeros pares digitados", contPar )
print("quantidade de numeros impares digitados", contImpar )
    
  
    
    