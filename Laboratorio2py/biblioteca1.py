# clase Libro
class Libro:
    
    def __init__(self, titulo, autor, año, isbn):
        # Inicializamos los atributos del libro con los datos proporcionados
        self.titulo = titulo
        self.autor = autor
        self.año = año
        self.isbn = isbn

    def mostrar_informacion(self):
          # este es el método para mostrar la información del libro
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Año: {self.año}")
        print(f"ISBN: {self.isbn}")
# Definimos  la clase Biblioteca
class Biblioteca:
    def __init__(self):
        # Inicializa una lista vacía para almacenar los libros
        self.libros = []

    def agregar_libro(self, libro):
        # este es el método para agregar un libro
        self.libros.append(libro)
        print(f"Libro '{libro.titulo}' agregado a la biblioteca.")

    def buscar_libro(self, titulo=None, autor=None):
        #metodo para buscar un libro por título o autor
        for libro in self.libros:
            if (titulo and libro.titulo == titulo) or (autor and libro.autor == autor):
                # Si se encuentra un libro que coincide, se devuelve
                return libro
            # Si no se encuentra el libro, se devuelve None
        return None

    def mostrar_libros(self):
        # metodo para mostrar todos los libros en la biblioteca
        if not self.libros:
            print("No hay libros en la biblioteca.")
        else:
            for libro in self.libros:
                # Muestra la información de cada libro
                libro.mostrar_informacion()

# Ejemplo de uso de las clases anteriormente definidas
biblioteca = Biblioteca()
while True:
    # Bucle principal que ofrece opciones al usuario
    print("\nOpciones: 1. Agregar Libro  2. Buscar Libro  3. Mostrar Libros  4. Salir")
    opcion = input("Elige una opción: ")
    
    if opcion == "1":
        # Agregar un nuevo libro a la biblioteca
        titulo = input("Título del libro: ")
        autor = input("Autor del libro: ")
        año = input("Año de publicación: ")
        isbn = input("ISBN: ")
        nuevo_libro = Libro(titulo, autor, año, isbn)
        biblioteca.agregar_libro(nuevo_libro)
    
    elif opcion == "2":
        # Buscar un libro en la biblioteca por título o autor
        criterio = input("Buscar por (1) Título o (2) Autor: ")
        if criterio == "1":
            titulo = input("Título del libro: ")
            libro = biblioteca.buscar_libro(titulo=titulo)
        elif criterio == "2":
            autor = input("Autor del libro: ")
            libro = biblioteca.buscar_libro(autor=autor)
        else:
            print("Opción no válida.")
            continue
        if libro:
            libro.mostrar_informacion()
        else:
            print("Libro no encontrado.")
    
    elif opcion == "3":
        # Mostrar todos los libros de la biblioteca
        biblioteca.mostrar_libros()
    
    elif opcion == "4":
        # Salir del bucle
        break
    
    else:
        print("Opción no válida.")
# este sistema simula la gestion de una biblioteca
# permite agregar libros
#buscar libros por titulo o autor y mostrar la lista de los libros disponibles.