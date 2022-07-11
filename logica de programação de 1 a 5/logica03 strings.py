"""
Strings ou str são comandos dentro de aspas exp = 'alguma coisa' ou "alguma coisa"
agora quando colocamos o comando print(1234) os numeros representam dados primitivos ou numeros inteiros
"""

# possiveis erros com o interpretador do python
# print('isso é uma string 'str') isso acontece devido ao o inicio começar com aspas simples e comando simples continuar com aspas simples
# solução para esse problema
print('isso é uma string "str"')  # simplesmente invertemos as posições.
#outro tipo de solução menos viavel seria:
print("Esse é meu \"texto\" (str).")  # a barra inversa separaria isso do interpretador do python