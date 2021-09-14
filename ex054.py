import datetime
cont = 0
anoat = datetime.date.today().year
for c in range(1, 8):
    a = float(input(f'Informe o ano de nascimento da {c}ª pessoa: '))
    if (anoat - a) > 18:
        cont = cont + 1
if cont == 0:
    print('''
Nenhuma das sete pessoas informadas atingiram a maioridade.''')
elif cont == 6:
    print('''
Uma pessoa não atingiu a maioridade e as outras seis sim.''')
elif cont == 7:
    print('''
Todas as pessoas informadas atingiram a maioridade.''')
else:
    print('''
{} pessoas não atingiram a maioridade e {} pessoas atingiram.'''.format(7 - cont, cont))
