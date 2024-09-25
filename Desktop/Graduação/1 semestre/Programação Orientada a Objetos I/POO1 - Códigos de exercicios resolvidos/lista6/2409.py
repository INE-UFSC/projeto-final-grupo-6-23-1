def colchao (h,l,a,b,c):
    # h > l
    # a < b < c
    if (a <= l) and (b <= h):
        return 'S'
    else:
        return 'N'

h= int(input('altura da porta = '))
l= int(input('largura da porta = '))
a= int(input('dimensão do primeiro lado do colchão = '))
b= int(input('dimensão do segundo lado do colchão = '))
c= int(input('dimensões do terceiro lado do colchão = '))

saida = colchao (h,l,a,b,c)

print(saida)