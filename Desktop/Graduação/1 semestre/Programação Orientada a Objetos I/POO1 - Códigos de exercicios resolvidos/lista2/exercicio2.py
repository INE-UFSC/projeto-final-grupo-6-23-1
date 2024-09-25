#exercicio 2

valor= int(input('Qual o valor do produto?'))
condicaodepagamento = str(input('Como você deseja realizar o pagamento?'))


# à vista (dinheiro ou cheque) – 10% de desconto
if (condicaodepagamento == 'a') :
    print(valor*0.9)

# 1x no cartão – 5% de desconto
elif (condicaodepagamento =='b') :
    print(valor*0.95)

# 2x cartão – preço normal
elif (condicaodepagamento == 'c') :
    print(valor)

# 3x ou mais no cartão - 20% de juros
elif (condicaodepagamento == 'd') :
    print(valor*1.2)
