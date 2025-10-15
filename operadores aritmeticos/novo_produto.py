estoque = {'caderno': '10',
           'lapiz': '25',
           'mochila': '87'
}
print('adicionado um novo itm ao estoque')
estoque['corretivo'] = 45

print('estoque atualizado')
for chave, valor in estoque,items():
    print(f'produto - {chave}' | qtd produto - {valor})

print('removendo um produto do estoque')
del estoque['lapiz']

print('estoque atualizado')
for chave, valor in estoque.items():
    print6(f'produto - {chave} | qtd produto - {valor}')

                print('limpando o estoque')
                estoque.clear()
                print(f'estoque limpo - {estoque}')
        
        