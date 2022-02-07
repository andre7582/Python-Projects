from time import sleep

print(f'{" Challenge 098 ":=^99}')
# Write a program that has a function called counter(), which takes three parameters: start, end, and step.
# Your program has to perform three counts through the created function: a) From 1 to 10 (1 by 1);
# b) From 10 to 0 (2 by 2); c) A custom count (*STEP MUST BE A POSITIVE VALUE*)
print('>>> Counter')
print("INSTRUCTIONS:\nInput the parameters and the program will show a sequence of numbers.")
print('-' * 99)


def separator():
	print('.' * 99)


def counter(start, end, step):
	if step <= 0:
		step = 1
		print('- STEP VALUE HA BEEN CHANGED TO 1 SO THAT PROGRAM WORKS CORRECTLY -')
	print(f'Counting from {start} to {end}. ({step} by {step})')
	sleep(2)
	if start < end:
		count = start
		while count <= end:
			print(f'{count}; ', end='')
			sleep(0.3)
			count += step
		print('<THE END!>')
		separator()
	else:
		count = start
		while count >= end:
			print(f'{count}; ', end='')
			sleep(0.3)
			count -= step
		print('<THE END!>')
		separator()


counter(1, 10, 1)
counter(10, 0, 2)

print('* CUSTOM COUNT *')
in1 = int(input('  Start: '))
in2 = int(input('  End: '))
in3 = int(input('  Step: '))
counter(in1, in2, in3)

print('=' * 99)
