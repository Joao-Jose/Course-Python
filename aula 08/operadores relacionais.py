"""
Operadores relacionais
== Igualdade , compara valores
> Maior que
>= Maior que ou igual a
< Menor que
<= Menor que ou igual a
!= Diferente
"""
nome = input('Informe seu nome: ')
idade = input('Informe sua idade: ')
idade = int(idade)
idade_limite = 18
if idade >= idade_limite:
    print(f'{nome} Pode pegar o emprestimo')
else:
    print(f'{nome} Não Pode pegar o emprestimo')
