import math
ang = float(input('Informe um ângulo: '))
sen = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tan = math.tan(math.radians(ang))
print('''O ângulo {}º tem o valor do seno de {:.3f},
o valor do cosseno de {:.3f} 
e o valor da tangente de {:.3f}.'''.format(ang, sen, cos, tan))
