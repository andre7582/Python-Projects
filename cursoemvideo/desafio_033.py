from time import sleep
print('====== Desafio 033 ======')
# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
print('< Qual nº é o maior? E o menor? >')
print()
print('Digite 3 valores para fazer a comparação!')
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
n3 = int(input('Terceiro valor: '))
men = n1
if n2 < n1 and n2 < n3:
    men = n2
if n3 < n1 and n3 < n2:
    men = n3
mai = n1
if n2 > n1 and n2 > n3:
    mai = n2
if n3 > n1 and n3 > n2:
    mai = n3
mei = (n1 + n2 + n3) - (men + mai)
print()
print('Comparando...')
sleep(3)
print()
print('O maior valor digitado foi o \033[34m{}\033[m e o menor foi o \033[33m{}\033[m.'.format(mai, men))
print('(O outro número digitado foi o \033[35m{}\033[m.)'.format(mei))
print()
print('=== FIM do Desafio 033 ====')
