from random import randint
print(f'{" Desafio 068 ":=^99}')
# Faça um programa que jogue par ou ímpar com o computador. O jogo é interrompido quando o jogador perder mostrando "
# "o total de vitórias consecutivas dele.
print('>>> JOGO DO PAR OU ÍMPAR')
print('.' * 99)
print("INSTRUÇÕES:\nEscolha se você quer [P = par] ou [I = ímpar].\nDigite um valor de 0 a 5 para jogar e "
      "veja se deu par ou ímpar.\nObs: O jogo segue até o computador vencer.")
print('.' * 99)
vit = 0
while True:
    print()
    tip = ' '
    while tip not in 'PI':
        tip = str(input('Escolha PAR ou ÍMPAR: ')).upper().strip()[0]
    njo = int(input('Escolha um número para jogar: '))
    nco = randint(0, 5)
    print(f'Você jogou {njo} e o computador jogou {nco}.')
    tot = njo + nco
    if tot % 2 == 0:
        tot = 'P'
        print('Deu par!')
        if tip == tot:
            print('Você venceu!')
            vit += 1
        else:
            print('Você perdeu!')
            break
    else:
        tot = 'I'
        print('Deu ímpar!')
        if tip == tot:
            print('Você venceu!')
            vit += 1
        else:
            print('Você perdeu!')
            break
if vit == 0:
    print('Que pena! Você não venceu nenhuma vez!')
elif vit == 1:
    print('Você venceu apenas uma vez!')
else:
    print(f'Você venceu {vit} vezes! Até mais!')
print('.' * 99)
