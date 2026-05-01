from .NodoUsuario import NodoUsuario

class ArbolUsuarios:

    def __init__(self):
        self.raiz = None

    # INSERTAR
    def insertar(self, usuario):
        if self.raiz is None:
            self.raiz = NodoUsuario(usuario)
        else:
            self._insertar(self.raiz, usuario)

    def _insertar(self, nodo, usuario):
        if usuario.get_id() < nodo.usuario.get_id():
            if nodo.izq is None:
                nodo.izq = NodoUsuario(usuario)
            else:
                self._insertar(nodo.izq, usuario)
        else:
            if nodo.der is None:
                nodo.der = NodoUsuario(usuario)
            else:
                self._insertar(nodo.der, usuario)

    # BUSCAR POR USUARIO (LOGIN)
    def buscar(self, username):
        return self._buscar(self.raiz, username)

    def _buscar(self, nodo, username):
        if nodo is None:
            return None

        if nodo.usuario.get_usuario() == username:
            return nodo.usuario

        # se recorre todo (porque el árbol está por ID)
        izq = self._buscar(nodo.izq, username)
        if izq:
            return izq

        return self._buscar(nodo.der, username)