vel = int(input('Qual a velocidade auferida do veículo em questão? '))
acm = vel - 80
mul = acm * 7
if vel > 80:
    print(f'''Você foi autuado pelo radar de velocidade!
A velocidade auferida do seu veículo foi de {vel}KM/H,
{acm}KM/H acima da velocidade permitida para o trecho.
O valor da multa a ser paga é de R${mul}.
Dirija com mais atenção numa próxima!''')
else:
    print(f'''Você não foi autuado.
A velocidade de {vel}KM/H é permitida no trecho.
De boas tartaruga!''')
