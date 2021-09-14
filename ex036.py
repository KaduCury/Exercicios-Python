vcasa = float(input('Qual o valor da casa a ser financiada? R$'))
tempo = int(input('Em quantos anos você pretende pagar o valor financiado? '))
sal = float(input('Qual o valor do seu salário? R$'))
vparc = vcasa / (tempo * 12)
if vparc < (0.3 * sal):
    print('''Financiamento aprovado! 
Sua parcela mensal será de R${:.2f} para pagar em {} meses.'''.format(vparc, tempo*12))
else:
    print('''Financiamento negado!
A parcela mensal de R${:.2f} para pagar em {} meses
é superior a 30% do seu salário.'''.format(vparc, tempo*12))
