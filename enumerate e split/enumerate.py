listas = [
     # 0      1       2           # listas
    ['Edu', 'João', 'Luiz'],
    ['Maria', 'Aline', 'Joana'],  # indices
    ['Helena', 'Ed', 'Lu'],

]

enumerada = list(enumerate(listas))
print(enumerada[1][1][2])

"""
[ <-- Enumerate

   (0, ['Edu', 'João', 'Luiz']), 
   (1, ['Maria', 'Aline', 'Joana']), 
   (2, ['Helena', 'Ed', 'Lu'])
]


"""

_list = ['João', 'Maria', 'José']

n1, n2, outra_lista = _list
print(n2)