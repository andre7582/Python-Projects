print(f'{" Desafio 073 ":=^99}')
# Crie uma tupla preenchida com os 20 primeiros colocados da tabela do Brasileirão 2017 e depois mostre:
# a) Os 5 primeiros; b) Os últimos 4; c) Times na ordem alfabética; d) Posição da Chapecoense.
print('>>> Brasileirão 2017')
print('-' * 99)
times = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio', 'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoense',
            'Atlético-MG', 'Botafogo', 'Athlético', 'Bahia', 'São Paulo', 'Fluminense', 'Sport', 'Vitória',
            'Coritiba', 'Avaí', 'Ponte Preta', 'Atlético-GO')
print('')
print(f'Lista de times: {times}')
print('')
print(f'Os 5 primeiros são: {times[0:5]}')
print('')
print(f'Os 4 últimos são: {times[-4:]}')
print('')
print(f'Times em ordem alfabética: {sorted(times)}')
print('')
print(f'A Chapecoense ficou na {times.index("Chapecoense")+1}ª posição.')
print('')
print('-' * 99)
