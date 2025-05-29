import pygame
import constantes

class Personaje:
    def __init__ (self, x, y, animaciones):
        self.flip = False # Jugador no se voltea
        self.animaciones = animaciones
        self.frame_index = 0 #imagen de la animacion que se muestra en el momento
        self.update_time = pygame.time.get_ticks() # Guarda el tiempo actual en milisegundos desde que empieza el pygame
        self.image = animaciones[self.frame_index] # Constructor de la imagen
        self.forma = pygame.Rect(0,0,constantes.ANCHO_PERSONAJE,constantes.ALTO_PERSONAJE) # Constructor de la forma del personaje
        self.forma.center = (x,y) # Constructor del punto inicial de la forma del personaje

    def update(self): # metodo para actualizar la animacion
        cooldown_animaciones = 50 # tiempo de la imagen antes de cambiar a otra
        self.image = self.animaciones[self.frame_index] # actualiza la imagen por cada frame_index
        if pygame.time.get_ticks() - self.update_time >= cooldown_animaciones: # Diferencia del tiempo actual frente al update time
            self.frame_index = self.frame_index + 1 # Se actualiza el frame_index cada vez que se llegue al cooldown
            self.update_time = pygame.time.get_ticks() # vueleve a empezar el tiempo actual
        if self.frame_index >= len(self.animaciones): # se actualiza hasta llegar al tope de la lista de animaciones
            self.frame_index = 0 # Se vuelve a iniciar  a la primera imagen del personaje

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
    