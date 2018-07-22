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
    
    teclas = pygame.key.get_pressed()

    if teclas[pygame.K_UP]:
        ejes[0], ejes[1], ejes[2], ejes[3] = True, False, False, False
    if teclas[pygame.K_DOWN]:
        ejes[0], ejes[1], ejes[2], ejes[3] = False, True, False, False
    if teclas[pygame.K_LEFT]:
        ejes[0], ejes[1], ejes[2], ejes[3] = False, False, True, False
    if teclas[pygame.K_RIGHT]:
        ejes[0], ejes[1], ejes[2], ejes[3] = False, False, False, True
    
    if ejes[0]:
        R1["y"] -= R1["velocidad"]
    if ejes[1]:
        R1["y"] += R1["velocidad"]
    if ejes[2]:
        R1["x"] -= R1["velocidad"]
    if ejes[3]:
        R1["x"] += R1["velocidad"]

    # for evento in pygame.event.get(): # esto devuelve una lista de los eventos y su estado
    #     if evento.type == pygame.QUIT: # si la tecla esc se presiona
    #         jugando = False # finaliza el bucle

    #     # detecta cuando una tecla sea presionada
    #     if evento.type in [pygame.KEYDOWN, pygame.KEYUP]:
    #         # key_name = pygame.key.name(evento.key)
    #         # print("Presiono " + str(key_name))
    #         if(evento.key == pygame.K_UP):
    #             ejes[0], ejes[1], ejes[2], ejes[3] = True, False, False, False
    #         if(evento.key == pygame.K_DOWN):
    #             ejes[0], ejes[1], ejes[2], ejes[3] = False, True, False, False
    #         if(evento.key == pygame.K_LEFT):
    #             ejes[0], ejes[1], ejes[2], ejes[3] = False, False, True, False
    #         if(evento.key == pygame.K_RIGHT):
    #             ejes[0], ejes[1], ejes[2], ejes[3] = False, False, False, True

    # if ejes[0]:
    #     R1["y"] -= R1["velocidad"]
    # if ejes[1]:
    #     R1["y"] += R1["velocidad"]
    # if ejes[2]:
    #     R1["x"] -= R1["velocidad"]
    # if ejes[3]:
    #     R1["x"] += R1["velocidad"]


    # print(R1["x"], R1["y"])

    
    # para evitar que mi rectangulo deje una marca dibujo el fondo nuevamente
    ventana["juego"].fill((0,0,0))

    # aca el 255,0,0 es un color RGBpygame.event.get()
    # rect es para dibujar un rectangulo
    # hay mas funciones para mas figuras geometricas...
    pygame.draw.rect(ventana["juego"],(255,0,0),(R1["x"],R1["y"],R1["ancho"],R1["alto"]))
    
    # si comento esto no se vuelve a dibujar mi rectangulo
    pygame.display.update()


pygame.quit() # termina el juego
        
