from personaje import Personaje
import pygame
import constantes

def escalar_img(image,scale):
    w = image.get_width() #Ancho de la imagen
    h = image.get_height() #Alto de la imagen
    nueva_imagen = pygame.transform.scale(image,(w*scale,h*scale)) # transformacion de la imagen por la escala
    return nueva_imagen

animaciones = []
for i in range(12):
    img = pygame.image.load(f"assets//images//characters//player//bitmap{i}.png") #Direccion de la imagen Personaje
    img = escalar_img(img,constantes.SCALA_PERSONAJE) # Tamaño de la imagen del personaje
    animaciones.append(img) # Guardar las imagenes en animaciones


jugador = Personaje(50, 50, animaciones) # Posicion inicial del jugador en la ventana grafica

# Movimiento del jugador en falso para que no se mueva
mover_arriba = False 
mover_abajo = False
mover_izquierda = False
mover_derecha = False


