print(f'{" Challenge 101 ":=^99}')
# Create a program that has a function called vote() that will receive as a parameter the year of birth of a person,
# returning a literal value indicating whether a person has a DENIED, OPTIONAL and MANDATORY vote in the elections.
print('>>> Voting program ')
print("INSTRUCTIONS:\nEnter the data and the program will return the person's condition regarding the next elections.")
print('-' * 99)


def vote(birth):
	from datetime import date
	current = date.today().year
	age = current - birth
	if age < 16:
		return f"> This voter does not vote."
	elif 16 <= age < 18 or age >= 65:
		return f'> This voter has optional vote.'
	else:
		return f'> This voter has a mandatory vote.'


year = int(input('Year of birth: '))
print(vote(year))

print('=' * 99)
