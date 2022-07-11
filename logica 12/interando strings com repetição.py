print('=+' * 50 + '=' )
frase = input('Digite uma frase: ')
execucao = ''

while not execucao.isdigit():
    print('=+' * 50 + '=')
    execucao = input("Oque você deseja fazer com a frase:\n\n"
                   "    [0] Construir a frase caractere por caractere\n"
                   "    [1] Apagar as vogais da frase\n"
                   "    [2] Inverter a frase\n"
                   "    [3] Apagar os espaços da frase\n"
                   "    [4] Mostrar o índice de cada caractere\n"
                   "    [5] Sair\n\n"
                   "Res.: ")

    if not execucao.isdigit():
        print('VALOR INFORMADO INVALIDO \n')
        continue

else:
    print('=+' * 50 + '=')

execucao = int(execucao)
frase = frase.upper()
frase = frase.strip()
cont = 0
quant_caract = len(frase)

if execucao == 0:
    nova_string = ''
    while cont < quant_caract:
        nova_string = nova_string + frase[cont]
        print(nova_string)
        cont = cont + 1
    else:
        msg = 'VOGAIS EXCLUIDAS COM SUCESSO'
        print("\n" + msg.center(61))

elif execucao == 3:
    while cont < quant_caract:
        print(f"{frase[cont]}  -->  {cont:0>3d}")
        cont = cont + 1




