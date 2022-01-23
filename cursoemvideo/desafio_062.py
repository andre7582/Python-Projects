print(f'{" Desafio 062 ":=^99}')
# Melhore o desafio 051, perguntando se o usuário quer mostrar mais termos. 0 finaliza o programa.
print('>>> PROGRESSÃO ARITMÉTICA V3.0')
print('.' * 99)
pt = int(input('Primeiro termo da PA: '))
rz = int(input('Razão: '))
qt = int(input('Quantidade de termos: '))
ct = 1
tt = 0
while qt != 0:
    tt += qt
    while ct <= tt:
        print('Resp.: ' if ct == tt - (qt-1) else '', end='')
        print('{}'.format(pt), end='')
        if ct < tt - 1:
            print(', ', end='')
        elif ct == tt - 1:
            print(' e ', end='')
        else:
            print('.', end='')
        pt += rz
        ct += 1
    print()
    print()
    qt = int(input('Para mostrar mais termos da PA, digite a quantidade desejada: '))
print('Programa encerrado. Foram mostrados {} termos.'.format(tt))
print('.' * 99)
