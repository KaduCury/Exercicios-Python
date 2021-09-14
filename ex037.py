num = int(input('Digite o número a ser convertido: '))
print('''Suas opções são:
[ 1 ] Binário
[ 2 ] Octal
[ 3 ] Hexadecimal''')
conv = int(input('Qual será a base de conversão: '))
if conv == 1:
    print('O número {} convertido para Binário é: {}.'.format(num, bin(num)[2:]))
elif conv == 2:
    print('O número {} convertido para Octal é: {}.'.format(num, oct(num)[2:]))
elif conv == 3:
    print('O número {} convertido para Hexadecimal é: {}.'.format(num, hex(num)[2:]))
else:
    print('OPÇÃO INVÁLIDA! Escolha 1, 2 ou 3!')
