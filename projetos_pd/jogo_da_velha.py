jx = 'X'
jo = 'O'
VAZIO = ' '
tabuleiro = [VAZIO, VAZIO, VAZIO,
             VAZIO, VAZIO, VAZIO,
             VAZIO, VAZIO, VAZIO]
jogada = 0
jogo_valido = True
vencedor = False
print('      < Jogo da Velha >     ')
print()
jogador1 = input('Antes de iniciar, JOGADOR 1, escolha se quer jogar com "X" ou "O": ').upper()
print()
if jogador1 == jx:
    jogador2 = jo
    print('O JOGADOR 1 será o "{}" e o JOGADOR 2 será o "{}".'.format(jx, jo))
    if jogador1 == jo:
        jogador2 = jx
        print('O JOGADOR 1 será o "{}" e o JOGADOR 2 será o "{}".'.format(jo, jx))
    for i in range(0, 9, 3):
        print(i, "|", i + 1, "|", i + 2, "      ",
              tabuleiro[i], "|", tabuleiro[i + 1], "|", tabuleiro[i + 2])
else:
    print('O JOGADOR 1 deve escolher "X" ou "O"!')

print()





print()
while jogo_valido:
    jogada = jogada + 1
    if jogada % 2 == 1:
        casa = int(input("JOGADOR 1, escolha onde jogar: "))
        tabuleiro[casa] = jogador1
    else:
        casa = int(input("JOGADOR 2, escolha onde jogar: "))
        tabuleiro[casa] = jogador2
    print()
    for i in range(0, 9, 3):
        print(i, "|", i + 1, "|", i + 2, "      ",
              tabuleiro[i], "|", tabuleiro[i + 1], "|", tabuleiro[i + 2])
    print()
    for i in range(0, 9, 3):
        if tabuleiro[i] == tabuleiro[i + 1] == tabuleiro[i + 2] != VAZIO:
            vencedor = tabuleiro[i]
    if not vencedor:
        for i in range(3):
            if tabuleiro[i] == tabuleiro[i + 3] == tabuleiro[i + 6] != VAZIO:
                vencedor = tabuleiro[i]
    if not vencedor:
        for i in range(0, 3, 2):
            if tabuleiro[0 + i] == tabuleiro[4] == tabuleiro[8 - i] != VAZIO:
                vencedor = tabuleiro[i]
    if vencedor:
        jogo_valido = False
        print("Vencedor: ", vencedor)
    else:
        if VAZIO in tabuleiro:
            continue
        jogo_valido = False
        print("Jogou empatou: Deu velha!")
