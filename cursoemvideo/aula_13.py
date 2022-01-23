# Estrutura de repetição "for"
n = int(input('Digite um número: '))
for c in range(0, n):
    print(c)
print('FIM')

# somando 5 valores em sequencia
soma = 0
for c in range(0, 5):
    num = int(input('Digite um valor para somar: '))
    soma = soma + num
print('A soma de todos os valores foi {}.'.format(soma))
