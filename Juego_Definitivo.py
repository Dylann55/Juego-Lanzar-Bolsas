import random
import sys
import pygame
import math

"""
Colores
"""
HEIGTH = 700
WIDTH = 900
BLACK = (50, 50, 50)
WHITE = (255, 255, 255)
RED = (255,0,122)
RED2 = (200,0,0)
PURPLE = (100,0,255)
YELLOW = (243, 255, 97)
GREEN = (131, 255, 114)
BLUE = (3, 121, 255)
LIGHT_BLUE = (159, 201, 255)
LIGHT_BLUE2 = (151, 255, 249)
BLUE2 = (59, 139, 255)
BLUE3 = (184, 255, 232)
BLUE4 = (159, 201, 255)

"""
Color del imput,fps,tamaños y posiciones de los textos
"""
color_active = pygame.Color(0, 62, 255)
color_passive = pygame.Color(LIGHT_BLUE2)
fps = 50
size=40
size4=20
size2=10
size3=40
suma=size-5
posicion_resultado=(15, 0)
posicion_sin_Bolsas=(15, 30)

"""
Mensajes
"""
Mensaje_Sin_Bolsas="Sin Bolsas Disponibles"
Mensaje_Vacio=""
Mensaje_Lanzando="Lanzando Bolsa...."
Mensaje_Entregado="Casa Abastecida"
Mensaje_no_Entregado="Casa no Abastecida"
Mensaje_Perdido="Bolsa Perdida"
Mensaje_Fuera_Lateral="Bolsa Fuera del Rango Lareral"
Mensaje_Fuera_Superior="Bolsa Fuera del Rango Superior"


"""
Direcciones de las imagenes
"""
Direcciones_Computadora=['Imagenes/AI_95 1.png','Imagenes/AI_95 2.png','Imagenes/AI_95 3.png','Imagenes/AI_95 4.png']
Direcciones_Jugador=['Imagenes/Pl_fire_highangle_1.png','Imagenes/Pl_fire_highangle_2.png','Imagenes/Pl_fire_highangle_3.png','Imagenes/Pl_fire_highangle_4.png']
Direcciones_Jugador_Bolsa=['Imagenes/peojwctile_deploy 1.png','Imagenes/peojwctile_deploy 2.png','Imagenes/peojwctile_deploy 3.png','Imagenes/peojwctile_deploy 4.png','Imagenes/peojwctile_deploy 6.png']
Direcciones_Computadora_Bolsa=['Imagenes/peojwctile_deploy 1.png','Imagenes/peojwctile_deploy 2.png','Imagenes/peojwctile_deploy 3.png','Imagenes/peojwctile_deploy 4.png','Imagenes/peojwctile_deploy 7.png']
Direcciones_Casa=['Imagenes/Dull building small.png']
Direcciones_Casa2=['Imagenes/lit building small.png']
Direcciones_Obstaculo=['Imagenes/lago_grande.png','Imagenes/lagochiico.png']

Direcciones_Boton_Iniciar=['Imagenes/a_button_start_2.png', 'Imagenes/a_button_start_1.png']
Direcciones_Boton_Salir= ['Imagenes/a_button_Exit_2.png', 'Imagenes/a_button_Exit_1.png']
Direcciones_Boton_Facil=['Imagenes/a_button_easy_2.png', 'Imagenes/a_button_easy_3.png']
Direcciones_Boton_Dificil=['Imagenes/a_button_hard_2.png', 'Imagenes/a_button_hard_3.png']
Direcciones_Boton_VS=['Imagenes/a_button_VS_2.png', 'Imagenes/a_button_VS_1.png']
Direcciones_Boton_Solo=['Imagenes/a_button_Solo_2.png', 'Imagenes/a_button_Solo_1.png']
Direcciones_Boton_Estadisticas=['Imagenes/a_button_stats_2.png', 'Imagenes/a_button_stats_1.png']
Direcciones_Boton_Volver=['Imagenes/a_button_return_2.png', 'Imagenes/a_button_return_1.png']
Direcciones_Boton_Lanzar=['Imagenes/a_button_launch_2.png', 'Imagenes/a_button_launch_1.png']

"""
Clases
"""
class Sprite_move(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, estado1, estado2):
        """
        Sprite_move encapsula las posiciones iniciales, el ancho, el largo , las direcciones de las imagenes del estado1 y las direcciones de las imagenes del estado2,
        si fue activado,si su animacion fue activado,una lista de Sprites del estado1 , una lista de Sprites del estado2,el indice,
        la imagen del sprite y donde sera guardado la imagen
        :param x:Posicion x del Button
        :param y:Posicion y del Button
        :param width:Ancho del Button
        :param height:Altura del Button
        :param estado1:Lista de Direcciones del Sprite desactivado
        :param estado2:Lista de Direcciones del Sprite activado
        """
        super().__init__()
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.estado1 = estado1
        self.estado2 = estado2
        self.active = False
        self.attack_animation = False
        self.sprites1 = []
        self.sprites2 = []

        for index, value in enumerate(estado1):
            img = pygame.image.load(value)
            img = pygame.transform.scale(img, (self.width, self.height))
            self.sprites1.append(img)

        for index, value in enumerate(estado2):
            img2 = pygame.image.load(value)
            img2 = pygame.transform.scale(img2, (self.width, self.height))
            self.sprites2.append(img2)

        self.current_sprite = 0
        self.image = self.sprites1[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.topleft = [self.x, self.y]

    def attack(self):
        """
        Funcion que marca como True el attack_animation,para que empieze la animacion
        """
        self.attack_animation = True

    def update(self, speed):
        """
        Funcion que inicia la animacion e intercambia del estado 1 al estado2 y viceversa cuando se vuelva a llamar a la funcion
        :param speed:Valor de la velocidad
        """
        if self.attack_animation == True:
            self.current_sprite += speed
            if int(self.current_sprite) >= len(self.sprites1):
                self.current_sprite = 0
                self.attack_animation = False
                if (len(self.sprites2) != 0):
                    aux = []
                    aux = self.sprites1
                    self.sprites1 = self.sprites2
                    self.sprites2 = aux

            self.image = self.sprites1[int(self.current_sprite)]

    def isOver(self, pos):
        """
        Funcion que detecta si la posicion esta dentro del Sprite
        :param pos:Posicion
        :return:Retorna un True si la posicion esta dentro del Sprite, en caso contrario devuelve un False
        """
        if pos[0] > self.rect.x and pos[0] < self.rect.x + self.width:
            if pos[1] > self.rect.y and pos[1] < self.rect.y + self.height:
                return True
        return False

class Sprite_Disparo(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, estado1,Trayectoria):
        """
        Sprite_Disparo encapsula las posiciones iniciales, el ancho, el largo , las direcciones de las imagenes del estado1,
        si fue activado,si su animacion fue activado,una lista de Sprites del estado1 ,el indice,una lista de posiciones
        la imagen del sprite y donde sera guardado la imagen
        :param x:Posicion x del Button
        :param y:Posicion y del Button
        :param width:Ancho del Button
        :param height:Altura del Button
        :param estado1:Lista de Direcciones del Sprite desactivado
        """
        super().__init__()
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.active = False
        self.attack_animation = False
        self.sprites1 = []
        self.cantidad = len(Trayectoria)
        self.Trayectoria = Trayectoria
        self.estado1 = estado1

        for index, value in enumerate(self.estado1):
            img = pygame.image.load(value)
            img = pygame.transform.scale(img, (self.width, self.height))
            self.sprites1.append(img)

        self.current_sprite = 0
        self.image = self.sprites1[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.topleft = [self.x, self.y]

    def attack(self):
        """
        Funcion que marca como True el attack_animation,para que empieze la animacion
         """
        self.attack_animation = True

    def update(self, speed):
        """
        Funcion que inicia la animacion cambiando la posicion del Sprite y termina dejando la ultima imagen de la Lista de Sprites
        :param speed:Valor de la velocidad
        """
        if self.attack_animation == True:
            self.current_sprite += speed
            if int(self.current_sprite) >= len(self.sprites1):
                self.current_sprite = len(self.sprites1)-1
                self.attack_animation = False
            self.rect.x =self.Trayectoria[int(self.current_sprite)][0]
            self.rect.y = self.Trayectoria[int(self.current_sprite)][1]
            self.image = self.sprites1[int(self.current_sprite)]

    def Posicion(self,Trayectoria,estado1):
        """
        Funcion que limpia la Lista de Sprites y modifica a el indice,el active,la imagen,la Lista de posiciones,las posiciones iniciales
        y las posiciones donde sera guardado la imagen
        :param Trayectoria:
        :param estado1:
        """
        self.sprites1.clear()
        for index, value in enumerate(estado1):
            img = pygame.image.load(value)
            img = pygame.transform.scale(img, (self.width, self.height))
            self.sprites1.append(img)
        self.active = False
        self.current_sprite = 0
        self.image = self.sprites1[self.current_sprite]
        self.Trayectoria = Trayectoria
        self.x = self.Trayectoria[0][0]
        self.y = self.Trayectoria[0][1]
        self.rect.topleft = [self.x, self.y]

class Casa:
    def __init__(self,cantidad):
        """
        Casa encapsula la cantidad, la posicion inicial aun no aleatoria,una lista de Sprite_move y lista donde seran guardados los Sprite_move
        :param cantidad: Cantidad de Casas
        """
        self.cantidad = cantidad
        self.Casa_position = (0,0)
        self.Casas_list = pygame.sprite.Group()
        self.Sprite_Casas=[]
        self.random_position()

    def random_position(self):
        """
        Funcion que inicializa las posiciones aleatorias de las Casas y guarda los Sprite_move en Casas_list
        """
        self.Casas_list.empty()
        self.Sprite_Casas.clear()
        self.Casa_position = [(random.randrange(50, 850, size3), random.randrange(50, 550, size3)) for i in range(self.cantidad)]
        for i in range(self.cantidad):
            Sprite_Casa = Sprite_move(self.Casa_position[i][0],self.Casa_position[i][1],size,size,Direcciones_Casa,[])
            self.Sprite_Casas.append(Sprite_Casa)
        for i in range(self.cantidad):
            self.Casas_list.add(self.Sprite_Casas[i])
        for i in set(self.Casa_position):
            if self.Casa_position.count(i) > 1:
                self.random_position()

    def draw_Casa(self, window):
        """
        Funcion que imprime las Casas en pantalla
        :param window:Pantalla donde se impriran las Casas
        """
        self.Casas_list.draw(window)

    def isOver(self, pos):
        """
        Funcion que detecta si la posicion esta dentro de una de las Casas
        :param pos: Posicion
        :return:Retorna el indice de la casa,en caso contrario devuelve un -1
        """
        for index, value in enumerate(self.Sprite_Casas):
            if (value.isOver(pos)==True):
                    return index
        return -1

class Obstaculo:
    def __init__(self,cantidad):
        """
        Obstaculo encapsula la cantidad, las posicion inicial aun no aleatoria,una lista de Sprite_move y lista donde seran guardados los Sprite_move
        :param cantidad:Cantidad de Obstaculos
        """
        self.cantidad = cantidad
        self.Obstaculo_position = (0,0)
        self.Sprite_Obstaculos_img=[random.choice(Direcciones_Obstaculo) for i in range(self.cantidad)]
        self.Obstaculos_list = pygame.sprite.Group()
        self.Sprite_Obstaculos = []
        self.random_position()

    def random_position(self):
        """
        Funcion que inicializa las posiciones aleatorias de los Obstaculos y guarda los Sprite_move en Obstaculos_list
        """
        self.Sprite_Obstaculos.clear()
        self.Obstaculos_list.empty()
        self.Obstaculo_position = [(random.randrange(50, 850,size3), random.randrange(50, 550,size3)) for i in range(self.cantidad)]

        for i in range(self.cantidad):
            Sprite_Obstaculo = Sprite_move(self.Obstaculo_position[i][0],self.Obstaculo_position[i][1],size3,size3,[self.Sprite_Obstaculos_img[i]],[])
            self.Sprite_Obstaculos.append(Sprite_Obstaculo)
        for i in range(self.cantidad):
            self.Obstaculos_list.add(self.Sprite_Obstaculos[i])

        for i in set(self.Obstaculo_position):
            if self.Obstaculo_position.count(i) > 1:
                self.random_position()

    def draw_Obstaculo(self, window):
        """
        Funcion que imprime los Obstaculos en pantalla
        :param window:Pantalla donde se impriran los Obstaculos
        """
        self.Obstaculos_list.draw(window)

    def isOver(self, pos):
        """
        Funcion que detecta si la posicion esta dentro de una de las Obstaculo
        :param pos: Posicion
        :return:Retorna True si posicion esta en el Obstaculo,en caso contrario devuelve un False
        """
        for index, value in enumerate(self.Sprite_Obstaculos):
            if (value.isOver(pos) == True):
                return True
        return False

class Bolsa:
    def __init__(self,direccion):
        """
        Bolsa encapsula la cantidad de bolsas,una lista de posiciones,las direcciones de las imagenes de las Bolsas y una lista donde seran guardados los Sprite_move
        """
        self.direccion=direccion
        self.Bolsa_position=[]
        self.cantidad=0
        self.Bolsas_list = pygame.sprite.Group()
    def Agregar(self,Position):
        """
        Funcion que agrega una la posicion de la Bolsa a la lista de posiciones y aumenta la cantidad en 1
        :param Position:Posicion de la bolsa
        """
        self.cantidad+=1
        self.Bolsa_position.append(Position)
    def Sprite(self):
        """
        Funcion que inicializa y guarda los Sprite_move en Bolsas_list
        """
        for i in range(self.cantidad):
            Sprite_Bolsa = Sprite_move(self.Bolsa_position[i][0],self.Bolsa_position[i][1],size2,size2,[self.direccion[len(self.direccion)-1]],[])
            self.Bolsas_list.add(Sprite_Bolsa)

    def draw_Bolsa(self, window):
        """
        Funcion que imprime las bolsas en pantalla
        :param window:Pantalla donde se impriran los bolsas
        """
        self.Bolsas_list.draw(window)

class Jugador:
    def __init__(self,nombre,cantidad,direccion,direccion2,direccion3):
        """
        Jugador encapsula el nombre,3 listas de direcciones de las imagenes, una Lista de direcciones de las imagenes auxiliar ,un objeto Bolsa,una lista donde seran guardados los Sprite_move,
        ,una lista de posiciones de la Trayectoria ,lista donde seran guardados los Sprite_Disparo,un mensaje dependiendo de resultado,
        una lista de Casas Abastecidas,una lista de Casas Visitadas,la cantidad de Casas abasteciad,la cantidad de Casas que no fueron abastecidas,
        la cantidad de Bolas perdidas,las distancia total de las bolsas perdidas,una lista de distancias de las casas que no fueron abastecidas,
        la distancia total y la posicion inical de Jugador
        :param nombre:El nombre del Jugador
        :param cantidad:La cantidad de Casas que tendra que abastecer
        :param direccion:Las direcciones de las imagenes del Jugador
        :param direccion2:Las direcciones de las imagenes secundarias del Jugador
        :param direccion3:Las direcciones de las imagenes de la Bolsa
        """
        self.nombre = nombre

        self.direccion = direccion
        self.direccion2 = direccion2
        self.direccion3 = direccion3
        self.direccion3_AUX = []

        self.Bolsas = Bolsa(self.direccion3)
        self.Jugador_list = pygame.sprite.Group()
        self.Tratectoria = []
        self.Tratectoria_list = pygame.sprite.Group()

        self.Resultado = Mensaje_Vacio
        self.Visitadas = [False for i in range(cantidad)]
        self.Abastecida = [False for i in range(cantidad)]
        self.entregada = 0
        self.no_entregada= 0
        self.perdido = 0
        self.distancia_perdida = 0
        self.distancias = [0 for i in range(cantidad)]
        self.distancia_Total = 0

        self.Jugador_position = (0,0)
        self.random_position()

    def random_position(self):
        """
        Funcion que inicializa las posiciones del Jugador y guarda los Sprite_move en Jugador_list
        """
        self.Jugador_list.empty()
        self.Jugador_position = (random.randrange(50, 850,size3), random.randrange(50, 550,size3))
        self.Sprite_Jugador = Sprite_move(self.Jugador_position[0],self.Jugador_position[1],size,size,self.direccion,self.direccion2)
        self.Jugador_list.add(self.Sprite_Jugador)

    def draw_Jugador(self, window):
        """
        Funcion que imprime el Jugador en Pantalla
        :param window:Pantalla donde se imprira el Jugador
        """
        self.Jugador_list.draw(window)

    def draw_Trayectoria(self, window):
        """
        Funcion que imprime la trayectoria donde va a caer la bolsa
        :param window:Pantalla donde se imprira la trayectoria de la bolsa
        """
        if(len(self.Tratectoria)!=0):
            self.Tratectoria_list.draw(window)

    def Cambiar_Vista(self,i):
        """
        Funcion que marca Verdadero si ya casa ya fue Visitada
        :param i:Posicion de la Casa ya Visitada
        """
        self.Visitadas[i]=True

    def entregado(self,i):
        """
        Funcion que incrementa en 1 en numero de bolsa entregadas
        """
        self.Resultado = Mensaje_Entregado
        self.Abastecida[i]=True
        self.entregada+=1

    def no_entregado(self,valor,i):
        """
        Funcion que incrementa en 1 en numero de bolsa no entregadas y la distancia de la bolsa no entregada
        :param valor:Distancia de la Bolsa no entregada
        :param i:Posicion de la Casa que no fue abastecida
        """
        self.Resultado = Mensaje_no_Entregado
        self.distancias[i]+=valor
        self.no_entregada+=1

    def perdida(self):
        """
        Funcion que incrementa en 1 en numero de bolsa no entregadas y en 5 la distancia de la bolsa perdida
        """
        self.Resultado = Mensaje_Perdido
        self.perdido+=1
        self.distancia_perdida+=5

    def suma_distancias(self):
        """
        Funcion que suma las distancias,las distancias perdidas y la distancia perdida
        """
        self.distancia_Total=sum(self.distancias)+self.distancia_perdida

    def agregar(self,a):
        """
        Funcion que agrega la posicion de la bolsa
        :param a:Posicion de la bolsa
        """
        self.Bolsas.Agregar(a)

    def simetria(self,a):
        """
        Funcion que cambia la posicion del punto de la trayectoria
        :param a:Posicion un punto de la Trayectoria
        """
        distancia = Distancia(a, (a[0], 320))
        return (a[0], (a[1] - (2 * distancia)))

    def Convertir_Trayectoria(self,AUX,Punto_Final,Cantidad_Puntos):
        """
        Funcion que reduce la lista de posiciones de la Trayectoria dependiendo de la cantidad que hay en direccion3
        :param AUX:Lista de posiciones de la Trayectoria
        :param Punto_Final:Posicion final de la Trayectoria
        :param Cantidad_Puntos:Cantida de posiciones en la Lista AUX
        """
        Cantidad_Imagenes=len(self.direccion3)
        S=int(Cantidad_Puntos/Cantidad_Imagenes)
        i=0
        if(S>=1):
            for index in range(Cantidad_Imagenes - 1):
                self.Tratectoria.append(self.simetria(AUX[i]))
                i += S
            self.Tratectoria.append(self.simetria(Punto_Final))
            self.direccion3_AUX = self.direccion3
        else:
            for index in range(Cantidad_Puntos):
                self.Tratectoria.append(self.simetria(AUX[index]))
            if(Cantidad_Puntos==1):
                self.direccion3_AUX = [self.direccion3[4]]
            elif (Cantidad_Puntos == 2):
                self.direccion3_AUX = [self.direccion3[0],self.direccion3[4]]
            elif (Cantidad_Puntos == 3):
                self.direccion3_AUX = [self.direccion3[0],self.direccion3[2],self.direccion3[4]]
            elif (Cantidad_Puntos == 4):
                self.direccion3_AUX = [self.direccion3[0],self.direccion3[1],self.direccion3[3],self.direccion3[4]]

    def Crear_Trayectoria(self):
        """
        Funcion que inicializa y guarda los Sprite_Disparo en Tratectoria_list
        """
        self.Tratectoria_list.empty()
        self.Sprite_Trayectoria=Sprite_Disparo(40,320-size,size2,size2,self.direccion3,[(40,320-size)])
        self.Tratectoria_list.add(self.Sprite_Trayectoria)

class Input():
    def __init__(self, color, x, y, width, height,text):
        """
        Input encapsula el color, las posiciones iniciales, el ancho, el largo y el contenido de ella
        :param color:Color del imput
        :param x:Posicion x del imput
        :param y:Posicion y del imput
        :param width:Ancho del imput
        :param height:Altura del imput
        :param text:Contenido del imput
        """
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.active = False


    def draw(self, window,font):
        """
        Funcion que imprime el Input en pantalla
        :param window:Pantalla donde se impriran el Input
        :param font:Fuente para el texto
        """
        input = pygame.Rect(self.x, self.y, self.width, self.height)
        text_surface = font.render(self.text, True, self.color)
        window.blit(text_surface, (input.x + 5, input.y + 5))
        input.w = max(100, text_surface.get_width() + 10)

    def isOver(self, pos):
        """
        Funcion que detecta si la posicion del mouse esta dentro del imput
        :param pos:Posicion del mouse
        :return:Retorna un True si la posicion esta dentro del input, en caso contrario devuelve un False
        """
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
        return False

"""
Funciones de Pantalla
"""
def Pantalla1():
    """
    Funcion de la Pantalla de la Vista de configuración
    """
    pygame.init()
    window = pygame.display.set_mode((WIDTH,HEIGTH))
    pygame.display.set_caption("Entrega de Suministros")

    base_font = pygame.font.SysFont("Helvetica", 28)
    width=250
    heigth=32
    y1=220
    y2=y1+40
    y3=y2+50
    x1=150
    x2=x1+width+25


    cant_nombre=0
    moving_sprites = pygame.sprite.Group()
    input_nombre = Input(color_passive,240,195,140,32,'')
    input_cantidad1 = Input(color_passive,270, y1, 140, 32,'')
    input_cantidad2 = Input(color_passive,270, y2, 140, 32,'')

    button_dificultad = Sprite_move(x1, 260, width, 32, Direcciones_Boton_Facil, Direcciones_Boton_Dificil)
    button_bot = Sprite_move(x2, 260, width, 32, Direcciones_Boton_Solo, Direcciones_Boton_VS)
    button_iniciar = Sprite_move(x1, y3, width, 32, Direcciones_Boton_Iniciar, [])
    button_salir = Sprite_move(x2, y3, width, 32, Direcciones_Boton_Salir, [])

    moving_sprites.add(button_dificultad)
    moving_sprites.add(button_bot)
    moving_sprites.add(button_iniciar)
    moving_sprites.add(button_salir)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_position = pygame.mouse.get_pos()

                if(button_dificultad.isOver(mouse_position)):
                    input_nombre.active = False
                    input_nombre.color = color_passive
                    input_cantidad1.active = False
                    input_cantidad1.color = color_passive
                    input_cantidad2.active = False
                    input_cantidad2.color = color_passive
                    if (button_dificultad.active == False):
                        button_dificultad.active = True
                        input_cantidad1.text=''
                        input_cantidad2.text=''
                        y1=300

                    else:
                        button_dificultad.active = False
                        input_cantidad1.text = ''
                        input_cantidad2.text = ''
                        y1=220

                    y2 = y1 + 40
                    y3 = y2 + 55
                    input_cantidad1.y = y1
                    input_cantidad2.y = y2
                    button_iniciar.rect.y = y3
                    button_salir.rect.y= y3
                    button_dificultad.attack()

                elif(button_bot.isOver(mouse_position)):
                    button_bot.attack()
                    input_nombre.active = False
                    input_nombre.color = color_passive
                    input_cantidad1.active = False
                    input_cantidad1.color = color_passive
                    input_cantidad2.active = False
                    input_cantidad2.color = color_passive
                    if(button_bot.active == False):
                        button_bot.active=True
                    else:
                        button_bot.active = False

                    button_bot.attack()

                elif(button_salir.isOver(mouse_position)):
                    button_salir.attack()
                    pygame.quit()
                    sys.exit()

                elif(button_iniciar.isOver(mouse_position)):
                    button_iniciar.attack()
                    if (input_nombre.text != ''):
                        if (button_dificultad.active == False):
                            Pantalla2_DF(window, input_nombre.text, button_bot.active)
                        else:
                            if ((es_entero(input_cantidad1.text)) and (es_entero(input_cantidad2.text))):
                                cantidad1 = Positivo(int(input_cantidad1.text), 0)
                                cantidad2 = Positivo(int(input_cantidad2.text), 0)
                                if (cantidad1 >= 3 and cantidad1 <= 7 and cantidad2 > 0 and cantidad2 <= 7):
                                    Pantalla2_DM(window, input_nombre.text, cantidad1, cantidad2,button_bot.active)
                                else:
                                    print("Ingrese las Variables corectamente")

                elif (input_nombre.isOver(mouse_position)):
                    input_nombre.active=True
                    input_nombre.color=color_active
                    input_cantidad1.active = False
                    input_cantidad1.color=color_passive
                    input_cantidad2.active = False
                    input_cantidad2.color=color_passive
                elif (input_cantidad1.isOver(mouse_position)):
                    input_nombre.active = False
                    input_nombre.color = color_passive
                    input_cantidad1.active = True
                    input_cantidad1.color = color_active
                    input_cantidad2.active = False
                    input_cantidad2.color = color_passive
                elif (input_cantidad2.isOver(mouse_position)):
                    input_nombre.active = False
                    input_nombre.color = color_passive
                    input_cantidad1.active = False
                    input_cantidad1.color = color_passive
                    input_cantidad2.active = True
                    input_cantidad2.color = color_active
                else:
                    input_nombre.active = False
                    input_nombre.color = color_passive
                    input_cantidad1.active = False
                    input_cantidad1.color = color_passive
                    input_cantidad2.active = False
                    input_cantidad2.color = color_passive

            if event.type == pygame.KEYDOWN:
                    if (input_nombre.active == True):
                        if event.key == pygame.K_BACKSPACE:
                            input_nombre.text = input_nombre.text[:cant_nombre-2]
                            cant_nombre-= 1
                        else:
                            cant_nombre+=1
                            input_nombre.text += event.unicode
                    elif (input_cantidad1.active == True):
                        if event.key == pygame.K_BACKSPACE:
                            input_cantidad1.text = input_cantidad1.text[:0]
                        else:
                            input_cantidad1.text += event.unicode
                    elif (input_cantidad2.active == True):
                        if event.key == pygame.K_BACKSPACE:
                            input_cantidad2.text = input_cantidad2.text[:0]
                        else:
                            input_cantidad2.text += event.unicode

        draw_grid(window,BLUE4)

        Nombre = base_font.render("Nombre:", True, BLACK)
        window.blit(Nombre, (150, 200))
        input_nombre.draw(window, base_font)

        if(button_dificultad.active==True):
            Cantidad1 = base_font.render("Cantidad Casas:", True, BLACK)
            window.blit(Cantidad1, (50, y1+5))
            input_cantidad1.draw(window, base_font)
            Cantidad2 = base_font.render("Cantidad Obstaculos:", True, BLACK)
            window.blit(Cantidad2, (50, y2+5))
            input_cantidad2.draw(window, base_font)


        moving_sprites.draw(window)
        moving_sprites.update(0.1)
        pygame.display.update()

def Pantalla2_DF(window,nombre,Existe):
    """
    Funcion de la Pantalla de la Vista superior en Dificultad fácil
    :param window:Pantalla de la vista superior
    :param nombre:Nombre del Jugador
    :param Existe:Existencia de la computadora
    """
    paused = True
    game_font = pygame.font.SysFont("Helvetica", 28)
    cantidad = 3
    moving_sprites = pygame.sprite.Group()
    moving_sprites_Fondo = pygame.sprite.Group()

    Casas = Casa(cantidad)
    Jugador1 = Jugador(nombre, cantidad,Direcciones_Jugador,[],Direcciones_Jugador_Bolsa)
    if Existe==True:
        Computadora = Jugador("Computadora", cantidad,Direcciones_Computadora,[],Direcciones_Computadora_Bolsa)
    Pasto=Sprite_move(0,0,WIDTH,HEIGTH,['Imagenes/grass03.png'],[])
    moving_sprites_Fondo.add(Pasto)
    button_Estadistica = Sprite_move(180, 600, 250, 32, Direcciones_Boton_Estadisticas, [])
    button_volver_inicio = Sprite_move(455, 600, 250, 32, Direcciones_Boton_Volver, [])
    moving_sprites.add(button_Estadistica)
    moving_sprites.add(button_volver_inicio)
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_position=pygame.mouse.get_pos()
                if(button_Estadistica.isOver(mouse_position)):
                    button_Estadistica.attack()
                    if Existe == True:
                        Pantalla4_Existe(window, Jugador1, Computadora, Casas)
                    else:
                        Pantalla4(window,Jugador1,Casas)
                elif(button_volver_inicio.isOver(mouse_position)):
                    button_volver_inicio.attack()
                    paused=False
                else:
                    index=Casas.isOver(mouse_position)
                    if (index != -1):
                        if (Jugador1.Visitadas[index] == False):
                            Pantalla3_DF(window, Casas, Jugador1, index)
                        else:
                            print(f"Casas Bloqueada {index + 1}")
                        if (Existe == True):
                            if (Computadora.Visitadas[index] == False):
                                Pantalla3_DF_Existe(window, Casas, Computadora, index)


        draw_grid(window,GREEN)
        moving_sprites_Fondo.draw(window)
        moving_sprites_Fondo.update(0.1)
        Pasto.attack()
        Casas.draw_Casa(window)
        Jugador1.draw_Jugador(window)
        while True:
            if (Jugador1.Jugador_position in Casas.Casa_position):
                Jugador1.random_position()
            break
        if Existe == True:
            Computadora.draw_Jugador(window)
            while True:
                if ((Computadora.Jugador_position == Jugador1.Jugador_position)) or (
                        Computadora.Jugador_position in Casas.Casa_position):
                    Computadora.random_position()
                break
        Casas.draw_Casa(window)

        if Existe == True:
            if (Computadora.Bolsas.cantidad != 0):
                Computadora.Bolsas.draw_Bolsa(window)
        if (Jugador1.Bolsas.cantidad != 0):
            Jugador1.Bolsas.draw_Bolsa(window)

        moving_sprites.draw(window)
        moving_sprites.update(0.1)
        pygame.display.update()

def Pantalla2_DM(window,nombre,cantidad,cantidad2,Existe):
    """
    Funcion de la Pantalla de la Vista superior en Dificultad Media
    :param window:Pantalla de la vista superior
    :param nombre:Nombre del Jugador
    :param Existe:Existencia de la computadora
    :param cantidad:Cantidad de Casas
    :param cantidad:Cantidad de Obstaculos
    """
    paused = True
    game_font = pygame.font.SysFont("Helvetica", 28)
    moving_sprites = pygame.sprite.Group()
    moving_sprites_Fondo = pygame.sprite.Group()
    Casas = Casa(cantidad)
    Obstaculos = Obstaculo(cantidad2)
    Jugador1 = Jugador(nombre, cantidad,Direcciones_Jugador,[],Direcciones_Jugador_Bolsa)
    if Existe==True:
        Computadora = Jugador("Computadora", cantidad,Direcciones_Computadora,[],Direcciones_Computadora_Bolsa)
    Pasto = Sprite_move(0, 0, WIDTH, HEIGTH, ['Imagenes/grass03.png'],[])
    moving_sprites_Fondo.add(Pasto)

    button_Estadistica = Sprite_move(180, 600, 250, 32, Direcciones_Boton_Estadisticas, [])
    button_volver_inicio = Sprite_move(455, 600, 250, 32, Direcciones_Boton_Volver, [])
    moving_sprites.add(button_Estadistica)
    moving_sprites.add(button_volver_inicio)
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_position=pygame.mouse.get_pos()
                if (button_Estadistica.isOver(mouse_position)):
                    button_Estadistica.attack()
                    if Existe == True:
                        Pantalla4_Existe(window, Jugador1, Computadora, Casas)
                    else:
                        Pantalla4(window,  Jugador1,Casas)
                elif (button_volver_inicio.isOver(mouse_position)):
                    button_Estadistica.attack()
                    paused = False
                else:
                    index = Casas.isOver(mouse_position)
                    if (index != -1):
                        if (Jugador1.Visitadas[index] == False):
                            Pantalla3_DM(window, Casas, Obstaculos, Jugador1, index)
                        else:
                            print(f"Casas Bloqueada {index + 1}")
                        if (Existe == True):
                            if (Computadora.Visitadas[index] == False):
                                Pantalla3_DM_Existe(window, Casas, Obstaculos, Computadora, index)

        draw_grid(window,GREEN)
        moving_sprites_Fondo.draw(window)
        moving_sprites_Fondo.update(0.1)
        Pasto.attack()
        Jugador1.draw_Jugador(window)
        while True:
            if (Jugador1.Jugador_position in Obstaculos.Obstaculo_position) or (
                    Jugador1.Jugador_position in Casas.Casa_position):
                Jugador1.random_position()
            break

        if Existe == True:
            Computadora.draw_Jugador(window)
            while True:
                if ((Computadora.Jugador_position == Jugador1.Jugador_position) or Computadora.Jugador_position in Obstaculos.Obstaculo_position) or (Computadora.Jugador_position in Casas.Casa_position):
                    Computadora.random_position()
                break
        Casas.draw_Casa(window)
        while True:
            for i, value in enumerate(Casas.Casa_position):
                if value in Obstaculos.Obstaculo_position:
                    Casas.random_position()
            break
        Obstaculos.draw_Obstaculo(window)

        if Existe == True:
            if (Computadora.Bolsas.cantidad != 0):
                Computadora.Bolsas.draw_Bolsa(window)
        if (Jugador1.Bolsas.cantidad != 0):
            Jugador1.Bolsas.draw_Bolsa(window)

        moving_sprites.draw(window)
        moving_sprites.update(0.1)
        pygame.display.update()

def Pantalla3_DF(window,Casas,Jugador1,i):
    """
    Funcion de la Pantalla de la Vista lateral en Dificultad fácil y sin computadora
    :param window:Pantalla de la vista lateral
    :param Casas:Clase Casa
    :param Jugador1:Clase Jugador
    :param i:Indice de la Casa que debe ser abastecida
    """
    paused = True
    game_font = pygame.font.SysFont("Helvetica", 28)
    clock = pygame.time.Clock()
    logrado1=False
    contador1=3
    moving_sprites = pygame.sprite.Group()
    Jugador1.Resultado=Mensaje_Vacio

    Sin_Bolsas = game_font.render(Mensaje_Vacio, True, BLACK)
    Resultado = game_font.render(f"{Jugador1.Resultado}", True, BLACK)

    A,B=Modificacion(Jugador1.Jugador_position,Casas.Casa_position[i])
    C=Distancia(A,B)
    angulo=SacarAngulo(A,B,C)
    Tam=int(size/math.cos(math.radians(angulo)))


    PJ=(40,320-size)
    PJ_Lanzar=(PJ[0]+size, PJ[1]+size+suma)
    PC = (PJ_Lanzar[0] + C,320-size)
    Y_Variable = 560
    Y_Variable2 = Y_Variable + 35
    Y_Lanzar = Y_Variable2 + 45

    Sprite_Jugador=Sprite_move(PJ[0],PJ[1],size,size,Jugador1.direccion,Jugador1.direccion2)
    Jugador1.Crear_Trayectoria()

    moving_sprites.add(Sprite_Jugador)
    input_vel = Input(color_passive,140, Y_Variable, 140, 32,'')
    input_ang = Input(color_passive,140, Y_Variable2, 140, 32,'')
    button_lanzar = Sprite_move(30, Y_Lanzar, 250, 32, Direcciones_Boton_Lanzar, [])
    button_Salir = Sprite_move(305, Y_Lanzar, 250, 32, Direcciones_Boton_Salir, [])
    moving_sprites.add(button_lanzar)
    moving_sprites.add(button_Salir)
    while paused:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_position=pygame.mouse.get_pos()
                if (button_lanzar.isOver(mouse_position)):
                    button_lanzar.attack()
                    button_lanzar.active = True
                    input_vel.color = color_passive
                    input_vel.active = False
                    input_ang.color = color_passive
                    input_ang.active = False

                elif (button_Salir.isOver(mouse_position)):
                    if (logrado1 == True or contador1 == 0):
                        button_Salir.attack()
                        Jugador1.Tratectoria.clear()
                        Jugador1.Cambiar_Vista(i)
                        paused = False

                elif (input_vel.isOver(mouse_position)):
                    input_vel.color=color_active
                    input_vel.active=True
                    input_ang.color=color_passive
                    input_ang.active=False
                elif (input_ang.isOver(mouse_position)):
                    input_vel.color=color_passive
                    input_vel.active=False
                    input_ang.color = color_active
                    input_ang.active = True
                else:
                    input_vel.color = color_passive
                    input_vel.active = False
                    input_ang.color = color_passive
                    input_ang.active = False

            if event.type == pygame.KEYDOWN:
                if (input_vel.active == True):
                    if event.key == pygame.K_BACKSPACE:
                        input_vel.text = input_vel.text[:0]
                    else:
                        input_vel.text += event.unicode
                elif (input_ang.active == True):
                    if event.key == pygame.K_BACKSPACE:
                        input_ang.text = input_ang.text[:0]
                    else:
                        input_ang.text += event.unicode

        draw_grid2(window,BLUE, C,game_font,Y_Variable,Tam)

        input_vel.draw(window, game_font)
        input_ang.draw(window,game_font)

        if(button_lanzar.active==True):
            if (es_entero(input_vel.text) and es_entero(input_ang.text)):
                vel = Positivo(int(input_vel.text), 0)
                angulo = Positivo(int(input_ang.text), 0)
                if (contador1 > 0 and logrado1 == False and angulo<90):
                    Resultado = game_font.render(Mensaje_Lanzando, True, BLACK)
                    logrado1 = Lanzamiento_Facil_Principal(Casas, PC, Jugador1, PJ_Lanzar, i, A, B, C, Tam, vel, angulo)
                    Jugador1.Bolsas.Sprite()
                    contador1 -= 1
                    Sprite_Jugador.attack()
                    button_lanzar.active = False
            else:
                print("Ingrese las Variables corectamente")
            button_lanzar.active = False

        if(Sprite_Jugador.current_sprite==len(Jugador1.direccion)-2):
            Jugador1.Sprite_Trayectoria.Posicion(Jugador1.Tratectoria,Jugador1.direccion3_AUX)
            Jugador1.Sprite_Trayectoria.attack()
            Jugador1.Sprite_Trayectoria.active=True

        if (Jugador1.Sprite_Trayectoria.active==True and Jugador1.Sprite_Trayectoria.attack_animation==False):
            Resultado = game_font.render(f"{Jugador1.Resultado}", True, BLACK)
            Jugador1.Sprite_Trayectoria.active=False
            if (contador1 == 0):
                Sin_Bolsas = game_font.render(Mensaje_Sin_Bolsas, True, BLACK)

        window.blit(Sin_Bolsas, posicion_sin_Bolsas)

        window.blit(Resultado,posicion_resultado)
        Jugador1.draw_Trayectoria(window)
        Jugador1.Tratectoria_list.update(0.25)
        moving_sprites.draw(window)
        moving_sprites.update(0.25)
        pygame.display.update()

def Pantalla3_DF_Existe(window,Casas,Computadora,i):
    """
    Funcion de la Pantalla de la Vista lateral en Dificultad fácil y con computadora
    :param window:Pantalla de la vista lateral
    :param Casas:Clase Casa
    :param Computadora:Clase Jugador
    :param i:Indice de la Casa que debe ser abastecida
    """
    paused = True
    game_font = pygame.font.SysFont("Helvetica", 28)
    clock = pygame.time.Clock()
    logrado1 = False
    contador1 = 3
    moving_sprites = pygame.sprite.Group()

    A, B = Modificacion(Computadora.Jugador_position, Casas.Casa_position[i])
    C = Distancia(A, B)
    angulo = SacarAngulo(A, B, C)
    Tam = int(size / math.cos(math.radians(angulo)))
    print(f"Tamaño de la Casa es {Tam}")
    PJ = (40, 320 - size)
    PJ_Lanzar=(PJ[0]+size, PJ[1]+size+suma)
    PC = (PJ_Lanzar[0] + C, 320 - size)
    Y_Variable = 560
    Y_Variable2 = Y_Variable + 35
    Y_Lanzar = Y_Variable2 + 45

    Sprite_Jugador = Sprite_move(PJ[0], PJ[1], size, size, Computadora.direccion, Computadora.direccion2)
    Computadora.Crear_Trayectoria()
    moving_sprites.add(Sprite_Jugador)
    input_vel = Input(color_passive, 140, Y_Variable, 140, 32, '')
    input_ang = Input(color_passive, 140, Y_Variable2, 140, 32, '')
    button_lanzar = Sprite_move(30, Y_Lanzar, 250, 32, Direcciones_Boton_Lanzar, [])
    button_Salir = Sprite_move(305, Y_Lanzar, 250, 32, Direcciones_Boton_Salir, [])
    moving_sprites.add(button_lanzar)
    moving_sprites.add(button_Salir)
    while paused:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        vel = random.randrange(1, 200)
        angulo = random.randrange(1, 89)
        if (logrado1 == True or contador1 == 0 and Sprite_Jugador.attack_animation==False):
            Computadora.Tratectoria.clear()
            Computadora.Cambiar_Vista(i)
            paused = False

        if (contador1 > 0 and logrado1 == False):
            Sprite_Jugador.attack()
            logrado1 = Lanzamiento_Facil_Principal(Casas, PC, Computadora, PJ_Lanzar, i, A, B, C, Tam, vel, angulo)
            Computadora.Bolsas.Sprite()
            contador1 -= 1

        if (Sprite_Jugador.current_sprite == len(Computadora.direccion) - 2):
            Computadora.Sprite_Trayectoria.Posicion(Computadora.Tratectoria, Computadora.direccion3_AUX)
            Computadora.Sprite_Trayectoria.attack()
        Computadora.draw_Trayectoria(window)
        Computadora.Tratectoria_list.update(0.25)

        draw_grid2(window,PURPLE,C,game_font,Y_Variable,Tam)
        input_vel.draw(window, game_font)
        input_ang.draw(window, game_font)
        moving_sprites.draw(window)
        moving_sprites.update(0.1)
        pygame.display.update()

def Pantalla3_DM(window,Casas,Obstaculos,Jugador1,i):
    """
    Funcion de la Pantalla de la Vista lateral en Dificultad media y sin computadora
    :param window:Pantalla de la vista lateral
    :param Casas:Clase Casa
    :param Jugador1:Clase Jugador
    :param Obstaculos:Clase Obstaculo
    :param i:Indice de la Casa que debe ser abastecida
    """
    paused = True
    game_font = pygame.font.SysFont("Helvetica", 28)
    clock = pygame.time.Clock()
    logrado1 = False
    contador1 = 3
    moving_sprites = pygame.sprite.Group()
    Jugador1.Resultado = Mensaje_Vacio

    Sin_Bolsas = game_font.render(Mensaje_Vacio, True, BLACK)
    Resultado = game_font.render(f"{Jugador1.Resultado}", True, BLACK)

    A, B = Modificacion(Jugador1.Jugador_position, Casas.Casa_position[i])
    C = Distancia(A, B)
    angulo = SacarAngulo(A, B, C)
    Tam = int(size / math.cos(math.radians(angulo)))
    print(f"Tamaño de la Casa es {Tam}")
    PJ = (40, 320 - size)
    PJ_Lanzar=(PJ[0]+size, PJ[1]+size+suma)
    PC = (PJ_Lanzar[0] + C, 320 - size)
    Y_Variable = 560
    Y_Variable2 = Y_Variable + 35
    Y_Lanzar = Y_Variable2 + 45

    Sprite_Jugador = Sprite_move(PJ[0], PJ[1], size, size, Jugador1.direccion, Jugador1.direccion2)
    Jugador1.Crear_Trayectoria()
    moving_sprites.add(Sprite_Jugador)
    input_vel = Input(color_passive, 140, Y_Variable, 140, 32, '')
    input_ang = Input(color_passive, 140, Y_Variable2, 140, 32, '')
    button_lanzar = Sprite_move(30, Y_Lanzar, 250, 32, Direcciones_Boton_Lanzar, [])
    button_Salir = Sprite_move(305, Y_Lanzar, 250, 32, Direcciones_Boton_Salir, [])
    moving_sprites.add(button_lanzar)
    moving_sprites.add(button_Salir)
    while paused:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_position = pygame.mouse.get_pos()
                if (button_lanzar.isOver(mouse_position)):
                    button_lanzar.attack()
                    button_lanzar.active = True
                    input_vel.color = color_passive
                    input_vel.active = False
                    input_ang.color = color_passive
                    input_ang.active = False
                elif(button_Salir.isOver(mouse_position)):
                    if (logrado1 == True or contador1 == 0):
                        button_Salir.attack()
                        Jugador1.Tratectoria.clear()
                        Jugador1.Cambiar_Vista(i)
                        paused = False
                elif (input_vel.isOver(mouse_position)):
                    input_vel.color = color_active
                    input_vel.active = True
                    input_ang.color = color_passive
                    input_ang.active = False
                elif (input_ang.isOver(mouse_position)):
                    input_vel.color = color_passive
                    input_vel.active = False
                    input_ang.color = color_active
                    input_ang.active = True
                else:
                    input_vel.color = color_passive
                    input_vel.active = False
                    input_ang.color = color_passive
                    input_ang.active = False
            if event.type == pygame.KEYDOWN:
                if (input_vel.active == True):
                    if event.key == pygame.K_BACKSPACE:
                        input_vel.text = input_vel.text[:0]
                    else:
                        input_vel.text += event.unicode
                elif (input_ang.active == True):
                    if event.key == pygame.K_BACKSPACE:
                        input_ang.text = input_ang.text[:0]
                    else:
                        input_ang.text += event.unicode
        draw_grid2(window,BLUE, C,game_font,Y_Variable,Tam)

        input_vel.draw(window, game_font)
        input_ang.draw(window, game_font)

        if(button_lanzar.active==True):
            if (es_entero(input_vel.text)and es_entero(input_ang.text)):
                vel = Positivo(int(input_vel.text), 0)
                angulo = Positivo(int(input_ang.text), 0)
                if (contador1 > 0 and logrado1 == False and angulo <90):
                    Resultado = game_font.render(Mensaje_Lanzando, True, BLACK)
                    logrado1 = Lanzamiento_Medio_Principal(Casas, PC, Jugador1, PJ_Lanzar, Obstaculos, i, A, B, C, Tam,vel, angulo)
                    Jugador1.Bolsas.Sprite()
                    contador1 -= 1
                    Sprite_Jugador.attack()
                    button_lanzar.active = False
            else:
                print("Ingrese las Variables corectamente")
                button_lanzar.active = False

        if (Sprite_Jugador.current_sprite == len(Jugador1.direccion) - 2):
            Jugador1.Sprite_Trayectoria.Posicion(Jugador1.Tratectoria, Jugador1.direccion3_AUX)
            Jugador1.Sprite_Trayectoria.attack()
            Jugador1.Sprite_Trayectoria.active = True

        if (Jugador1.Sprite_Trayectoria.active == True and Jugador1.Sprite_Trayectoria.attack_animation == False):
            Resultado = game_font.render(f"{Jugador1.Resultado}", True, BLACK)
            Jugador1.Sprite_Trayectoria.active = False
            if (contador1 == 0):
                Sin_Bolsas = game_font.render(Mensaje_Sin_Bolsas, True, BLACK)

        window.blit(Sin_Bolsas, posicion_sin_Bolsas)
        window.blit(Resultado,posicion_resultado)
        Jugador1.draw_Trayectoria(window)
        Jugador1.Tratectoria_list.update(0.25)
        moving_sprites.draw(window)
        moving_sprites.update(0.25)
        pygame.display.update()

def Pantalla3_DM_Existe(window,Casas,Obstaculos,Computadora,i):
    """
    Funcion de la Pantalla de la Vista lateral en Dificultad media y con computadora
    :param window:Pantalla de la vista lateral
    :param Casas:Clase Casa
    :param Computadora:Clase Jugador
    :param Obstaculos:Clase Obstaculo
    :param i:Indice de la Casa que debe ser abastecida
    """
    paused = True
    game_font = pygame.font.SysFont("Helvetica", 28)
    clock = pygame.time.Clock()
    logrado1 = False
    contador1 = 3
    moving_sprites = pygame.sprite.Group()

    A, B = Modificacion(Computadora.Jugador_position, Casas.Casa_position[i])
    print(f"A y B {A, B}")
    C = Distancia(A, B)
    angulo = SacarAngulo(A, B, C)
    Tam = int(size / math.cos(math.radians(angulo)))
    print(f"Tamaño de la Casa es {Tam}")
    PJ = (40, 320 - size)
    PJ_Lanzar=(PJ[0]+size, PJ[1]+size+suma)
    PC = (PJ_Lanzar[0] + C, 320 - size)
    Y_Variable = 560
    Y_Variable2 = Y_Variable + 35
    Y_Lanzar = Y_Variable2 + 45

    Sprite_Jugador = Sprite_move(PJ[0], PJ[1], size, size, Computadora.direccion, Computadora.direccion2)
    Computadora.Crear_Trayectoria()
    moving_sprites.add(Sprite_Jugador)
    input_vel = Input(color_passive, 140, Y_Variable, 140, 32, '')
    input_ang = Input(color_passive, 140, Y_Variable2, 140, 32, '')
    button_lanzar = Sprite_move(30, Y_Lanzar, 250, 32, Direcciones_Boton_Lanzar, [])
    button_Salir = Sprite_move(305, Y_Lanzar, 250, 32, Direcciones_Boton_Salir, [])
    moving_sprites.add(button_lanzar)
    moving_sprites.add(button_Salir)
    while paused:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        vel = random.randrange(1, 200)
        angulo = random.randrange(1, 89)
        if (logrado1 == True or contador1 == 0 and Sprite_Jugador.attack_animation):
            Computadora.Tratectoria.clear()
            Computadora.Cambiar_Vista(i)
            paused = False
        if (contador1 > 0 and logrado1 == False):
            Sprite_Jugador.attack()
            Lanzamiento_Medio_Principal(Casas, PC, Computadora, PJ_Lanzar, Obstaculos, i, A, B, C, Tam, vel, angulo)
            Computadora.Bolsas.Sprite()
            contador1 -= 1

        if (Sprite_Jugador.current_sprite == len(Computadora.direccion) - 2):
            Computadora.Sprite_Trayectoria.Posicion(Computadora.Tratectoria, Computadora.direccion3_AUX)
            Computadora.Sprite_Trayectoria.attack()
        Computadora.draw_Trayectoria(window)
        Computadora.Tratectoria_list.update(0.25)

        draw_grid2(window,PURPLE,C,game_font,Y_Variable,Tam)
        input_vel.draw(window, game_font)
        input_ang.draw(window, game_font)
        moving_sprites.draw(window)
        moving_sprites.update(0.1)
        pygame.display.update()

def Pantalla4(window,Jugador1,Casas):
    """
    Funcion de la Pantalla de la Vista de estadísticas del juego sin computadora
    :param window:Pantalla de la vista estadísticas del juego
    :param Jugador1:Clase Jugador
    :param Casas:Clase Casa
    """
    paused = True
    clock = pygame.time.Clock()
    game_font = pygame.font.SysFont("Helvetica", 28)
    moving_sprites = pygame.sprite.Group()

    Lista_Sprite = []
    j = 287
    x1=60
    clock = pygame.time.Clock()
    for i in range(Casas.cantidad):
        if (Jugador1.Abastecida[i] == True):
            Sprite_Casa = Sprite_move(x1, j, size4, size4,Direcciones_Casa2,[])
        else:
            Sprite_Casa = Sprite_move(x1, j, size4, size4,Direcciones_Casa,[])
        Lista_Sprite.append(Sprite_Casa)
        j += 30
    for i in range(Casas.cantidad):
        moving_sprites.add(Lista_Sprite[i])

    Sprite_Jugador1=Sprite_move(105, 57,size4,size4,Jugador1.direccion,[])
    moving_sprites.add(Sprite_Jugador1)
    Sprite_Obstaculo=Sprite_move(60,j+5,size4,size4,Direcciones_Obstaculo,[])
    moving_sprites.add(Sprite_Obstaculo)
    button_volver = Sprite_move(300, j + 100, 250, 32, Direcciones_Boton_Volver, [])
    moving_sprites.add(button_volver)

    while paused:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_position = pygame.mouse.get_pos()
                if(button_volver.isOver(mouse_position)):
                    button_volver.attack()
                    paused = False
        draw_grid(window,BLUE4)

        Nombre1 = game_font.render(f"{Jugador1.nombre}", True, BLACK)
        window.blit(Nombre1, (135, 50))
        entregado = game_font.render(f"{Jugador1.entregada} Entregada", True, BLACK)
        window.blit(entregado, (110, 100))
        no_entregado = game_font.render(f"{Jugador1.no_entregada} No Entregadas", True, BLACK)
        window.blit(no_entregado, (110, 130))
        perdido = game_font.render(f"{Jugador1.perdido} Perdidas", True, BLACK)
        window.blit(perdido, (110, 160))
        Titulo2 = game_font.render("Distancia Total de bolsas alejadas de la casa", True, BLACK)
        window.blit(Titulo2, (110, 220))

        i = 280
        for index in range(Casas.cantidad):
            linea = game_font.render(f"{Jugador1.distancias[index]} metros", True, BLACK)
            window.blit(linea, (110, i))
            i += 30
        linea2 = game_font.render(f"{Jugador1.distancia_perdida} metros", True, BLACK)
        window.blit(linea2, (110, i + 5))
        Jugador1.suma_distancias()
        linea3 = game_font.render(f"Distancia Total: {Jugador1.distancia_Total} metros", True, BLACK)
        window.blit(linea3, (65, i + 50))

        Sprite_Jugador1.attack()
        Sprite_Obstaculo.attack()

        moving_sprites.draw(window)
        moving_sprites.update(0.1)

        pygame.display.update()
    moving_sprites.empty()

def Pantalla4_Existe(window,Jugador1,Computadora,Casas):
    """
    Funcion de la Pantalla de la Vista de estadísticas del juego sin computadora
    :param window:Pantalla de la vista de estadísticas del juego
    :param Jugador1:Clase Jugador
    :param Computadora:Clase Jugador
    :param Casas:Clase Casa
    """
    paused = True
    clock = pygame.time.Clock()
    game_font = pygame.font.SysFont("Helvetica", 28)
    moving_sprites = pygame.sprite.Group()

    Lista_Sprite = []
    Lista_Sprite2 = []
    j = 287
    x1 = 60
    x2 = 455
    clock = pygame.time.Clock()
    for i in range(Casas.cantidad):
        if (Jugador1.Abastecida[i] == True):
            Sprite_Casa = Sprite_move(x1, j, size4, size4, Direcciones_Casa2,[])
        else:
            Sprite_Casa = Sprite_move(x1, j, size4, size4,Direcciones_Casa,[])
        Lista_Sprite.append(Sprite_Casa)
        if (Computadora.Abastecida[i] == True):
            Sprite_Casa2 = Sprite_move(x2, j, size4, size4,Direcciones_Casa2,[])
        else:
            Sprite_Casa2 = Sprite_move(x2, j, size4, size4,Direcciones_Casa,[])
        Lista_Sprite2.append(Sprite_Casa2)

        j += 30
    for i in range(Casas.cantidad):
        moving_sprites.add(Lista_Sprite[i])
        moving_sprites.add(Lista_Sprite2[i])

    Sprite_Jugador1 = Sprite_move(105, 57, size4, size4,Jugador1.direccion,[])
    moving_sprites.add(Sprite_Jugador1)
    Sprite_Jugador2 = Sprite_move(500, 57, size4, size4, Computadora.direccion, [])
    moving_sprites.add(Sprite_Jugador2)
    Sprite_Obstaculo = Sprite_move(60, j + 5, size4, size4,Direcciones_Obstaculo,[])
    moving_sprites.add(Sprite_Obstaculo)
    Sprite_Obstaculo2 = Sprite_move(455, j + 5, size4, size4,Direcciones_Obstaculo, [])
    moving_sprites.add(Sprite_Obstaculo2)
    button_volver = Sprite_move(300, j + 100, 250, 32, Direcciones_Boton_Volver, [])
    moving_sprites.add(button_volver)

    while paused:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_position = pygame.mouse.get_pos()
                if (button_volver.isOver(mouse_position)):
                    button_volver.attack()
                    paused = False
        draw_grid(window,BLUE4)

        Nombre1 = game_font.render(f"{Jugador1.nombre}", True, BLACK)
        window.blit(Nombre1, (135, 50))
        entregado = game_font.render(f"{Jugador1.entregada} Entregada", True, BLACK)
        window.blit(entregado, (110, 100))
        no_entregado = game_font.render(f"{Jugador1.no_entregada} No Entregadas", True, BLACK)
        window.blit(no_entregado, (110, 130))
        perdido = game_font.render(f"{Jugador1.perdido} Perdidas", True, BLACK)
        window.blit(perdido, (110, 160))

        Nombre2 = game_font.render(f"{Computadora.nombre}", True, BLACK)
        window.blit(Nombre2, (530, 50))
        entregado = game_font.render(f"{Computadora.entregada} Entregada", True, BLACK)
        window.blit(entregado, (505, 100))
        no_entregado = game_font.render(f"{Computadora.no_entregada} No Entregadas", True, BLACK)
        window.blit(no_entregado, (505, 130))
        perdido = game_font.render(f"{Computadora.perdido} Perdidas", True, BLACK)
        window.blit(perdido, (505, 160))

        Titulo2 = game_font.render("Distancia Total de bolsas alejadas de la casa", True, BLACK)
        window.blit(Titulo2, (110, 220))

        i = 280
        for index in range(Casas.cantidad):
            linea = game_font.render(f"{Jugador1.distancias[index]} metros", True, BLACK)
            window.blit(linea, (110, i))
            linea2 = game_font.render(f"{Computadora.distancias[index]} metros", True, BLACK)
            window.blit(linea2, (505, i))
            i += 30

        linea3 = game_font.render(f"{Jugador1.distancia_perdida} metros", True, BLACK)
        window.blit(linea3, (110, i + 5))
        Jugador1.suma_distancias()
        linea4 = game_font.render(f"Distancia Total: {Jugador1.distancia_Total} metros", True, BLACK)
        window.blit(linea4, (65, i + 50))

        linea3 = game_font.render(f"{Computadora.distancia_perdida} metros", True, BLACK)
        window.blit(linea3, (505, i + 5))
        Computadora.suma_distancias()
        linea4 = game_font.render(f"Distancia Total: {Computadora.distancia_Total} metros", True, BLACK)
        window.blit(linea4, (460, i + 50))

        Sprite_Jugador1.attack()
        Sprite_Jugador2.attack()
        Sprite_Obstaculo.attack()
        Sprite_Obstaculo2.attack()

        moving_sprites.draw(window)
        moving_sprites.update(0.1)

        pygame.display.update()

    moving_sprites.empty()
"""
Funciones de Lanzamiento
"""
def Lanzamiento_Facil_Principal(Casas,PC,Jugador,PJ_Lanzar,i,A,B,C,Tam,vel,angulo):
    """
    Funcion Principal del Lanzamiento en Dificultad Facil
    :param Casas:Clase Casa
    :param PC:Posicion de la Casa en Visitadas Lateral
    :param Jugador:Clase Jugador
    :param PJ_Lanzar:Posicion del Jugador al momento de lanzar en Visitadas Lateral
    :param i:indice de la Casa que deber ser abastecida
    :param C:Distancia entre la posicion superior del Jugador y la Casa que deber ser abastecida
    :param vel:Valor de la Velocidad
    :param angulo:Valor del Angulo
    :return:Retorna True si la Bolsa cayo en la Casa y False si no cayo en la Casa
    """
    Jugador.Tratectoria.clear()
    tiempo = 0
    position = (40, 320)
    Trayectoria=[]
    while (Dentro_Pantalla(position) and Dentro_Casa(position,PC,Tam)==False):
        position = Lanzamiento_Facil2(PJ_Lanzar, vel, math.radians(angulo), tiempo)
        Trayectoria.append(position)
        tiempo += 0.1
    cantidad_p = len(Trayectoria)
    if (cantidad_p > 0):
        if (position[0] <= 900 and position[0] >= 0 and position[1] <= 900):
            if (Dentro_Casa(position,PC,Tam)):
                print("Cayo en la Casa")
                referencia = Trayectoria[cantidad_p - 1]
                C_prima = Pitagoras(Distancia([PJ_Lanzar[0],PJ_Lanzar[1]-suma], referencia), 320 - referencia[1])
                Diferencia = Positivo(C, C_prima)
                position_nueva = Calcular_Punto(A, B, C, C_prima)
                Jugador.Convertir_Trayectoria(Trayectoria,referencia,cantidad_p)
                Jugador.entregado(i)
                Jugador.agregar(position_nueva)
                return True
            else:
                referencia = Trayectoria[cantidad_p - 2]
                C_prima = Pitagoras(Distancia([PJ_Lanzar[0],PJ_Lanzar[1]-suma],referencia),320-referencia[1])
                Diferencia=Positivo(C,C_prima)

                position_nueva = Calcular_Punto(A,B,C,C_prima)
                Jugador.Convertir_Trayectoria(Trayectoria, referencia, cantidad_p - 1)
                return Lanzamiento_Facil(Jugador, position_nueva, i, B)
        else:
            Jugador.Convertir_Trayectoria(Trayectoria, Trayectoria[cantidad_p-1], cantidad_p)
            Jugador.Resultado=Mensaje_Fuera_Superior
            print("Fuera de Rango Lateral")
            return False
    else:
        return False

def Lanzamiento_Medio_Principal(Casas,PC,Jugador,PJ_Lanzar,Obstaculos,i,A,B,C,Tam,vel,angulo):
    """
    Funcion Principal del Lanzamiento en Dificultad Media
    :param Casas:Clase Casa
    :param PC:Posicion de la Casa en Visitadas Lateral
    :param Jugador:Clase Jugador
    :param PJ_Lanzar:Posicion del Jugador en Visitadas Lateral
    :param Obstaculos:Clase Obstaculo
    :param i:indice de la Casa que deber ser abastecida
    :param C:Distancia entre la posicion superior del Jugador y la Casa que deber ser abastecida
    :param vel:Valor de la Velocidad
    :param angulo:Valor del Angulo
    :return:Retorna True si la Bolsa cayo en la Casa y False si no cayo en la Casa
    """
    tiempo = 0
    Jugador.Tratectoria.clear()
    position = (40, 320)
    Trayectoria=[]
    while (Dentro_Pantalla(position) and Dentro_Casa(position,PC,Tam)==False):
        position = Lanzamiento_Medio2(PJ_Lanzar, vel, math.radians(angulo), tiempo)
        Trayectoria.append(position)
        tiempo += 0.2
    cantidad_p = len(Trayectoria)
    if (cantidad_p > 0):
        if (position[0] <= 900 and position[0] >= 0 and position[1] <= 900):
            print("Cayo al suelo")
            if (Dentro_Casa(position,PC,Tam)):
                referencia = Trayectoria[cantidad_p - 1]
                C_prima = Pitagoras(Distancia([PJ_Lanzar[0],PJ_Lanzar[1]-suma], referencia), 320 - referencia[1])
                position_nueva = Calcular_Punto(A, B, C, C_prima)
                Jugador.Convertir_Trayectoria(Trayectoria, referencia, cantidad_p)
                Jugador.entregado(i)
                Jugador.agregar(position_nueva)
                return True
            else:
                referencia = Trayectoria[cantidad_p - 2]
                C_prima = Pitagoras(Distancia([PJ_Lanzar[0],PJ_Lanzar[1]-suma], referencia), 320 - referencia[1])
                position_nueva = Calcular_Punto(A, B, C, C_prima)
                Jugador.Convertir_Trayectoria(Trayectoria, referencia, cantidad_p - 1)
                return Lanzamiento_Medio(Obstaculos, Jugador, position_nueva, i, B)
        else:
            Jugador.Convertir_Trayectoria(Trayectoria, Trayectoria[cantidad_p - 2], cantidad_p - 1)
            Jugador.Resultado = Mensaje_Fuera_Lateral
            print("Fuera de Rango Lateral")
            return False
    else:
        return False

def Lanzamiento_Facil(Jugador,position,i,B):
    """
    Funcion que determina si la Bolsa esta dentro de la pantalla superior y la marca como no entregada.
    :param Jugador:Clase Jugador
    :param position:Posicion de la Bolsa
    :param i:Indice de la Casa que debe ser abastecida
    :param B:Posicion de la Casa que debe ser abastecida
    :return:False
    """
    if(position[0] in range(5, 895) and position[1] in range(5, 595)):
        print("Bolsado no Entregada")
        distancia=Distancia(position,B)
        Jugador.agregar(position)
        Jugador.no_entregado(distancia,i)
        return False
    else:
        Jugador.Resultado=Mensaje_Fuera_Superior
        print("Lanzada fuera de rango")
        return False

def Lanzamiento_Medio(Obstaculos,Jugador,position,i,B):
    """
    Funcion que determina si la Bolsa esta dentro de la pantalla superior y marca si cayo en obstaculo o no.
    :param Obstaculos:Clase Obstaculo
    :param Jugador:Clase Jugador
    :param position:Posicion de la Bolsa
    :param i:Indice de la Casa que debe ser abastecida
    :param B:Posicion de la Casa que debe ser abastecida
    :return:Retorna False
    """
    if (position[0] in range(5, 895) and position[1] in range(5, 595)):
        if (Obstaculos.isOver(position)):
            print("Bolsado perdida")
            Jugador.perdida()
            Jugador.agregar(position)
            return False

        distancia = Distancia(position, B)
        Jugador.agregar(position)
        Jugador.no_entregado(distancia, i)
        return False

    else:
        Jugador.Resultado = Mensaje_Fuera_Superior
        print("Lanzada fuera de rango")
        return False

def Lanzamiento_Medio2(PJ_Lanzar,velocidad,angulo,tiempo):
    """
    Funcion que retorna la posicion de la Bolsa en Dificultad Media
    :param PJ_Lanzar:Posicion del Jugador al momento de lanzar en Visitadas Lateral
    :param velocidad:Velocidad de la Bolsa lanzada
    :param angulo:Angulo del lanzamiento
    :param tiempo:Valor del tiempo
    :return:Posicion de la Bolsa
    """
    Vx=velocidad*math.cos(angulo)
    Vy=velocidad*math.sin(angulo)
    masa=2
    gravedad = 9.81
    c=1

    exp = (c / masa) * -tiempo
    e = 1 - (math.pow(math.e, exp))
    Ry = ((masa * gravedad) / c) + Vy

    X = (PJ_Lanzar[0]) + ((masa / c) * Vx * e)
    Y = (PJ_Lanzar[1]) + ((masa / c) * Ry * e) - (((masa * gravedad) / c) * tiempo)

    position = (int(X), int(Y))
    return position

def Lanzamiento_Facil2(PJ_Lanzar,velocidad,angulo,tiempo):
    """
    Funcion que retorna la posicion de la Bolsa en Dificultad Media
    :param PJ_Lanzar:Posicion del Jugador al momento de lanzar en Visitadas Lateral
    :param velocidad:Velocidad de la Bolsa lanzada
    :param angulo:Angulo del lanzamiento
    :param tiempo:Valor del tiempo
    :return:Posicion de la Bolsa
    """
    Vx=velocidad*(math.cos(angulo))
    Vy=velocidad*(math.sin(angulo))
    gravedad = 9.81

    X=(PJ_Lanzar[0]) + (Vx * tiempo)
    Y=(PJ_Lanzar[1]) + (Vy * tiempo) - ((gravedad/2)* (math.pow(tiempo,2)))
    position = (int(X), int(Y))
    return position

"""
Funciones de Dibujo
"""
def draw_grid(window,color):
    """
    Funcion que le da color a la Pantalla
    :param window:Pantalla de la vista de configuracion o lateral o estadísticas del juego
    :param color:Color de la Pantalla
    """
    window = pygame.display.set_mode((WIDTH,HEIGTH))
    window.fill(color)

def draw_grid2(window,color2,distancia,game_font,Y_Base,Tam):
    """
    Funcion que impreme un Jugador y la Casa que va a ser abastecida de la Pantalla de la vista lateral
    :param window:Pantalla de la vista lateral
    :param color2:Color del Jugador
    :param distancia:Distancia entre la Jugador y la Casa que va a ser abastecida
    :param game_font:Fuente para los texto
    :param Y_Base:Distancia Inicial para los input
    """
    window = pygame.display.set_mode((WIDTH,HEIGTH))
    window.fill(GREEN)
    pygame.draw.rect(window,(223, 236, 255), [0, 550, WIDTH, 150])
    pygame.draw.line(window, BLACK, (0, 550), (WIDTH, 550))

    Velocidad = game_font.render("Velocidad:", True, BLACK)
    window.blit(Velocidad, (30, Y_Base+5))

    Angulo = game_font.render("Angulo:", True, BLACK)
    window.blit(Angulo, (30, Y_Base+40))

    pygame.draw.rect(window, LIGHT_BLUE, [0, 0, WIDTH, 320])
    pygame.draw.rect(window, RED, [40+size+distancia,320-size, Tam, size])

"""
Funciones Logicas
"""
def Dentro_Pantalla(position):
    """
    Funcion que detecto si la position esta dentro de la Pantalla
    :param position:Posicion del punto de la Trayectoria
    :return:Retorna True si esta dentro de la Pantalla, en caso contrario retorna un False
    """
    if ((position[0] >= 0 and position[0] <= 900) and (position[1] <= 900 and position[1] >= 320)):
        return True
    else:
        return False

def Dentro_Casa(position,PC,Tam):
    """
    Funcion que detecto si la position esta dentro de la Casa
    :param position:Posicion del punto de la Trayectoria
    :return:Retorna True si esta dentro de la Casa, en caso contrario retorna un False
    """
    if((position[0] >= PC[0] and position[0] <= PC[0] + Tam) and (position[1] >= 320 and position[1] <= 320+size)):
        return True
    else:
        return False

def Distancia(a,b):
    """
    Funcion que retorna la distancia entre dos posiciones
    :param a:Posicion del punto a
    :param b:Posicion del punto b
    :return:Distancia entre las dos posiciones
    """
    c=int(math.sqrt(math.pow((a[0]-b[0]), 2) + math.pow((a[1]-b[1]),2)))
    return c

def Calcular_Punto(a,b,C,C_prima):
    """
    Funcion que convierte una posicion de la pantalla lateral a la de la pantalla superior
    :param a:Posicion del Jugador
    :param b:Posicion de la Casa que debe ser abastecida
    :param C_prima: Distancia entre el Posicion jugador y la Posicion de la Bolsa
    :return:
    """
    if (C==0):
        return b
    if(C_prima==0):
        return a

    if (a[0] < b[0] and a[1] > b[1]):
        c = (min(a[0], b[0]), min(a[1], b[1]))
        e = (max(a[0], b[0]), max(a[1], b[1]))
        A = Positivo(a[1], b[1])
        B = Positivo(a[0], b[0])
        A_prima = int((A * C_prima) / C)
        B_prima = int((B * C_prima) / C)
        if (C_prima < C):
            return (c[0] + B_prima, e[1] - A_prima)
        else:
            return (e[0] + (B_prima - B), c[1] - (A_prima - A))

    elif (a[0] > b[0] and a[1] < b[1]):
        c = (min(a[0], b[0]), min(a[1], b[1]))
        e = (max(a[0], b[0]), max(a[1], b[1]))
        A = Positivo(a[1], b[1])
        B = Positivo(a[0], b[0])
        A_prima = int((A * C_prima) / C)
        B_prima = int((B * C_prima) / C)
        if (C_prima < C):
            return (e[0] - B_prima, c[1] + A_prima)
        else:
            return (c[0] - (B_prima - B), e[1] + (A_prima - A))

    elif (a[0] < b[0] and a[1] < b[1]):
        c = (max(a[0], b[0]), min(a[1], b[1]))
        e = (min(a[0], b[0]), max(a[1], b[1]))
        A = Positivo(a[1], b[1])
        B = Positivo(a[0], b[0])
        A_prima = int((A * C_prima) / C)
        B_prima = int((B * C_prima) / C)
        if (C_prima < C):
            return (e[0] + B_prima, c[1] + A_prima)
        else:
            return (c[0] + (B_prima - B), e[1] + (A_prima - A))
    elif (a[0] > b[0] and a[1] > b[1]):
        c = (max(a[0], b[0]), min(a[1], b[1]))
        e = (min(a[0], b[0]), max(a[1], b[1]))
        A = Positivo(a[1], b[1])
        B = Positivo(a[0], b[0])
        A_prima = int((A * C_prima) / C)
        B_prima = int((B * C_prima) / C)
        if (C_prima < C):
            return (c[0] - B_prima, e[1] - A_prima)
        else:
            return (e[0] - (B_prima - B), c[1] - (A_prima - A))
    else:
        if(a[0]==b[0] and a[1]<b[1]):
            return (a[0],a[1]+C_prima)
        elif(a[0]==b[0] and a[1]>b[1]):
            return (a[0], a[1]-C_prima)
        elif(a[0]<b[0] and a[1]==b[1]):
            return (a[0]+C_prima, a[1])
        elif(a[0]>b[0] and a[1]==b[1]):
            return (a[0]-C_prima, a[1])

def Pitagoras(H,C1):
    """
    Funcion que devuelve un Cateto mas 20
    :param H:Valor de la Hipotenusa
    :param C1:Valor de un Cateto
    :return:Retorna el cateto si es mayor a 0, en caso contrario retorna la hipotenusa
    """
    if(C1>0):
        C2=int(math.sqrt(math.pow(H, 2) + math.pow(C1,2)))
        return C2
    else:
        return H

def es_entero(a):
    """
    Funcion que detecto si la variable es un Entero
    :param a:Valor de la Variable
    :return:Retorna True si es un Entero, en caso contrario retorna un False
    """
    try:
        int(a)
        return True
    except:
        return False

def Positivo(a,b):
    """
    Funcion que retorna las resta entre a y b positivo
    :param a:Valor de la Posicion a
    :param b:Valor de la Posicion b
    :return:Retorna la resta de a y b,asegurando que este ultimo sea positivo
    """
    valor=a-b
    if(valor < 0):
        return (valor*-1)
    return valor

def Modificacion(a,b):
    """
    Funcion que retorna las posiciones modificaddas del Jugador y la Casa
    :param a:Posicion del Jugador
    :param b:Posicion de la Casa
    :return:Retorna a y b modificadas
    """
    if (a[0] <b[0] and a[1] > b[1]):
        b = (b[0], b[1] + size)
        a = (a[0] + size, a[1])
        return a, b

    elif (a[0] > b[0] and a[1] < b[1]):
        b = (b[0]+ size, b[1])
        a = (a[0] , a[1]+ size)
        return a,b

    elif (a[0] < b[0] and a[1] < b[1]):
        a = (a[0] + size, a[1] + size)
        return a,b
    elif (a[0] > b[0] and a[1] > b[1]):
        b=(b[0]+size,b[1]+size)
        return a,b

    else:
        if (a[0] == b[0] and a[1] < b[1]):
            a = (a[0] + int(size/2), a[1] + size)
            b = (b[0] + int(size/2), b[1])
            return a, b
        elif (a[0] == b[0] and a[1] > b[1]):
            a = (a[0] + int(size/2), a[1])
            b = (b[0] + int(size/2), b[1]+size)
            return a, b
        elif (a[0] < b[0] and a[1] == b[1]):
            a = (a[0] + size, a[1]+int(size/2))
            b = (b[0], b[1] + int(size/2))
            return a, b
        elif (a[0] > b[0] and a[1] == b[1]):
            a = (a[0], a[1]+int(size/2))
            b = (b[0] + size, b[1]+int(size/2))
            return a, b
        else:
            return a,b

def SacarAngulo(a,b,C):
    """
    Funcion que retorna el angulo formado entre la posicion de la Casa que debe ser abastecida y el Jugador
    :param a:Posicion del Jugador
    :param b:Posicion de la Casa
    :param C:Distancia entre la Jugador y la Casa
    :return:Retorna el angulo
    """
    if(C==0):
        return 0
    if (a[0] < b[0] and a[1] > b[1]):
        e = (max(a[0], b[0]), max(a[1], b[1]))
        lado=Distancia(e,a)
        angulo = int(math.degrees(math.acos(lado / C)))
        print(f"Angulo es {angulo}")
        if (angulo >= 45):
            return 90 - angulo
        return angulo

    elif (a[0] > b[0] and a[1] < b[1]):
        d = (min(a[0], b[0]), min(a[1], b[1]))
        lado = Distancia(d, d)
        angulo = int(math.degrees(math.acos(lado / C)))
        print(f"Angulo es {angulo}")
        if (angulo >= 45):
            return 90 - angulo
        return angulo

    elif (a[0] < b[0] and a[1] < b[1]):
        d = (max(a[0], b[0]), min(a[1], b[1]))
        lado = Distancia(d, a)
        angulo = int(math.degrees(math.acos(lado / C)))
        print(f"Angulo es {angulo}")
        if (angulo >= 45):
            return 90 - angulo
        return angulo
    elif (a[0] > b[0] and a[1] > b[1]):
        e = (min(a[0], b[0]), max(a[1], b[1]))
        lado = Distancia(e, a)
        angulo = int(math.degrees(math.acos(lado / C)))
        print(f"Angulo es {angulo}")
        if (angulo >= 45):
            return 90 - angulo
        return angulo

    else:
        if (a[0] == b[0] and a[1] < b[1]):
            return 0
        elif (a[0] == b[0] and a[1] > b[1]):
            return 0
        elif (a[0] < b[0] and a[1] == b[1]):
            return 0
        elif (a[0] > b[0] and a[1] == b[1]):
            return 0
"""
Funciones Pydoc
"""
def Pydoc():
    '''
    Funcion hecha exclusivamente para crear el PyDoc correctamente,para iniciar con el juego use la funcion 'Pantalla1' para iniciar el Juego
    '''
    print("Ha creado un Pydoc correctamente")
    print("Ahora Inicie con 'Pantalla 1' para iniciar el Juego")


Pantalla1()
#Pydoc()