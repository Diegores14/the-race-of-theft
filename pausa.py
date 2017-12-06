import pygame
from pygame.locals import*

def pausa():
    pausado = True
    while pausado:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    pausado = False

                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()
