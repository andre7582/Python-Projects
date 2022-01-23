from random import randint
print(f'{" Desafio 057 ":=^99}')
# Melhore o jogo do desafio 028, onde o computador vai "pensar" em um número entre
# 0 a 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final
# quantos palpites foram necessários.
print('>>> JOGO DA ADIVINHAÇÃO V.2.0')
print('.' * 99)
computador = randint(1, 10)
print('Sou seu computador...Acabei de pensar em um número de 1 a 10.')
resp = str(input('Você quer adivinhar qual foi? [ S = Sim, N = Não]: ')).upper()
acertou = False
palpites = 0
if resp in 'S':
    while not acertou:
        jogador = int(input('Qual é o seu palpite? '))
        palpites += 1
        if jogador <= 10:
            if jogador != computador:
                print('Que pena, você errou! Tente outra vez!')
                if jogador > computador:
                    print('O computador pensou num número menor!')
                if jogador < computador:
                    print('O computador pensou num número maior!')
                # print('Nº do computador: {}.'.format(computador))
            if jogador == computador:
                acertou = True
        elif jogador > 10:
            print('Você é cego ou é burro? Só valores de 1 a 10!')
    print('Parabéns! Você acertou com "apenas" {} tentativa(s)!'.format(palpites))
elif resp in 'N':
    print('Seu cagão!')
else:
    print('Não sabe digitar, não?\nSeu burro!')
print('.' * 99)
