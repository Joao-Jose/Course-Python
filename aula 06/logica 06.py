"""
VARIAVEIS:
variaveis são operadores armazenados na memoria, e devido a isso atribuimos valores a ela
variaveis não podem iniciar com numeros não podem conter espaços e o viavel para separar nomes
é usando o _
exp: nome_de_alguem
     data_1
     idade_de_alguem

"""
nome = 'João'
idade = 22
altura = 1.87
e_maior = idade > 18
peso = 95
imc = peso / (altura ** 2)

print('nome:', nome)
print('idade:', 22)
print('altura:', 1.87)
print('é maior de idade ?', e_maior)
print(f'{nome} tem {idade} de idade e seu imc é {imc:.2f}')  #devemos atribuir .2f para formatarmos essa soma

