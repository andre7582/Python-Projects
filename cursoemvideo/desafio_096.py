print(f'{" Challenge 096 ":=^99}')
# Write a program that has a function called area(), which receives the dimensions of a rectangular terrain
# (width and length) and show the area of the terrain.
print('>>> Terrain Area Calculator')
print("INSTRUCTIONS:\nInput the dimensions of a terrain (width and length) and the program will show the area of it.")
print('-' * 99)


def title(txt):
	print('-' * 60)
	print(txt)
	print('-' * 60)


def entry(width, length):
	area = width * length
	print(f'\nA terrain measuring {width}m X {length}m has an area of {area}m².')


title(f'{"TERRAIN AREA CALCULATOR":^60}')

measure1 = float(input('Width(m): '))
measure2 = float(input('Length(m): '))
entry(measure1, measure2)
print('-' * 60)
print('=' * 99)
