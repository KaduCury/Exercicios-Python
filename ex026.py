frase = input('Digite uma frase: ').strip()
vez = frase.upper().count('A')
ap = frase.upper().find('A')+1
au = frase.upper().rfind('A')+1
print('''A letra "A" aparece {} vezes,
sendo a primeira vez na posição {}
e a última na posição {}.'''.format(vez, ap, au))
