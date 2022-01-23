print('====== Desafio 036 ======')
# Escreva um programa para aprovar o empréstimo de uma casa. O programa vai perguntar o valor da casa,
# o salário do comprador e em quantos anos ele vai pagar.
# Condição: Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30%  do salário.
print()
print('< Simulador de empréstimo bancário para compra de uma casa>')
print('-' * 51)
vac = float(input('Qual é o valor do imóvel que pretende financiar? R$ '))
qan = float(input('Em quantos anos pretende pagar o empréstimo? '))
sal = float(input('Qual é o valor da sua renda mensal? R$ '))
emp = vac / (qan * 12)
oky = sal * 0.3
# print(emp)
# print(oky)
if emp <= oky:
    print('Você vai pagar uma prestação de R$ {:.2f} mensais. Empréstimo aprovado!'.format(emp))
else:
    print('O valor da mensalidade excede 30% da sua renda! Seu empréstimo foi negado.')
print('-' * 51)
