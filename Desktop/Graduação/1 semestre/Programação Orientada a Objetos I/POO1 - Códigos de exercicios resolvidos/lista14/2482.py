dic = {} 

n = int(input('Quantidade de traduções: '))

for i in range(n):
    dic[input('Digite o nome do país: ')] = str(input('Digite o "Feliz Natal" do país que você deseja registrar: '))
print(dic)

qtd_criancas = int(input('Qual a quantidade de crianças: '))
for i in range(qtd_criancas):
        pais = str(input('Digite o país da criança: '))
        print(dic.get(pais, 'Não encontrado'))  