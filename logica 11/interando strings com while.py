print("*-" * 30 + "*")
frase = input("Escreva uma frase: ")
action = ""

# Input: ação a ser realizada
while not action.isdigit():
    print("*-" * 30 + "*")
    action = input("Oque você deseja fazer com a frase:\n\n"
                   "    [0] Construir a frase caractere por caractere\n"
                   "    [1] Apagar as vogais da frase\n"
                   "    [2] Inverter a frase\n"
                   "    [3] Apagar os espaços da frase\n"
                   "    [4] Mostrar o índice de cada caractere\n"
                   "    [5] Sair\n\n"
                   "Res.: ")

    # Bloqueio de caracteres
    if not action.isdigit():
        print("\nVALOR INFORMADO INVÁLIDO, TENTE NOVAMENTE.")
        continue

else:
    print("*-" * 30 + "*")

# Variáveis
action = int(action)
frase = frase.upper()
frase = frase.strip()
cont = 0
quantiaCaracteres = len(frase)

# Exibir letra por letra
if action == 0:
    novaString = ""
    while cont < quantiaCaracteres:
        novaString = novaString + frase[cont]
        print(novaString)
        cont = cont + 1
    else:
        mnsg = "FRASE CONSTRUÍDA COM SUCESSO."
        print("\n" + mnsg.center(61))

# Exclusão das vogais
elif action == 1:
    while cont < quantiaCaracteres:
        if frase[cont] == "A" or frase[cont] == "E" or frase[cont] == "I" or frase[cont] == "O" or frase[cont] == "U":
            cont = cont + 1
            continue
        print(frase[cont])
        cont = cont + 1
    else:
        mnsg = "VOGAIS EXCLUÍDAS COM SUCESSO"
        print("\n" + mnsg.center(61))

# Inversão da frase
elif action == 2:
    cont = quantiaCaracteres - 1
    while cont >= 0:
        print(frase[cont])
        cont = cont - 1
    else:
        mnsg = "FRASE INVERTIDA COM SUCESSO."
        print("\n" + mnsg.center(61))

# Exlusão dos espaços
elif action == 3:
    while cont < quantiaCaracteres:
        if frase[cont] == " ":
            cont = cont + 1
            continue
        print(frase[cont])
        cont = cont + 1
    else:
        mnsg = "ESPAÇOS DA FRASE EXCLUÍDOS COM SUCESSO."
        print("\n" + mnsg.center(61))

# Indicar o índice dos caracteres
elif action == 4:
    while cont < quantiaCaracteres:
        print(f"{frase[cont]}  -->  {cont:0>3d}")
        cont = cont + 1
    else:
        mnsg = "ÍNDICES INDICADOS COM SUCESSO"
        print("\n" + mnsg.center(61))

# Sair do programa
elif action == 5:
    mnsg = "EXECUÇÃO DO PROGRAMA FINALIZADA."
    print(mnsg.center(61))

elif action > 5:
    mnsg = "NÃO ENCONTREI ESTE VALOR, TENTE NOVAMENTE."
    print(mnsg.center(61))

# ERRO 3SC0LH44C40: Algo deu errado na seleção da ação do usuário
else:
    mnsg = "OPS! ALGO DEU ERRADO, CONSULTE O SUPORTE\nCÓDIGO INSTABILIDADE: 3SC0LH44C40"
    print("\n" + mnsg.center(61))

print("*-" * 30 + "*")