nome = input('Qual o seu nome? ')
idade = input('Qual a sua idade? ')
altura = float(input('Qual sua altura? '))
peso = float(input('Qual seu peso? '))
imc = (round(peso / altura ** 2, 2))
ideal_min = 18.5
ideal_max = 24.99
peso_min = float(round(ideal_min * altura ** 2, 2))
peso_max = float(round(ideal_max * altura ** 2, 2))

print()
print(f'{nome} tem {idade} anos e {altura}m de altura')
print(f'{nome} pesa {peso}kg e seu IMC é {imc}.')

if imc < 17:
    print(f'{nome} está muito abaixo do peso.')
    dif_peso1 = round(peso_min - peso, 2)
    print(f'{nome} precisa ganhar {dif_peso1}kg para atingir o IMC normal.')
elif imc <= 18.49:
    print(f'{nome} está abaixo do peso.')
    dif_peso2 = round(peso_min - peso, 2)
    print(f'{nome} precisa ganhar {dif_peso2}kg para atingir o IMC normal.')
elif imc <= 24.99:
    print(f'Parabéns, {nome}, você está dentro do peso normal, que deve ser entre {peso_min}kg e {peso_max}kg.')
elif imc <= 29.99:
    print(f'{nome} está acima do peso.')
    dif_peso3 = round(peso - peso_max, 2)
    print(f'{nome} precisa perder {dif_peso3}kg para atingir o IMC normal.')
elif imc <= 34.99:
    print(f'{nome} está com obesidade grau I.')
    dif_peso4 = round(peso - peso_max, 2)
    print(f'{nome} precisa perder {dif_peso4}kg para atingir o IMC normal.')
elif imc <= 39.99:
    print(f'{nome} está com obesidade grau II.')
    dif_peso5 = round(peso - peso_max, 2)
    print(f'{nome} precisa perder {dif_peso5}kg para atingir o IMC normal.')
else:
    print(f'{nome} está com obesidade mórbida.')
    dif_peso6 = round(peso - peso_max, 2)
    print(f'{nome} precisa perder {dif_peso6}kg para atingir o IMC normal.')