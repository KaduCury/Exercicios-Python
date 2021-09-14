preco = float(input('Informe o valor do produto: R$'))
print('''Formas de pagamento:
[ 1 ] Dinheiro ou Cheque à vista, 
[ 2 ] Cartão à vista,
[ 3 ] 2 vezes no cartão de crédito,
[ 4 ] 3 vezes ou mais no cartão de crédito.''')
forma = int(input('Informe o número da opção de pagamento: '))
if forma == 1:
    print('No cheque à vista e no dinheiro o valor é de R${:.2f}.'.format(preco * 0.9))
elif forma == 2:
    print('À vista no cartão o valor é de R${:.2f}.'.format(preco * 0.95))
elif forma == 3:
    print('''Em duas vezes no cartão de crédito 
o valor total é de R${:.2f}
e cada parcela fica no valor de R${:.2f}.'''.format(preco, preco / 2))
elif forma == 4:
    parcela = int(input('Em quantas parcelas? '))
    print('''Em {} vezes o valor é de R${:.2f}
e cada parcela fica no valor de R${:.2f}.'''.format(parcela, preco * 1.2, preco * 1.2 / parcela))
else:
    print('Opção de Pagamento Inválida!')
