# faça um programa que peça ao usuario para digitar um numero inteiro,
# informe se este numero é par ou impar. caso o usuario nao didigite um numero inteiro,
# informe que não é um numero inteiro.


# Desafio concluido 1/3
num1 = input('Informe um numero inteiro: ')
try:
    num1 = int(num1)
    resto_div = num1 % 2
    if resto_div == 0:
        print(f'Seu numero {num1} é par')
    else:
        print(f'Seu numero {num1} é impar')  # lembre-se de verificar que else deve estar dentro de if
except:
    print(f'Seu numero {num1} não é inteiro')


# faça um programa que pergunte a hora ao usuario e, baseando-se no horario
# descrito, exiba a saudação apropriada. ex.
# bom dia meu querido 0-11, boa tarde meu querido 12-17 e boa noite meu querido 18-23.


# Desafio de 2/3

hora1 = int(input('Digite seu horario: '))
hora2 = int(input('Informe os minutos: '))

if hora1 < 60 and hora2 < 24:
    print(f'Bom dia meu querido seu horario é {hora1}:{hora2} da manhã')
elif 12 <= hora1 <= 17:
    print(f'Bom dia meu querido seu horario é {hora1}:{hora2} da tarde')
else:
    print(f'Boa noite meu querido são {hora1}:{hora2} da noite')
    print(f'SEU NUMERO É INVALIDO')

# desafio 3/3
# faça um programa que peça o primeiro nome do usuario. se o nome tiver 4 letras ou
# menos escreva "seu nome é curto; se tiver entre 5 e 6 letras, escreva
# "seu nome é normal", maior que 6 letras "seu nome é muito grande".

name = input('Escreva seu nome: ')
name = len(name)
if name <= 4:
    print(f'seu nome {name} é curto')
elif 5 >= name <= 6:
    print(f'Seu nome {name} é normal ')
elif name > 6:
    print(f'Seu nome {name} é muito grande')
else:
    print(f'seu nome {name} é muito grande')


