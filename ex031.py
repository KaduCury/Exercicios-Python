print('Calcule o valor da sua próxima passagem aqui!')
kms = int(input('Qual a distância da viagem em KMs? ').strip())
if kms > 200:
    print('O valor da passagem desse trecho é R${:.2f}.'.format(kms * 0.45))
else:
    print('O valor da passagem desse trecho é de R${:.2f}.'.format(kms * 0.5))
