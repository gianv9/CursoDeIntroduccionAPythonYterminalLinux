import pygame
import os # libreria para intectuar con el sistema operativo

pygame.init()

# sets the window title
pygame.display.set_caption(u'Load image')

# sets the window size
screen = pygame.display.set_mode((538, 500))

# obten la ruta de la imagen
ruta_imagen = os.path.join(u'imagenes', u'Mario_8_bit.png')

# obten la imagen
imagen = pygame.image.load(ruta_imagen)
# convierte la imagen  al mismo formato que el de la pantalla
# para dibujar mas rapido
image = imagen.convert_alpha()
# dibuja la imagen en la posicion 20,20
screen.blit(image, (20, 20))

# updates the screen
pygame.display.flip()

# infinite loop
while True:
    # gets a single event from the event queue
    event = pygame.event.wait()

    # if the 'close' button of the window is pressed
    if event.type == pygame.QUIT:
        break

# finalizes Pygame
pygame.quit()