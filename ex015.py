dias = int(input('Informe o número de dias alugados: '))
kms = float(input('Informe quantos quilómetros foram rodados: '))
print('''O total a pagar é R${:.2f}. 
Obrigado e volte sempre!'''.format(dias * 60 + kms * 0.15))
