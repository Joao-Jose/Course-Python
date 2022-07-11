"""
para obtermos a quantidade de caracteres seja ele dentro de uma string
usamos o comand o len para isso
"""

nome = input('Digite seu Nome: ')
qtd_caracteres = len(nome)  # usamos len para indentificar a quantidade de caracteres

if qtd_caracteres < 8:  # if para que se não for verdadeiro não efetue o "cadastro"
    print('vc precisa pelo menos digitar oito caracteres')
else:  # se caso tiver a quantidade de 8 caracteres o "cadastro" é efetuado com sucesso
    print('voce foi cadastrado no sistema')

# podemos tambem realizar somas entre strings usando o comand o len

string1 = input('Informe seu nome: ')
string2 = input('Informe seu nome novamente: ')
print(f'A quantidade de caracteres é {len(string1) + len(string2)}')  # feito isso o comando len executa para nós a soma entre strings

# podemos tambem usar uma função "objeto" para fazermos essa soma
# string1(__len__) e assim usando desta maneira fazemos a soma de caracteres