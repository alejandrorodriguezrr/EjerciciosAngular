from clases import libro, StockSucursal

def opcion1(catalogo):
    codigo = input("Ingrese el codigo del libro: ")

    if codigo in catalogo:
        print("El codigo ya existe")
        return

    titulo = input("Ingrese el titulo del libro: ")
    autores = [input("Ingrese el autor del libro: ")]
    stock = []

    libro_nuevo = libro(codigo=codigo, titulo=titulo, autores=autores, stock=stock)

    while True:
        nombre = input("Ingrese el nombre de la ciudad: ")
        ejemplares = int(input("Ingrese el numero de ejemplar del libro: "))
        stock = StockSucursal(nombre_sucursal=nombre, ejemplares=ejemplares)
        libro_nuevo.stock.append(stock)

        respuesta = input("¿Desea añadir una sucursal mas?")

        if respuesta != "si":
            break

    catalogo[codigo]=libro_nuevo
    print("Libro añadido correctamente")


def opcion2(catalogo):
    for codigo, li in catalogo.items():
        print(li)

def opcion3(catalogo):
    cod=input("Ingrese el codigo del libro que quieras buscar: ")

    if cod in catalogo:
        print(catalogo[cod])
    else:
        print("El codigo no existe")


def menu():
    catalogo={}

    while True:
        print("============ Menu ============")
        print("1. Añadir un nuevo libro")
        print("2. Mostrar el catalogo")
        print("3. Buscar un libro por su codigo")
        print("4. Consultar el numero de ejemplares disponibles")
        print("5. Listar todos los libros disponibles en una sucursal")
        print("6. Calcular el numero total de ejemplares de un libro")
        print("7. Actualizar el stock de un libro")
        print("8. Eliminar un libro del catalogo")
        print("9. Eliminar una sucursal del sistema")
        print("10. Finalizar el programa")
        print("")
        opcion= int(input("Elije una opcion: "))

        if opcion == 1:
            opcion1(catalogo)
        elif opcion == 2:
            opcion2(catalogo)
        elif opcion == 3:
            opcion3(catalogo)

menu()
