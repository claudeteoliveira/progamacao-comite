carros ={'marca':'fiat',
         'modelo':'uno r',
         'ano':'2002'}
print(carros)
print('            ')

carros.update({'ano':'2007'})
del carros['modelo']
print(carros)
print('            ')

#print(carros['modelo])
print(carros.get('modelo'))