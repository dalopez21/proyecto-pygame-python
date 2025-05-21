import pygame
import constantes

class Personaje:
    def __init__ (self, x, y, image):
        self.image = image # Constructor de la imagen
        self.forma = pygame.Rect(0,0,constantes.ANCHO_PERSONAJE,constantes.ALTO_PERSONAJE) # Constructor de la forma del personaje
        self.forma.center = (x,y) # Constructor del punto inicial de la forma del personaje

    def dibujar (self, interfaz): # metodo para dibujar el jugador en la interfaz de la ventana
        interfaz.blit(self.image, self.forma)
        
        #pygame.draw.rect(interfaz,constantes.AZUL,self.forma,width=1)

    def movimiento (self, delta_x, delta_y): # metodo para movimiento del jugador
        self.forma.x = self.forma.x + delta_x
        self.forma.y = self.forma.y + delta_y
    