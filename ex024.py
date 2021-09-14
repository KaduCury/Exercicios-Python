cidade = str(input('Digite o Nome da sua cidade: ')).strip()
  # div = cidade.split()
  # saint = div[0].upper().count('SANTO')
  # if saint == 1:
  #     print('O nome da sua cidade começa com "Santo".')
  # else:
  #     print('O nome da sua cidade não começa com "Santo".')
print('O nome da sua cidade começa com Santo? {}.'.format(cidade[:5].upper() == 'SANTO'))
