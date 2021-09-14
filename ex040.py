a = float(input('Informe a primeira nota: '))
b = float(input('Informe a segunda nota: '))
m = (a + b) / 2
if m < 5:
    print('Sua média foi {:.1f}. Aluno REPROVADO!'.format(m))
elif m >= 6.94:
    print('Sua média foi {:.1f}. Aluno APROVADO!'.format(m))
else:
    print('Sua média foi {:.1f}. Aluno em RECUPERAÇÃO!'.format(m))
