p = int(input('Qual o primeiro termo da Progressão Aritimética desejada? '))
r = int(input('Qual a razão da Progressão Aritimética desejada? '))
u = p + r * 10
print('Os dez primeiros termos dessa Progressão Aritimética são: ', end=' ')
for c in range(p, u, r):
    print(c, end=', ')
