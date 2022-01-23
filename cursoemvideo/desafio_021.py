import pygame
print('====== Desafio 021 ======')
# Faça um programa em Python que abra e reproduza o aúdio de um arquivo MP3.
pygame.init()
pygame.mixer.music.load('music.mp3')
pygame.mixer.music.play()
pygame.event.wait()
