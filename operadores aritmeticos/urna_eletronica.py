opção = -1
senha_encerrar = 1903
encerrar_votaçao=1900
candidatos = []
contagem_votos ={'nulos': 0}

#menu principal
while opção != senha_encerrar:
    opção = input('o que deseja fazer? \n'
                  'opção 1: cadastrar candidato \n'
                  'opção 2:iniciar votação'
                  'opção 3: mostrar voto e vencedor \n'
                  'opção 0: sair \n\n'
                  'opção -> ')
    
    #valida se a opção é um numero
    if opção.isdigit():
        opção = int(opção)

        #testar para opção urna
        if opção == 1:
            qtd_candidatos = int(input('qtd candidatos deseja cadastrar -> '))
            
            for c in range(1, qtd_candidatos+1):
                candidato = []
                nome_candidato = input(f'nome do candidato {c} -> ')
                num_candidato = int(input(f'numero do candidato {c} -> '))

                #salva candidato
                candidato.append(nome_candidato)
                candidato.append(num_candidato)
                #adiciona candidato na lista principal
                candidato.append(tuple(candidato))

            print('\n\n')

        if opção == 2:
            voto =-1
        
            #mostrar lista de candidatos
            while voto != encerrar_votaçao:
                for candidato in candidatos:
                    print(f'candidato {candidato[0]} | numero{candidato[1]}')
                          
                voto = int(input('vote no numero de um candidato ->'))

                #contabilizar a votação
                cont = 0
                for candiudato in candidatos:
                    cont += 1
                    if voto == candidato[1]:
                        if candidato[0] not in contagem_votos:
                            contagem_votos.update({candidato[0]: 1})
                            break
                        else:
                            contagem_votos[candidato[0]] += 1
                            break
                    else:
                        if cont == len(candidatos):
                            contagem_votos['nulos'] += 1
        elif opção == 3:
            #remove nulo incorreto da saida da votação '1900'
            contagem_votos['nulos'] -= 1

            #mostra resultados e vencedor
            maioir = 0
            vencedor = ''
            for key, value in contagem_votos.items():
                if value > maior:
                    maior = value
                    vencedor = key
                print(f'{key} | votos {value}')

            print(f'o vencedor é {vencedor} com {maior} votos')
            print('\n\n')
        # se a opção digitada não for um numero cai aqui
    else:
        print('\n\nopção invalida\n\n')                    
                










#valida se a 0pção


