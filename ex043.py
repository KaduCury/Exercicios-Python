peso = float(input('Informe o peso em kg: '))
altura = float(input('Informe a altura em m: '))
imc = peso / (altura ** 2)
if imc < 18.5:
    print(f'IMC = {imc:.1f}. Você está Abaixo do seu peso ideal.')
elif 18.5 <= imc < 25:
    print(f'IMC = {imc:.1f}. Você está no seu Peso Ideal.')
elif 25 <= imc < 30:
    print(f'IMC = {imc:.1f}. Você está com Sobrepeso.')
elif imc >= 30 and imc < 40:
    print(f'IMC = {imc:.1f}. Você está com Obesidade.')
elif imc >= 40:
    print(f'IMC = {imc:.1f}. Você está com Obesidade Mórbida.')
