adj = float(input('Informe o Cateto Adjacente: '))
opo = float(input('Informe agora o Cateto Oposto: '))
hip = (adj ** 2 + opo ** 2) ** 0.5  # math.hypot(adj, opo) also works
print('''O triângulo retângulo de medidas 
do cateto adjacente de {} e cateto oposto de {}
tem a medida da hipotenusa de {:.3f}.'''.format(adj, opo, hip))
