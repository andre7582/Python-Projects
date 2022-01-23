print('=== aula 09 ===')

#Análise strings

frase = str('Curso em Video Python')
print(frase)
print(frase[9])
print(frase[9:14])
print(len(frase))
print(frase.count('o'))
print(frase.find('deo'))
print('Curso' in frase)

#Transformação

print(frase.replace('Python', 'Android'))
print(frase.upper())
print(frase.lower())
frase = (frase.replace('Python', 'Android'))
print(frase)
print(frase.split())
print('+'.join(frase))
