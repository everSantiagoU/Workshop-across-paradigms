#declaracion de tipos de datos
from enum import Enum
x = 1 # entero
y = 3.1416 #decimal
z = True #booleano
w = "Santiago" # caracter
arreglo = ["sara","santiago","miguel","simon","pedro"]
#funcion enum
class Estacion(Enum):
    PRIMAVERA = 1
    VERANO = 2
    OTOÑO = 3
#declarcion de la clase
class Bicicleta:
    def __init__(self, color, tipo):
        self.color = color
        self.tipo = tipo
#declaracion del diccionario
edades = {
    "Juan": 30,
    "María": 25,
    "Pedro": 35
}

