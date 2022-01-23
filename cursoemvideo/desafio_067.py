print(f'{" Desafio 067 ":=^99}')
# Faça um programa que mostre a tabuada do número digitado pelo usuário. O programa será interompido quando " "o
# valor digitado for negativo.
print('>>> TABUADA V3.0')
print('.' * 99)
print("INSTRUÇÕES:\nDigite um número inteiro para ver sua tabuada.\nQuando desejar parar "
      "digite um número negativo.")
print('.' * 99)
while True:
    print()
    num = int(input('Digite um número para ver sua tabuada: '))
    print()
    if num < 0:
        break
    elif num == 0:
        print('Todos os resultados serão iguais a zero!')
    else:
        print(f'-= TABUADA DO {num} =-')
        for con in range(1, 11):
            print(f'   {num} x {con:^2} = {num * con}')
        print('-=-=-=-=-=-=-=-=-')
print('Programa encerrado.')
print('.' * 99)
