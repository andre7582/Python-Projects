from random import randint
from time import sleep
print(f'{" Challenge 088 ":=^99}')
# Make a program that helps the gambler to generate guesses. The program will allow you to choose the number
# of guesses and will draw 6 numbers between 1 and 60 for each bet, registering everything in a composite list.
print('>>> Lottery game')
print("INSTRUCTIONS:\nChoose the number of bets and the program will generate guesses for you.")
print('-' * 99)
bet = []
finalbet = []
amount = int(input('How many bets do you want to make? '))
bets = 1
while bets <= amount:
	numbers = 0
	while True:
		guess = randint(1, 60)
		if guess not in bet:
			bet.append(guess)
			numbers += 1
		if numbers >= 6:
			break
	bet.sort()
	finalbet.append(bet[:])
	bet.clear()
	bets += 1
print('-' * 99)
for entry, listing in enumerate(finalbet):
	print(f'Bet {entry:<3}: {listing}')
	sleep(0.5)
print('-' * 99)
print('Good Luck!')
print('=' * 99)
