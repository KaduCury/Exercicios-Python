# numero = int(input('Digite um número: '))
# resultado = numero % 2
# print('O resultado foi {}.'.format(resultado))
# if resultado == 0:
#    print('O número {} é par.'.format(numero))
# else:
#    print('O número {} é ímpar.'.format(numero))
#from random import randint
#poui = input('Escolha par ou ímpar: ')
#njo = int(input('Escolha um número: '))
#npc = int(randint(0 , 1))
#result = njo + npc % 2
#if result == 0:
 #   if poui == par:
  #      print('Você escolheu Par e Venceu!')
   # elif poui == ímpar:
    #    print ('O computador escolheu Par e Venceu!')
#else:
 #   if poui == ímpar:
  #      print('Você escolheu Ímpar e Venceu!')
   # elif poui == par:
    #    print('O computador escolheu Ímpar e Venceu!')

from random import randint
v=0
while True:
    jogador = int(input('Diga o valor: '))
    pc = randint(0, 10)
    total = jogador + pc
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    print(f'Você escolheu {jogador} e o computador escolheu {pc}. A soma desses números é {total}.', end='')
    print(' Deu par!' if total % 2 == 0 else ' '
                                             'Deu ímpar!')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você ganhou!!!')
            v += 1
        else:
            print('Você perdeu...')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você ganhou!!!')
            v += 1
        else:
            print('Você ganhou!!!')
            break
    print('Vamos jogar novamente...')
print(f'Game Over! Você venceu {v} vezes.') 
