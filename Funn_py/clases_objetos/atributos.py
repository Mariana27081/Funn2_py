#1. Atributos de instancia
print("===========================================================")
class Estudiante:
    def __init__(self, nombre, edad):
        self.nombre = nombre  # Atributo de instancia
        self.edad = edad      # Atributo de instancia
        self.activo = True    # Atributo de instancia con valor predeterminado

# Creamos dos estudiantes
estudiante1 = Estudiante("María", 20)
estudiante2 = Estudiante("Carlos", 22)

# Cada estudiante tiene sus propios valores para los atributos
print(estudiante1.nombre)  # Imprime: María
print(estudiante2.nombre)  # Imprime: Carlos

#2. Atributos de clase
print("===========================================================")
class Estudiante:
    # Atributo de clase
    universidad = "Universidad Autónoma"

    def __init__(self, nombre, edad):
        self.nombre = nombre  # Atributo de instancia
        self.edad = edad      # Atributo de instancia

# Creamos dos estudiantes
estudiante1 = Estudiante("María", 20)
estudiante2 = Estudiante("Carlos", 22)

# Ambos comparten el mismo atributo de clase
print(estudiante1.universidad)  # Imprime: Universidad Autónoma
print(estudiante2.universidad)  # Imprime: Universidad Autónoma
print(Estudiante.universidad)   # También podemos acceder desde la clase

# Si modificamos el atributo de clase, afecta a todas las instancias
Estudiante.universidad = "Universidad Complutense"
print(estudiante1.universidad)  # Imprime: Universidad Complutense
print(estudiante2.universidad)  # Imprime: Universidad Complutense

#3. Acceso a atributos
print("===========================================================")
class Producto:
    impuesto = 0.21  # Atributo de clase

    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

# Creamos un producto
laptop = Producto("Laptop", 1000)

# Accedemos a sus atributos
print(laptop.nombre)    # Atributo de instancia
print(laptop.precio)    # Atributo de instancia
print(laptop.impuesto)  # Atributo de clase (accedido desde la instancia)
print(Producto.impuesto)  # Atributo de clase (accedido desde la clase)

#4. Modificación de atributos
print("===========================================================")
class Coche:
    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.kilometraje = 0

# Creamos un coche nuevo
mi_coche = Coche("Toyota", "Corolla", "Azul")
print(f"Color inicial: {mi_coche.color}")  # Imprime: Color inicial: Azul
print(f"Kilometraje inicial: {mi_coche.kilometraje}")  # Imprime: Kilometraje inicial: 0

# Modificamos sus atributos
mi_coche.color = "Rojo"  # Pintamos el coche
mi_coche.kilometraje = 1500  # Actualizamos el kilometraje

print(f"Nuevo color: {mi_coche.color}")  # Imprime: Nuevo color: Rojo
print(f"Kilometraje actual: {mi_coche.kilometraje}")  # Imprime: Kilometraje actual: 1500

#5. Atributos dinámicos
print("===========================================================")
class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

# Creamos una persona
juan = Persona("Juan")

# Añadimos atributos dinámicamente
juan.edad = 30
juan.profesion = "Ingeniero"

print(f"{juan.nombre} tiene {juan.edad} años y es {juan.profesion}")
# Imprime: Juan tiene 30 años y es Ingeniero

#6. Atributos privados y convenciones de nomenclatura
print("===========================================================")
class CuentaBancaria:
    tasa_interes = 0.03  # Atributo de clase público

    def __init__(self, titular, saldo_inicial, pin):
        self.titular = titular        # Atributo público
        self._saldo = saldo_inicial   # Atributo "protegido"
        self.__pin = pin              # Atributo "privado"

    def verificar_pin(self, pin_ingresado):
        return self.__pin == pin_ingresado

# Creamos una cuenta
cuenta = CuentaBancaria("Ana López", 1000, "1234")

# Acceso a atributos según su visibilidad
print(cuenta.titular)  # Funciona: atributo público
print(cuenta._saldo)   # Funciona, pero no deberíamos hacerlo por convención
# print(cuenta.__pin)  # Error: no existe tal atributo debido al name mangling

# El atributo privado existe, pero con un nombre modificado
print(cuenta._CuentaBancaria__pin)  # Funciona, pero es una mala práctica

#7. Propiedades: atributos con comportamiento controlado
print("===========================================================")
class Temperatura:
    def __init__(self):
        self._celsius = 0

    # Definimos la propiedad celsius
    @property
    def celsius(self):
        """Obtiene la temperatura en grados Celsius"""
        return self._celsius

    @celsius.setter
    def celsius(self, valor):
        """Establece la temperatura en grados Celsius"""
        if valor < -273.15:
            raise ValueError("La temperatura no puede ser menor que el cero absoluto")
        self._celsius = valor

    # Definimos la propiedad fahrenheit
    @property
    def fahrenheit(self):
        """Obtiene la temperatura en grados Fahrenheit"""
        return self._celsius * 9/5 + 32

    @fahrenheit.setter
    def fahrenheit(self, valor):
        """Establece la temperatura en grados Fahrenheit"""
        self.celsius = (valor - 32) * 5/9

# Creamos un objeto temperatura
temp = Temperatura()

# Usamos las propiedades como si fueran atributos normales
temp.celsius = 25
print(f"{temp.celsius}°C = {temp.fahrenheit}°F")  # Imprime: 25°C = 77.0°F

temp.fahrenheit = 68
print(f"{temp.celsius}°C = {temp.fahrenheit}°F")  # Imprime: 20.0°C = 68.0°F

# La validación funciona
try:
    temp.celsius = -300  # Esto lanzará un error
except ValueError as e:
    print(f"Error: {e}")  # Imprime: Error: La temperatura no puede ser menor que el cero absoluto

#8. Atributos calculados
print("===========================================================")
class Rectangulo:
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

    @property
    def area(self):
        """Área del rectángulo, calculada dinámicamente"""
        return self.ancho * self.alto

    @property
    def perimetro(self):
        """Perímetro del rectángulo, calculado dinámicamente"""
        return 2 * (self.ancho + self.alto)

# Creamos un rectángulo
rect = Rectangulo(5, 3)

# Accedemos a los atributos calculados
print(f"Área: {rect.area}")        # Imprime: Área: 15
print(f"Perímetro: {rect.perimetro}")  # Imprime: Perímetro: 16

# Si modificamos el rectángulo, los atributos calculados se actualizan automáticamente
rect.ancho = 7
print(f"Nueva área: {rect.area}")  # Imprime: Nueva área: 21

#9. Atributos especiales
class Ejemplo:
    """Clase de ejemplo para mostrar atributos especiales"""
    def __init__(self, valor):
        self.valor = valor

# Creamos una instancia
obj = Ejemplo(42)

# Atributos especiales
print(obj.__class__)  # Muestra la clase del objeto
print(Ejemplo.__name__)  # Nombre de la clase
print(Ejemplo.__doc__)  # Documentación de la clase
print(obj.__dict__)  # Diccionario que almacena los atributos de instancia

#10. Gestión de atributos con funciones integradas
print("===========================================================")
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

p = Persona("Laura", 29)

# Verificar si un objeto tiene un atributo
print(hasattr(p, "nombre"))  # True
print(hasattr(p, "apellido"))  # False

# Obtener el valor de un atributo
print(getattr(p, "nombre"))  # Laura
print(getattr(p, "apellido", "No especificado"))  # No especificado (valor predeterminado)

# Establecer un atributo
setattr(p, "apellido", "García")
print(p.apellido)  # García

# Eliminar un atributo
delattr(p, "apellido")
# print(p.apellido)  # Esto daría error porque ya no existe
