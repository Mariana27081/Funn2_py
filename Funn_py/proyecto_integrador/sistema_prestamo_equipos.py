import datetime

# Estructura inicial del inventario
# Llave: Nombre del equipo
# Valor: Diccionario con 'disponible' (Booleano) y 'historial' (Lista de tuplas)
inventario = {
    "Laptop Dell": {"disponible": True, "historial": []},
    "Tablet Samsung": {"disponible": True, "historial": []},
    "Proyector Epson": {"disponible": True, "historial": []}
}

def mostrar_equipos():
    """Muestra todos los equipos y su estado actual."""
    print("\n--- ESTADO DEL INVENTARIO ---")
    for nombre, info in inventario.items():
        estado = "Disponible" if info["disponible"] else "Prestado"
        print(f"Equipo: {nombre:15} | Estado: {estado}")

def registrar_prestamo():
    """Registra un préstamo validando disponibilidad."""
    mostrar_equipos()
    nombre_equipo = input("\nIngrese el nombre exacto del equipo a prestar: ")
    
    if nombre_equipo in inventario:
        if inventario[nombre_equipo]["disponible"]:
            usuario = input("Nombre del usuario: ")
            fecha = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
            
            # Uso de TUPLA para integridad de datos (Usuario, Fecha)
            datos_prestamo = (usuario, fecha)
            
            # Uso de LISTA para el historial
            inventario[nombre_equipo]["historial"].append(datos_prestamo)
            inventario[nombre_equipo]["disponible"] = False
            
            print(f"¡Éxito! El equipo '{nombre_equipo}' ha sido prestado a {usuario}.")
        else:
            print("Error: El equipo ya se encuentra prestado.")
    else:
        print("Error: El equipo no existe en el sistema.")

def devolver_equipo():
    """Marca un equipo como disponible nuevamente."""
    nombre_equipo = input("\nIngrese el nombre del equipo que desea devolver: ")
    
    if nombre_equipo in inventario:
        if not inventario[nombre_equipo]["disponible"]:
            inventario[nombre_equipo]["disponible"] = True
            print(f"¡Éxito! El equipo '{nombre_equipo}' ha sido devuelto y está disponible.")
        else:
            print("El equipo ya estaba marcado como disponible.")
    else:
        print("Error: El equipo no existe.")

def ver_historial():
    """Muestra la lista de préstamos de cada equipo."""
    print("\n--- HISTORIAL DE PRÉSTAMOS ---")
    for nombre, info in inventario.items():
        print(f"\nEquipo: {nombre}")
        if not info["historial"]:
            print("   Sin préstamos registrados.")
        else:
            for prestamo in info["historial"]:
                # Desempaquetado de tupla
                usuario, fecha = prestamo
                print(f"   - Usuario: {usuario} | Fecha: {fecha}")

def agregar_equipo():
    """Añade un nuevo equipo al diccionario principal."""
    nuevo_nombre = input("\nIngrese el nombre del nuevo equipo: ")
    
    if nuevo_nombre not in inventario:
        inventario[nuevo_nombre] = {"disponible": True, "historial": []}
        print(f"Equipo '{nuevo_nombre}' registrado correctamente.")
    else:
        print("Error: El equipo ya existe en el inventario.")

def menu():
    """Función principal que gestiona el flujo del programa."""
    while True:
        print("\n==============================")
        print(" SISTEMA DE PRÉSTAMOS EQUIPOS")
        print("==============================")
        print("1. Ver equipos disponibles")
        print("2. Registrar préstamo")
        print("3. Devolver equipo")
        print("4. Ver historial de préstamos")
        print("5. Agregar nuevo equipo")
        print("6. Salir")
        
        opcion = input("\nSeleccione una opción (1-6): ")
        
        if opcion == "1":
            mostrar_equipos()
        elif opcion == "2":
            registrar_prestamo()
        elif opcion == "3":
            devolver_equipo()
        elif opcion == "4":
            ver_historial()
        elif opcion == "5":
            agregar_equipo()
        elif opcion == "6":
            print("Saliendo del sistema... ¡Hasta pronto!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

# Punto de entrada del script
if __name__ == "__main__":
    menu()