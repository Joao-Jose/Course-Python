"""
CALCULADORA DE IMC
"""
print('Bem vindo(a) a sua Calculadora de IMC')
print()

nome = input('Qual o seu nome? ')
idade = input('Qual a sua idade? ')
peso = float(input('Qual o seu peso? '))
altura = float(input('Qual a sua altura? '))
imc = (peso / altura ** 2)

min_normal = 18.5
max_normal = 24.9
acima_min = 24.0
acima_max = 29.9
obeso_min = 30.0
obeso_max = 34.9
obeso_sev_min = 35
obeso_sev_max = 39.9

print()

print(f'{nome} tem {idade} anos de idade, pesa {peso} kg e mede {altura} metros de altura.'
      f' Seu imc é igual a: {imc:.2f}')
if imc >= min_normal and imc <= max_normal:
    print(f'O peso de {nome} está norma')
elif imc >= acima_min and imc <= acima_max:
    print(f'{nome} Está acima do peso')
elif imc >= obeso_min and imc <= obeso_max:
    print(f'{nome} Está obeso!')
elif imc >= obeso_sev_min and imc <= obeso_sev_max:
    print(f'{nome} Está com obesidade severa')
else:
    print()
print('Para saber qual seria o seu peso ideal, favor digite os dados a seguir:')

altura_ideal = int(input('Favor digite novamente a altura sem utilizar o ponto(.): '))
sexo = input('Qual o seu sexo? ')
peso_ideal_masc = 52 + (altura_ideal - 152.4) * 0.75
peso_ideal_fem = 52 + (altura_ideal - 152.4) * 0.67
peso_ideal_ajst_fem = ((peso - peso_ideal_fem) * 0.25) + peso_ideal_fem
peso_ideal_ajst_masc = ((peso - peso_ideal_masc) * 0.25) + peso_ideal_masc
if sexo == ('masculino'):
    print(f'O peso ideal de {nome} seria {peso_ideal_masc:.2f}')
    print(f'O peso ideal ajustado de {nome} seria {peso_ideal_ajst_masc:.2f}')
elif sexo == ('feminino'):
    print(f'O peso ideal de {nome} seria {peso_ideal_fem:.2f}')
    print(f'O peso ideal ajustado de {nome} seria {peso_ideal_ajst_fem:.2f}')
else:
    print()
print('Obrigado por usar a calculadora de IMC!! Cuide da sua Saúde!')