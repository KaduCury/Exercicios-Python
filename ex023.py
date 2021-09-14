n = int(input('Digite um número de 0 a 9999: '))
print('''O número {} possui:
{} milhares,
{} centenas,
{} dezenas
e {} unidades.'''.format(n, (n // 1000 % 10), (n // 100 % 10), (n // 10 % 10), (n // 1 % 10)))
