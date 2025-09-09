#include <stdio.h>
#include <string.h>
int main() {
    int x = 100;
    float y = 3.1416;
    bool w = true;
    char z = "a";

    //agregamos nodos a la lista enlazada
    struct Nodo* cabeza = NULL;
    agregar_al_inicio(&cabeza, 10);
    agregar_al_inicio(&cabeza, 20);
    agregar_al_inicio(&cabeza, 30);

    //declaracion del enum
    enum Color {
        ROJO,
        VERDE,
        AZUL
    };
    //declaracion de la clase
    struct Libro {
        char titulo[50];
        char autor[50];
        int paginas;
    };

    //declaracion del diccionario
    char* claves[] = {"Juan", "Maria", "Pedro"};
    int valores[] = {30, 25, 35};
    int tamano = 3;

    //linked list
    //funcion para los nodos
    struct Nodo {
    int dato;
    struct Nodo* siguiente;
    };
    //funcion para agregar nodo al comienzo de la lista enlazada
    void agregar_al_inicio(struct Nodo** cabeza_ref, int nuevo_dato) {
    // creamos un nuevo nodo
    struct Nodo* nuevo_nodo = (struct Nodo*)malloc(sizeof(struct Nodo));
    nuevo_nodo->dato = nuevo_dato;
    //enlazamos el nuevo nodo con el nodo de la cabeza
    nuevo_nodo->siguiente = (*cabeza_ref); 
    (*cabeza_ref) = nuevo_nodo;
    }

    //funcion para imprimir la lista
    void imprimir_lista(struct Nodo* nodo) {
    while (nodo != NULL) {
        printf("%d -> ", nodo->dato);
        nodo = nodo->siguiente;
    }
    printf("\n");
    }





}