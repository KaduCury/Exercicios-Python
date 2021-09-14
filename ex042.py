a = float(input('Informe a medida do primeiro segmento de reta: '))
b = float(input('Informe a medida do segundo segmento de reta: '))
c = float(input('Informe a medida da terceiro segmento de reta: '))
if a == b == c:
    print('Com as medidas dos segmentos de reta informados é possível formar um triângulo equilátero.')
elif ((b-c) < a < b+c) and ((a-c) < b < a+c) and ((a-b) < c < a+b) and a == b or a == c or b == c:
    print('Com as medidas dos segmentos de reta informados é possível formar um triângulo isósceles.')
elif ((b-c) < a < b+c) and ((a-c) < b < a+c) and ((a-b) < c < a+b) and a != b != c:
    print('Com as medidas dos segmentos de reta informados é possível formar um triângulo escaleno.')
else:
    print('Não é possível formar um triângulo com os segmentos de reta informados.')
#  if a < b + c and b < a + c and c < a + b:
#      print('Com as medidas dos segmentos de reta informados é possível formar um triângulo ', end='')
#      if a == b == c:
#          print('Equilátero.')
#      elif a != b != c != a:
#          print('Escaleno.')
#      else:
#          print('Isósceles.')
#  else:
#      print('Com as medidas dos segmentos de reta informados Não é possível formar um triângulo.')
