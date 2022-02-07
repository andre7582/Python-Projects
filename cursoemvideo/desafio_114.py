import urllib.error
import urllib.request
print(f'{" Challenge 114 ":=^99}')
#
print('>>> ')
print("INSTRUCTIONS:\n# .")
print('-' * 99)
# main program
try:
	site = urllib.request.urlopen('https://www.google.xom')
except urllib.error.URLError:
	print('404')
else:
	print('Conected')
print('=' * 99)
