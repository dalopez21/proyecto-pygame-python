import pygame
import constantes

class Personaje:
    def __init__ (self, x, y):
        self.forma = pygame.Rect(0,0,constantes.ANCHO_PERSONAJE,constantes.ALTO_PERSONAJE)
        self.forma.center = (x,y)

    def dibujar (self, interfaz): # metodo para dibujar el jugador en la interfaz de la ventana
        pygame.draw.rect(interfaz,constantes.AZUL,self.forma)

    def movimiento (self, delta_x, delta_y): # metodo para movimiento del jugador
        self.forma.x = self.forma.x + delta_x
        self.forma.y = self.forma.y + delta_y
    