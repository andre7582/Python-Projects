print('====== Desafio 010 ======')
# Crie um programa que leia quanto dinheiro uma pessoa tem e mostre quantos dólares ela pode comprar.
# Considere US$1,00 = R$3,27
print()
r = float(input('Digite o valor em Reais que você deseja converter em dólares: R$ '))
d = float(r / 3.27)
print()
if r == 3.27:
    print('R$ {:.2f} é igual a US$ {:.2f}.'.format(r, d))
else:
    print('R$ {:.2f} são US$ {:.2f}.'.format(r, d))
