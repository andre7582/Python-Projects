print(f'{" Challenge 097 ":=^99}')
# make a program that has a function called write(), which takes any text as a parameter and displays
# a message with an adaptable size.
print('>>> Adaptive Hello World')
print("INSTRUCTIONS:\nEdit write() in the code.")
print('-' * 99)


def write(text):
	print('*' * (len(text) + 6))
	print(f'*  {text}  *')
	print('*' * (len(text) + 6))


write('Hello, World!')

print('=' * 99)
