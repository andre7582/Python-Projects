print(f'{" Challenge 103 ":=^99}')
# Write a program that has a function called profile(), which takes two optional parameters: a player's name
# and how many goals he has scored. The program must be able to show the player's file, even if some data has
# not been entered correctly.
print(">>>  Player's profile")
print("INSTRUCTIONS:\n# Enter a player's name and the number of goals scored by him/her.")
print('-' * 99)


def profile(player='<Unknown>', goals='<uncounted>'):
	print(f'* The player {player} scored {goals} goals.')


name = str(input("- Player's name: "))
score = str(input("- Goals scored: "))
if name.strip() == '' and score.strip() == '':
	profile()
elif score.strip() == '':
	profile(player=name)
elif name.strip() == '':
	profile(goals=score)
else:
	profile(name, score)
print('=' * 99)
