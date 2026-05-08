#1. El metodo constructor
print("===========================================================")
class Producto:
    def __init__(self, nombre, precio, stock=0):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

# Creamos productos con y sin especificar el stock
laptop = Producto("Laptop XPS", 1200)  # stock será 0
teclado = Producto("Teclado mecánico", 80, 15)  # stock será 15

print(laptop.stock)  # Imprime: 0
print(teclado.stock)  # Imprime: 15

# Inicialización de atributos con cálculos
class Rectangulo:
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto
        self.area = ancho * alto  # Calculamos y almacenamos el área
        self.perimetro = 2 * (ancho + alto)  # Calculamos y almacenamos el perímetro

# Creamos un rectángulo
rect = Rectangulo(5, 3)
print(rect.area)      # Imprime: 15
print(rect.perimetro) # Imprime: 16

#2. Atributos con validación
print("===========================================================")
class Cuenta:
    def __init__(self, titular, saldo_inicial):
        self.titular = titular

        # Validamos que el saldo inicial no sea negativo
        if saldo_inicial < 0:
            raise ValueError("El saldo inicial no puede ser negativo")

        self.saldo = saldo_inicial

# Esto funcionará
cuenta_ana = Cuenta("Ana García", 1000)

# Esto lanzará un ValueError
try:
    cuenta_problematica = Cuenta("Juan López", -500)
except ValueError as e:
    print(f"Error: {e}")  # Imprime: Error: El saldo inicial no puede ser negativo

#3. Ejemplo práctico: Modelando una biblioteca
print("===========================================================")
class Libro:
    def __init__(self, titulo, autor, paginas, isbn, disponible=True):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        self.isbn = isbn
        self.disponible = disponible
        self.pagina_actual = 0  # Inicializamos en la página 0 (cerrado)

# Creamos algunos libros
libro1 = Libro("Python Crash Course", "Eric Matthes", 544, "9781593279288")
libro2 = Libro("Clean Code", "Robert C. Martin", 464, "9780132350884", False)

# Verificamos si están disponibles
print(f"{libro1.titulo} está {'disponible' if libro1.disponible else 'prestado'}")
print(f"{libro2.titulo} está {'disponible' if libro2.disponible else 'prestado'}")

#4. Constructores alternativos con métodos de clase
print("===========================================================")
class Fecha:
    def __init__(self, dia, mes, año):
        self.dia = dia
        self.mes = mes
        self.año = año

    @classmethod
    def desde_texto(cls, texto):
        """Constructor alternativo que crea una Fecha desde un texto con formato DD-MM-AAAA"""
        dia, mes, año = map(int, texto.split('-'))
        return cls(dia, mes, año)

    @classmethod
    def hoy(cls):
        """Constructor alternativo que crea una Fecha con la fecha actual"""
        import datetime
        fecha_actual = datetime.date.today()
        return cls(fecha_actual.day, fecha_actual.month, fecha_actual.year)

# Diferentes formas de crear objetos Fecha
fecha1 = Fecha(15, 3, 2023)  # Constructor normal
fecha2 = Fecha.desde_texto("25-12-2023")  # Constructor alternativo
fecha3 = Fecha.hoy()  # Constructor alternativo que usa la fecha actual

print(f"{fecha1.dia}/{fecha1.mes}/{fecha1.año}")  # Imprime: 15/3/2023
print(f"{fecha2.dia}/{fecha2.mes}/{fecha2.año}")  # Imprime: 25/12/2023

