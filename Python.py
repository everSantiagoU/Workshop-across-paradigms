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

#lista enlazada
# clase para el nodo
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None  # cabeza de la lista

# clase para la lista enlazada
class ListaEnlazada:
    def __init__(self):
        self.cabeza = None #referencia a la cabeza

    # Funcion para agregar un nodo al inicio de la lista
    def agregar_al_inicio(self, nuevo_dato):
        nuevo_nodo = Nodo(nuevo_dato)
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo

    # Funcion para imprimir la lista enlazad
    def imprimir_lista(self):
        nodo_actual = self.cabeza
        while nodo_actual is not None:
            print(nodo_actual.dato, end=" -> ")
            nodo_actual = nodo_actual.siguiente
        print("None")


