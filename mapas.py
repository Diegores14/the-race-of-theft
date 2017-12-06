import configparser
import pygame
import sys
import time
import math
import random
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
		self.image = pygame.image.load('Imagenes/Cuchilla1.png').convert_alpha()
		self.i=0
		self.rect=self.image.get_rect()
		self.rect.x = x
		self.rect.y = y

	def update(self):
		self.image = pygame.image.load('Imagenes/'+self.giro[self.i]).convert_alpha()
		self.i+=1
		if self.i>5:
			self.i=0

class Barra(pygame.sprite.Sprite):
	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load('Imagenes/Barra.png').convert_alpha()
		self.rect=self.image.get_rect()
		self.rect.x = x
		self.rect.y = y

class Final(pygame.sprite.Sprite):
	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load('Imagenes/Rayo.png').convert_alpha()
		self.rect=self.image.get_rect()
		self.rect.x = x
		self.rect.y = y

class Dafebe(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.dir = 0
		self.x =0
		self.IsDer = True
		self.var_x = 0
		self.var_y = 7
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
		aux = []
		self.m.append([pygame.image.load('Imagenes/Dafebe17.png').convert_alpha()])
		for j in correr:
			aux.append(pygame.transform.flip(pygame.image.load('Imagenes/'+j).convert_alpha(),False,True))
		self.m.append(aux)
		self.m.append([pygame.transform.flip(pygame.image.load('Imagenes/Dafebe17.png').convert_alpha(),False, True)])
		self.image = self.m[self.dir][self.x]
		self.rect=self.image.get_rect()
		self.rect.y = 278
		self.rect.x = 170

	def update(self):
		self.rect.x+=self.var_x
		self.rect.y+=self.var_y
		self.aux += 1
		#if self.aux == 2:
		#	self.aux = 0
		#if (self.var_x != 0 or self.var_y != 0) and self.aux == 0:
		self.x += 1
		if self.rect.x>ANCHO/2-self.rect[2]:
			self.rect.x = ANCHO/2-self.rect[2]
			self.var_x = 0
		if self.rect.x<0:
			self.rect.x=-self.rect[2]-10
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
			self.var_x = 7
		if self.dir == 3:
			self.x = 0
		if self.dir ==4 and self.x > 5:
			self.x = 0
		if self.dir == 5:
			self.x = 0
		self.image=self.m[self.dir][self.x]
		self.rect[2] = self.image.get_width()
		self.rect[3] = self.image.get_height()

class Diare(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.dir = 0
		self.x =0
		self.var_x = 0
		self.var_y = 7
		self.IsDer = True
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
		aux = []
		self.m.append([pygame.transform.flip(pygame.image.load('Imagenes/Diare21.png').convert_alpha(),False, True)])
		for j in correr:
			aux.append(pygame.image.load('Imagenes/'+j).convert_alpha())
		self.m.append(aux)
		self.m.append([pygame.image.load('Imagenes/Diare21.png').convert_alpha()])
		self.image = self.m[self.dir][self.x]
		self.rect=self.image.get_rect()
		self.rect.y = 420
		self.rect.x = 170

	def update(self):
		self.rect.x+=self.var_x
		self.rect.y+=self.var_y
		self.aux += 1
		#if self.aux == 2:
		#	self.aux = 0
		#if (self.var_x != 0 or self.var_y != 0) and self.aux == 0:
		self.x += 1
		if self.rect.x>ANCHO/2-self.rect[2]:
			self.rect.x = ANCHO/2-self.rect[2]
			self.var_x = 0
		if self.rect.x<0:
			self.rect.x=-self.rect[2]-10
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
			self.var_x = 7
		if self.dir == 3:
			self.x = 0
		if self.dir ==4 and self.x > 5:
			self.x = 0
		if self.dir == 5:
			self.x = 0
		self.image=self.m[self.dir][self.x]
		self.rect[2] = self.image.get_width()
		self.rect[3] = self.image.get_height()

class Sesagon(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.dir = 0
		self.x =0
		self.var_x = 0
		self.var_y = 7
		self.IsDer = True
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
		aux = []
		self.m.append([pygame.image.load('Imagenes/Sesagon22.png').convert_alpha()])
		for j in correr:
			aux.append(pygame.transform.flip(pygame.image.load('Imagenes/'+j).convert_alpha(),False,True))
		self.m.append(aux)
		self.m.append([pygame.transform.flip(pygame.image.load('Imagenes/Sesagon22.png').convert_alpha(),False, True)])
		self.image = self.m[self.dir][self.x]
		self.rect=self.image.get_rect()
		self.rect.y = 133
		self.rect.x = 170

	def update(self):
		self.rect.x+=self.var_x
		self.rect.y+=self.var_y
		self.aux += 1
		#if self.aux == 2:
		#	self.aux = 0
		#if (self.var_x != 0 or self.var_y != 0) and self.aux == 0:
		self.x += 1
		if self.rect.x>ANCHO/2-self.rect[2]:
			self.rect.x = ANCHO/2-self.rect[2]
			self.var_x = 0
		if self.rect.x<0:
			self.rect.x=-self.rect[2]-10
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
			self.var_x = 7
		if self.dir == 3:
			self.x = 0
		if self.dir ==4 and self.x > 5:
			self.x = 0
		if self.dir == 5:
			self.x = 0
		self.image=self.m[self.dir][self.x]
		self.rect[2] = self.image.get_width()
		self.rect[3] = self.image.get_height()

class Caboom(pygame.sprite.Sprite):
	def __init__(self,x,y, grupo):
		pygame.sprite.Sprite.__init__(self)
		self.dir = 0
		self.x =-1
		self.m = []
		self.general = grupo
		for i in range(4):
			self.m.append(pygame.image.load('Explosion.png').subsurface(i*64,128,64,64))
		self.image = self.m[0]
		self.rect = self.image.get_rect()
		self.rect.y = y
		self.rect.x = x

	def update(self):
		self.x += 1
		self.rect.x -= 3
		if self.x > 3:
			self.x = 3
			self.general.remove(self)
		self.image = self.m[self.x]


def drop_string(cad):
	i=0
	ncad=''
	for c in cad:
		if i == 0:
			i+=1
		else:
			ncad= ncad + c
	return ncad


def inicio(nivel):
	#inicio de pygame con fondo negro
	pygame.init()
	pygame.display.set_caption('Mapas')
	pantalla=pygame.display.set_mode([ANCHO,ALTO])
	pantalla.fill(NEGRO)
	#lectura del mapa
	interprete=configparser.ConfigParser()
	if nivel == 1:
		interprete.read('mapa.map')
	elif nivel == 2:
		interprete.read('mapa1.map')
	else:
		interprete.read('mapa2.map')

	# Musica y asignacion de nivel
	pygame.mixer.music.load('Musica/Vegasis_-_Nightwatcher.ogg')
	pygame.mixer.music.load('Musica/Hannes_Hofkind_-_Emphasize.ogg')
	pygame.mixer.music.load('Musica/ONSTEAD_-_Nightfall.ogg')
	pygame.mixer.music.load('Musica/Zero-project_-_Distorted_reality.ogg')
	pygame.mixer.music.play(-1,0.0)

	#carga y transfomacion de las imagenes necesarias
	if nivel==1:
		fondo1=pygame.image.load('Fondo1.jpg')
	elif nivel==2:
		fondo1=pygame.image.load('Fondo4.jpg')
	else:
		fondo1=pygame.image.load('Fondo5.jpg')

	fondo1_1=pygame.transform.scale(fondo1,(900,710))
	nada=pygame.image.load('inv.png')

	#dividiendo el mapa en lineas
	dicc={}
	for seccion in interprete.sections():
		descripcion=dict(interprete.items(seccion))
		dicc[seccion]=descripcion

	#definiendo variables y grupos de sprites necesarios
	reloj=pygame.time.Clock()
	jp1=Dafebe()
	jp2 = Diare()
	jp3 = Sesagon()
	jp1.image=pygame.image.load('Imagenes/Dafebe1.png')
	jp2.image=pygame.transform.flip(pygame.image.load('Imagenes/Diare4.png').convert_alpha(),False,True)
	jp3.image=pygame.image.load('Imagenes/Sesagon4.png')
	general = pygame.sprite.Group()
	players=pygame.sprite.Group()
	cuchillas = pygame.sprite.Group()
	barras= pygame.sprite.Group()
	bloques= pygame.sprite.Group()
	finales= pygame.sprite.Group()
	general.add(bloques)
	general.add(cuchillas)
	general.add(barras)
	general.add(players)
	general.add(finales)
	general.add(jp1)
	general.add(jp2)
	general.add(jp3)
	players.add(jp1)
	players.add(jp2)
	players.add(jp3)
	inicio=pygame.time.get_ticks() # variable de tiempo
	if nivel == 1:
		mapa=dicc['nivel1-tutorial']['mapa'] # mapa
	elif nivel == 2:
		mapa=dicc['nivel2']['mapa'] # mapa
	else:
		mapa=dicc['nivel3']['mapa'] # mapa)
	lineas=mapa.split()
	fin=False
	x=50 #variable que controla la velocidad
	in_game=True # variable que controla el refresco de pantalla, si esta en juego usa time.delay(x) y si no usa, reloj.tick(60)
	vel=True # variable para que el tiempo no se reduzca en varias iteraciones donde el tiempo es el mismo, ya que es un aproximado
	jugar = False
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
				if o =='&':
					cu=Cuchilla(j*36,i*36)
					cuchillas.add(cu)
					general.add(cu)	
				if o =='f':
					fin=Final(j*13,i*36)
					finales.add(fin)
					general.add(fin)
				if j>21:
					lineas[i]=drop_string(lineas[i])
					break
				j+=1
		'''if len(lineas[len(lineas)-1])==0:
			for '''

		if nivel ==1:
			pass
		general.draw(pantalla)
		pygame.display.flip()
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				sys.exit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_z:
					jp1.dir = 1
					jp1.var_y *= -1
					jp1.IsDer = not jp1.IsDer  
					jp1.var_x = 0
				if event.key == pygame.K_b:
					jp2.dir = 1
					jp2.var_y *= -1
					jp2.IsDer = not jp2.IsDer  
					jp2.var_x = 0
				if event.key == pygame.K_RIGHT:
					jp3.dir = 1
					jp3.var_y *= -1
					jp3.IsDer = not jp3.IsDer  
					jp3.var_x = 0

			while not jugar:
				for event in pygame.event.get():
					if event.type==pygame.QUIT:
						sys.exit()
					if event.type == pygame.KEYDOWN:
						if event.key == pygame.K_p:
							jugar = True

		collide_jp_br=pygame.sprite.spritecollide(jp1,barras,False)
		collide_jp_br1 = pygame.sprite.spritecollide(jp1,cuchillas,False)
		if collide_jp_br1:
			players.remove(jp1)
			general.remove(jp1)
			explosion = Caboom(jp1.rect.x, jp1.rect.y, general)
			general.add(explosion)
			jp1.rect.x = -50
			jp1.rect.y = -50
		if collide_jp_br == [] and jp1.dir==0 and jp1.x!=0 and jp1.x!=2:
			jp1.dir = 1
		if collide_jp_br == [] and jp1.dir==4 :
			#print(jp1.x)
			jp1.dir = 1
		
		'''if collide_jp_br != [] and jp1.dir==1 and ((y1+jp1.rect[3])-y2) <= 12  and ((y1+jp1.rect[3])-y2):
			jp1.dir = 0
			jp1.rect.y -= 20
		if collide_jp_br != [] and jp1.dir==1 and (y2+36)-y1 <= 7  and (y2+36)-y1 >= 0:
			jp1.dir = 4
			jp1.rect.y += 20'''
		for i in collide_jp_br:
			y1 = jp1.rect.y
			x1 = jp1.rect.x
			y2 = i.rect.y
			x2 = i.rect.x
			##print(jp1.dir,jp1.IsDer,((y1+jp1.rect[3])-y2),((y1+jp1.rect[3])-y2))
			if jp1.dir==1 and jp1.IsDer and ((y1+jp1.rect[3])-y2) <= 12  and ((y1+jp1.rect[3])-y2)>=0:
				jp1.dir = 0
				jp1.rect.y -= 20
				y1 -= 20
				#print('holi1')
			if jp1.dir == 1 and not jp1.IsDer and (y2+36)-y1 <= 7  and (y2+36)-y1 >= 0:
				jp1.dir = 4
				jp1.rect.y = y2+36
				#print('holi2')
			if (y2+36)-y1 <= 7  and (y2+36)-y1 >= 0:
				jp1.rect.y += 7
				#print('holi3')
			else: 
				if ((y1+jp1.rect[3])-y2) <= 12  and ((y1+jp1.rect[3])-y2) >= 0:
					jp1.rect.y = i.rect.y - jp1.rect[3] - 5
					#print('holi4')
				else:
					if (y2+36)-y1 <= 0 or (y1+(jp1.rect[3])-y2) <= 0:
						#print('holi5')
						break
					else:
						jp1.rect.x = i.rect.x - jp1.rect[2] - 50
						#print('holi6')

		for i in collide_jp_br1:
			print("Perdiste")
#################################################################################################################################
###################################            JUGADOR 2        #################################################################
#################################################################################################################################
		collide_jp_br=pygame.sprite.spritecollide(jp2,barras,False)
		collide_jp_br1 = pygame.sprite.spritecollide(jp2,cuchillas,False)
		if collide_jp_br1:
			players.remove(jp2)
			general.remove(jp2)
			explosion = Caboom(jp2.rect.x, jp2.rect.y, general)
			general.add(explosion)
			jp2.rect.x = -50
			jp2.rect.y = -50
		if collide_jp_br == [] and jp2.dir==0 and jp2.x!=0 and jp2.x!=2:
			jp2.dir = 1
		if collide_jp_br == [] and jp2.dir==4 :
			#print(jp2.x)
			jp2.dir = 1
		
		'''if collide_jp_br != [] and jp2.dir==1 and ((y1+jp2.rect[3])-y2) <= 12  and ((y1+jp2.rect[3])-y2):
			jp2.dir = 0
			jp2.rect.y -= 20
		if collide_jp_br != [] and jp2.dir==1 and (y2+36)-y1 <= 7  and (y2+36)-y1 >= 0:
			jp2.dir = 4
			jp2.rect.y += 20'''
		for i in collide_jp_br:
			y1 = jp2.rect.y
			x1 = jp2.rect.x
			y2 = i.rect.y
			x2 = i.rect.x
			##print(jp2.dir,jp2.IsDer,((y1+jp2.rect[3])-y2),((y1+jp2.rect[3])-y2))
			if jp2.dir==1 and jp2.IsDer and ((y1+jp2.rect[3])-y2) <= 12  and ((y1+jp2.rect[3])-y2)>=0:
				jp2.dir = 0
				jp2.rect.y -= 20
				y1 -= 20
				#print('holi1')
			if jp2.dir == 1 and not jp2.IsDer and (y2+36)-y1 <= 7  and (y2+36)-y1 >= 0:
				jp2.dir = 4
				jp2.rect.y = y2+36
				#print('holi2')
			if (y2+36)-y1 <= 7  and (y2+36)-y1 >= 0:
				jp2.rect.y += 7
				#print('holi3')
			else: 
				if ((y1+jp2.rect[3])-y2) <= 12  and ((y1+jp2.rect[3])-y2) >= 0:
					jp2.rect.y = i.rect.y - jp2.rect[3] - 5
					#print('holi4')
				else:
					if (y2+36)-y1 <= 0 or (y1+(jp2.rect[3])-y2) <= 0:
						#print('holi5')
						break
					else:
						jp2.rect.x = i.rect.x - jp2.rect[2] - 50
						#print('holi6')

		for i in collide_jp_br1:
			print("Perdiste")

#################################################################################################################################
###################################            JUGADOR 3        #################################################################
#################################################################################################################################
		collide_jp_br=pygame.sprite.spritecollide(jp3,barras,False)
		collide_jp_br1 = pygame.sprite.spritecollide(jp3,cuchillas,False)
		if collide_jp_br1:
			players.remove(jp3)
			general.remove(jp3)
			explosion = Caboom(jp3.rect.x, jp3.rect.y, general)
			general.add(explosion)
			jp3.rect.x = -50
			jp3.rect.y = -50
		if collide_jp_br == [] and jp3.dir==0 and jp3.x!=0 and jp3.x!=2:
			jp3.dir = 1
		if collide_jp_br == [] and jp3.dir==4 :
			#print(jp3.x)
			jp3.dir = 1
		
		'''if collide_jp_br != [] and jp3.dir==1 and ((y1+jp3.rect[3])-y2) <= 12  and ((y1+jp3.rect[3])-y2):
			jp3.dir = 0
			jp3.rect.y -= 20
		if collide_jp_br != [] and jp3.dir==1 and (y2+36)-y1 <= 7  and (y2+36)-y1 >= 0:
			jp3.dir = 4
			jp3.rect.y += 20'''
		for i in collide_jp_br:
			y1 = jp3.rect.y
			x1 = jp3.rect.x
			y2 = i.rect.y
			x2 = i.rect.x
			##print(jp3.dir,jp3.IsDer,((y1+jp3.rect[3])-y2),((y1+jp3.rect[3])-y2))
			if jp3.dir==1 and jp3.IsDer and ((y1+jp3.rect[3])-y2) <= 12  and ((y1+jp3.rect[3])-y2)>=0:
				jp3.dir = 0
				jp3.rect.y -= 20
				y1 -= 20
				#print('holi1')
			if jp3.dir == 1 and not jp3.IsDer and (y2+36)-y1 <= 7  and (y2+36)-y1 >= 0:
				jp3.dir = 4
				jp3.rect.y = y2+36
				#print('holi2')
			if (y2+36)-y1 <= 7  and (y2+36)-y1 >= 0:
				jp3.rect.y += 7
				#print('holi3')
			else: 
				if ((y1+jp3.rect[3])-y2) <= 12  and ((y1+jp3.rect[3])-y2) >= 0:
					jp3.rect.y = i.rect.y - jp3.rect[3] - 5
					#print('holi4')
				else:
					if (y2+36)-y1 <= 0 or (y1+(jp3.rect[3])-y2) <= 0:
						#print('holi5')
						break
					else:
						jp3.rect.x = i.rect.x - jp3.rect[2] - 50
						#print('holi6')
			

		general.update()

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
		for p in players:
			if p.rect.x<-40 or p.rect.y<-40 or p.rect.x > ANCHO or p.rect.y>ALTO:
				players.remove(p) 
		if len(players)==0:
			g_o=pygame.image.load("gameover.png")
			pantalla.blit(g_o, (0,0))
			pygame.display.flip()
			pygame.time.delay(5000)
			return
		if not(in_game) or x <=0:
			reloj.tick(60)
		else:
			pygame.time.delay(x)
			#reloj.tick(60)
if __name__== '__main__':
	opciones = [
        ("Nivel 1", juegonuevo),
        ("Nivel 2", multijugador),
        ("Nivel 3", tutorial),
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
			'''if event.type == pygame.KEYDOWN:
				if event.key == K_RETURN:
					print(menu.cursor.rect.y)
					if menu.cursor.rect.y == 269:
						inicio(2)
					if menu.cursor.rect.y == 219:
						inicio(1)'''

		pantalla.blit(fondo, (0,0))
		menu.actualizar()
		menu.imprimir(pantalla)
		pygame.display.flip()
		pygame.time.delay(10)