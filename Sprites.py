import pygame
import random
import sys

ALTO=500
ANCHO=700

class Dafebe(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		# self.jugador = self.imagen.subsurface((1555,1744, 106, 82))
		self.dir = 0
		self.x =0
		self.var_x = 0
		self.var_y = 0
		self.m = []
		correr = ['Dafebe2.png', 'Dafebe3.png', 'Dafebe4.png', 'Dafebe5.png', 'Dafebe1.png', 'Dafebe7.png']
		saltar = ['Dafebe9.png', 'Dafebe10.png', 'Dafebe11.png', 'Dafebe12.png', 'Dafebe13.png', 'Dafebe14.png', 'Dafebe15.png', 'Dafebe16.png']
		caer = ['Dafebe17.png', 'Dafebe17.png', 'Dafebe17.png', 'Dafebe18.png', 'Dafebe18.png', 'Dafebe18.png']
		self.aux = 0 
		aux = []
		for j in correr:
			aux.append(pygame.image.load('Imagenes/'+j).convert_alpha())
		self.m.append(aux)
		aux = []
		for j in saltar:
			aux.append(pygame.image.load('Imagenes/'+j).convert_alpha())
		self.m.append(aux)
		aux = []
		for j in caer:
			aux.append(pygame.image.load('Imagenes/'+j).convert_alpha())
		self.m.append(aux)
		self.image = self.m[self.dir][self.x]
		self.rect=self.image.get_rect()
		self.rect.y = 250

	def update(self):
		self.rect.x+=self.var_x
		self.rect.y+=self.var_y
		# if pygame.sprite.spritecollide(jp, objetos, False) != []:
		# 	self.rect.x -= self.var_x
		# 	self.rect.y -= self.var_y
		# 	self.var_x = 0
		# 	self.var_y = 0
		self.aux += 1
		if self.aux == 2:
			self.aux = 0
		if (self.var_x != 0 or self.var_y != 0) and self.aux == 0:
			self.x += 1
		if self.rect.x>ANCHO-self.rect[2]:
			self.rect.x = ANCHO-self.rect[2]
			self.var_x = 0
		if self.rect.x<0:
			self.rect.x=0
			self.var_x=0
		# if self.rect.y>ALTO-self.rect[3]:
		# 	self.rect.y = ALTO-self.rect[3]
		# 	self.var_y = 0
		# if self.rect.y<0:
		# 	self.rect.y=0
		# 	self.var_y = 0
		if self.dir ==0 and self.x > 5:
			self.x = 0
		if self.dir ==1 and self.x > 7:
			self.x = 0
		if self.dir ==2 and self.x > 5:
			self.x = 0
			self.dir = 0
		self.image=self.m[self.dir][self.x]

if __name__=='__main__':
	pygame.init()
	pantalla=pygame.display.set_mode([ANCHO,ALTO])
	nivel = 1
	jp = Dafebe()
	general = pygame.sprite.Group()
	general.add(jp)
	reloj=pygame.time.Clock()
	while True:
		while nivel == 1:
			for event in pygame.event.get():
				if event.type==pygame.QUIT:
					sys.exit()
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_ESCAPE:
						sys.exit()
					# if event.key == pygame.K_DOWN or event.key == pygame.K_s:
					# 	jp.dir = 0
					# 	jp.var_y = 1 
					if event.key == pygame.K_LEFT or event.key == pygame.K_a:
						jp.dir = 2
						jp.x = 0
						jp.var_x = 1
					if event.key == pygame.K_UP or event.key == pygame.K_w:
						jp.dir = 1
						jp.var_y = -1 
					if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
						jp.dir = 0
						jp.var_x = 3
					# if event.key == pygame.K_v :
					# 	if pygame.sprite.spritecollide(jp, Maquinas, False) != []:
					# 		if jp.rect.x < 465:
					# 			nivel = 2
					# 		else:
					# 			nivel = 3
					# 		pygame.mixer.music.stop()
				if event.type == pygame.KEYUP:
					# jp.var_x = 0
					jp.var_y = 0
			jp.update()
			pantalla.fill((0,160,0))
			general.draw(pantalla)
			pygame.display.flip()
			reloj.tick(60)