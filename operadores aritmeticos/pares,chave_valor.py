carros ={'gipe':'renegete',
         'fiat':'uno',
         'ano':'215'}

for chave in carros.keys():
    print(f'chave {chave } | ', end=' ')
   
print('\n')

for chave in carros.values():
    print(f'chave {chave } | ', end=' ')

print('\n')

for chave, valor in carros.items():
    print(f'chave {chave} | valor {valor}')

print('\n')


