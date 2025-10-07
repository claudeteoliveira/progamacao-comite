numeros = []
for i in range(5):
    numeros.append(int(input(f'informe o {i+1}° numero')))

print(f'os numeros digitados foram', end=' ')
for i in numeros:
    print(i, end=' ')    
print(f'\no maior numero digitado foi {max(numeros)}')
print(f'o menor numero digitado foi {min(numeros)}')
print(f'a média dos numeros é {sum(numeros)/len(numeros)}')    
