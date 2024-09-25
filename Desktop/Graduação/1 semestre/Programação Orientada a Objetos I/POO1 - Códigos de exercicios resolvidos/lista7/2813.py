#2813

saldoE = 0
saldoC = 0
compraE= 0
compraC= 0

N= int(input('Quantidade de dias previstos pelo sistema metereológico = '))
for i in range(N):
    previsão = input('Qual a previsão para a ida ao trabalho = ').split()
    SD= previsão[0]
    SN= previsão[1]
    
    
    if SD == 'CHUVA' and saldoC == 0:
        compraC = compraC + 1
        saldoE = saldoE + 1
    
    if SD == 'CHUVA' and saldoC != 0:
        saldoC = saldoC - 1
        saldoE = saldoE + 1
    
    if SN == 'CHUVA' and saldoE == 0:
        compraE = compraE + 1
        saldoC = saldoC + 1
    
    if SN == 'CHUVA' and saldoE != 0:
        saldoC = saldoC + 1
        saldoE = saldoE - 1
    
print(compraC , compraE)
    
    