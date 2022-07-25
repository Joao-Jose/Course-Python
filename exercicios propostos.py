"""
exercicio 01:
 Crie uma função1 que recebe uma função2  como paramentro e retorne o valor da funcao2 executada.

 exercicio 02:
 Crie uma funcao1 que recebe uma funcao2 como parametro e retorne o valor da funcao2 executada. faça a
 funcao1 executar duas funcoes que recebam um numero diferente de argumentos
"""


# exercicio 01:

def hello_world():
    return 'olá, mundo'

def master(hello_world):
    return hello_world()

print(hello_world())



# exercicio 02:

def mestre(funcao, *args, **kwargs):
    return funcao(*args, **kwargs)

def fala_oi(nome = 'João'):
    return f'Olá, {nome}'

def saudacao(nome, saudacao):
    return f'{saudacao}, {nome}'

action01 = mestre(fala_oi, 'João')
action02 = mestre(saudacao, 'João', saudacao = 'Welcome')
print(action01)
print(action02)
