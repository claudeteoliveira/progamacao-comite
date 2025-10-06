usuario = "admin "
senha = " 123456"
tentativas = 3

while tentativas > 0:
    if input('informe o usuario') == usuario:
        if input('informe a senha') ==senha:
            print(f' bem vindo{usuario}')
            break
        else: 
            print('senha incorretr5a, tente novamente')

            tentativas -= 1

            print(f' tentativas restantes {tentativas}')
    else:
        print('usuario incorreto, tente novamente')

        tentativas -= 1
        print('tentativas restantes {tentativas}')