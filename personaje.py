import pygame
import constantes

class Personaje:
    def __init__ (self, x, y, image):
        self.flip = False # Jugador no se voltea
        self.image = image # Constructor de la imagen
        self.forma = pygame.Rect(0,0,constantes.ANCHO_PERSONAJE,constantes.ALTO_PERSONAJE) # Constructor de la forma del personaje
        self.forma.center = (x,y) # Constructor del punto inicial de la forma del personaje

    def dibujar (self, interfaz): # metodo para dibujar el jugador en la interfaz de la ventana
        imagen_flip = pygame.transform.flip(self.image, self.flip, False) # gira el personaje en eje x si es true
        interfaz.blit(imagen_flip, self.forma) # con la funcion blit se dibuja la imagen en pantalla
        
        #pygame.draw.rect(interfaz,constantes.AZUL,self.forma,width=1)

    def movimiento (self, delta_x, delta_y): # metodo para movimiento del jugador
        if delta_x < 0:
            self.flip = True # Si el jugador se mueve a la izquierda se voltea
        if delta_x > 0:
            self.flip = False # si el jugador se mueve a la derecha no se voltea

        self.forma.x = self.forma.x + delta_x
        self.forma.y = self.forma.y + delta_y
    