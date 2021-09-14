print('Programa para verificação de Condições de Existência de um Triângulo')
a = float(input('Informe o tamanho da reta a: '))
b = float(input('Informe o tamanho da reta b: '))
c = float(input('Informe o tamanho da reta c: '))
if ((b-c) < a < b+c) and ((a-c) < b < a+c) and ((a-b) < c < a+b):
    print('Com as medidas das retas a, b e c é possível formar um triângulo.')
else:
    print('Não é possível formar um triângulo com as retas a, b e c.')
