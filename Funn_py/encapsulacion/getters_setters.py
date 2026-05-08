# ===========================================================
# 1 & 2. Clase Persona y Uso de Getters/Setters
# ===========================================================
class Persona:
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad

    # Getter para nombre
    def get_nombre(self):
        return self._nombre

    # Setter para nombre
    def set_nombre(self, nuevo_nombre):
        if isinstance(nuevo_nombre, str) and len(nuevo_nombre.strip()) > 0:
            self._nombre = nuevo_nombre
        else:
            raise ValueError("El nombre debe ser una cadena no vacía")

    # Getter para edad
    def get_edad(self):
        return self._edad

    # Setter para edad
    def set_edad(self, nueva_edad):
        if isinstance(nueva_edad, int) and 0 <= nueva_edad <= 120:
            self._edad = nueva_edad
        else:
            raise ValueError("La edad debe ser un entero entre 0 y 120")

# ===========================================================
# 3. Ejemplo práctico: Clase Producto
# ===========================================================
class Producto:
    def __init__(self, nombre, precio, stock=0):
        self._nombre = nombre
        self._precio = precio
        self._stock = stock
        self._descuento = 0.0

    # Getters
    def get_nombre(self):
        return self._nombre

    def get_precio(self):
        # Aplicamos el descuento al devolver el precio
        return self._precio * (1 - self._descuento)

    def get_precio_base(self):
        return self._precio

    def get_stock(self):
        return self._stock

    # Setters
    def set_precio(self, nuevo_precio):
        if not isinstance(nuevo_precio, (int, float)) or nuevo_precio < 0:
            raise ValueError("El precio debe ser un número positivo")
        self._precio = nuevo_precio

    def set_descuento(self, nuevo_descuento):
        if not isinstance(nuevo_descuento, (int, float)) or not 0 <= nuevo_descuento <= 1:
            raise ValueError("El descuento debe ser un número entre 0 y 1 (ej: 0.2 para 20%)")
        self._descuento = float(nuevo_descuento)

# ===========================================================
# 4. Getters y setters en herencia
# ===========================================================
class Electronico(Producto):
    def __init__(self, nombre, precio, stock, garantia_meses):
        super().__init__(nombre, precio, stock)
        self._garantia_meses = garantia_meses
        self._activado = False

    def get_garantia_meses(self):
        return self._garantia_meses

    def esta_activado(self):
        return self._activado

    def activar(self):
        self._activado = True
        print(f"[{self._nombre}] Dispositivo activado.")

    # Sobrescribir el setter de precio para añadir lógica adicional
    def set_precio(self, nuevo_precio):
        super().set_precio(nuevo_precio)
        # Lógica de negocio: productos caros incluyen garantía extendida
        if nuevo_precio > 1000:
            self._garantia_meses = max(self._garantia_meses, 24)
            print(f"Nota: Precio superior a 1000€. Garantía extendida a {self._garantia_meses} meses.")

# ===========================================================
# PUNTO DE SALIDA (Pruebas de ejecución)
# ===========================================================
if __name__ == "__main__":
    print("=== PRUEBA PERSONA ===")
    ana = Persona("Ana López", 29)
    print(f"Nombre original: {ana.get_nombre()}")
    ana.set_nombre("Ana María López")
    print(f"Nombre modificado: {ana.get_nombre()}")

    try:
        ana.set_edad(150)
    except ValueError as e:
        print(f"Validación correcta: {e}")

    print("\n=== PRUEBA PRODUCTO Y DESCUENTO ===")
    laptop = Producto("Laptop", 1000)
    laptop.set_descuento(0.15) # 15% de descuento
    print(f"Producto: {laptop.get_nombre()}")
    print(f"Precio Base: {laptop.get_precio_base()}€")
    print(f"Precio con Descuento: {laptop.get_precio()}€")

    print("\n=== PRUEBA HERENCIA (Electrónico) ===")
    tv = Electronico("Smart TV", 800, 10, 12)
    print(f"Garantía inicial: {tv.get_garantia_meses()} meses")
    # Subimos el precio a más de 1000 para disparar la lógica del setter
    tv.set_precio(1200)
    print(f"Nueva garantía tras cambio de precio: {tv.get_garantia_meses()} meses")
    tv.activar()