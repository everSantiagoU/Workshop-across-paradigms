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

#arbol binario
#clase para el nodo
class NodoArbol:
    def __init__(self, dato):
        self.dato = dato
        self.izquierda = None
        self.derecha = None

# clase para el arbol binario
class ArbolBinario:
    def __init__(self):
        self.raiz = None

    # funcion para insertar
    def insertar(self, dato):
        self.raiz = self._insertar_recursivo(self.raiz, dato)

    def _insertar_recursivo(self, raiz, dato):
        if raiz is None:
            return NodoArbol(dato)
        if dato < raiz.dato:
            raiz.izquierda = self._insertar_recursivo(raiz.izquierda, dato)
        elif dato > raiz.dato:
            raiz.derecha = self._insertar_recursivo(raiz.derecha, dato)
        return raiz

    #funciuon para el orden transversal del arbol binario
    def inorden(self):
        self._inorden_recursivo(self.raiz)

    def _inorden_recursivo(self, raiz):
        if raiz is not None:
            self._inorden_recursivo(raiz.izquierda)
            print(raiz.dato, end=" ")
            self._inorden_recursivo(raiz.derecha)

