print(f'{" Desafio 069 ":=^99}')
# Crie um programa que leia a idade e o sexo de várias pessoas e no final mostre quantas pessoas são maiores de idade "
# "quantos homens foram cadastrados e quantas mulheres tem menos de 20 anos.
print('>>> ANÁLISE DE DADOS EM GRUPO')
print('.' * 99)
print("INSTRUÇÕES:\nDigite a idade e o sexo de quantas pessoas desejar.\nQuando quiser sair basta digitar [N = não].")
print('.' * 99)
maior = homem = novinha = 0
while True:
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    if idade >= 18:
        maior += 1
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: ')).strip().upper()[0]
    if sexo == 'M':
        homem += 1
    if sexo == 'F' and idade <18:
        novinha += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'Total dos cadastrados maiores de 18 anos: {maior}')
print(f'Total de homens cadastrados: {homem}')
print(f'Total de mulheres com menos de 18 anos: {novinha}')
print('Obrigado por usar o nosso sistema! Tenha um bom dia!')
print('.' * 99)
