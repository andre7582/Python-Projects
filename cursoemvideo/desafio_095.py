print(f'{" Challenge 095 ":=^99}')
# Enhance challenge 93 to work with multiple player, including a system to view details of each player's performance.
print('>>> Performance of a football players')
print("INSTRUCTIONS:\nEnter the data and the programa shows some select info about the players.")
print('-' * 99)
data = dict()
career = list()
team = list()
while True:
	career.clear()
	data['name'] = str(input('Player name: '))
	data['matches'] = int(input(f'How many matches {data["name"]} played? '))
	for game in range(0, data['matches']):
		career.append(int(input(f'-> How many goals did he score in the {game + 1}º game? ')))
	data['goals'] = career[:]
	data['totalgoals'] = sum(career)
	team.append(data.copy())
	towant = str(input('Do you want to enter more players? [Y/N]: ')).upper().strip()[0]
	while towant not in 'YN':
		print('Unexpected answer!')
		towant = str(input('Do you want to enter more players? [Yes or No]: ')).upper().strip()[0]
	if towant in 'N':
		break
print('-' * 99)
'''print('Ref.: ', end='')
for index in data.keys():
	print(f'{index:<25}', end='')
print()
for index, value in enumerate(team):
	print(f'{index+1:>5}', end='.')
	for players in value.values():
		print(f'{str(players):<25}', end='')
	print()'''
for index in team:
	print('    * ', end='')
	for key, value in index.items():
		print(f'{key}: {value}; ', end='')
	print()
print('-' * 99)
for index in team:
	print(f'< Summary of player career statistics >')
	for key, value in index.items():
		print(f'  * {key}: {value}.')
	print('_' * 39)
print('=' * 99)
# print(data)
# print(career)
# print(team)
