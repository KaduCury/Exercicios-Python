print('Calculadora do aumento salarial 2021')
sal = float(input('Informe seu salário: R$'))
if sal > 1250:
    print('''O seu salário de R${:.2f} será acrescido de R${:.2f},
alcançando assim o valor de R${:.2f}.'''.format(sal, (sal * 0.1), (sal * 1.1)))
else:
    print('''O seu salário de R${:.2f} será acrescido de R${:.2f},
alcançando assim o valor de R${:.2f}.'''.format(sal, (sal * 0.15), (sal * 1.15)))
