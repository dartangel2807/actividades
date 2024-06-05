import pygame
import random

pygame.init()
pygame.mixer.music.load('merrygo.ogg')
pygame.mixer.music.play(loops=-1)

ANCHO, ALTO = 1024, 768
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("¡Encuentra la palabra!")

COLOR_FONDO = (30, 144, 255)
COLOR_TEXTO = (255, 255, 255)
COLOR_BOTON = (70, 130, 180)
COLOR_BOTON2 = (100, 149, 237)
COLOR_CORRECTO = (50, 205, 50)
COLOR_ERROR = (255, 0, 0)

fuente = pygame.font.Font(None, 36)
fuente2 = pygame.font.Font(None, 72)
def mostrarTexto(text, font, color, surface, x, y, align="topleft"):
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect(**{align: (x, y)})
    surface.blit(textobj, textrect)
def mostrarBoton(text, font, color, hover_color, surface, x, y, width, height, mouse_pos, mouse_click):
    if x <= mouse_pos[0] <= x + width and y <= mouse_pos[1] <= y + height:
        pygame.draw.rect(surface, hover_color, (x, y, width, height))
        if mouse_click[0] == 1:
            return True
    else:
        pygame.draw.rect(surface, color, (x, y, width, height))

    mostrarTexto(text, font, COLOR_TEXTO, surface, x + 10, y + 10)
    return False
def menuInicio():
    while True:
        ventana.fill(COLOR_FONDO)
        mostrarTexto("¡Encuentra la palabra!", fuente2, COLOR_TEXTO, ventana, 150, 80)
        mostrarTexto("Desarrollado por el grupo 432", fuente2, COLOR_TEXTO, ventana, 150, 400)
        mostrarTexto("Ricardo Valenzuela y Kevin Solorzano", fuente2, COLOR_TEXTO, ventana, 50, 500)

        mouse_pos = pygame.mouse.get_pos()
        mouse_click = pygame.mouse.get_pressed()

        if mostrarBoton("Iniciar Juego", fuente, COLOR_BOTON, COLOR_BOTON2, ventana, 150, 150, 500, 50, mouse_pos, mouse_click):
            juegoLoop()
        if mostrarBoton("Instrucciones", fuente, COLOR_BOTON, COLOR_BOTON2, ventana, 150, 210, 500, 50, mouse_pos, mouse_click):
            instrucciones()
        if mostrarBoton("Salir", fuente, COLOR_BOTON, COLOR_BOTON2, ventana, 150, 270, 500, 50, mouse_pos, mouse_click):
            pygame.quit()
            return

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

def instrucciones():
    run = True
    while run:
        ventana.fill(COLOR_FONDO)
        mostrarTexto("Instrucciones", fuente2, COLOR_TEXTO, ventana, 150, 100)
        mostrarTexto("Encuentra la palabra correcta a partir de las letras mixteadas.", fuente, COLOR_TEXTO, ventana, 20, 200)
        mostrarTexto("Recibirás una descripción y una pista adicional si es necesario.", fuente, COLOR_TEXTO, ventana, 20, 250)

        mouse_pos = pygame.mouse.get_pos()
        mouse_click = pygame.mouse.get_pressed()

        if mostrarBoton("Regresar", fuente, COLOR_BOTON, COLOR_BOTON2, ventana, 20, 360, 200, 50, mouse_pos, mouse_click):
            run = False

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

    menuInicio()

palabras = [
    {"palabra": "banana", "descripcion": "Una fruta amarilla", "pista": "Le gusta mucho a los monos"},
    {"palabra": "elefante", "descripcion": "Un animal grande con trompa", "pista": "Es un animal muy grande, vive en Africa"},
    {"palabra": "bicicleta", "descripcion": "Un medio de transporte con dos ruedas", "pista": "Se usa para pedalear"},
    {"palabra": "computadora", "descripcion": "Máquina electrónica", "pista": "Tiene teclado y pantalla"},
    {"palabra": "avion", "descripcion": "Medio de transporte que vuela", "pista": "Se usa para viajar largas distancias a través del cielo"},
    {"palabra": "reloj", "descripcion": "Lo usamos para ver la hora", "pista": "Se lleva en la muñeca"},
    {"palabra": "guitarra", "descripcion": "Instrumento musical de cuerdas", "pista": "Se toca con las manos o con una pua"},
    {"palabra": "montaña", "descripcion": "Tiene forma de pico y está elevada por desde el suelo", "pista": "Más alta que una colina"},
    {"palabra": "sol", "descripcion": "Cosa brillante en el cielo, nos da luz", "pista": "¡No lo veas! Podría lastimarte"},
    {"palabra": "oceano", "descripcion": "Gran masa de agua salada que cubre la mayor parte de la Tierra", "pista": "Más grande que un mar"},
    {"palabra": "helado", "descripcion": "Postre frío y dulce", "pista": "Se derrite rápidamente"},
    {"palabra": "ventana", "descripcion": "Nos permite ver hacia afuera estando dentro de una casa", "pista": "Se puede abrir y cerrar"},
    {"palabra": "jirafa", "descripcion": "Animal con el cuello muy largo", "pista": "El animal más alto de la sabana"},
    {"palabra": "libro", "descripcion": "Conjunto de hojas escritas o impresas", "pista": "Se usa para leer"},
    {"palabra": "cohete", "descripcion": "Es el vehiculo donde los astronautas viajan", "pista": "Es lanzado desde una plataforma"},
    {"palabra": "tren", "descripcion": "Medio de transporte sobre rieles", "pista": "Se mueve en vías"},
    {"palabra": "casa", "descripcion": "Lugar donde vive la gente", "pista": "Tiene habitaciones y techo"},
    {"palabra": "perro", "descripcion": "Animal conocido como el mejor amigo del hombre", "pista": "Ladra"},
    {"palabra": "gato", "descripcion": "Animal que maúlla", "pista": "Le gusta cazar ratones"},
    {"palabra": "auto", "descripcion": "Vehículo de cuatro ruedas", "pista": "Se usa para viajar por carretera"},
    {"palabra": "luna", "descripcion": "Sale de noche, a veces llena y otras media", "pista": "Brilla en la noche"},
    {"palabra": "estrella", "descripcion": "Tiene 5 puntas, y está en el espacio", "pista": "El Sol es una de ellas"},
    {"palabra": "árbol", "descripcion": "Planta grande con tronco y ramas", "pista": "Da sombra y oxígeno"},
    {"palabra": "flor", "descripcion": "Parte colorida de una planta", "pista": "Puede tener pétalos y perfume"},
    {"palabra": "zapato", "descripcion": "Se usa en los pies para caminar", "pista": "Puede tener cordones o velcro"},
    {"palabra": "camisa", "descripcion": "Prenda de vestir para la parte superior del cuerpo", "pista": "Puede tener botones"},
    {"palabra": "silla", "descripcion": "Mueble para sentarse", "pista": "Tiene respaldo y a veces brazos"},
    {"palabra": "mesa", "descripcion": "Mueble con superficie plana y patas", "pista": "Se usa para comer o trabajar"},
    {"palabra": "puerta", "descripcion": "Se usa para entrar o salir de un cuarto", "pista": "Se puede abrir y cerrar"},
    {"palabra": "refrigerador", "descripcion": "Objeto que mantiene los alimentos fríos", "pista": "Se encuentra en la cocina"},
    {"palabra": "telefono", "descripcion": "Con este objeto se pueden hacer llamadas", "pista": "Se usa para hacer llamadas"}
]

def mezclarLetras(palabra):
    letras = list(palabra)
    random.shuffle(letras)
    return " ".join(letras)

def juegoLoop():
    puntaje = 0
    pistas_usadas = 0
    errores = 0
    indexPalabras = 0
    running = True

    random.shuffle(palabras)
    palabrasSelecc = palabras[:5]

    while running and indexPalabras < len(palabrasSelecc):
        palabraActual = palabrasSelecc[indexPalabras]
        palabraMezclada = mezclarLetras(palabraActual["palabra"])
        descripcion = palabraActual["descripcion"]
        pista = palabraActual["pista"]

        user_input = ""
        pista_usada = False
        correct = False
        show_error = False

        while not correct and running:
            ventana.fill(COLOR_FONDO)
            mostrarTexto("Encuentra la palabra:", fuente, COLOR_TEXTO, ventana, 20, 20)
            mostrarTexto(f"Letras mezcladas: {palabraMezclada}", fuente, COLOR_TEXTO, ventana, 20, 100)
            mostrarTexto(f"Descripción: {descripcion}", fuente, COLOR_TEXTO, ventana, 20, 150)
            mostrarTexto(f"Tu respuesta: {user_input}", fuente, COLOR_TEXTO, ventana, 20, 200)
            mostrarTexto(f"Pistas usadas: {pistas_usadas}", fuente, COLOR_TEXTO, ventana, 20, 250)

            if pista_usada:
                mostrarTexto(f"Pista: {pista}", fuente, COLOR_TEXTO, ventana, 20, 300)

            mouse_pos = pygame.mouse.get_pos()
            mouse_click = pygame.mouse.get_pressed()

            solicitar_pista_visible = not pista_usada
            if solicitar_pista_visible and mostrarBoton("Solicitar Pista", fuente, COLOR_BOTON, COLOR_BOTON2, ventana, 20, 350, 200, 50, mouse_pos, mouse_click):
                pista_usada = True
                pistas_usadas += 1

            if mostrarBoton("Regresar", fuente, COLOR_BOTON, COLOR_BOTON2, ventana, 240, 350, 200, 50, mouse_pos, mouse_click):
                running = False
                break

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        user_input = user_input[:-1]
                    elif event.key == pygame.K_RETURN:
                        if user_input.lower() == palabraActual["palabra"]:
                            puntaje += 1
                            indexPalabras += 1
                            correct = True

                            ventana.fill(COLOR_CORRECTO)
                            mostrarTexto("¡Correcto!", fuente2, COLOR_TEXTO, ventana, 150, 100)
                            mostrarTexto(f"Palabra: {palabraActual['palabra']}", fuente, COLOR_TEXTO, ventana, 20, 200)
                            pygame.display.flip()
                            pygame.time.wait(2000)
                            break
                        else:
                            show_error = True
                            errores += 1
                            ventana.fill(COLOR_ERROR)
                            mostrarTexto("Error: palabra incorrecta.", fuente2, COLOR_TEXTO, ventana, ANCHO // 2, ALTO // 2, align="center")
                            pygame.display.flip()
                            pygame.time.wait(2000)
                            user_input = ""
                            show_error = False
                    elif event.key == pygame.K_ESCAPE:
                        running = False

                elif event.type == pygame.TEXTINPUT:
                    user_input += event.text

    if running:
        final_screen(puntaje, pistas_usadas, errores)

def final_screen(score, pistas_usadas, errors):
    running = True
    while running:
        ventana.fill(COLOR_FONDO)
        mostrarTexto("Juego Terminado", fuente2, COLOR_TEXTO, ventana, 150, 100)
        mostrarTexto(f"Puntuación final: {score}", fuente, COLOR_TEXTO, ventana, 20, 200)
        mostrarTexto(f"Pistas usadas: {pistas_usadas}", fuente, COLOR_TEXTO, ventana, 20, 250)
        mostrarTexto(f"La cantidad de errores es: {errors}", fuente, COLOR_TEXTO, ventana, 20, 300)

        mouse_pos = pygame.mouse.get_pos()
        mouse_click = pygame.mouse.get_pressed()

        if mostrarBoton("Volver a jugar", fuente, COLOR_BOTON, COLOR_BOTON2, ventana, 20, 400, 200, 50, mouse_pos, mouse_click):
            juegoLoop()
            return
        if mostrarBoton("Salir", fuente, COLOR_BOTON, COLOR_BOTON2, ventana, 240, 400, 200, 50, mouse_pos, mouse_click):
            pygame.quit()
            return

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

if __name__ == "__main__":
    menuInicio()
    pygame.quit()
