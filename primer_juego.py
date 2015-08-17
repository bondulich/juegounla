# COLOR RGB rojo, verde, azul (0-255)
import pygame, sys

from pygame.locals import *
from random import randint
from math import sin, cos, radians

#CLASES Y FUNCIONES PRINCIPALES
def dibujaTerreno():
	posX = 0
	while posX<=anchoVentana:
		ventana.blit(terreno, (posX, 360))
		posX+=40


class Obstaculo:
	def __init__(self, alto):
		self.alto = alto
		self.visible = True
		self.x=anchoVentana

	def mover(self):
		self.rect = pygame.Rect(self.x,self.alto,30,100)
		pygame.draw.rect(ventana, (255, 120, 5), self.rect)
		#pygame.draw.rect(ventana, (255, 120, 5), (x,self.alto,30,100))

	def ocultar(self):
		self.visible=False

class Personaje:
	def __init__(self):
		self.y = 180
		self.saltando = False
		self.sube=True
		self.vida = True

		self.personajeImg = pygame.image.load("texturas/personaje.png")
		self.personajeImg_saltando = pygame.image.load("texturas/personaje_saltando.png")

		self.rect = self.personajeImg.get_rect()
		self.rect.centerx = 50
		self.rect.centery = self.y

	def dibujar(self):
		if(self.saltando==True):
			ventana.blit(self.personajeImg_saltando, (50, self.y))
		else:
			ventana.blit(self.personajeImg, (50, self.y))

	def saltar(self, opc):
		self.saltando = opc
		self.sube=True

#-----------------------------------------------------
#inicio pygame
pygame.init()

#CONFIGURACIONES
anchoVentana, altoVentana = 800, 400
ColorFondo = (50,121,0)
Color = (120, 120, 120)

terreno = pygame.image.load("texturas/terreno.jpg")
fondoImg = pygame.image.load("texturas/fondo.jpg")
fuente = pygame.font.Font(None,30)
velocidad = 1.8

#Defino ventana y titulo
ventana = pygame.display.set_mode((anchoVentana, altoVentana))
pygame.display.set_caption("Primer juego")


#Inicializo objetos
obstaculo = Obstaculo(randint(300, 350))
personaje = Personaje()

#blcle principal
while True:
	#cambia color fondo
	#ventana.fill(ColorFondo)
	ventana.blit(fondoImg, (0,0))

	#puntaje
	tiempo = pygame.time.get_ticks() / 100		
	miTexto = fuente.render("Puntaje: " + str(tiempo),0,(255,100,100))
	ventana.blit(miTexto, (5,5))
	
	#EVENTOS DEL JUEGO (Teclado, etc)
	for evento in pygame.event.get():
		if evento.type == QUIT: # si cierro la ventana
			pygame.quit()
			sys.exit()
		elif evento.type == pygame.KEYDOWN:
			if evento.key==K_ESCAPE:
				pygame.quit()
				sys.exit()
			elif evento.key==K_SPACE:
				if(personaje.saltando==False):
					personaje.saltar(True)


	#muestra obstaculos
	if(obstaculo.x<=-50):
		obstaculo = Obstaculo(randint(300, 350))
	obstaculo.x -= velocidad
		
	#personaje saltando
	if(personaje.saltando==True):
		if(personaje.sube==True):
			if(personaje.y>50):
				personaje.y -= velocidad + (personaje.y / 200)
			else:
				personaje.sube=False

		elif(personaje.sube == False):
			personaje.y += velocidad + (personaje.y / 200)
			if(personaje.y>=180):
				personaje.y=180
				personaje.saltar(False)
	
	#Impresion de objetos en el juego		
	obstaculo.mover()
	personaje.dibujar()
	#dibujaTerreno()

	pygame.display.update()
