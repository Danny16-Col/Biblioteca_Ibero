from Models.NodoLibro import NodoLibro

# clase arbol binario de busqueda de libros
class ArbolLibros:

    # arbol vacio sin raiz
    def __init__(self):
        self.raiz = None

    # metodo de insercion #

    # se inserta un nuevo libro en el arbol respetando el orden del ABB o en ingles BST
    def insertar(self, libro):
        if self.raiz is None:  # si el arbol esta vacio, el libro se convierte en la raiz
            self.raiz = NodoLibro(libro)
            return True

        return self._insertar_rec(self.raiz, libro) # si ya existe raiz, se inserta de forma recursiva

    # metodo auxiliar recursivo que ubica la posicion correcta del libro en el arbol
    def _insertar_rec(self, nodo, libro):
        if libro.getId() == nodo.libro.getId():
            return False                              #  si el ID ya existe no se permiten duplicados

        elif libro.getId() < nodo.libro.getId():      # si el ID es menor, se va al subarbol izquierdo
            if nodo.izquierda is None:
                nodo.izquierda = NodoLibro(libro)
                return True
            return self._insertar_rec(nodo.izquierda, libro)

        else:                                          # si es mayor, se va al subarbol derecho
            if nodo.derecha is None:                   # si no hay hijo derecho, se inserta ahi
                nodo.derecha = NodoLibro(libro)
                return True
            return self._insertar_rec(nodo.derecha, libro)
        
    # metodo de busqueda #

    # busca un libro por su ID dentro del arbol
    def buscar(self, id_libro):
        return self._buscar_rec(self.raiz, id_libro)

    # metodo recursivo para encontrar el libro
    def _buscar_rec(self, nodo, id_libro):

        # si no se encuentra, retorna None
        if nodo is None:
            return None

        # si encuentra el ID, retorna el libro
        if id_libro == nodo.libro.getId():
         return nodo.libro

        # si es menor, busca a la izquierda
        elif id_libro < nodo.libro.getId():
            return self._buscar_rec(nodo.izquierda, id_libro)

        # si es mayor, busca a la derecha
        else:
            return self._buscar_rec(nodo.derecha, id_libro)
        

    # metodo LISTAR inorden #

    # recorre el arbol en inorden y devuelve los libros ordenados por ID
    def listar(self):
        resultado = []
        self._inorden(self.raiz, resultado)
        return resultado

    # metodo recursivo para recorrer el arbol
    def _inorden(self, nodo, lista):

        if nodo is not None:
            # primero izquierda (menores)
            self._inorden(nodo.izquierda, lista)

            # luego el nodo actual
            lista.append(nodo.libro)

            # luego derecha (mayores)
            self._inorden(nodo.derecha, lista)    