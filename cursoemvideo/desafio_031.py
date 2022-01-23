print('====== Desafio 031 ======')
# Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem cobrando
# R$0,50 por Km para viagens até 200Km e R$0,45 para viagens mais longas.
print()
print('< CUSTO DA VIAGEM >')
print('-' * 51)
cuvi = float(input('Qual é a distância da sua viagem? '))
preço = cuvi * 0.50 if cuvi <= 200 else cuvi * 0.45
print('O preço da passagem será de {}R${:.2f}{}.'.format('\033[34m', preço, '\033[m'))
print('-' * 51)
