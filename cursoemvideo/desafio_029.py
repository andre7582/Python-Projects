print('====== Desafio 029 ======')
# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem
# dizendo que ele foi multado. Condição: A multa deve custar R$7,00 por cada Km acima do limite.
print()
print('< MULTA >')
print('-' * 51)
vel = float(input('Qual é a velocidade atual do carro? '))
if vel > 80:
    print('Multado! Você excedeu o limite de 80KM/h!')
    multa = (vel - 80) * 7
    print('Você pagará uma multa de R${:.2f}!'.format(multa))
else:
    print('Tenha um bom dia! Dirija com cuidado!')
print('-' * 51)