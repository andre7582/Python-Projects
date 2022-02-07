from random import randint
from time import sleep
print(f'{" Challenge 100 ":=^99}')
# Write a program that has a list called numbers and two functions called draw() and sumPair().
# The first function will sort between 5 numbers and sort within the list and the second function will show
# the sum of all even values sorted by the previous function.
print('>>> Functions: another exercise')
print("INSTRUCTIONS:\nEdit the functions (in the end of code) to change results.")
print('-' * 99)


def draw(values):
	print('Drawing five numbers... ')
	for count in range(0, 5):
		raffle = randint(1, 10)
		values.append(raffle)
		print(f'{raffle}; ', end='')
		sleep(0.5)
	print('< END! >')


def sumpair(values):
	addingpairs = 0
	for value in values:
		if value % 2 == 0:
			addingpairs += value
	print(f'+ Adding the even numbers we get {addingpairs}.')


numbers = list()
draw(numbers)
sumpair(numbers)

print('=' * 99)
# print(numbers)
# print(draw)
