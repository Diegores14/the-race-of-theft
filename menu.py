import pygame
import random
from cursor import*
from opcion import*
from pygame.locals import*
from main import*

class Menu():

    def __init__(self, opciones):
        self.opciones = []
        fuente = pygame.font.Font('explosive.ttf', 30)
        x = 210
        y = 160
        p = 1

        self.cursor = Cursor(x - 30, y+12 , 90)

        for titulo, f in opciones:
            self.opciones.append(Opcion(fuente, titulo, x, y, p, f))
            y += 90
            if p == 1:
                p -= 1
            else:
                p = 1

        self.seleccionado = 0
        self.total = len(self.opciones)
        self.pulsa = False

    def actualizar(self):
        k = pygame.key.get_pressed()

        if not self.pulsa:
            if k[K_UP]:
                self.seleccionado -= 1
            elif k[K_DOWN]:
                self.seleccionado += 1
            elif k[K_RETURN]:
                self.opciones[self.seleccionado].activar()


        if self.seleccionado < 0:
            self.seleccionado = 0
        elif self.seleccionado > self.total - 1:
            self.seleccionado = self.total - 1

        self.cursor.seleccionar(self.seleccionado)

        self.pulsa = k[K_UP] or k[K_DOWN] or k[K_RETURN]

        self.cursor.actualizar()

        for o in self.opciones:
            o.actualizar()

    def imprimir(self, pantalla):
        self.cursor.imprimir(pantalla)

        for opcion in self.opciones:
                opcion.imprimir(pantalla)
