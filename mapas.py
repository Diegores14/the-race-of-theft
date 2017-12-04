import configparser
import pygame
import sys
import time
import math

ALTO=610
ANCHO=700
ROJO=(255,0,0)
BLANCO=(255,255,255)
NEGRO=(0,0,0)
AZUL=(59,131,189)
centro=[ANCHO/2,ALTO/2]

class Cuchilla(pygame.sprite.Sprite):
	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)
		self.giro = ['Cuchilla2.png', 'Cuchilla3.png', 'Cuchilla4.png', 'Cuchilla5.png', 'Cuchilla6.png','Cuchilla7.png']
		self.image = pygame.image.load('Cuchilla1.png').convert_alpha()
		self.i=0
		self.rect=self.image.get_rect()
		self.rect.x = x
		self.rect.y = y

	def update(self):
		self.image = pygame.image.load(self.giro[self.i]).convert_alpha()
		self.i+=1
		if self.i>5:
			self.i=0

class Barra(pygame.sprite.Sprite):
	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load('Barra.png').convert_alpha()
		self.rect=self.image.get_rect()
		self.rect.x = x
		self.rect.y = y

class Bloque(pygame.sprite.Sprite):
	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load('Bloque.png').convert_alpha()
		self.rect=self.image.get_rect()
		self.rect.x = x
		self.rect.y = y

class Player1(pygame.sprite.Sprite):
	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load('Dafebe1.png').convert_alpha()
		self.corre = [pygame.image.load('Dafebe2.png').convert_alpha(),pygame.image.load('Dafebe3.png').convert_alpha(),pygame.image.load('Dafebe4.png').convert_alpha(),pygame.image.load('Dafebe5.png').convert_alpha(),pygame.image.load('Dafebe6.png').convert_alpha(),pygame.image.load('Dafebe7.png').convert_alpha(),pygame.image.load('Dafebe8.png').convert_alpha()]
		self.rect=self.image.get_rect()
		self.salto=False
		self.i=0
		self.rect.x = x
		self.rect.y = y
		self.vary = 0
		self.varx = 0

	def update(self):
		if not self.salto:
			self.image=self.corre[self.i]
			self.i+=1
			if self.i>6:
				self.i=0

class Player2(pygame.sprite.Sprite):
	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load('Dafebe1.png').convert_alpha()
		self.rect=self.image.get_rect()
		self.rect.x = x
		self.rect.y = y

class Player3(pygame.sprite.Sprite):
	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load('Dafebe1.png').convert_alpha()
		self.rect=self.image.get_rect()
		self.rect.x = x
		self.rect.y = y



def drop_string(cad):
	i=0
	ncad=''
	for c in cad:
		if i == 0:
			i+=1
		else:
			ncad= ncad + c
	return ncad


if __name__== '__main__':
	#inicio de pygame con fondo negro
	pygame.init()
	pygame.display.set_caption('Mapas')
	pantalla=pygame.display.set_mode([ANCHO,ALTO])
	pantalla.fill(NEGRO)

	#lectura del mapa
	interprete=configparser.ConfigParser()
	interprete.read('mapa.map')

	#carga y transfomacion de las imagenes necesarias
	fondo1=pygame.image.load('Fondo1.jpg')
	fondo1_1=pygame.transform.scale(fondo1,(900,710))
	nada=pygame.image.load('inv.png')

	#dividiendo el mapa en lineas
	dicc={}
	for seccion in interprete.sections():
		descripcion=dict(interprete.items(seccion))
		dicc[seccion]=descripcion

	#definiendo variables y grupos de sprites necesarios
	reloj=pygame.time.Clock()
	jp1=Player1(20,100)
	general = pygame.sprite.Group()
	cuchillas = pygame.sprite.Group()
	barras= pygame.sprite.Group()
	bloques= pygame.sprite.Group()
	general.add(bloques)
	general.add(cuchillas)
	general.add(barras)
	general.add(jp1)
	inicio=pygame.time.get_ticks() # variable de tiempo
	mapa=dicc['nivel1-tutorial']['mapa'] # mapa
	lineas=mapa.split()
	fin=False
	x=80 #variable que controla la velocidad
	in_game=True # variable que controla el refresco de pantalla, si esta en juego usa time.delay(x) y si no usa, reloj.tick(60)
	vel=True # variable para que el tiempo no se reduzca en varias iteraciones donde el tiempo es el mismo, ya que es un aproximado

	# ciclo del juego
	while not fin:
		#carga del fondo
		pantalla.blit(fondo1_1,(-50,-100))
		#conversion de milisegundos a segundos, con aproximacion a piso
		tiempo=(math.floor((pygame.time.get_ticks()-inicio)/1000))

		# condicional de que cada 5 segundos, el tiempo de espera se reduzca, y asi aumentar la velocidad del juego
		if tiempo%5==0 and tiempo!=0 and vel and x >= 0:
			x-=1
			vel=False
		else:
			vel = True

		# ciclos para mostrar el mapa por pantalla
		for i in range(len(lineas)):
			j=0
			for o in lineas[i]:
				if o =='.':
					pantalla.blit(nada,(j*36,i*36))
				if o =='$':
					barra=Barra(j*36,i*36)
					barras.add(barra)
					general.add(barra)
				if o =='#':
					bloque=Bloque(j*36,i*36)
					bloques.add(bloque)
					general.add(bloque)
				if o =='&':
					cu=Cuchilla(j*36,i*36)
					cuchillas.add(cu)
					general.add(cu)	
				if j>21:
					lineas[i]=drop_string(lineas[i])
					break
				j+=1

		general.update()
		general.draw(pantalla)
		pygame.display.flip()
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				sys.exit()
		# se eliminan los objetos anteriores, para no consumir memoria innecesariamente
		for cu in cuchillas:
			cuchillas.remove(cu)
			general.remove(cu)
		for ba in barras:
			barras.remove(ba)
			general.remove(ba)
		for bl in bloques:
			barras.remove(bl)
			general.remove(bl)
		if not(in_game) or x <=0:
			reloj.tick(60)
		else:
			pygame.time.delay(x)
			#reloj.tick(60)