nome = input('Olá, qual o seu nome? ')
print('Seja bem vindo, '+ nome +'!')
dia = input('Qual o dia do seu nascimento? ')
print('Certo '+ nome +'.')
mes = input('E qual é o mês do seu aniversário? ')
ano = input('E por último mas não menos importante, qual o ano em que você nasceu? ')
# print(nome +', você nasceu no dia',dia,'de',mês,'de '+ano+'.')
print('{}, você nasceu no dia {} de {} de {}.'.format(nome, dia, mes, ano))

