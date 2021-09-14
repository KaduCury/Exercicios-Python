nome = input('Digite seu nome: ').strip()
print('Este é seu nome com letras maiúsculas: {}.'.format(nome.upper()))
print('Este agora com letras minúsculas: {}.'.format(nome.lower()))
div = nome.split()
joi = ''.join(div)
print('O número de letras do seu nome é: {}.'.format(len(joi)))  # format(len(nome) - nome.count(' ')) also works
print('O número de letras do seu primeiro nome é: {}.'.format(len(div[0])))  # format(nome.find(' ')) also works
