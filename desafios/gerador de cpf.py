cpf = input('Informe o seu CPF, por favor. ')

x = 1
novocpf = ''
soma, digito, multiplicador = 0, 0, 10

for sonumeros in cpf[:-2]:
    if sonumeros.isdecimal():
        novocpf = novocpf + sonumeros

while x <= 2:
    for numero in novocpf:
        soma = soma + int(numero) * multiplicador
        multiplicador -= 1

    digito = 11 - (soma % 11)
    multiplicador = 11

    if digito > 9:
        novocpf = novocpf + '0'
    else:
        novocpf = novocpf + str(digito)
    digito, soma = 0, 0
    x += 1

if cpf[-2:] == novocpf[-2:]:
    print('CPF válido.')
else:
    print('Verifique o número digitado. CPF Inválido')