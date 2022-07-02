#! /usr/bin/env python
import os, random, sys, math

import pygame
from pygame.locals import *
from configuracion import *
from extras import *
from funcionesSeparador import *

from funcionesVACIAS import *

#Funcion principal
def main():
        #Centrar la ventana y despues inicializar pygame
        os.environ["SDL_VIDEO_CENTERED"] = "1"
        pygame.init()
        #pygame.mixer.init()

        #Preparar la ventana

        screen = pygame.display.set_mode((ANCHO, ALTO))
        pygame.display.set_caption('Los 8 escalones')

        #tiempo total del juego
        gameClock = pygame.time.Clock()
        totaltime = 0
        segundos = TIEMPO_MAX
        fps = FPS_inicial

        puntos = 0
        palabra = ""
        lemarioEnSilabas=[]
        listaPalabrasDiccionario=[]
        palabra_anterior= ""

        archivo= open("lemario.txt","r")

        #lectura del diccionario
        lectura(archivo, listaPalabrasDiccionario)

        #elige una al azar
        palabraEnPantalla=nuevaPalabra(listaPalabrasDiccionario)

        dibujar(screen, palabra, palabraEnPantalla, puntos, segundos, palabra_anterior)

        while segundos > fps/1000:
        # 1 frame cada 1/fps segundos
            gameClock.tick(fps)
            totaltime += gameClock.get_time()

            if True:
            	fps = 3

            #Buscar la tecla apretada del modulo de eventos de pygame
            for e in pygame.event.get():

                #QUIT es apretar la X en la ventana
                if e.type == QUIT:
                    pygame.quit()
                    return()

                #Ver si fue apretada alguna tecla
                if e.type == KEYDOWN:
                    letra = dameLetraApretada(e.key)
                    palabra += letra #es la palabra que escribe el usuario
                    if e.key == K_BACKSPACE:
                        palabra = palabra[0:len(palabra)-1]
                    if e.key == K_RETURN:
                        #pasa la palabra a silabas
                        palabraEnPantallaEnSilabas=palabraTOsilaba(palabraEnPantalla)
                        if esCorrecta(palabraEnPantallaEnSilabas, palabra):
                            puntos += puntaje(palabraEnPantalla)

                            pygame.mixer.music.load(SONIDO_VERDADERO)
                            pygame.mixer.music.play(1)                                     #Me reproduce este audio cuando es correcto
                            pygame.mixer.music.set_volume(0.3)

                        else:
                            puntos-=1
                            
                            pygame.mixer.music.load(SONIDO_FALSO)
                            pygame.mixer.music.play(1)                                      #Me reproduce este audio cuando es incorrecto
                            pygame.mixer.music.set_volume(0.3)

                        #Almaceno la palabra anterior separada en silabas para luego mostrarla en pantalla
                        palabra_anterior= palabraEnPantallaEnSilabas
                        
                        #elige una al azar
                        palabraEnPantalla=nuevaPalabra(listaPalabrasDiccionario)

                        palabra = ""

            segundos = TIEMPO_MAX - pygame.time.get_ticks()/1000

            #Limpiar pantalla anterior
            screen.fill(COLOR_FONDO)

            #Icono del juego
            icono= pygame.image.load(IMAGEN_ICONO)
            pygame.display.set_icon(icono)

            #Fondo del juego
            fondo_juego = pygame.image.load(IMAGEN_FONDO).convert()
            screen.blit(fondo_juego, (0 ,0))

            #Dibujar de nuevo todo
            dibujar(screen, palabra, palabraEnPantalla, puntos,segundos, palabra_anterior)

            pygame.display.flip()


        while 1:
            #Esperar el QUIT del usuario
            for e in pygame.event.get():
                if (e.type == QUIT):
                    pygame.quit()
                    return
        
        
        archivo.close()

#Programa Principal ejecuta Main
if __name__ == "__main__":
    main()
