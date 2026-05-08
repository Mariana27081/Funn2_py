# ===========================================================
# 1 & 2. Encapsulación y Atributos Privados
# ===========================================================
class CuentaBancaria:
    def __init__(self, titular, saldo_inicial, pin):
        # Atributo Protegido (Convención: "No me toques desde fuera si no sabes qué haces")
        self._titular = titular
        self._saldo = saldo_inicial
        # Atributo Privado (Name Mangling: Python cambia su nombre internamente)
        self.__pin = pin 

    def depositar(self, cantidad):
        if cantidad > 0:
            self._saldo += cantidad
            return True
        return False

    def validar_pin(self, pin_ingresado):
        """Método público para verificar el PIN sin exponerlo."""
        return self.__pin == pin_ingresado

# ===========================================================
# 3. Validación de Datos en el Constructor
# ===========================================================
class Producto:
    def __init__(self, nombre, precio):
        self._nombre = nombre
        # Es buena práctica validar datos críticos desde el inicio
        if precio < 0:
            raise ValueError("El precio no puede ser negativo")
        self._precio = precio

    def mostrar_precio(self):
        return f"El producto {self._nombre} cuesta ${self._precio}"

# ===========================================================
# 4. Atributos Privados vs. Protegidos en Herencia
# ===========================================================
class Vehiculo:
    def __init__(self, marca, modelo):
        self._marca = marca      # Protegido: accesible en subclases
        self.__modelo = modelo   # Privado: solo accesible en esta clase

class Coche(Vehiculo):
    def __init__(self, marca, modelo, puertas):
        super().__init__(marca, modelo)
        self._puertas = puertas

    def mostrar_info(self):
        # _marca es accesible porque es protegido
        print(f"Marca: {self._marca}")
        
        # __modelo lanzará un error porque el nombre fue "ofuscado" por Python
        try:
            print(f"Modelo: {self.__modelo}")
        except AttributeError:
            print("Resultado: No se puede acceder a __modelo (privado) desde la subclase Coche")

# ===========================================================
# PUNTO DE SALIDA (Pruebas de comportamiento)
# ===========================================================
if __name__ == "__main__":
    print("=== PRUEBA CUENTA BANCARIA ===")
    mi_cuenta = CuentaBancaria("Juan Pérez", 1000, "1234")
    
    # Acceso a protegido (funciona, pero no se recomienda)
    print(f"Saldo (protegido): {mi_cuenta._saldo}") 
    
    # Intento de acceso a privado
    try:
        print(mi_cuenta.__pin)
    except AttributeError:
        print("Privacidad: No se puede acceder a __pin directamente.")

    # ¿Cómo lo ve Python por dentro? (Name Mangling)
    # Python renombra __pin como _CuentaBancaria__pin
    print(f"Acceso 'hacker': {mi_cuenta._CuentaBancaria__pin}")

    print("\n=== PRUEBA HERENCIA VEHÍCULO ===")
    mi_auto = Coche("Toyota", "Corolla", 4)
    mi_auto.mostrar_info()

    print("\n=== PRUEBA VALIDACIÓN PRODUCTO ===")
    try:
        p = Producto("Radio", -50)
    except ValueError as e:
        print(f"Error esperado: {e}")