saida = ' '
tamanho_piramide = int(input('infoirmwe o tamanho da piramide+1'))



for n in range(1,  tamanho_piramide +1):
    saida += str(n)
    print(saida)

print()    





for n in range(1, tamanho_piramide+1):
    for n2 in range(1, n+1):
            print(n2, end=' ')
    print()