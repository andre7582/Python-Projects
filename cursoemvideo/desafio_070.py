print(f'{" Desafio 070 ":=^99}')
# Crie um programa que leia o nome e o preço de vários produtos e no final mostre o total gasto, quantos produtos
# custam mais de R$1000,00 e qual é o nome do produto mais barato.
print('>>> ESTATÍSTICAS EM PRODUTOS (COMÉRCIO)')
print('.' * 99)
print("INSTRUÇÕES:\nDigite o nome e o preço de quantos produtos desejar.\nQuando quiser sair basta digitar [N = não].")
print('.' * 99)
total = milhares = menor = cont = 0
barato = ' '
while True:
	produto = str(input('nome do produto: '))
	# noinspection NonAsciiCharacters
	preço = float(input('Preço: R$ '))
	cont += 1
	total += preço
	if preço > 1000:
		milhares += 1
	if cont == 1 or preço < menor:
		menor = preço
		barato = produto
	resp = ' '
	while resp not in 'SN':
		resp = str(input('Acrescentar outro produto: ')).upper().strip()[0]
	if resp == 'N':
		break
print(f'O total gasto foi de R$ {total:.2f}.')
print(f'Total de produtos custando mais de R$ 1000,00: {milhares}')
print(f'O produto mais barato foi a/o {barato} e custou R$ {menor:.2f}.')
print('Obrigado por usar nosso sistema!')
print('.' * 99)
