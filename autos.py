# Definición de la clase ConcesionarioAutos
class ConcesionarioAutos:
    def __init__(self):
        # Inicializa una lista vacía para almacenar los autos
        self.autos = []

    # Método para registrar un auto en el concesionario
    def registrar_auto(self, marca, modelo, año, color, capacidad, tipo_combustible, transmision, kilometraje, precio_compra, es_importado):
        # Calcula el precio de venta del auto aplicando un margen de ganancia del 40%
        precio_venta = precio_compra * 1.40
        # Crea un diccionario que almacena los detalles del auto
        auto = {
            "Marca": marca,
            "Modelo": modelo,
            "Año": año,
            "Color": color,
            "Capacidad": capacidad,
            "Tipo de Combustible": tipo_combustible,
            "Transmisión": transmision,
            "Kilometraje": kilometraje,
            "Precio de Compra": precio_compra,
            "Importado": "Sí" if es_importado else "No",
            "Precio de Venta": precio_venta
        }
        # Agrega el diccionario del auto a la lista de autos
        self.autos.append(auto)
        # Muestra un mensaje confirmando el registro del auto con su precio de venta
        print(f"Auto {marca} {modelo} registrado con precio de venta de {precio_venta:.2f}.")

    # Método para mostrar todos los autos registrados en el concesionario
    def mostrar_autos(self):
        # Recorre la lista de autos y muestra los detalles de cada uno
        for auto in self.autos:
            print(auto)

# Ejemplo de uso interactivo de la clase ConcesionarioAutos
concesionario = ConcesionarioAutos()

# Bucle para permitir al usuario registrar múltiples autos
while True:
    print("\nRegistro de autos en el concesionario")
    marca = input("Ingrese la marca del auto: ")
    modelo = input("Ingrese el modelo del auto: ")
    año = input("Ingrese el año del auto: ")
    color = input("Ingrese el color del auto: ")
    capacidad = input("Ingrese la capacidad (número de pasajeros): ")
    tipo_combustible = input("Ingrese el tipo de combustible (Gasolina, Diesel, etc.): ")
    transmision = input("Ingrese el tipo de transmisión (Automática, Manual): ")
    kilometraje = input("Ingrese el kilometraje del auto: ")
    precio_compra = float(input("Ingrese el precio de compra del auto: "))
    es_importado = input("¿El auto es importado? (s/n): ").lower() == 's'

    # Registrar el auto con los datos ingresados
    concesionario.registrar_auto(marca, modelo, año, color, capacidad, tipo_combustible, transmision, kilometraje, precio_compra, es_importado)
    
    # Preguntar al usuario si desea registrar otro auto
    continuar = input("¿Desea registrar otro auto? (s/n): ").lower()
    if continuar != 's':
        break

# Mostrar todos los autos registrados
print("\nAutos registrados en el concesionario:")
concesionario.mostrar_autos()
