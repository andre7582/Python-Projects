print(f'{" Desafio 044 ":=^99}')
# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço inicial e condições
# de pagamento. Condições: à vista(dinheiro/cheque): -10%, à vista (cartão): -5%, até 2x: preço normal, >3x: preço +20%
print('>>> GERENCIADOR DE PAGAMENTOS')
print('.' * 99)
pre = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO:
[1] à vista (dinheiro/cheque)
[2] à vista (cartão)
[3] até 2x no cartão
[4] 3x ou mais no cartão''')
esc = int(input('Qual é a sua opção? '))
if esc == 1:
    tot = pre - (pre * 0.1)
elif esc == 2:
    tot = pre - (pre * 0.05)
elif esc == 3:
    tot = pre
    par = tot / 2
    print('Sua compra será parcelada em 2x de R${:.2f}.'.format(par))
elif esc == 4:
    tot = pre + (pre * 0.2)
    top = int(input('Quantas parcelas? '))
    if top >= 3:
        tpa = tot / top
        print('Sua compra será parcelada em {}x de R${:.2f}.'.format(top, tpa))
    elif top < 3:
        tot = pre - pre
        print('Opção inválida. Escolha 3x ou mais.')
else:
    tot = pre - pre
    print('Opção inválida. Escolha opções de 1 a 4.')
print('O total a pagar é de R${:.2f}.'.format(tot))
print('.' * 99)
