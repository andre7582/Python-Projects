print('====== Desafio 025 ======')
# Crie um programa que leia o nome de uma pessoa e diga se tem "SILVA" no nome dela.
print()
sil = str(input('Qual é seu nome completo? Res.: ')).strip()
s = 'silva' in sil.lower()
if s:
    print('Que legal! Seu nome também tem Silva!!')
else:
    print('Que pena! Seu nome não tem Silva!!')
