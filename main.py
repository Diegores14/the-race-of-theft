import pygame
import random
from cursor import*
from opcion import*
from pygame.locals import*
from menu import*
from juegonuevo import*
from multijugador import*
from tutorial import*
from creditos import*
from salir import*


if __name__ == '__main__':

    opciones = [
        ("Jugar", juegonuevo),
        ("Multijugador", multijugador),
        ("Tutorial inicio", tutorial),
        ("Creditos", creditos),
        ("Salir", salir)
        ]

    pygame.font.init()
    pantalla = pygame.display.set_mode([700, 610])
    fondo = pygame.image.load("fondo5.png")
    menu = Menu(opciones)

    fin = False

    while not fin:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin = True

        pantalla.blit(fondo, (0,0))
        menu.actualizar()
        menu.imprimir(pantalla)
        pygame.display.flip()
        pygame.time.delay(10)
