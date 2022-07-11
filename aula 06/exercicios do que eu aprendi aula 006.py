
nome = 'João'
ano_atual = 2022
peso = 95.5
altura = 1.87
ano_nascimento = 2000
idade = ano_atual - ano_nascimento
imc = peso / (altura **2)

print(f'{nome} tem {idade} de idade tem {altura} de altura e pesa {peso}')
print(f'o seu imc é {imc:.2f}')
print(f'João nasceu em {ano_nascimento}')
print(bool(input('João acertou ?'),))

input('Qual o seu Nome ? :')
input('Qual o seu Peso ?: ')
input('Qual a sua Altura ?: ')
print('Agora vamos calcular seu IMC')
input('Calculando...')
input('Aperte ENTER para ober seu resultado')
print(f'{imc:.2f}')  # .2f são duas casas decimais, usamos isso para foramatar calculos com resto de divisão