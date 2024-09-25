#1708

trapido = int(input('tempo de volta do piloto mais rapido = '))
tdevagar = int(input('tempo de volta do piloto mais devagar = '))

# nvoltasdevagar + 1 = nvoltasrapido

# tdevagar*nvoltasdevagar = trapido*nvoltasrapido

nvoltasdevagar = trapido/(tdevagar - trapido)
nvoltasrapido = nvoltasdevagar+1

print(nvoltasdevagar)
print(nvoltasrapido)