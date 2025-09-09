public class paradigmas {

    public static void main(String[] args) {
        //declaracion de variables
        int x = 12;
        float y = 3.1416;
        String w = "hola";
        boolean = True;
        String arr[5] = {"sara","santiago","miguel","simon","pedro"};
        //declaracion del enum
        public enum DiaSemana {
            LUNES,
            MARTES,
            MIERCOLES
        }
        //declaracion del clase
        public class Animal{
            String especie;
            int edad;
            double id;

        }

        //declaracion del diccionario
        Map<String, Integer> edades = new HashMap<>();
        edades.put("juan", 30);
        edades.put("maría", 25);
        edades.put("pedro", 35);

        //lista enlazada
        // Clase para el nodo
        class Nodo {
            int dato;
            Nodo siguiente;

            // Constructor del nodo
            Nodo(int dato) {
                this.dato = dato;
                this.siguiente = null;
            }
        }

        // Clase para la lista enlazada
        class ListaEnlazada {
            Nodo cabeza; // primer nodo de la lista enlazada
            // Funcion para agregar un nodo al inicio
            public void agregarAlInicio(int nuevoDato) {
                Nodo nuevoNodo = new Nodo(nuevoDato);
                nuevoNodo.siguiente = cabeza;
                cabeza = nuevoNodo;
        }
        // Función para imprimir la lista
        public void imprimirLista() {
            Nodo nodoActual = cabeza;
            while (nodoActual != null) {
                System.out.print(nodoActual.dato + " -> ");
                nodoActual = nodoActual.siguiente;
            }
            System.out.println("NULL");
        }
        }

    }

        //clase para el nodo
        class NodoArbol {
            int dato;
            NodoArbol izquierda;
            NodoArbol derecha;

        public NodoArbol(int dato) {
            this.dato = dato;
            izquierda = null;
            derecha = null;
        }
        }

        //clase para el arbol binario
        class ArbolBinario {
            NodoArbol raiz;

            public ArbolBinario() {
                raiz = null;
            }

        //metodo para insertar
        public void insertar(int dato) {
            raiz = insertarRecursivo(raiz, dato);
        }

        private NodoArbol insertarRecursivo(NodoArbol raiz, int dato) {
            if (raiz == null) {
                return new NodoArbol(dato);
            }
            if (dato < raiz.dato) {
                raiz.izquierda = insertarRecursivo(raiz.izquierda, dato);
            } else if (dato > raiz.dato) {
                raiz.derecha = insertarRecursivo(raiz.derecha, dato);
            }
            return raiz;
        }

        // funcion para el orden transversal del arbol
        public void inorden() {
            inordenRecursivo(raiz);
        }

        private void inordenRecursivo(NodoArbol raiz) {
            if (raiz != null) {
                inordenRecursivo(raiz.izquierda);
                System.out.print(raiz.dato + " ");
                inordenRecursivo(raiz.derecha);
            }
        }
    }

}