#2229

i= int(input('Quantas vezes você deseja testar'))

for n in range(i):

    dobradura= int(input('quantas vezes foi dobrado='))
    if dobradura==1:
        print('Foram produzidos 2 pedaços de papel')
    elif dobradura >1:
        print('Foram produzidos', dobradura**2,'pedaços de papel')