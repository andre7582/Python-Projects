# Mundo 3 - Estruturas compostas (Tuplas)
# Tuplas são imutáveis

# lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')
# for comida in lanche:
# 	print(f'{comida}')

# lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')
# for contador in range(0, len(lanche)):
# 	print(f'{contador} {lanche[contador]}')

# lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')
# for contador, comida in enumerate(lanche):
# 	print(f'{contador} {comida}')

# lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')
# print(sorted(lanche))

a = (2, 5, 8)
b = (1, 3, 13)
c = (a + b)
# print(sorted(c))
for n in c:
	print(n)
