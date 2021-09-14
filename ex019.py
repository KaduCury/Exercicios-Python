from random import choice
a = input('Digite o nome do primeiro aluno: ')
b = input('Digite o nome do segundo aluno: ')
c = input('Digite o nome do terceiro aluno: ')
d = input('E finalmente digite o nome do quarto aluno: ')
l = [a, b, c, d]
s = choice(l)
print(f'Dos quatro alunos informados o sorteado foi: {s}.')
