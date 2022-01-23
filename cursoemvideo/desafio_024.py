print('====== Desafio 024 ======')
# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO". .
print()
cid = str(input('Em que cidade você nasceu? Res.: ')).strip()
print(cid[:5].upper() == 'SANTO')
