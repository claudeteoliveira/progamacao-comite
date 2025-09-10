q=float(input("informe um lado do triangulo "))
w=float(input("informe o outro lado do triangulo"))
qw=float(input("informe a base do triangulo"))

if q==w==qw:
    print("tringulo equilatero")
elif q+w>qw:
    print("triangulo isosceles")
else:
    print("triangulo escaleno")

if lado_1 + lado_2 > lado_3:
    print("triangulo valido")

    if lado_1 ==lado_2 == lado_3:
        print("triangulo equilatero")

        elif lado_1 == lado