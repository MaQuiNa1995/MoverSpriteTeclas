#!/bin/python
import pygame,sys
from pygame.locals import *

# Salir De Luego
def Salir(): 
	pygame.quit()
	sys.exit()



pygame.init()

# Teclas
pygame.key.set_repeat(1,25)

#Ventana Atributos
Ventana = pygame.display.set_mode([500, 500])
pygame.display.set_caption('Titulo ventana')

#Sprite Jugador
Jugador_Parado = pygame.image.load('Mat/Sprite_Zorro/Zorro_Parado_Ab.png')
Jugador_Andando = pygame.image.load('Mat/Sprite_Zorro/Zorro_Andando_Ab.png')

Posicion_JugadoX = 250
Posicion_JugadoY = 250

Posicion_Antigua_JugadorY = Posicion_JugadoY

Mov = False

Velocidad = 10
Rosa=(165,25,145)
derecha = True


# Reloj
Fps = 20
Reloj = pygame.time.Clock()

while True:
	
	#Limpiar Pantalla
	Ventana.fill(Rosa)

	if Mov == False:
		Ventana.blit(Jugador_Parado,(Posicion_JugadoX, Posicion_JugadoY))

	if Mov == True:
		Ventana.blit(Jugador_Andando,(Posicion_JugadoX, Posicion_JugadoY))
        
	for event in pygame.event.get():
            if event.type == QUIT:
                Salir()
			
     	    elif event.type==KEYDOWN:
           	if event.key==K_LEFT:
           	  	Posicion_JugadoX=Posicion_JugadoX-Velocidad
          	elif event.key==K_RIGHT:
         		Posicion_JugadoX=Posicion_JugadoX+Velocidad
		elif event.key==K_UP:
			Posicion_JugadoY=Posicion_JugadoY-Velocidad
		elif event.key==K_DOWN:
			Posicion_JugadoY=Posicion_JugadoY+Velocidad
			if Mov == True:
				Mov = False
			else:
				Mov = True

                elif event.key==K_ESCAPE:
                        Salir()
							
	pygame.display.update ()
	Reloj.tick(Fps)
