# exercicio 01

# crie uma funcao que exiba uma saudaçao com os parametros saudaçao e nome


def saudacao(msg='Olá', nome='João'):
    msg = msg
    nome = nome
    return f'{msg} me chamo {nome}'


funcao = saudacao()
print(funcao)


# exercicio 02
# faça uma funcao que receba 3 numeros com parametros e exiba a soma entre eles

def soma(n1=10, n2=20):
    n1 = n1
    m2 = n2
    return n1 + n2


_soma = soma()
print(_soma)


# exercicio 03
# crie uma funcao que receba 2 numeros, o primeiro é um valor e o segundo um percentual retorne (return) o primeiro valor
# do primeiro numero somado do aumento do percentual do mesmo

def soma_percentual(valor, percentual):
    return valor + (valor * percentual / 100)

soma_de_valores = soma_percentual(50,10)
print(soma_de_valores)

# Exercicio 04
# Fizz Buzz

def fb(numero):
    if numero % 3 == 0 and numero % 5 == 0:
        return 'FizzBuzz'
    if numero % 5 == 0:
        return 'Buzz'
    if numero % 3 == 0:
        return 'Fizz'
    return numero

print(fb(15))
