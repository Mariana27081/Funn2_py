import hashlib
import re
import math

# 1. Convención para métodos privados (Name Mangling)
class Autenticador:
    def __init__(self, usuario, contraseña):
        self._usuario = usuario
        self._contraseña_hash = self.__generar_hash(contraseña)

    def __generar_hash(self, contraseña):
        """Método privado: Python renombra esto internamente a _Autenticador__generar_hash."""
        return hashlib.sha256(contraseña.encode()).hexdigest()

    def verificar_contraseña(self, contraseña_ingresada):
        hash_ingresado = self.__generar_hash(contraseña_ingresada)
        return hash_ingresado == self._contraseña_hash

# 2. Ejemplo: Procesamiento de datos en etapas
class ProcesadorTexto:
    def __init__(self):
        self._texto = ""
        self._estadísticas = {}

    def procesar_archivo_directo(self, contenido):
        """Simulación de procesar contenido (para no depender de un archivo externo en el ejemplo)."""
        self._texto = self.__normalizar_texto(contenido)
        self._estadísticas = self.__calcular_estadísticas(self._texto)

    def __normalizar_texto(self, texto):
        texto = texto.lower()
        texto = re.sub(r'[^\w\s]', '', texto)
        texto = re.sub(r'\s+', ' ', texto).strip()
        return texto

    def __calcular_estadísticas(self, texto):
        palabras = texto.split()
        return {
            'total_palabras': len(palabras),
            'palabras_únicas': len(set(palabras)),
            'longitud_promedio': sum(len(p) for p in palabras) / len(palabras) if palabras else 0
        }

    def obtener_estadísticas(self):
        return self._estadísticas.copy()

# 4. Métodos privados en herencia
class Base:
    def método_público(self):
        print("Base: Llamando a mi propio método privado...")
        self.__método_privado()

    def __método_privado(self):
        print("Este es el secreto de la clase Base")

class Derivada(Base):
    def __método_privado(self):
        print("Este es el secreto de la clase Derivada")

# 5. Métodos protegidos (Uso de un solo guion bajo)
class Forma:
    def __init__(self):
        self._tipo = "Forma genérica"

    def calcular_área(self):
        return self._obtener_área()

    def _obtener_área(self):
        raise NotImplementedError("Subclases deben implementar _obtener_área")

    def _validar_dimensiones(self, valor):
        if not isinstance(valor, (int, float)) or valor <= 0:
            raise ValueError("Las dimensiones deben ser números positivos")
        return True

class Circulo(Forma):
    def __init__(self, radio):
        super().__init__()
        self._validar_dimensiones(radio)
        self._radio = radio

    def _obtener_área(self):
        return math.pi * self._radio ** 2

# 6. Ejemplo práctico: Validación de datos complejos
class Formulario:
    def __init__(self):
        self._datos = {}
        self._errores = {}

    def validar(self, datos):
        self._datos = datos.copy()
        self._errores = {}
        self.__validar_campos_requeridos()
        self.__validar_email()
        self.__validar_contraseña()
        return len(self._errores) == 0

    def obtener_errores(self):
        return self._errores

    def __validar_campos_requeridos(self):
        for campo in ['nombre', 'email', 'contraseña']:
            if campo not in self._datos or not self._datos[campo]:
                self._errores[campo] = "Campo obligatorio"

    def __validar_email(self):
        patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if 'email' in self._datos and not re.match(patron, self._datos['email']):
            self._errores['email'] = "Email inválido"

    def __validar_contraseña(self):
        if 'contraseña' in self._datos:
            contraseña = self._datos['contraseña']
            if len(contraseña) < 8:
                self._errores['contraseña'] = "Mínimo 8 caracteres"

# ===========================================================
# PUNTO DE SALIDA (Pruebas de ejecución)
# ===========================================================
if __name__ == "__main__":
    print("=== 1. PRUEBA AUTENTICADOR ===")
    auth = Autenticador("admin", "12345")
    print(f"¿Contraseña correcta?: {auth.verificar_contraseña('12345')}")
    # Intentar acceder al método privado fallará:
    try:
        auth.__generar_hash("hacker")
    except AttributeError:
        print("Éxito: No se puede acceder a __generar_hash desde fuera.")

    print("\n=== 2. PRUEBA PROCESADOR TEXTO ===")
    proc = ProcesadorTexto()
    proc.procesar_archivo_directo("Hola mundo! Este es un TEST, test de Python.")
    print(f"Estadísticas: {proc.obtener_estadísticas()}")

    print("\n=== 4. PRUEBA HERENCIA (Name Mangling) ===")
    d = Derivada()
    d.método_público() # Ejecuta el privado de Base
    d._Derivada__método_privado() # Ejecuta el privado de Derivada

    print("\n=== 5. PRUEBA MÉTODOS PROTEGIDOS ===")
    c = Circulo(10)
    print(f"Área del círculo: {c.calcular_área():.2f}")

    print("\n=== 6. PRUEBA FORMULARIO ===")
    f = Formulario()
    datos_malos = {"nombre": "Pepe", "email": "correo-falso", "contraseña": "123"}
    if not f.validar(datos_malos):
        print(f"Errores encontrados: {f.obtener_errores()}")