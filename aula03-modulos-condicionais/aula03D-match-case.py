# imagina um programa que recebe a escolha de um usuário
# 0 --> sair do programa
# 1 --> entrar no programa
# ----> erro!

escolha_usuario = 1

match escolha_usuario:
    case 0:
        print("Sair do programa")
    case 1:
        print("Entrar no programa")
    case _:
        print("Erro!!")

# Faixa de valores --> elseif
# Valores únicos ----> case