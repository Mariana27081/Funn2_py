class CuentaBancaria:
    def __init__(self, titular, saldo=0.0):
        self.__titular = titular
        self.__saldo = saldo

    # Método para retirar dinero
    def retirar(self, cantidad):
        if cantidad > 0 and self.__saldo >= cantidad:
            self.__saldo -= cantidad
            return True
        return False
    
    # Propiedad solo de lectura
    @property
    def titular(self):
        return self.__titular
    
    # Propiedad con validación para el saldo
    @property
    def saldo(self):
        return self.__saldo
    
    @saldo.setter
    def saldo(self, valor):
        if valor < 0:
            raise ValueError("El saldo no puede ser negativo.")
        self.__saldo = valor

    #Depositar dinero
    def depositar(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad
            return True
        return False
    
# Ejemplo de uso
def main():
    cuenta = CuentaBancaria("Andrés", 100)

    print("=== Estado inicial ===")
    print("Titular:", cuenta.titular)
    print("Saldo:", cuenta.saldo)

    print("\n=== Depósito ===")
    print("Depósito 50:", cuenta.depositar(50))
    print("Saldo:", cuenta.saldo)

    print("\n=== Retiro ===")
    print("Retiro 30:", cuenta.retirar(30))
    print("Saldo:", cuenta.saldo)

    print("\n=== Retiro sin fondos ===")
    print("Retiro 200:", cuenta.retirar(200))
    print("Saldo:", cuenta.saldo)

    print("\n=== Intento de saldo negativo ===")
    try:
        cuenta.saldo = -10
    except ValueError as e:
        print("Error:", e)


if __name__ == "__main__":
    main()