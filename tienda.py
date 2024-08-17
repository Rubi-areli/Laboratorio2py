# clase AlmacenTecnologia
class AlmacenTecnologia:
    def __init__(self):
      #lista vacía para almacenar los productos    
        self.productos = []

    def registrar_producto(self, tipo, marca, modelo, precio_compra, es_importado):
        # Margen de ganancia del 70%
        # Crea un diccionario que almacena los detalles del producto
        precio_venta = precio_compra * 1.70
        producto = {
            "Tipo": tipo,
            "Marca": marca,
            "Modelo": modelo,
            "Precio de Compra": precio_compra,
            "Importado": "Sí" if es_importado else "No",
            "Precio de Venta": precio_venta
        }
        # Agrega el diccionario del producto a la lista de productos
        self.productos.append(producto)
        print(f"{tipo} {marca} {modelo} registrado con precio de venta de {precio_venta:.2f}.")
# Método para mostrar todos los productos registrados en el almacén
    def mostrar_productos(self):
        # Recorre la lista de productos y muestra los detalles de cada uno
        for producto in self.productos:
            print(producto)

# Ejemplo de uso interactivo
almacen = AlmacenTecnologia()
# Bucle para permitir al usuario registrar múltiples productos
while True:
    print("\nRegistro de productos en el almacén de tecnología")
    tipo = input("Ingrese el tipo de producto (Celular, Tablet, Laptop, etc.): ")
    marca = input("Ingrese la marca del producto: ")
    modelo = input("Ingrese el modelo del producto: ")
    precio_compra = float(input("Ingrese el precio de compra del producto: "))
    es_importado = input("¿El producto es importado? (s/n): ").lower() == 's'

    # Registrar el producto con los datos ingresados
    almacen.registrar_producto(tipo, marca, modelo, precio_compra, es_importado)
    # Preguntar al usuario si desea registrar otro producto
    continuar = input("¿Desea registrar otro producto? (s/n): ").lower()
    if continuar != 's':
        break

# Mostrar todos los productos registrados
print("\nProductos registrados en el almacén de tecnología:")
almacen.mostrar_productos()
