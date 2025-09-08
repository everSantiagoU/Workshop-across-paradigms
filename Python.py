#declaracion de tipos de datos
from enum import Enum
x = 1 # entero
y = 3.1416 #decimal
z = True #booleano
w = "Santiago" # caracter
arreglo = ["sara","santiago","miguel","simon","pedro"]

class Estacion(Enum):
    PRIMAVERA = 1
    VERANO = 2
    OTOÑO = 3

class Bicicleta:
    def __init__(self, color, tipo):
        self.color = color
        self.tipo = tipo

