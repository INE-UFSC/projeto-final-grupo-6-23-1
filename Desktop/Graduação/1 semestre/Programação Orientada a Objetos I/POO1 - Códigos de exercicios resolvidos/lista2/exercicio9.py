#exercicio 9

a= float(input( 'Qual valor você deseja para A? '))
b= float(input( 'Qual valor você deseja para B? '))
c= float(input( 'Qual valor você deseja para C?'))

delta= (b**2 - 4*a*c)

if (delta < 0):
    print('impossivel calcular')
else:
    x1= (-b + delta**(1/2))/(2*a)
    x2= (-b - delta**(1/2))/(2*a)
    
    print(x1)
    print(x2)
    
    



    
