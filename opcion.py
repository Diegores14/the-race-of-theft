import pygame
from cursor import*
from configuracion import*

class Opcion:

    def __init__(self, fuente, titulo, x, y, paridad, funcion):
        self.imagen_normal = fuente.render(titulo, 1, BLANCO)
        self.image = self.imagen_normal
        self.rect = self.image.get_rect()
        self.rect.x = x * paridad
        self.rect.y = y
        self.funcion = funcion
        self.x = float(self.rect.x)

    def actualizar(self):
        destino_x = 100
        self.x += (destino_x  - self.x)
        self.rect.x = int(self.x)

    def imprimir(self, pantalla):
        pantalla.blit(self.image, self.rect)


    def activar(self):
        self.funcion()
