"""
Operador ternário em Python
"""

idade = input('Digite sua idade: ')

if not idade.isnumeric():
    print('Apenas numeros.')
else:
    idade = int(idade)
    e_de_maior = (idade >= 18)
    msg = 'Pode acessar' if e_de_maior else 'Não pode acessar'
    print(msg)