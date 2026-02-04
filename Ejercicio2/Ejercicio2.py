class Producto:
    contador = 0

    def __init__(self):
        Producto.contador += 1
        self.codigo = f"VG{Producto.contador:03d}"
        self.nombre = ""

    def pedirDatos(self):
        self.nombre = input("Ingrese el nombre del producto: ").strip()


class Videojuego(Producto):
    def __init__(self):
        super().__init__()
        self.plataforma = ""
        self.stock = {}  # diccionario: ciudad -> unidades

    def crearVideojuego(self):
        super().pedirDatos()
        self.plataforma = input("Ingrese el nombre de la plataforma: ").strip()

        num_ciudades = int(input("Ingrese el numero de ciudades: "))

        for i in range(num_ciudades):
            nom_ciudad = input("Ingrese el nombre de la ciudad: ").strip()
            unidades = int(input("Ingrese el numero de stock: "))
            self.stock[nom_ciudad] = unidades

        return self  # devuelve el objeto ya relleno

inventario = []

cantidad = int(input("¿Cuántos videojuegos quieres añadir? "))

for i in range(cantidad):
    v = Videojuego()
    v.crearVideojuego()
    inventario.append(v)

# Mostrar inventario
for v in inventario:
    print(v.codigo, v.nombre, v.plataforma, v.stock)
