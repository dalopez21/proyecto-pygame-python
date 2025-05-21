from personaje import Personaje
import pygame
import constantes

#Jugador_1
player_image = pygame.image.load("assets//images//characters//player//bitmap.png") # Direccion de la imagen

player_image = pygame.transform.scale(player_image, (player_image.get_width()*constantes.SCALA_PERSONAJE,
                                                     player_image.get_height()*constantes.SCALA_PERSONAJE)) # El tamaño de la imagen del jugador_1

jugador = Personaje(50, 50, player_image) # Posicion inicial del jugador en la ventana grafica

# Movimiento del jugador en falso para que no se mueva
mover_arriba = False 
mover_abajo = False
mover_izquierda = False
mover_derecha = False


