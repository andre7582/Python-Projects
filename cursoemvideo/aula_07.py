print('=== aula 07 ===')
#Ordem de precedência: () | ** | * / // % | + -

print('<As quatro operações com os mesmos valores predeterminados>')
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
sm = n1 + n2
sb = n1 - n2
ml = n1 * n2
dv = n1 / n2
print('A soma dos números é {}, a diferença entre eles é {}, o produto é {} e a divisão é {:.1f}'.format(sm, sb, ml, dv))
