import random
import time
pc = random.randint(0, 2)
print('''
JOKEMPÔ!!!

[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
player = int(input('Faça sua escolha [0, 1 ou 2]: '))
print('''
PROCESSANDO...''')
time.sleep(2)
print('''
JO''')
time.sleep(1)
print('KEM')
time.sleep(1)
print('''PO!
 ''')
if pc == player:
    print('Empatou! Escolhemos o mesmo!')
elif pc == 0 and player == 1:
    print('Você GANHOU! Escolhi PEDRA e Você escolheu PAPEL!')
elif pc == 0 and player == 2:
    print('Você PERDEU! Escolhi PEDRA e Você escolheu TESOURA!')
elif pc == 1 and player == 0:
    print('Você PERDEU! Escolhi PAPEL e Você escolheu PEDRA!')
elif pc == 1 and player == 2:
    print('Você GANHOU! Escolhi PAPEL e Você escolheu TESOURA!')
elif pc == 2 and player == 0:
    print('Você GANHOU! Escolhi TESOURA e Você escolheu PEDRA!')
elif pc == 2 and player == 1:
    print('Você PERDEU! Escolhi TESOURA e Você escolheu PAPEL!')
else:
    print('JODADA INVÁLIDA!')
