"""
Desempacotamento de lista em Python
"""


_list = ['João', 'Maria', 'José', 1,2,3,4,5,6,7,8,9,100]

# podemos tambem caso os valores a seguir forem ignorados usar *_
# podemos usar o operador * para utilizar outros valores dentro da lista
n1, n2, n3, *outra_lista, ultimoda_lista = _list
print(ultimoda_lista)

# realizando troca de valores dentro do python

nome = 'João'
idade = 22
profissao = 'desenhista'
nome, idade, profissao = profissao, idade, nome
print(f'nome é {nome}, idade é {idade}, profissão é {profissao}')


# Operador ternario