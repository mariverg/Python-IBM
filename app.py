class Libro:
    """
    Clase que representa un libro en la biblioteca.
    
    Atributos:
        titulo (str): Título del libro.
        autor (str): Autor del libro.
        isbn (str): ISBN único del libro.
        disponible (bool): Estado de disponibilidad del libro (True = disponible, False = prestado).
    """
    
    def __init__(self, titulo, autor, isbn, disponible=True):
        """
        Inicializa un nuevo libro con los parámetros dados.
        
        Args:
            titulo (str): Título del libro.
            autor (str): Autor del libro.
            isbn (str): ISBN único del libro.
            disponible (bool, opcional): Estado inicial de disponibilidad. Por defecto es True.
        """
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = disponible
    
    def prestar(self):
        """
        Cambia el estado del libro a prestado si está disponible.
        
        Returns:
            bool: True si el préstamo fue exitoso, False si ya estaba prestado.
        """
        if self.disponible:
            self.disponible = False
            return True
        else:
            print(f"El libro '{self.titulo}' ya está prestado.")
            return False
    
    def devolver(self):
        """
        Cambia el estado del libro a disponible si estaba prestado.
        
        Returns:
            bool: True si la devolución fue exitosa, False si ya estaba disponible.
        """
        if not self.disponible:
            self.disponible = True
            return True
        else:
            print(f"El libro '{self.titulo}' ya está disponible.")
            return False
    
    def __str__(self):
        """
        Retorna una representación en cadena del libro.
        
        Returns:
            str: Cadena con la información del libro.
        """
        estado = "Sí" if self.disponible else "No"
        return f"- {self.titulo} ({self.autor}) - ISBN: {self.isbn} - Disponible: {estado}"


def agregar(biblioteca):
    """
    Permite al usuario añadir un nuevo libro a la biblioteca.
    
    Args:
        biblioteca (list): Lista de objetos Libro.
    """
    titulo = input("Título: ")
    autor = input("Autor: ")
    isbn = input("ISBN: ")
    
    # Verificar si el ISBN ya existe
    for libro in biblioteca:
        if libro.isbn == isbn:
            print("Error: Ya existe un libro con ese ISBN.")
            return
    
    # Crear y añadir el nuevo libro
    nuevo_libro = Libro(titulo, autor, isbn)
    biblioteca.append(nuevo_libro)
    print("Libro agregado con éxito.")


def prestar(biblioteca):
    """
    Permite prestar un libro buscándolo por su ISBN.
    
    Args:
        biblioteca (list): Lista de objetos Libro.
    """
    isbn = input("Ingresa el ISBN: ")
    
    for libro in biblioteca:
        if libro.isbn == isbn:
            if libro.prestar():
                print("Libro prestado con éxito.")
            return
    
    print("El libro con ISBN", isbn, "no existe en la biblioteca.")


def devolver(biblioteca):
    """
    Permite devolver un libro buscándolo por su ISBN.
    
    Args:
        biblioteca (list): Lista de objetos Libro.
    """
    isbn = input("Ingresa el ISBN: ")
    
    for libro in biblioteca:
        if libro.isbn == isbn:
            if libro.devolver():
                print("Libro devuelto con éxito.")
            return
    
    print("El libro con ISBN", isbn, "no existe en la biblioteca.")


def mostrar(biblioteca):
    """
    Muestra todos los libros de la biblioteca.
    
    Args:
        biblioteca (list): Lista de objetos Libro.
    """
    if not biblioteca:
        print("La biblioteca está vacía.")
        return
    
    for libro in biblioteca:
        print(libro)


def buscar(biblioteca):
    """
    Busca un libro por su ISBN y muestra su información.
    
    Args:
        biblioteca (list): Lista de objetos Libro.
    """
    isbn = input("Ingresa el ISBN a buscar: ")
    
    for libro in biblioteca:
        if libro.isbn == isbn:
            print(libro)
            return
    
    print("El libro con ISBN", isbn, "no existe en la biblioteca.")


def main():
    """
    Función principal que ejecuta el Sistema de Gestión de Biblioteca.
    """
    biblioteca = []
    
    print("Bienvenido al Sistema de Gestión de Biblioteca")
    
    while True:
        print("\n1. Agregar libro")
        print("2. Prestar libro")
        print("3. Devolver libro")
        print("4. Mostrar libros")
        print("5. Buscar")
        print("6. Salir")
        
        try:
            opcion = int(input("Elige una opción: "))
        except ValueError:
            print("Error: Ingresa un número válido.")
            continue
        
        if opcion == 1:
            agregar(biblioteca)
        elif opcion == 2:
            prestar(biblioteca)
        elif opcion == 3:
            devolver(biblioteca)
        elif opcion == 4:
            mostrar(biblioteca)
        elif opcion == 5:
            buscar(biblioteca)
        elif opcion == 6:
            print("Gracias por usar el Sistema de Gestión de Biblioteca. ¡Hasta pronto!")
            break
        else:
            print("Opción inválida. Por favor, elige una opción del 1 al 6.")


if __name__ == "__main__":
    main()