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
}