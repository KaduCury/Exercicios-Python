from random import shuffle
print('Vamos sortear a ordem de apresentação do grupo de 4 alunos!')
a = input('Informe o nome do primeiro aluno: ')
b = input('Informe o nome do segundo aluno: ')
c = input('Diga o nome do terceiro aluno: ')
d = input('E finalmente insira o nome do quarto aluno: ')
l = [a, b, c, d]
shuffle(l)
print(f'A ordem sorteada é: {l}.')
