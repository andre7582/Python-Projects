print('====== Desafio 042 ======')
# Refaça o desafio 035, acrescentando o recurso de mostrar que tipo de triângulo será formado.
print()
print('< Analisando triângulos >')
print('.' * 99)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima podem formar um triângulo ', end='')
    if r1 == r2 == r3:
        print('EQUILÁTERO.')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO.')
    else:
        print('ISÓSCELES.')
else:
    print('Os segmentos acima NÃO podem formar um triângulo!')
print('.' * 99)
