# Aula 22 - Módulos e pacotes
from mathPackage.myFunctions import *


# main program
numberi = int(input("Enter a positive integer number: "))
factori = factoriali(numberi)
squari = squaredi(numberi)
squaredri = squaredrooti(numberi)
print(f'> The factorial of {numberi} is {factori}.')
print(f'> The number {numberi} squared is {squari}.')
print(f'> The square root of {numberi} is {squaredri}.')
