#exercicio2

def calculartempo (horasaida, tempoviagem, relacaoorigem):
    
    horaquevaichegar= horasaida + tempoviagem + relacaoorigem
    if horaquevaichegar > 24:
        print(horaquevaichegar % 24)
        
    else:
        print(horaquevaichegar)
        
horasaida= int(input('digite o horario que você saiu = '))
tempoviagem= int(input('digite o tempo da viagem = '))
relacaoorigem= int(input('digite o fuso horario em relação a origem = '))


calculartempo(horasaida, tempoviagem, relacaoorigem)

