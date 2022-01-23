print(f'{" Desafio 053 ":=^99}')
# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
print('>>> DETECTOR DE PALÍNDROMOS')
print('.' * 99)
frase = str(input('Digite uma frase para ver se ela é um palíndromo: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) - 1, - 1, - 1):
    inverso += junto[letra]
if junto == inverso:
    print('Temos um palíndromo!')
else:
    print('Não é um palíndromo!')
print(junto, '=', inverso)
print('.' * 99)
