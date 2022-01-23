print('====== Desafio 008 ======')
# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
vm = float(input('Digite um valor em metros: '))
cc = vm * 100
cm = vm * 1000
if vm == 1:
    print('Resp.: {:.0f} metro é igual a {:.0f} centímetros ou {:.0f} milímetros.'.format(vm, cc, cm))
else:
    print('Resp.: {} metros são {:.0f} centímetros ou {:.0f} milímetros.'.format(vm, cc, cm))
