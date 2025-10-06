import random
n = random.randint (1, 100)
chute = 0
tentativas = 0

while True:
    chute = int(input('chute um numero'))
    tentativas += 1

    if chute == n:
        print(f'parabens você acertou co {tentativas} tentativas')
        break
    elif chute < n:
        print(f'o numero {chute}é menor que o numero secreto')
    elif chute > n:
        print(f'o numero {chute}é maior que o numero secreto')
    
