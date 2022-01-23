print('====== Desafio 012 ======')
# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto.
p = float(input('Digite o valor de um produto que você deseja ver com 5% de desconto: R$ '))
p = p - (p * 0.05)
print('O novo preço do produto com 5% de desconto é de R$ {:.2f}.'.format(p))
