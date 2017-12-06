import pygame
from opcion import*

class Cursor:

    def __init__(self, x, y, var_y):

         self.image = pygame.image.load('cursorb.png')
         self.rect = self.image.get_rect()
         self.rect.x = x
         self.y_ini = y
         self.var_y = var_y
         self.y = 0
         self.seleccionar (0)

    def actualizar(self):
        self.y += (self.sel - self.y) /10
        self.rect.y = self.y

    def seleccionar(self, indice):
        self.sel = self.y_ini + (indice * self.var_y)

    def imprimir( self, pantalla):
        pantalla.blit(self.image, self.rect)
