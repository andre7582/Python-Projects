# laços de repetição (parte 3)
# interrompendo repetições while

n = s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
print(f'A soma vale {s}.')

'''# modo de interpolação f strings
nome = 'José'
idade = 33
salário = 987.3
print(f'O {nome:^10} tem {idade:^10} anos e ganha R$ {salário:^10.2f}')'''


