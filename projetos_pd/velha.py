X = 'X'
O = 'O'
VAZ = ' '

tab = [X, X, X,
       O, VAZ, O,
       VAZ, VAZ, O]

ali = False
venc = VAZ

# horizontal
for i in range(0, 9, 3):
    if tab[i] == tab[i + 1] == tab[i + 2:] != VAZ:
        ali = True
        venc = tab[i]

# vertical
if not ali:
    for i in range(3):
        if tab[i] == tab[i + 3] == tab[i + 6:] != VAZ:
            ali = True
            venc = tab[i]

# diagonal
if not ali:
    for i in range(0, 3, 2):
        if tab[0 + i] == tab[4] == tab[8 - i] != VAZ:
            ali = True
            venc = tab[i]

if ali:
    print('Vencedor: ', vencedor)
else:
    if not VAZ in tab:
        print('O jogo empatou: Deu velha!')
