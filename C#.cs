//declaracion de variables
using System;
using System.Collections.Generic;

int x = 128;
float y = 3.1416;
string saludon = "hola";
bool estado = true;
string Arr[5] = {"sara","santiago","miguel","simon","pedro"};
//declaracion del enum
public enum Mes {
    ENERO,
    FEBRERO,
    MARZO
}
//declaracion de la clase
public class Carro {
    public string marca;
    public int año;

}

//declaracion del diccionario
Dictionary<string, string> capitales = new Dictionary<string, string>();
capitales.Add("Colombia", "Bogota");
capitales.Add("Peru", "Lima");
capitales.Add("Chile", "Santiago");

//lista enlazada
//clase para el nodo
public class Nodo {
    public int dato;
    public Nodo siguiente;

    public Nodo(int dato) {
        this.dato = dato;
        siguiente = null;
    }
}
//clase de la lista enlazada
public class ListaEnlazada {
    public Nodo cabeza; // Referencia al priner nodo

    // Funcion para agregar un nodo al inicio
    public void AgregarAlInicio(int nuevoDato) {
        Nodo nuevoNodo = new Nodo(nuevoDato);
        nuevoNodo.siguiente = cabeza;
        cabeza = nuevoNodo;
    }

    // Funcion para imprimir la lista
    public void ImprimirLista() {
        Nodo nodoActual = cabeza;
        while (nodoActual != null) {
            Console.Write(nodoActual.dato + " -> ");
            nodoActual = nodoActual.siguiente;
        }
        Console.WriteLine("NULL");
    }
}

//arbol binario
//clase para el nodo
public class NodoArbol {
    public int dato;
    public NodoArbol izquierda;
    public NodoArbol derecha;

    public NodoArbol(int dato) {
        this.dato = dato;
        izquierda = null;
        derecha = null;
    }
}

//clase para el arbol binario
public class ArbolBinario {
    NodoArbol raiz;

    public ArbolBinario() {
        raiz = null;
    }

    //metodo para insertar
    public void Insertar(int dato) {
        raiz = InsertarRecursivo(raiz, dato);
    }

    private NodoArbol InsertarRecursivo(NodoArbol raiz, int dato) {
        if (raiz == null) {
            return new NodoArbol(dato);
        }
        if (dato < raiz.dato) {
            raiz.izquierda = InsertarRecursivo(raiz.izquierda, dato);
        } else if (dato > raiz.dato) {
            raiz.derecha = InsertarRecursivo(raiz.derecha, dato);
        }
        return raiz;
    }

    //metodo para el orden transversal del arbol binario
    public void Inorden() {
        InordenRecursivo(raiz);
    }

    private void InordenRecursivo(NodoArbol raiz) {
        if (raiz != null) {
            InordenRecursivo(raiz.izquierda);
            Console.Write(raiz.dato + " ");
            InordenRecursivo(raiz.derecha);
        }
    }
}



