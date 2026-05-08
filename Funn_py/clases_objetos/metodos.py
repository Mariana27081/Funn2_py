# ===========================================================
# 1 & 2. Definición y Llamada a métodos básicos
# ===========================================================
print("--- 1 & 2: Métodos Básicos ---")
class Coche:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.velocidad = 0
        self.encendido = False

    def encender(self):
        if not self.encendido:
            self.encendido = True
            return f"{self.marca} {self.modelo} encendido"
        return f"{self.marca} {self.modelo} ya estaba encendido"

    def apagar(self):
        if self.encendido:
            self.encendido = False
            self.velocidad = 0
            return f"{self.marca} {self.modelo} apagado"
        return f"{self.marca} {self.modelo} ya estaba apagado"

mi_coche = Coche("Toyota", "Corolla")
print(mi_coche.encender())
print(mi_coche.encender())
print(mi_coche.apagar())

# ===========================================================
# 3. Métodos con parámetros (Aceleración)
# ===========================================================
print("\n--- 3: Métodos con Parámetros ---")
class CocheAvanzado(Coche): # Heredamos para no repetir init
    def __init__(self, marca, modelo):
        super().__init__(marca, modelo)
        self.velocidad_maxima = 200

    def acelerar(self, incremento):
        if not self.encendido:
            return f"No se puede acelerar: {self.marca} {self.modelo} está apagado"
        self.velocidad = min(self.velocidad + incremento, self.velocidad_maxima)
        return f"Velocidad actual: {self.velocidad} km/h"

    def frenar(self, decremento):
        if self.velocidad == 0: return "El coche ya está detenido"
        self.velocidad = max(self.velocidad - decremento, 0)
        return f"Velocidad actual: {self.velocidad} km/h"

coche_pro = CocheAvanzado("Ferrari", "Roma")
print(coche_pro.encender())
print(coche_pro.acelerar(50))
print(coche_pro.frenar(20))

# ===========================================================
# 4. Métodos que interactúan con atributos (Cuenta Bancaria)
# ===========================================================
print("\n--- 4: Interacción con Atributos ---")
class CuentaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self._saldo = saldo_inicial

    def consultar_saldo(self):
        return f"Saldo actual de {self.titular}: ${self._saldo}"

    def depositar(self, cantidad):
        if cantidad <= 0: return "Cantidad inválida"
        self._saldo += cantidad
        return f"Depósito: ${cantidad}. Nuevo saldo: ${self._saldo}"

    def retirar(self, cantidad):
        if cantidad > self._saldo: return "Fondos insuficientes"
        self._saldo -= cantidad
        return f"Retiro: ${cantidad}. Nuevo saldo: ${self._saldo}"

cuenta = CuentaBancaria("Ana", 100)
print(cuenta.consultar_saldo())
print(cuenta.depositar(50))
print(cuenta.retirar(30))

# ===========================================================
# 5. Métodos que devuelven valores (Calculadora)
# ===========================================================
print("\n--- 5: Devolución de Valores ---")
class Calculadora:
    def sumar(self, a, b): return a + b
    def calcular_estadisticas(self, numeros):
        if not numeros: return {"suma": 0, "promedio": 0}
        return {"suma": sum(numeros), "promedio": sum(numeros)/len(numeros)}

calc = Calculadora()
print(f"Suma: {calc.sumar(10, 5)}")
stats = calc.calcular_estadisticas([10, 20, 30])
print(f"Estadísticas: {stats}")

# ===========================================================
# 6. Métodos que llaman a otros métodos (Persona)
# ===========================================================
print("\n--- 6: Llamadas Internas ---")
class Persona:
    def __init__(self, nombre, apellido, edad):
        self.nombre, self.apellido, self.edad = nombre, apellido, edad

    def nombre_completo(self): return f"{self.nombre} {self.apellido}"
    def es_mayor_de_edad(self): return self.edad >= 18
    def presentarse(self):
        estado = "mayor" if self.es_mayor_de_edad() else "menor"
        return f"Hola, soy {self.nombre_completo()} y soy {estado} de edad."

p = Persona("Luis", "Pérez", 25)
print(p.presentarse())

# ===========================================================
# 7. Métodos especiales (Dunder)
# ===========================================================
print("\n--- 7: Métodos Especiales ---")
class Punto:
    def __init__(self, x, y): self.x, self.y = x, y
    def __str__(self): return f"({self.x}, {self.y})"
    def __add__(self, otro): return Punto(self.x + otro.x, self.y + otro.y)

pt1 = Punto(1, 2)
pt2 = Punto(3, 4)
print(f"Punto 1: {pt1}")
print(f"Suma de puntos: {pt1 + pt2}")

# ===========================================================
# 8. Métodos estáticos (MathUtils)
# ===========================================================
print("\n--- 8: Métodos Estáticos ---")
class MathUtils:
    @staticmethod
    def es_primo(n):
        if n < 2: return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0: return False
        return True

print(f"¿Es 7 primo?: {MathUtils.es_primo(7)}")
print(f"¿Es 10 primo?: {MathUtils.es_primo(10)}")

# ===========================================================
# 9. Métodos de clase (Empleado)
# ===========================================================
print("\n--- 9: Métodos de Clase ---")
class Empleado:
    num_empleados = 0
    def __init__(self, nombre, salario):
        self.nombre, self.salario = nombre, salario
        Empleado.num_empleados += 1
    
    @classmethod
    def desde_salario_anual(cls, nombre, anual):
        return cls(nombre, anual / 12)

emp1 = Empleado("Jose", 2000)
emp2 = Empleado.desde_salario_anual("Maria", 24000)
print(f"Empleados creados: {Empleado.num_empleados}")
print(f"Salario Maria (mensual): {emp2.salario}")

# ===========================================================
# 10. Ejemplo Práctico: Biblioteca
# ===========================================================
print("\n--- 10: Ejemplo Final Biblioteca ---")
class Libro:
    def __init__(self, titulo, autor, paginas):
        self.titulo, self.autor, self.paginas = titulo, autor, paginas
        self.pagina_actual = 0
        self.abierto = False

    def abrir(self): 
        self.abierto = True
        return f"Abriendo {self.titulo}..."

    def leer(self, num):
        if not self.abierto: return "El libro está cerrado."
        self.pagina_actual = min(self.pagina_actual + num, self.paginas)
        return f"Progreso: {self.pagina_actual}/{self.paginas}"

libro1 = Libro("Cien Años de Soledad", "García Márquez", 400)
print(libro1.abrir())
print(libro1.leer(50))
print(libro1.leer(350))