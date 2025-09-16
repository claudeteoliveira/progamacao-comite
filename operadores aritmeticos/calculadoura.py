numero_1 = int(input("escolha um numero ->"))
numero_2 = int(input("escolha um segundo numero"))
operacao = input("qual calculo vai ser usado!")

if operacao == " + " :
    soma = numero_1 + numero_2
    print("o resultado da soma é", soma )
elif operacao == " - ":
    soma = numero_1 - numero_2
    print("o resultado é", soma)
elif operacao == "*":
    soma =numero_1 * numero_2
    print("a multiplicacao é",soma )
elif operacao == " / ":
    soma = numero_1 / numero_2
    print("a divisão é", soma)
else:
    print("a operacao e invalida")

