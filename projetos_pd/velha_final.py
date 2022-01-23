X = "X"
O = "O"
VAZIO = " "

tabuleiro = [VAZIO, VAZIO, VAZIO,
             VAZIO, VAZIO, VAZIO,
             VAZIO, VAZIO, VAZIO]
jogada = 0
# tabuleiro = [0, 1, 2,
#              3, 4, 5,
#              6, 7, 8]

jogo_valido = True
vencedor = False

jogador1 = VAZIO
jogador2 = VAZIO

print('      < Jogo da Velha >     ')
print()
jogador1 = input('Antes de iniciar, JOGADOR 1, escolha se quer jogar com "X" ou "O": ').upper()
print()
if jogador1 == X:
    jogador2 = O
    print('O JOGADOR 1, será o "X" e o JOGADOR 2, será o "O"')
else:
    jogador2 = X
    print('O JOGADOR 1, será o "O" e o JOGADOR 2, será o "X"')

print()
for i in range(0, 9, 3):
    print(i, "|", i+1, "|", i+2, "      ",
        tabuleiro[i], "|", tabuleiro[i+1], "|", tabuleiro[i+2])
print()
while jogo_valido:
    jogada = jogada + 1

    if jogada%2 == 1:
        casa = int(input("JOGADOR 1, escolha onde jogar: "))
        tabuleiro[casa] = jogador1
    else:
        casa = int(input("JOGADOR 2, escolha onde jogar: "))
        tabuleiro[casa] = jogador2
    print()
    for i in range(0, 9, 3):
        print(i, "|", i+1, "|", i+2, "      ",
            tabuleiro[i], "|", tabuleiro[i+1], "|", tabuleiro[i+2])
    print()

    # TODO: verificar se o jogo acabou
    # horizontal
    for i in range(0, 9, 3):
        if tabuleiro[i] == tabuleiro[i+1] == tabuleiro[i+2] != VAZIO:
            vencedor = tabuleiro[i]

    # vertical
    if not vencedor:
        for i in range(3):
            if tabuleiro[i] == tabuleiro[i+3] == tabuleiro[i+6] != VAZIO:
                vencedor = tabuleiro[i]

    # diagonal
    if not vencedor:
        for i in range(0, 3, 2):
            if tabuleiro[0+i] == tabuleiro[4] == tabuleiro[8-i] != VAZIO:
                vencedor = tabuleiro[i]

    if vencedor:
        jogo_valido = False
        print("Vencedor: ", vencedor)
    else:
        if not VAZIO in tabuleiro:
            jogo_valido = False
            print("Jogou empatou: Deu velha!")
