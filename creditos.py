import pygame
from main import*

def creditos():
    #print "creditos"
    pantalla = pygame.display.set_mode([ANCHO, ALTO])
    fondocreditos = pygame.image.load("creditos.png")
    pantalla.blit(fondocreditos, (0,0))
    pygame.display.flip()
    time.sleep(7)
