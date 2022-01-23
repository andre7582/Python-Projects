print(f'{" Desafio 057 ":=^99}')
# FAça um programa que leia o sexo de uma pessoa, mas só aceite os valores "M" ou "F". Caso esteja errado,
# peça a digitação novamente até ter um valor correto.
print('>>> VALIDAÇÃOZINHA DE DADOS')
print('.' * 99)
sexo = str(input('Informe seu sexo [ M = masculino, F = feminino ]: ')).strip().upper()
while sexo not in 'MmFf':
    print('Ocorreu um erro na validação dos dados. Por favor, digite novamente.')
    sexo = str(input('Informe seu sexo [ M = masculino, F = feminino ]: ')).strip().upper()
if sexo in 'M':
    print('Sexo masculino registrado com sucesso!')
if sexo in 'F':
    print('Sexo feminino registrado com sucesso!')
print('.' * 99)
