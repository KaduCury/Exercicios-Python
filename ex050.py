soma = 0
par = 0
for c in range(0, 6):
    n = int(input('Digite um número inteiro: '))
    if n % 2 == 0:
        par += 1
        soma += n
if par > 1:
    print(f'O valor da soma dos {par} números pares informados é {soma}.')
elif par == 1:
    print(f'Você informou apenas o número {soma} par.')
else:
    print('Você não informou nenhum número par.')
