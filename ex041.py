import datetime
anonasc = int(input('Informe o ano de nascimento do nadador: '))
anoatual = datetime.date.today().year
idade = anoatual - anonasc
if idade <= 9:
    print('O nadador em questão é da categoria Mirim.')
elif idade <= 14:
    print('O nadador em questão é da categoria Infantil.')
elif idade <= 19:
    print('O nadador em questão é da categoria Júnior.')
elif idade <= 25:
    print('O nadador em questão é da categoria Sênior.')
else:
    print('O nadador em questão é da categoria Master.')
