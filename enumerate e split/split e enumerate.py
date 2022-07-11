"""
Split, Joim, Enumerate em python
* Split - dividir uma string #str
* Join - juntar uma lista #str
* Enumerate - enumerar elementos da lista  # iteraveis
"""

string = 'O Brasil é o o país do futebol, O Brasil é penta. '
lista_1 = string.split(' ')
lista_2 = string.split(',')
string.join(lista_1)
print(string)
lista_3 = ' '.join(lista_1)

palavra = ''
contagem = 0
# utilizando o laço for para iterarmos o valor da listas
for valor in lista_1:
    qtd_vezes = lista_1.count(valor)
    print(f'A palavra {valor} apareceu {lista_1.count(valor)}x na frase.')

    if qtd_vezes > contagem:
        contagem = qtd_vezes
        palavra = valor

print(f'A palavra que apareceu mais vezes é {palavra} ({contagem}x)')

