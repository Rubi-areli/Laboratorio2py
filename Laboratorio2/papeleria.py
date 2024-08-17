# clase Papeleria
class Papeleria:
    def __init__(self):
        # lista vacía para almacenar los productos
        self.productos = []

    # Método para registrar un producto en la papelería
    def registrar_producto(self, tipo, cantidad, precio_compra):
        # Calcula el precio de venta del producto aplicando un margen de ganancia del 30%
        precio_venta = precio_compra * 1.30
        # Crea un diccionario que almacena los detalles del producto
        producto = {
            "Tipo": tipo,
            "Cantidad": cantidad,
            "Precio de Compra": precio_compra,
            "Precio de Venta": precio_venta
        }
        # Agrega el diccionario del producto a la lista de productos
        self.productos.append(producto)
        # Muestra un mensaje confirmando el registro del producto con su precio de venta
        print(f"{tipo} registrado con precio de venta de {precio_venta:.2f}.")

    # Método para mostrar todos los productos registrados en la papelería
    def mostrar_productos(self):
        # Recorre la lista de productos y muestra los detalles de cada uno
        for producto in self.productos:
            print(producto)

# Ejemplo de uso interactivo de la clase Papeleria
papeleria = Papeleria()

# Bucle para permitir al usuario registrar múltiples productos
while True:
    print("\nRegistro de productos en la papelería")
    tipo = input("Ingrese el tipo de producto (Cuaderno 50 hojas, Cuaderno 100 hojas, Lápiz Grafito, Lápiz Colores): ")
    cantidad = int(input("Ingrese la cantidad de productos: "))
    precio_compra = float(input("Ingrese el precio de compra del producto: "))

    # Registrar el producto con los datos ingresados
    papeleria.registrar_producto(tipo, cantidad, precio_compra)
    
    # Preguntar al usuario si desea registrar otro producto
    continuar = input("¿Desea registrar otro producto? (s/n): ").lower()
    if continuar != 's':
        break

# Mostrar todos los productos registrados
print("\nProductos registrados en la papelería:")
papeleria.mostrar_productos()
