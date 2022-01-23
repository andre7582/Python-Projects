print('====== Desafio 022 ======')
# Crie um programa que leia o nome completo de uma pessoa e mostre:
# > O nome com todas as letras maiúsculas e também todas em minúsculas.
# > Quantas letras tem o nome (sem considerar os espaços)
# > Quantas letras tem o primeiro nome.
print()
nome = str(input('Digite seu nome: ')).strip()
print('Seu nome com todas as letras maiúsculas:', nome.upper())
print('Seu nome com todas as letras minúsculas é {}.'.format(nome.lower()))
# print('Seu nome tem ao todo {} letras.'.format(len(nome) - nome.count(' ')))
# print('Seu primeiro nome tem {} letras.'.format(nome.find(' ')))
div = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras.'.format(div[0], len(div[0])))
