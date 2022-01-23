print(f'{" Desafio 056 ":=^99}')
# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas e no final mostre: a média de idade do grupo,
# quantas mulheres tem menos de 20 anos e qual é o nome do homem mais velho.
print('>>> ANALISADOR COMPLETO')
print('.' * 99)
contmu = 0
velhoi = 0
velhon = 0
somida = 0
medida = 0
n = int(input('Quantos pessoas serão comparadas? '))
for p in range(1, n + 1):
    print('------- {}ª PESSOA -------'.format(p))
    nome = str(input('Nome: ')).strip().upper()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    somida += idade
    if p == 1 and sexo in 'M':
        velhoi = idade
        velhon = nome
    if sexo in 'M' and idade > velhoi:
        velhoi = idade
        velhon = nome
    if sexo in 'F' and idade < 20:
        contmu += 1
medida = somida / n
print('-' * 99)
print('Soma das idades registradas é de {} anos e a média é de {:.1f} anos.'.format(somida, medida))
if velhoi == 0:
    print('Não havia homens entre os nomes cadastrados!')
else:
    print('Nome do homem mais velho: {}. Idade dele: {} anos.'.format(velhon, velhoi))
if contmu == 0:
    print('Não havia homens entre os nomes cadastrados!')
elif contmu == 1:
    print('Há apenas uma mulher com menos de 20 anos.')
else:
    print('Ao todo são {} mulheres com menos de 20 anos.'.format(contmu))
print('.' * 99)
