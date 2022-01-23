print('====== Desafio 007 ======')
# Desenvolva um programa que leia as notas de um aluno, calcule e mostre sua média.
n1 = float(input('Digite a nota do 1º trimestre: '))
n2 = float(input('Digite a nota do 2º trimestre: '))
n3 = float(input('Digite a nota do 3º trimestre: '))
r = (n1 + n2 + n3) / 3
print('A média obtida a partir das notas é: {:.1f}.'.format(r))
