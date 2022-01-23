print('====== Desafio 012 ======')
# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto.
print()
print('Quer saber o novo preço de um produto que está com desconto?')
p = float(input('Digite o valor do produto: R$ '))
d = float(input('Digite o desconto em porcentagem: '))
pd = p - (p * d / 100)
print()
print('O novo preço do produto com {:.0f}% de desconto é de R$ {:.2f}.'.format(d, pd))
