qtd_letras_maiuscula = 0
alfabeto = "ABCDEEFGHIJLMNOPQRSTUVWXYZ"
palavra = input ("informe uma palavra")
for letra_maiuscula in palavra:
    for letra in alfabeto:
        if letra_maiuscula == letra:
            qtd_letras_maiuscula += 1

print(qtd_letras_maiuscula)            