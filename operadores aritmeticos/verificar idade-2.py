idade = int("input(informe uma idade"))

if idade>= 0 and idade <= 12:
    print("vocce é criança!")

elif idade >= 13 and idade <= 17:
    print("voce é adolecente!")

elif idade > 17:
    print("voce é adulto")

else:
    print("idade invalida")            