nome = input('Informe seu nome completo: ')
div = nome.split()
pn = div[0]
un = div[len(div)-1]
print('{} tem como primeiro nome {} e último nome {}.'.format(nome, pn, un))
