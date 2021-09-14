divisores = 0
n = int(input('Informe um número para saber se ele é primo: '))
for c in range(1, n+1):
    if n % c == 0:
        divisores += 1
if divisores == 2:
    print(f'O número {n} é primo. Sendo divisível apenas {divisores} vezes, por 1 e por {n}.')
elif divisores != 2:
    print(f'O número {n} não é primo. Sendo divisível {divisores} vezes.')
