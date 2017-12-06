import pygame
import random
import time
from cursor import*
from opcion import*
#from pygame.locals import*
from menu import*
from juegonuevo import*
from multijugador import*
from tutorial import*
from creditos import*
from salir import*
from configuracion import*
from pausa import*




if __name__ == '__main__':


    opciones = [
        ("Jugar", juegonuevo),
        ("Multijugador", multijugador),
        ("Tutorial inicio", tutorial),
        ("Creditos", creditos),
        ("Salir", salir)
        ]

    pygame.font.init()
    fuente = pygame.font.Font('explosive.ttf', 30)
    pantalla = pygame.display.set_mode([ANCHO, ALTO])
    fondo = pygame.image.load("fondo8.png")
    menu = Menu(opciones)
    gameover = False

    fin = False
    k = pygame.key.get_pressed()
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin = True


        pantalla.blit(fondo, (0,0))
        menu.actualizar()
        menu.imprimir(pantalla)
        pygame.display.flip()
        pygame.time.delay(10)
