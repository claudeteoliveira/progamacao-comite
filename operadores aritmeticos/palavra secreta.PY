palavra = ''

palavra_secreta = int(input('fale uma palavra secreta' ))
palavra_encontrada = ['-'] * len(palavra_secreta)

chute_letra = ''
tentativas = 4

for tentativa in range(tentativas+1):
      chute_letra = input('chute uma letra {palavra_encontrada}')

    for t in range(len(palavra_secreta)):
        if palavra_secreta{t}== chute_letra:
        palavra_encontrada{t} =chute_letra
    if '-'not in palavra_encontrada:
        print(você venceu!!!)
              break
    print(f'faltan apenaqs (tentativas - tentativas)tentativas')

else:
     print(f('você perdeu, a palavra era (palav ra_secreta)'))    

        
            







