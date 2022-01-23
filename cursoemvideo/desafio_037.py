print('====== Desafio 037 ======')
# Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
# 1 para binário; 2 para octal; e 3 para hexadicimal.
print()
print('< Conversor numérico >')
print('-' * 51)
num = int(input('Digite um número inteiro que deseja converter: '))
print('''Escolha umas das opções a seguir para realizar a conversão:
[ 1 ] Converter para BINÁRIO.
[ 2 ] Converter para OCTAL.
[ 3 ] Converter para HEXADECIMAL''')
esc = int(input('Opção escolhida: '))
if esc == 1:
    print('{} convertido para BINÁRIO é igual a {}.'.format(num, bin(num)[2:]))
elif esc == 2:
    print('{} convertido para OCTAL é igual a {}.'.format(num, oct(num)[2:]))
elif esc == 3:
    print('{} convertido para HEXADECIMAL é igual a {}.'.format(num, hex(num)[2:]))
else:
    print('Opção inválida! Escolha uma das 3 opções!')
print('-' * 51)
