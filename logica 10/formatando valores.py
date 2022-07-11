"""
Fomatando valores no python

formtação de strings: (:s)
formatação de inteiros: (:d)
formatação de flutuantes: (:2f)
:. (Numero) (> ou < ou ^) (quantidade) (tipo - s, d ou f)
> - esquerda
< - direita
^ - centro
"""
# exp de formatações
name = 'João'
print((name.upper()))  # tudo minusculo
print((name.lower()))  # tudo maiusculo
print((name.title()))  # primeira letra maiuscula

numero = 1
print(f'{numero:0>10}')  # o numero sera preenchido com 0 para esquerda
print(f'{numero:0^10}')  # o numero sera preenchido com a variavel centralizada
nomede_formatacao = 'João José'
print(50-len(nomede_formatacao)/ 2 )  # vamos pegar a quantidade de caracteres e fazer a subtração por um valor
print(f'{nomede_formatacao:#^50}')  # vejamos outro tipo de formatação, fazemos a divisao da variavael com o resultado da subtração
