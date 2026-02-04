from functools import total_ordering


class Producto():

    contador=0
    def pedirdatos(self):
        Producto.contador=Producto.contador+1
        codigo=f"VG{Producto.contador:03d}"
        nombre=input("Ingrese el nombre del videojuego: ")

        return codigo,nombre

class Videojuego(Producto):

    def pedirdatos(self):
        codigo, nombre=super().pedirdatos()
        plataforma=input("Ingrese la plataforma del videojuego: ")
        stock_por_tienda={}
        num_ciudades=int(input("Ingrese el numero de ciudades que quieres añadir: "))

        for ciudad in range(num_ciudades):
            nom_ciudad=input("Ingrese el nombre del ciudad: ")
            stock=int(input("Ingrese el numero de stock de esa ciudad: "))
            stock_por_tienda[nom_ciudad]=stock

        videojuego = [codigo, nombre, plataforma, stock_por_tienda]
        return videojuego

    def mostrar(self, videojuego):
        print("Videojuego(")
        print(f"  codigo='{videojuego[0]}',")
        print(f"  nombre='{videojuego[1]}',")
        print(f"  plataforma='{videojuego[2]}',")
        print(f"  stock_por_tienda={videojuego[3]}")
        print(")")

    def opcion2(self, videojuego):
        cod=input("Ingrese el codigo del videojuego: ")
        total=0







def menu():
    inventario=[]
    vg = Videojuego()

    while True:
        print("=== MENU ===")
        print("[1] Registrar")
        print("[2] Calcular")
        print("[3] Eliminar")
        print("[4] Stock")
        print("[5] Listado")
        print("[6] Salir")
        print("")
        opcion=int(input("Ingrese su opcion: "))

        if opcion==1:
            juego=vg.pedirdatos()
            inventario.append(juego)


menu()
