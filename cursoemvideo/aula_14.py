# Estrutura de repetição "while"
# n = 999
# par = impar = 0
# while n != 0:
#    n = int(input('Digite um valor: '))
#    if n != 0:
#        if n % 2 == 0:
#            par += 1
#        else:
#            impar += 1
# print('Você digitou {} número(s) par(es) e {} número(s) ímpar(es).'.format(par, impar))

# Perguntando se quer continuar
par = impar = 0
r = str(input('Quer digitar um número? [S/N]: ')).upper()
while r == 'S':
    n = int(input('Digite um valor: '))
    if n % 2 == 1:
        impar += 1
    else:
        par += 1
    r = str(input('Quer digitar outro número? [S/N]: ')).upper()
print('Você digitou {} número(s) par(es) e {} número(s) ímpar(es).'.format(par, impar))
