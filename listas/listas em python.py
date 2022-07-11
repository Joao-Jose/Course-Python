"""
Listas em Pyhton:
Fatiamentos
append, isert, pop, del, clear, extend, +
min, max
range


#         '0'  '1'  '2'  '3'  '4'  '5'
litas = ['A,', 'B', 'C', 'D', 'E', 10]  # Podemos acessar cada letra usando seus indices, e esses indices tambem são numeros negativos

strings = 'ABCDE'
print(strings[4])
print(litas[-1])
print(litas[0:5])
print(litas[::-1])
print(litas[::4])
#  listas suportam varios tipos de valores

"""

# Append:
#                 0 1 2 3 4
int_list = [1,2,3,4,5]
int_list2 = [5,7,8,9]
int_list.append(int_list2)
print(int_list)
# usamos indices para acessar valores, por isso começamos com 0

# Insert:
listas_fruit = ['Banana', 'Maçã', 'Pêra']
listas_fruit.insert(3, 'Uva')
print(listas_fruit)

# Pop:
lista_pop = ['Python', 'é', 'ruim', 'Bom']
lista_pop.pop(2)
print(lista_pop)

# Del:
lista_del = [1,2,3,4,5,6,7,8,9,10]
del(lista_del[3:5])
print(lista_del)

# Clear:
list_clear = [2,4,6,8,10]
list_clear.clear()
print(list_clear)

# Extend:
