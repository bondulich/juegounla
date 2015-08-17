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

	def mover(self, x):
		pygame.draw.rect(ventana, (255, 120, 5), (x,self.alto,30,100))

	def ocultar(self):
		self.visible=False

class Personaje:
	def __init__(self):
		self.y = 230
		self.saltando = False
		self.sube=True

	def dibujar(self):
		ventana.blit(personajeImg, (50, self.y))

	def saltar(self, opc):
		self.saltando = opc
		self.sube=True

#-----------------------------------------------------
#inicio pygame
pygame.init()

#CONFIGURACIONES
anchoVentana, altoVentana = 600, 400
ColorFondo = (50,121,0)
Color = (120, 120, 120)
personajeImg = pygame.image.load("texturas/personaje.png")
terreno = pygame.image.load("texturas/terreno.jpg")
fuente = pygame.font.Font(None,30)
velocidad = 0.5

#Defino ventana y titulo
ventana = pygame.display.set_mode((anchoVentana, altoVentana))
pygame.display.set_caption("Primer juego")


#Inicializo objetos
obstaculo = Obstaculo(randint(300, 350))
personaje = Personaje()

posXobj = anchoVentana
#blcle principal
while True:
	#cambia color fondo
	ventana.fill(ColorFondo)

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
	if(posXobj<0):
		obstaculo.ocultar()
		posXobj=anchoVentana

	if(obstaculo.visible==False):
		obstaculo = Obstaculo(randint(300, 350))

	posXobj -= velocidad
		
	#personaje saltando
	if(personaje.saltando==True):
		if(personaje.sube==True):
			if(personaje.y>100):
				personaje.y -= velocidad + (personaje.y / 500)
			else:
				personaje.sube=False

		elif(personaje.sube == False):
			personaje.y += velocidad + (personaje.y / 500)
			if(personaje.y>=230):
				personaje.y=230
				personaje.saltar(False)
	
	#Impresion de objetos en el juego		
	obstaculo.mover(posXobj)
	personaje.dibujar()
	dibujaTerreno()

	pygame.display.update()

