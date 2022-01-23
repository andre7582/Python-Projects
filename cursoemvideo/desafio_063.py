print(f'{" Desafio 063 ":=^99}')
# Escreva um programa que leia um número inteiro qualquer e mostre ns tela os n primeiros elementos de uma
# Sequência de Fibonacci.
print('>>> SEQUÊNCIA DE FIBONACCI')
print('.' * 99)
nt = int(input('Digite a quantidade de termos que você quer ver: '))
t1 = 0
t2 = 1
ct = 3
if nt == 1:
    print('Resp.: {}.'.format(t1))
elif nt == 2:
    print('Resp.: {} e {}.'.format(t1, t2))
elif nt == 3:
    print('Resp.: {}, {} e {}.'.format(t1, t2, (t1 + t2)))
else:
    print('Resp.: {}, {}, '.format(t1, t2), end='')
    while ct <= nt:
        t3 = t1 + t2
        print('{}'.format(t3), end='')
        if ct < nt - 1:
            print(', ', end='')
        elif ct == nt - 1:
            print(' e ', end='')
        else:
            print('.', end='')
        t1 = t2
        t2 = t3
        ct += 1
    print()
print('.' * 99)
