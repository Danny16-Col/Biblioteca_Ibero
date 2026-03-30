from Models.Libro import Libro
from Models.Usuario import Usuario

# Base de datos quemada para poder hacer pruebas..

# Lista de libros
libros = [
    Libro(1, "Clean Code", "Robert C. Martin"),
    Libro(2, "The Pragmatic Programmer", "Andrew Hunt"),
    Libro(3, "Introduction to Algorithms", "Thomas H. Cormen"),
    Libro(4, "Design Patterns", "Erich Gamma"),
    Libro(5, "Python Crash Course", "Eric Matthes")
]


# Lista de préstamos (estructura lineal)
prestamos = []