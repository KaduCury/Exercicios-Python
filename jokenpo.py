from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Suas opções:
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura''')
jogador = int(input('Qual é a sua jogada? '))
print('-=' * 16)
print('O Jogador escolheu {}.'.format(itens[jogador]))
print('O Computador escolheu {}.'.format(itens[computador]))
print('=-' * 16)
if computador == 0: # computador jogou Pedra
    if jogador == 0:
        print('EMPATOU!')
    elif jogador == 1:
        print('VOCÊ GANHOU!!!')
    elif jogador == 2:
        print('Você perdeu...')
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 1: # computador jogou Papel
    if jogador == 0:
        print('Você perdeu...')
    elif jogador == 1:
        print('EMPATOU!')
    elif jogador == 2:
        print('VOCÊ GANHOU!!!')
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 2: # computador jogou Tesoura
    if jogador == 0:
        print('VOCÊ GANHOU!!!')
    elif jogador == 1:
        print('Você perdeu...')
    elif jogador == 2:
        print('EMPATOU!')
    else:
        print('JOGADA INVÁLIDA!')
