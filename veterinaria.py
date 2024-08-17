# Definimos  la clase Veterinaria
class Veterinaria:
    def __init__(self):
        # Inicializamos una lista vacía para almacenar los perros
        self.perros = []

    # metodo para registrar un perro en la veterinaria
    def registrar_perro(self, nombre, raza, edad, color_pelaje, dueño, peso, estado="NO ATENDIDO"):
        # Clasifica el perro como "Perro Grande" o "Perro Pequeño" basado en su peso
        tipo_perro = "Perro Pequeño" if peso < 10 else "Perro Grande"
        # Cambia automáticamente el estado a "ATENDIDO"
        estado = "ATENDIDO"
        # Crea un diccionario que almacena los detalles del perro
        perro = {
            "Nombre": nombre,
            "Raza": raza,
            "Edad": edad,
            "Color del pelaje": color_pelaje,
            "Dueño": dueño,
            "Peso": peso,
            "Estado": estado,
            "Tipo": tipo_perro
        }
        # Agrega el diccionario del perro a la lista de perros
        self.perros.append(perro)
        # Muestra un mensaje confirmando el registro del perro
        print(f"{nombre} ha sido registrado como {tipo_perro} y su estado es {estado}.")

    # Método para mostrar todos los perros registrados en la veterinaria
    def mostrar_perros(self):
        # Recorre la lista de perros y muestra los detalles de cada uno
        for perro in self.perros:
            print(perro)

# Ejemplo de uso interactivo de la clase Veterinaria
veterinaria = Veterinaria()

# Bucle para permitir al usuario registrar múltiples perros
while True:
    print("\nRegistro de perros en la veterinaria")
    nombre = input("Nombre del perro: ")
    raza = input("Raza del perro: ")
    edad = int(input("Edad del perro: "))
    color_pelaje = input("Color del pelaje: ")
    dueño = input("Nombre del dueño: ")
    peso = float(input("Peso del perro en kg: "))

    # Registrar el perro con los datos ingresados
    veterinaria.registrar_perro(nombre, raza, edad, color_pelaje, dueño, peso)
    
    # Preguntar al usuario si desea registrar otro perro
    continuar = input("¿Desea registrar otro perro? (s/n): ").lower()
    if continuar != 's':
        break

# Mostrar todos los perros registrados
print("\nPerros registrados en la veterinaria:")
veterinaria.mostrar_perros()
