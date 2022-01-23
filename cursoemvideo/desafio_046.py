from time import sleep
print(f'{" Desafio 046 ":=^99}')
# Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0.
print('>>> NEW YEAR COUNTDOWN')
print('.' * 99)
for c in range(10, 0, -1):
    print(c)
    sleep(1)
print("HAPPY NEW YEAR!!!")
print('.' * 99)