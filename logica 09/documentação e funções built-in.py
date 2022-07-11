"""
funções logicas:
islower, isnumeric, isturtile
"""

#print(bool(num2))  # um outro exemplo é que mesmo colando o comando bool o resultado mostrado no terminal é o mesmo
# as funções logicas me informam se é true ou false assim como a função bool
# então entendemos que funções logicas tambem tem suas caracteriscas transformando-as em objetos mostrado ali em cima
# porem essa função isnumeric() é um método embutido usado para manipulação de strings.
# O método issnumeric() retorna “True” se todos os caracteres da string forem numéricos positivos
# caso contrário, retorna “False”.
# exp: 12345678910 retorna true se for 1.2.3.4.5.6.7 ou -1 -2 -3 -4 retorna false

num3 = input('Iforme um valor: ')
num4 = input('Informe outro valor: ')

if num3.isdigit() and num4.isdigit():
    num3 = int(num3)
    num4 = int(num4)
    print(num3 + num4)
else:
    print('Não pude converter')

    # podemos tambem colocar no lugar de if e else os comandos try(tenta executar meu codigo) e except(se der erro fala isso)

