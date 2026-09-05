"""
============================================================
 Sprint 02 - Algoritmo em Python
 Desafio: Carregamento Inteligente GoodWe
 Equipe: ChargeGrid Intelligence  -  Turma 1CCPX
============================================================

Este programa reproduz, EM SOFTWARE, a mesma logica do circuito
digital criado na Sprint 01 para controlar uma estacao de recarga
de veiculos eletricos.

ENTRADAS (condicoes do mundo real -> 1 = verdadeiro / 0 = falso):
    A = RFID            -> o usuario passou a tag de autenticacao?
    B = Saldo           -> o usuario tem saldo positivo?
    C = Cabo Conectado  -> o cabo esta plugado no veiculo?
    D = Carga Completa  -> a bateria ja esta cheia?
    E = Sobrecarga      -> ha alerta de sobrecarga / falha?

SAIDAS (acoes e sinalizacao da estacao):
    S1 = Rele de Carga       (liga a energia para carregar)
    S2 = LED Azul            (carregando)
    S3 = LED Verde           (estacao livre / liberada para uso)
    S4 = LED Amarelo         (aviso: conectado mas carga nao liberada)
    S5 = LED Vermelho        (sobrecarga - suspender o uso)

Expressoes booleanas (vindas da Sprint 01):
    S1 = A . B . C . D' . E'
    S2 = A . B . C . D' . E'
    S3 = C' . E'
    S4 = C . E' . (A' + B' + D)      (forma fatorada de A'.C.E' + B'.C.E' + C.D.E')
    S5 = E
"""


def ler_entrada(nome):
    """
    Le uma entrada digitada pelo usuario e garante que seja 0 ou 1.
    Fica repetindo a pergunta enquanto o valor for invalido.
    """
    while True:
        valor = input(f"{nome} (0 ou 1): ").strip()
        if valor in ("0", "1"):
            return int(valor)
        print("  >> Valor invalido! Digite apenas 0 ou 1.")


def calcular_saidas(A, B, C, D, E):
    """
    Recebe as 5 entradas e devolve as 5 saidas (S1..S5).

    Tradução dos operadores booleanos para Python:
        '.' (E)   -> and
        '+' (OU)  -> or
        "'" (NAO) -> not
    """

    # S1 = A . B . C . D' . E'
    # So carrega quando TUDO esta certo: autenticado, com saldo,
    # cabo conectado, bateria ainda nao cheia e sem sobrecarga.
    S1 = A and B and C and (not D) and (not E)

    # S2 = A . B . C . D' . E'  -> mesma condicao do S1.
    # O LED azul acende exatamente quando o rele de carga liga.
    S2 = A and B and C and (not D) and (not E)

    # S3 = C' . E'
    # Estacao livre: nao ha cabo conectado e nao ha falha.
    S3 = (not C) and (not E)

    # S4 = C . E' . (A' + B' + D)
    # Aviso amarelo: cabo conectado e sistema seguro, mas a carga
    # NAO inicia porque falta RFID (A'), falta saldo (B') OU a
    # bateria ja esta cheia (D).
    S4 = C and (not E) and ((not A) or (not B) or D)

    # S5 = E
    # Sobrecarga tem prioridade maxima: sempre que E=1, o LED
    # vermelho acende (e, como S1/S2/S3/S4 exigem E'=1, todos apagam).
    S5 = E

    # Converte True/False em 1/0 para manter o padrao da tabela verdade.
    return int(bool(S1)), int(bool(S2)), int(bool(S3)), int(bool(S4)), int(bool(S5))


def exibir_resultado(A, B, C, D, E, S1, S2, S3, S4, S5):
    """Mostra de forma legivel o estado de cada saida e um resumo."""
    print("\n----------- ESTADO DA ESTACAO -----------")
    print(f"Entradas -> A={A} B={B} C={C} D={D} E={E}")
    print(f"S1 Rele de Carga ...... {'LIGADO' if S1 else 'desligado'}")
    print(f"S2 LED Azul ........... {'ACESO (carregando)'      if S2 else 'apagado'}")
    print(f"S3 LED Verde .......... {'ACESO (livre)'           if S3 else 'apagado'}")
    print(f"S4 LED Amarelo ........ {'ACESO (aguardando acao)' if S4 else 'apagado'}")
    print(f"S5 LED Vermelho ....... {'ACESO (SOBRECARGA!)'     if S5 else 'apagado'}")

    # Mensagem-resumo do que esta acontecendo (prioridade de cima para baixo).
    print("\nResumo:")
    if S5:
        print("  >> SOBRECARGA detectada! Uso suspenso imediatamente.")
    elif S1:
        print("  >> Carregando o veiculo normalmente...")
    elif S3:
        print("  >> Estacao livre e pronta para uso.")
    elif S4:
        print("  >> Cabo conectado, mas a carga nao foi liberada.")
        print("     (verifique RFID, saldo ou se a bateria ja esta cheia.)")
    else:
        print("  >> Nenhuma acao ativa no momento.")
    print("-----------------------------------------")


def gerar_tabela_verdade():
    """
    Gera as 32 combinacoes possiveis das entradas e imprime as saidas.
    Serve para PROVAR que o codigo bate exatamente com a tabela verdade
    da Sprint 01 (mesma ordem: E e o bit menos significativo).
    """
    print("\nLinha | A B C D E | S1 S2 S3 S4 S5")
    print("-" * 39)
    linha = 1
    for A in (0, 1):
        for B in (0, 1):
            for C in (0, 1):
                for D in (0, 1):
                    for E in (0, 1):
                        S1, S2, S3, S4, S5 = calcular_saidas(A, B, C, D, E)
                        print(f"{linha:>5} | {A} {B} {C} {D} {E} |"
                              f"  {S1}  {S2}  {S3}  {S4}  {S5}")
                        linha += 1


def main():
    print("=== Estacao de Recarga GoodWe - logica da Sprint 01 ===\n")
    print("Escolha o modo:")
    print("  1 - Testar uma combinacao manualmente")
    print("  2 - Gerar a tabela verdade completa (32 linhas)")
    opcao = input("Opcao: ").strip()

    if opcao == "2":
        gerar_tabela_verdade()
    else:
        # Modo manual (padrao)
        A = ler_entrada("A - RFID           ")
        B = ler_entrada("B - Saldo          ")
        C = ler_entrada("C - Cabo Conectado ")
        D = ler_entrada("D - Carga Completa ")
        E = ler_entrada("E - Sobrecarga     ")
        S1, S2, S3, S4, S5 = calcular_saidas(A, B, C, D, E)
        exibir_resultado(A, B, C, D, E, S1, S2, S3, S4, S5)


if __name__ == "__main__":
    main()