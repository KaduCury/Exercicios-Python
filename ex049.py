import time
n = int(input('Digite o número que você quer saber a tabuada: '))
print(f'A Tabuada do {n} é...')
time.sleep(1)
for c in range(0, 11):
    print('{} X {:2} = {}'.format(n, c, n * c))
    time.sleep(4/5)
