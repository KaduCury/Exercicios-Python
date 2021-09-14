somaidade = 0
mnova = 0
maioridadehomem = 0
nomevelho = ''
for c in range(1, 5):
    print(f'{c}ª PESSOA')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    somaidade += idade
    if c == 1 and sexo == 'M':
        maioridadehomem = idade
        nomevelho = nome
    if sexo == 'M' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo == 'F' and idade < 20:
        mnova += 1
mediaidade = somaidade / 4
print(f'A média de idade das pessoas informadas é {mediaidade} anos.')
print(f'O homem mais velho é o {nomevelho}, ele tem {maioridadehomem} anos.')
print(f'{mnova} são mulheres com menos de 20 anos.')
