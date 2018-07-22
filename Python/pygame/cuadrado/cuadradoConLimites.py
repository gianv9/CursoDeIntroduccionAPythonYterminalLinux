# importamos la libreria
import pygame

# inicializamos el juego
pygame.init()

# atributos de la ventana
ventana = {"juego": None, "alto": 500, "ancho": 500, "titulo": "Mi primer juego en python!"}

# atributos del rectangulo
R1 = {"x": 50, "y": 100, "ancho": 50, "alto": 60, "velocidad": 5}

ventana["juego"] = pygame.display.set_mode(  (ventana["alto"], ventana["ancho"])  )
pygame.display.set_caption( ventana["titulo"] )

# cada juego debe tener un bucle principal
jugando = True

ejes = [False, False, False, False]

while jugando:
    # hago una pausa de 0.1 segundo
    pygame.time.delay(10)

    ejes[0], ejes[1], ejes[2], ejes[3] = False, False, False, False

    for evento in pygame.event.get(): # esto devuelve una lista de los eventos y su estado
        if evento.type == pygame.QUIT: # si la tecla esc se presiona
            jugando = False # finaliza el bucle
    
    # ver documentacion en --> https://www.pygame.org/docs/ref/key.html
    teclas = pygame.key.get_pressed()

    if teclas[pygame.K_UP]:
        ejes[0], ejes[1], ejes[2], ejes[3] = True, False, False, False
    if teclas[pygame.K_DOWN]:
        ejes[0], ejes[1], ejes[2], ejes[3] = False, True, False, False
    if teclas[pygame.K_LEFT]:
        ejes[0], ejes[1], ejes[2], ejes[3] = False, False, True, False
    if teclas[pygame.K_RIGHT]:
        ejes[0], ejes[1], ejes[2], ejes[3] = False, False, False, True


    # añadimos restricciones al momento de mover
    # verificando si sale de la pantalla en alguno de los ejes...
    if ejes[0] and R1["y"] > R1["velocidad"]:
        R1["y"] -= R1["velocidad"]
    if ejes[1] and R1["y"] < ( ventana["alto"] - R1["alto"] - R1["velocidad"] ) :
        R1["y"] += R1["velocidad"]
    if ejes[2] and R1["x"] > R1["velocidad"]:
        R1["x"] -= R1["velocidad"]
    if ejes[3] and R1["x"] < ( ventana["ancho"] - R1["ancho"] - R1["velocidad"] ):
        R1["x"] += R1["velocidad"]

    
    # para evitar que mi rectangulo deje una marca dibujo el fondo nuevamente
    ventana["juego"].fill((0,0,0))

    # aca el 255,0,0 es un color RGBpygame.event.get()
    # rect es para dibujar un rectangulo
    # hay mas funciones para mas figuras geometricas...
    pygame.draw.rect(ventana["juego"],(255,0,0),(R1["x"],R1["y"],R1["ancho"],R1["alto"]))
    
    # si comento esto no se vuelve a dibujar mi rectangulo
    pygame.display.update()


pygame.quit() # termina el juego
        
