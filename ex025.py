nome = input('Digite o seu nome: ').strip()
# silva = nome.upper().count('SILVA')
# if silva == 0:
#     print('Você não tem "Silva" no seu nome.')
# else:
#     print('Você tem "Silva" no seu nome.')
print('Seu nome tem "Silva"? {}.'.format('SILVA' in nome.upper()))
