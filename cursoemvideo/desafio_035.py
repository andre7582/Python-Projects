print('====== Desafio 035 ======')
# Desenvolva um programa que leia o comprimentto de três retas e diga ao usuário se elas podem ou não formar um
# triângulo.
print()
print('< Desafio do triângulo >')
print('-' * 51)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
print()
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos \033[32mpodem\033[m formar um triângulo!')
else:
    print('Os segmentos \033[31mNÃO podem\033[m formar um triângulo!')
print('-' * 51)
