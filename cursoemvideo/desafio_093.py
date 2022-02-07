print(f'{" Challenge 093 ":=^99}')
# Create a program that manages the performance of a football player. The program will read the player's name
# and how many matches he played. Then will read the number of goals scored in each match.
# In the end, all this will be stored in a dictionary, including the total goals scored during the championship.
print('>>> Performance of a football player')
print("INSTRUCTIONS:\nEnter the data and the programa shows some select info about the player.")
print('-' * 99)
data = dict()
career = list()
data['name'] = str(input('Player name: '))
data['matches'] = int(input(f'How many matches {data["name"]} played? '))
for game in range(0, data['matches']):
	career.append(int(input(f'-> How many goals did he score in the {game+1}º game? ')))
data['goals'] = career[:]
data['totalgoals'] = sum(career)
print('-' * 99)
print(f' {data["name"]} played a total of {data["matches"]} matches. Below a list of his goals in each match:')
for index, value in enumerate(data['goals']):
	print(f' => {index+1}º match: {value} goals. ')
print('-' * 99)
print(f'< Summary of player career statistics >')
for key, value in data.items():
	print(f'  * {key}: {value}.')
print('=' * 99)
# print(data)
# print(career)
