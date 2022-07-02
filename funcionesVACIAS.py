from principal import *
from configuracion import *
import random
import funcionesSeparador as fs
import funcion_cambio_espacio as fce



def lectura(archivo, salida):
    seleccion= archivo.readline()

    while seleccion != "":                     #Defino que Mientras hayan palabras se ejecute el while 
        salida.append(seleccion[:-1])          #El -1 para que no me tome el enter (ya que tambien es un caracter)
        seleccion = archivo.readline()         #Para leer la siguiente palabra

def nuevaPalabra(lista):
    return random.choice(lista)

def palabraTOsilaba(palabra):
    return fs.separador(palabra)
    
def esCorrecta(palabraEnSilabasEnPantalla, palabra):
    if fce.espacioToGuion(palabra) == palabraEnSilabasEnPantalla:
        return True
    return False

def puntaje(palabra):
    if len(palabra) >= 9:
        return PUNTAJE_MAXIMO
    elif len(palabra) > 5:
        return PUNTAJE_MEDIO
    return PUNTAJE_MINIMO

