import pygame
import random
import sys
import configparser

ALTO=465
ANCHO=700

class Dafebe(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
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
			self.var_x = 3
		self.image=self.m[self.dir][self.x]

class Diare(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.dir = 0
		self.x =0
		self.var_x = 0
		self.var_y = 0
		self.m = []
		correr = ['Diare1.png', 'Diare2.png', 'Diare3.png', 'Diare4.png', 'Diare5.png', 'Diare6.png', 'Diare7.png',
					'Diare7.png','Diare8.png','Diare9.png','Diare10.png','Diare11.png']
		saltar = ['Diare12.png', 'Diare13.png', 'Diare14.png', 'Diare15.png', 'Diare16.png', 'Diare17.png', 'Diare18.png', 'Diare19.png', 'Diare20.png']
		caer = ['Diare21.png', 'Diare21.png', 'Diare21.png', 'Diare22.png', 'Diare22.png', 'Diare22.png']
		self.aux = 0 
		aux = []
		for j in correr:
			aux.append(pygame.transform.flip(pygame.image.load('Imagenes/'+j).convert_alpha(),False,True))
		self.m.append(aux)
		aux = []
		for j in saltar:
			aux.append(pygame.image.load('Imagenes/'+j).convert_alpha())
		self.m.append(aux)
		aux = []
		for j in caer:
			aux.append(pygame.transform.flip(pygame.image.load('Imagenes/'+j).convert_alpha(),True,False))
		self.m.append(aux)
		self.image = self.m[self.dir][self.x]
		self.rect=self.image.get_rect()
		self.rect.y = 250

	def update(self):
		self.rect.x+=self.var_x
		self.rect.y+=self.var_y
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
		if self.dir ==0 and self.x > 10:
			self.x = 0
		if self.dir ==1 and self.x > 8:
			self.x = 0
		if self.dir ==2 and self.x > 5:
			self.x = 0
			self.dir = 0
			self.var_x = 3
		self.image=self.m[self.dir][self.x]

class Sesagon(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.dir = 0
		self.x =0
		self.var_x = 0
		self.var_y = 0
		self.m = []
		correr = ['Sesagon1.png', 'Sesagon2.png', 'Sesagon3.png', 'Sesagon4.png', 'Sesagon5.png', 'Sesagon6.png', 'Sesagon7.png',
					'Sesagon7.png','Sesagon8.png','Sesagon9.png','Sesagon10.png','Sesagon11.png']
		saltar = ['Sesagon12.png', 'Sesagon13.png', 'Sesagon14.png', 'Sesagon15.png', 'Sesagon16.png', 'Sesagon17.png', 'Sesagon18.png', 'Sesagon19.png', 'Sesagon20.png', 'Sesagon21.png',]
		caer = ['Sesagon22.png', 'Sesagon22.png', 'Sesagon23.png', 'Sesagon23.png', 'Sesagon24.png', 'Sesagon24.png']
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
			self.var_x = 3
		self.image=self.m[self.dir][self.x]

class Interfaz():
	def __init__(self, pantalla,  mapa):
		self.interprete=configparser.ConfigParser()
		self.interprete.read(mapa)
		self.interprete.items('nivel1')
		# for i in interprete.items(nivel):
		# 	print(i)
		# 	if i[0] == 'imagen':
		# 		self.imagen = pygame.image.load(i[1]).convert_alpha()
		# 	else:
		# 		corte = self.imagen.subsurface(eval(interprete.get('cortes',i[0])))
		# 		for pos in eval(i[1]):
		# 			pantalla.blit(corte,pos)		
		# pygame.display.flip()

if __name__=='__main__':
	pygame.init()
	pantalla=pygame.display.set_mode([ANCHO,ALTO])
	# interprete=configparser.ConfigParser()
	# interprete.read('Mapa.map')
	# inter = Interfaz(pantalla, 'Mapa.map')
	pygame.mixer.music.load('Musica/Vegasis_-_Nightwatcher.ogg')
	pygame.mixer.music.load('Musica/Hannes_Hofkind_-_Emphasize.ogg')
	pygame.mixer.music.load('Musica/ONSTEAD_-_Nightfall.ogg')
	pygame.mixer.music.load('Musica/Zero-project_-_Distorted_reality.ogg')
	pygame.mixer.music.play(-1,0.0)
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