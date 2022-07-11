# obs: não existe soma de numero inteiro e strings
# o mesmo vale pra divisão de strings
# fazer muito comentarios no seu codigo não é recomendavel

"""
Entrada de dados
"""

nome = input('Qual é o seu nome ?: ')
idade = input('Qual a sua idade ?: ')
ano_nascimento = 2022
ano_nascimento2 = ano_nascimento - int(idade)  # usamos int para a conversão de valores e assim segue para outros comando
print()
print(f'{nome} tem {idade} anos e nasceu em {ano_nascimento2}')


