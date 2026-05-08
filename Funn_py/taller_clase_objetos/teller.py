class Libros:
    def __init__(self, titulo, autor, paginas, disponible=True):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        self.disponible = disponible

# def prestar...
    def prestar(self):
        if self.disponible:
            self.disponible = False
            return ("Se presto el libro con exito")
        else:
            return ("El libro ya ha sido prestado")
        
    # def devolver...
    def devolver(self):
        if not self.disponible:
            self.disponible = True
            return ("Se devolvio con exito")
        else:
            return ("El libro ya esta en la biblioteca")
    
    # def informacion...
    def informacion(self):
        estado = "Disponible" if self.disponible else "No disponible"
        return f"Título: {self.titulo}, Autor: {self.autor}, Páginas: {self.paginas}, Estado: {estado}"


# Prueba de la clase Libro
def main():
    # Crear dos objetos libro diferentes
    libro1 = Libros("Don Quijote de la Mancha", "Miguel de Cervantes", 863)
    libro2 = Libros("Cien años de soledad", "Gabriel García Márquez", 471)
    
    # Mostrar información inicial de los libros
    print("=== Información inicial de los libros ===")
    print(libro1.informacion())
    print("\n")
    print(libro2.informacion())
    print("\n")
    
    # Prestar los libros
    print("=== Préstamo de libros ===")
    print(libro1.prestar())
    print(libro2.prestar())
    print("\n")
    
    # Intentar prestar un libro ya prestado
    print("=== Intento de préstamo de libros ya prestados ===")
    print(libro1.prestar())
    print("\n")
    
    # Mostrar información después del préstamo
    print("=== Información después del préstamo ===")
    print(libro1.informacion())
    print("\n")
    
    # Devolver un libro
    print("=== Devolución de libros ===")
    print(libro1.devolver())
    print("\n")
    
    # Intentar devolver un libro ya disponible
    print("=== Intento de devolución de libros ya disponibles ===")
    print(libro1.devolver())
    print("\n")
    
    # Mostrar información final
    print("=== Información final de los libros ===")
    print(libro1.informacion())
    print("\n")
    print(libro2.informacion())


if __name__ == "__main__":
    main()