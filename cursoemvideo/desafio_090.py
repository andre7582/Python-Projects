print(f'{" Challenge 090 ":=^99}')
# Write a program that reads a student's name and average grade, saves the data in a dictionary (dict).
# At the end, show the contents on the screen.
print('>>> School result')
print("INSTRUCTIONS:\nEnter a student's name and their average grade and the program will show the final result.")
print('-' * 99)
pupil = dict()
pupil['name'] = str(input('Name: '))
pupil['average'] = float(input(f'Average grade of {pupil["name"]}: '))
if pupil['average'] >= 7:
	pupil['status'] = 'Passed'
elif 5 <= pupil['average'] < 7:
	pupil['status'] = 'Recovery'
else:
	pupil['status'] = 'Failed'
for key, value in pupil.items():
	print(f' - {key}: {value}.')
print('=' * 99)
# print(pupil)
