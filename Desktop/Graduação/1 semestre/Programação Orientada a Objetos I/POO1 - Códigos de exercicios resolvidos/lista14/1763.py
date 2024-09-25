#1763

my_dict = {'brasil': 'Feliz Natal!', 'alemanha' : ' Frohliche Weihnachten!' , 'austria' : 'Frohe Weihnacht!', 'coreia' : 'Chuk Sung Tan!' , 'espanha' : 'Feliz Navidad!' , 'grecia' : 'Kala Christougena!' , 'estados-unidos' : 'Merry Christmas!' , 'inglaterra': 'Merry Christmas!' , 'australia' : 'Merry Christmas!' , 'portugal' : 'Feliz Natal!' , 'suecia' : 'God Jul!', 'turquia' : 'Mutlu Noeller' , 'argentina' : 'Feliz Navidad!' , 'chile' : 'Feliz Navidad!' , 'mexico' : 'Feliz Navidad!' , 'antardida' : 'Merry Christmas!' , 'canada' : 'Merry Christmas!' , 'irlanda' : 'Nollaig Shona Dhuit!' , 'belgica' : 'Zalig Kerstfeest!' , 'italia' : 'Buon Natale!' , 'libia' : 'Buon Natale!' , 'siria' : 'Milad Mubarak!' , 'marrocos' : 'Milad Mubarak!' , 'japao' : 'Merii Kurisumasu!'}
n_casos = int(input('Quantos lugares no mundo: '))
for i in range(n_casos):

    nome_pais = str(input('Indique qual o nome do pais: '))
    print(my_dict.get(nome_pais, 'Não encontrado'))
