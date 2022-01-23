from datetime import date
print(f'{" Desafio 054 ":=^99}')
# Crie um programa que leia o ano de nascimento de sete pessoas e mostre quantas pessoas são maiores de idade e
# quantas ainda não atingiram a maioridade.
print('>>> ANALISANDO IDADES')
print('.' * 99)
maior = 0
for pess in range(1, 8):
    nasc = int(input('Em que ano a {}ª pessoa nasceu? '.format(pess)))
    if date.today().year - nasc >= 18:
        maior += 1
print('Do total, {} pessoas são maiores de idade e {} ainda não atingiram a maioridade.'.format(maior, 7 - maior))
print('.' * 99)
