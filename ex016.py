from math import floor
n = float(input('Informe um número: '))
print('Você escolheu o número {} e sua porção inteira é {:.0f}.'.format(n, floor(n)))
# pode ser usado tb os comandos: int(n) ou math.trunc(n)