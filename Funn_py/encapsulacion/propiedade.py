import math

# 1. Creando propiedades con el decorador @property
print("=== 1. Temperatura ===")
class Temperatura:
    def __init__(self, celsius=0):
        self._celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, valor):
        if valor < -273.15:
            raise ValueError("La temperatura no puede ser menor que el cero absoluto")
        self._celsius = valor

    @property
    def fahrenheit(self):
        return self._celsius * 9/5 + 32

    @fahrenheit.setter
    def fahrenheit(self, valor):
        celsius = (valor - 32) * 5/9
        if celsius < -273.15:
            raise ValueError("La temperatura no puede ser menor que el cero absoluto")
        self._celsius = celsius

# 2. Anatomía de una propiedad
print("=== 2. Persona ===")
class Persona:
    def __init__(self, nombre):
        self._nombre = nombre
        self._amigos = []

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        if not isinstance(valor, str) or not valor:
            raise ValueError("El nombre debe ser una cadena no vacía")
        self._nombre = valor

    @property
    def amigos(self):
        # Retorna copia para evitar que modifiquen la lista original desde fuera
        return self._amigos.copy()
    
    def agregar_amigo(self, amigo):
        self._amigos.append(amigo)

    @amigos.deleter
    def amigos(self):
        self._amigos = []
        print("Lista de amigos eliminada")

# 3. Propiedades de solo lectura
print("=== 3. Círculo ===")
class Circulo:
    def __init__(self, radio):
        self._radio = radio

    @property
    def radio(self):
        return self._radio

    @radio.setter
    def radio(self, valor):
        if valor <= 0:
            raise ValueError("El radio debe ser positivo")
        self._radio = valor

    @property
    def area(self):
        return math.pi * self._radio ** 2

    @property
    def perimetro(self):
        return 2 * math.pi * self._radio

# 4. Propiedades calculadas
print("=== 4. Empleado ===")
class Empleado:
    def __init__(self, nombre, salario_base, horas_extra=0, tarifa_extra=0):
        self._nombre = nombre
        self._salario_base = salario_base
        self._horas_extra = horas_extra
        self._tarifa_extra = tarifa_extra

    @property
    def salario_total(self):
        return self._salario_base + (self._horas_extra * self._tarifa_extra)

# 6. Propiedades en clases heredadas (Corregido Indentación)
print("=== 6. Herencia ===")
class Producto:
    def __init__(self, nombre, precio):
        self._nombre = nombre
        self._precio = precio

    @property
    def info(self):
        return f"{self._nombre}: {self._precio}€"

class ProductoDigital(Producto):
    def __init__(self, nombre, precio, tamaño_mb):
        super().__init__(nombre, precio)
        self._tamaño_mb = tamaño_mb

    @property
    def info(self):
        return f"{self._nombre}: {self._precio}€ ({self._tamaño_mb} MB)"

# ===========================================================
# PUNTO DE SALIDA (Pruebas del código)
# ===========================================================
if __name__ == "__main__":
    print("\n--- RESULTADOS DE EJECUCIÓN ---")

    # Prueba Temperatura
    t = Temperatura(25)
    print(f"Celsius: {t.celsius}°C | Fahrenheit: {t.fahrenheit}°F")
    t.fahrenheit = 100
    print(f"Tras ajustar a 100°F -> Celsius: {t.celsius:.2f}°C")

    # Prueba Persona
    p = Persona("Ana")
    p.agregar_amigo("Luis")
    print(f"Persona: {p.nombre}, Amigos: {p.amigos}")
    del p.amigos # Llama al deleter
    print(f"Amigos después del deleter: {p.amigos}")

    # Prueba Círculo
    c = Circulo(5)
    print(f"Círculo radio {c.radio}: Área = {c.area:.2f}")

    # Prueba Empleado
    e = Empleado("Juan", 1000, 10, 20)
    print(f"Empleado {e._nombre}: Salario Total = {e.salario_total}")

    # Prueba Herencia
    pd = ProductoDigital("E-book Python", 15, 2.5)
    print(f"Info Producto: {pd.info}")