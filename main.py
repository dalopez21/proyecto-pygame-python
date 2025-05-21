import pygame
import sys
import constantes
import variables
from personaje import Personaje



if __name__ == '__main__': # Condicion para empezar el programa en python
    pygame.init() # Inicio del juego

    
    variables.player_image # variable de la imagen personaje
    variables.jugador # Jugador

    ventana = pygame.display.set_mode((constantes.ANCHO_VENTANA, constantes.ALTO_VENTANA)) # Creacion de ventana grafica
    pygame.display.set_caption("Guerra de numeros") # Titulo del juego

    #movimiento jugador
    variables.mover_arriba 
    variables.mover_abajo
    variables.mover_izquierda
    variables.mover_derecha

    reloj = pygame.time.Clock() # Controla el frame rate o tasa de fotogramas
 
    while True: # Condicion repetitiva para mostrar pantalla

        reloj.tick(constantes.FPS) # Corre a la velocidad del fotograma por segundo
        ventana.fill(constantes.NEGRO) # Rellena el espacio de la interfaz con un color de fondo
        
        # Calcular el movimiento del jugador que empieza en cero
        desplazamiento_x = 0
        desplazamiento_y = 0

        if variables.mover_derecha:
            desplazamiento_x = constantes.VELOCIDAD # velocidad del eje x a la derecha
        if variables.mover_izquierda:
            desplazamiento_x = -constantes.VELOCIDAD #velocidad del eje x a la izquierda
        if variables.mover_arriba:
            desplazamiento_y = -constantes.VELOCIDAD # velocidad del eje y hacia arriba
        if variables.mover_abajo:
            desplazamiento_y = constantes.VELOCIDAD # velocidad del eje y hacia abajo

        variables.jugador.movimiento(desplazamiento_x, desplazamiento_y) # Movimiento del jugador en la pantalla

        for evento in pygame.event.get(): # Recorre los eventos del juego
            if evento.type == pygame.QUIT: # Si el tipo de evento es Quit (cerrar en la x o alt f4)
                pygame.quit() # Sale del juego
                sys.exit() # Sale de la ventana principal

            elif evento.type == pygame.KEYDOWN: # Tipo de evento que al presionar una tecla ejecuta algo
                if evento.key == pygame.K_a:
                    variables.mover_izquierda = True
                elif evento.key == pygame.K_d:
                    variables.mover_derecha = True
                elif evento.key == pygame.K_w:
                    variables.mover_arriba = True
                elif evento.key == pygame.K_s:
                    variables.mover_abajo = True

            elif evento.type == pygame.KEYUP: # Tipo de evento que al soltar la tecla no sigue ejecutandose
                if evento.key == pygame.K_a:
                    variables.mover_izquierda = False
                elif evento.key == pygame.K_d:
                    variables.mover_derecha = False
                elif evento.key == pygame.K_w:
                    variables.mover_arriba = False
                elif evento.key == pygame.K_s:
                    variables.mover_abajo = False
        
        
        
        variables.jugador.dibujar(ventana)
        pygame.display.update() # Actualiza la pantalla

        