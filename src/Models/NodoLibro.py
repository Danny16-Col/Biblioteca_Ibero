# clase nodo del arbol de libro

# recibe un objeto Libro y lo guarda dentro del nodo
class NodoLibro:
    def __init__(self, libro):
        self.libro = libro
        self.izquierda = None   # referencia al hijo izquierdo
        self.derecha = None     # referencia al hijo derecho