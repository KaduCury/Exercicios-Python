print('DETECTOR DE PALÍNDROMO!')
frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''  # = junto[::-1]
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
if inverso == junto:
    print(f'A frase {frase} é um PALÍNDROMO!')
if inverso != junto:
    print(f'A frase {frase} não é um palíndromo...')
