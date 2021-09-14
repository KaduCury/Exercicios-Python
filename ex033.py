a = int(input('Diga o primeiro número: '))
b = int(input('Digite o segundo número: '))
c = int(input('Digite o terceiro e último número: '))
l = [a, b, c]
l.sort()
mai = l[2]
 #  mai = a
 #  if b > a and b > c:
 #      mai = b
 #  if c > a and c > b:
 #      mai = c
men = l[0]
 #  men = a
 #  if b < a and b < c:
 #      men = b
 #  if c < a and c < b:
 #      men = c
print(f'''O maior número que você escolheu foi o {mai},
e o menor escolhido foi o número {men}.''')
