#exercicio 4

primeiranota= float(input( 'qual sua primeira nota?'))
segundanota= float(input( 'qual sua segunda nota?'))
terceiranota= float(input( 'qual sua terceira nota?'))

media= (primeiranota + segundanota + terceiranota) /3

if (5 > media):
    print('Abaixo de 5 – Reprovado')
elif ((5<=media)and(media <= 7)):
    print('Entre 5 e menor que 7 – Em recuperação')
elif (media>=7):
    print('Igual ou maior que 7 – Aprovado')

print(media)

