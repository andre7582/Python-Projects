from random import randint
from time import sleep
from operator import itemgetter
print(f'{" Challenge 091 ":=^99}')
# Create a program where 4 players roll a dice and get random results. Store these results in a Python dictionary.
# In the end, put that dictionary in order, knowing that the winner has taken the highest number on the die.
print('>>> Rolling a dice')
print("INSTRUCTIONS:\n*automatic*")
print('-' * 99)
game = {'player1': randint(1, 6), 'player2': randint(1, 6), 'player3': randint(1, 6), 'player4': randint(1, 6)}
result = list()
print('Rolling...')
for key, value in game.items():
	print(f' - {key}: rolled {value} on the dice.')
	sleep(0.5)
print('.-' * 17)
print('   >>> Result:')
result = sorted(game.items(), key=itemgetter(1), reverse=True)
for index, value in enumerate(result):
	print(f'   {index+1}º place: {value[0]} rolled a {value[1]}.')
print('=' * 99)
# print(game)
# print(result)
