from random import randint
from time import sleep
pc = randint(0, 5)
print('Escolhi um número entre 0 e 5 e duvido que você descubra qual é!')
pl = int(input('Digite seu palpite [0/5]: ').strip())
print('PROCESSANDO...')
sleep(0.5)
if pl == pc:
    print(f'Você acertou! o número escolhido foi o {pc}!')
else:
    print(f'O número escolhido não fora o {pl}, escolhi o {pc}, tente novamente!')
