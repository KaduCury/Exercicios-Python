import datetime
sex = int(input('Informe se você é do sexo [ 1 ]Masculino ou [ 2 ]Feminino: '))
anonasc = int(input('Informe o ano de seu nascimento: '))
anoatual = datetime.date.today().year
idade = anoatual - anonasc
if sex == 1:
    if idade == 18:
        print('Você deve se alistar esse ano! Procure a unidade mais próxima.')
    elif idade == 19:
        print('''Você já deveria ter se alistado ano passado!
Procure a unidade mais próxima para regularizar sua situação.''')
    elif idade == 17:
        print('Você deve se alistar ano que vem! Falta apenas um ano!')
    elif idade > 19:
        print('''Você deveria ter se alistado em {}! 
Já se passaram {} anos do seu alistamento! 
Procure a unidade mais próxima para regularizar sua situação.'''.format((anonasc + 18), (anoatual - (anonasc + 18))))
    elif idade < 17:
        print('Você deverá se alistar apenas em {}. Falta {} anos.'.format((anonasc + 18), ((anonasc + 18) - anoatual)))
elif sex == 2:
    print('Não é obrigatório o seu alistamento militar.')
else:
    print('Opção de sexo inválida! Informe 1 para Masculino ou 2 para Feminino!')
