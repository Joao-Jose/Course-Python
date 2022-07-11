""""

# estrutura de repetição

while True:  # loop infinito
    nome_do_usuario = input('Digite seu nome: ')
    print(f'olá {nome_do_usuario}, como voce está ?' )
    break  #a instrução break oferece a possibilidade de sair de um loop


x = 0
y = 0

while x < 10:
    print(x)
    x += 1  # aqui dizemdo que x é igual a x + 1
print('acabou')
"""
while True:
    numero1 = input('informe um numero: ')
    numero2 = input('informe outro numero: ')
    operador = input('informe um operador: ')

    if not numero1.isnumeric() or not numero2.isnumeric():
        print('SEU NUMERO É INVALIDO')
        continue

    numero1 = int(numero1)
    numero2 = int(numero2)

    if operador == '+':
        print(numero1 + numero2)
    elif operador == '-':
        print(numero1 - numero2)
    elif operador == '/':
        print(numero1 / numero2)
    elif operador == '*':
        print(numero1 * numero2)
    else:
        print('Informe um operador valido')
