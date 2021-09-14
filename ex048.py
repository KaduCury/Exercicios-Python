cont = 0
soma = 0
for c in range(3, 500, 3):
    if c % 2 == 1:
        soma += c
        cont += 1
print(f'''A somatória entre todos os {cont} números ímpares 
que são múltiplos de 3 
no intervalo entre 1 e 500 é igual a {soma}.''')
