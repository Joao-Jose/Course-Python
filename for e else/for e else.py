"""
FOR ELSE EM PYTHON

"""

name_list = ['João', 'josé', 'Melo']

comeca_com_j = False
for valor in name_list:  # o laço for cria uma variavel para fazer a iteração
    if valor.lower().startswith('j'):
        comeca_com_j = True

if comeca_com_j:
    print('começa com J')
else:
    print('não começa com J')

