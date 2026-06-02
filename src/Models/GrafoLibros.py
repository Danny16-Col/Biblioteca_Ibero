class GrafoLibros:

    def __init__(self):
        self.grafo = {}

    def agregar_libro(self, id_libro):

        if id_libro in self.grafo:
            return False
        
        self.grafo[id_libro] = []

        return True
        

    def relacionar_libros(self, id_libro1, id_libro2):

        # No puede relacionarse consigo mismo
        if id_libro1 == id_libro2:
            return False

        # Ambos libros deben existir
        if id_libro1 not in self.grafo or id_libro2 not in self.grafo:
            return False

        # Evitar duplicados
        if id_libro2 in self.grafo[id_libro1]:
            return False

        self.grafo[id_libro1].append(id_libro2)
        self.grafo[id_libro2].append(id_libro1)

        return True
        

    def obtener_relaciones(self, id_libro):

        if not id_libro in self.grafo:
            return[]

        return self.grafo[id_libro] 
        
            
    

    
    
        