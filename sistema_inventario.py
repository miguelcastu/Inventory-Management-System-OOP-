# sistema_inventario.py

class Producto:
    def __init__(self, nombre: str, precio: float, cantidad: int):
        # Validaciones básicas
        if not nombre.strip():
            raise ValueError("El nombre del producto no puede estar vacío.")
        if precio < 0:
            raise ValueError("El precio no puede ser negativo.")
        if cantidad < 0:
            raise ValueError("La cantidad no puede ser negativa.")

        self.nombre = nombre.strip()
        self.precio = float(precio)
        self.cantidad = int(cantidad)

    def actualizar_precio(self, nuevo_precio):
        if nuevo_precio < 0:
            raise ValueError("El nuevo precio no puede ser negativo.")
        self.precio = float(nuevo_precio)

    def actualizar_cantidad(self, nueva_cantidad):
        if nueva_cantidad < 0:
            raise ValueError("La nueva cantidad no puede ser negativa.")
        self.cantidad = int(nueva_cantidad)

    def calcular_valor_total(self):
        return self.precio * self.cantidad

    def __str__(self):
        return (
            f"Producto: {self.nombre}\n"
            f"Precio: {self.precio:.2f} €\n"
            f"Cantidad: {self.cantidad}\n"
            f"Valor total: {self.calcular_valor_total():.2f} €"
        )


class Inventario:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto: Producto):
        if not isinstance(producto, Producto):
            raise TypeError("Solo se pueden agregar objetos de tipo Producto.")
        self.productos.append(producto)

    def buscar_producto(self, nombre):
        nombre = nombre.strip().lower()
        for prod in self.productos:
            if prod.nombre.lower() == nombre:
                return prod
        return None

    def calcular_valor_inventario(self):
        total = 0
        for p in self.productos:
            total += p.calcular_valor_total()
        return total

    def listar_productos(self):
        if not self.productos:
            print("El inventario está vacío.")
        else:
            print("\n======= LISTA DE PRODUCTOS =======")
            for p in self.productos:
                print(p)
                print("----------------------------------")


def menu_principal(inventario: Inventario):
    while True:
        print("\n=========== MENÚ PRINCIPAL ===========")
        print("1. Agregar producto")
        print("2. Buscar producto")
        print("3. Listar productos")
        print("4. Calcular valor total del inventario")
        print("5. Salir")
        print("======================================")

        opcion = input("Selecciona una opción: ")

        try:
            if opcion == "1":
                nombre = input("Nombre del producto: ").strip()
                precio = float(input("Precio del producto: "))
                cantidad = int(input("Cantidad: "))

                producto = Producto(nombre, precio, cantidad)
                inventario.agregar_producto(producto)
                print("\nProducto agregado correctamente.")

            elif opcion == "2":
                nombre_buscar = input("Nombre del producto a buscar: ")
                producto = inventario.buscar_producto(nombre_buscar)

                if producto:
                    print("\nProducto encontrado:")
                    print(producto)
                else:
                    print("Producto no encontrado.")

            elif opcion == "3":
                inventario.listar_productos()

            elif opcion == "4":
                total = inventario.calcular_valor_inventario()
                print(f"\nValor total del inventario: {total:.2f} €")

            elif opcion == "5":
                print("Saliendo del sistema. ¡Hasta pronto!")
                break

            else:
                print("Opción no válida. Intenta nuevamente.")

        except ValueError as ve:
            print(f"Error de valor: {ve}")
        except TypeError as te:
            print(f"Error de tipo: {te}")
        except Exception as e:
            print(f"Ocurrió un error inesperado: {e}")


if __name__ == "__main__":
    inventario = Inventario()
    menu_principal(inventario)
