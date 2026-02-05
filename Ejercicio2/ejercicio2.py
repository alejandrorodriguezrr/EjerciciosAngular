from Clases import videojuegos

def opcion1(listado):
    cl=videojuegos()

    while True:
        cl.id=int(input("Ingrese el id del juego"))

        for juego in listado:
            if juego.id==cl.id:
                print("El id del juego ya existe")
                cl.id = int(input("Ingrese otro id del juego"))
            else:
                break

        cl.nombre=input("Ingrese su nombre")
        cl.plataforma=input("Ingrese la plataforma del juego")
        cl.stock_por_tienda={}
        num_ciudades=int(input("Ingrese el numero de ciudades que quieres añadir"))

        for i in range(num_ciudades):
            nom_ciudad=input(f"Ingrese el numero de la ciudad {i+1}:")
            stock=int(input("Ingrese el stock del juego"))
            cl.stock_por_tienda[nom_ciudad]=stock

        return cl

def opcion2(listado):

    id=int(input("Ingrese el id del juego a buscar el stock"))
    suma=0
    for juego in listado:
        if juego.id==id:
            for stock in juego.stock_por_tienda:
                suma+=juego.stock_por_tienda[stock]
        else:
            print("El id del juego no existe")

    print("Stock disponible",suma)

def opcion3(listado):
    id=int(input("Ingrese el id del juego a buscar el stock"))

    for juego in listado:
        if listado[juego].id==id:
            del listado[juego]
            print("Videojuego borrado")

def opcion4(listado):
    id=int(input("Ingrese el id del juego a buscar el stock"))
    encontrado=False

    for juego in listado:
        if juego.id==id:
            encontrado=True

            nom_ciudad = input("Ingrese el nombre de la ciudad que quieres buscar")

            if nom_ciudad in juego.stock_por_tienda:
                cantidad=juego.stock_por_tienda[nom_ciudad]
                if cantidad>0:
                    if cantidad > 0:
                        print(f"Sí hay stock en {nom_ciudad}. Cantidad: {cantidad}")
                    else:
                        print(f"No hay stock en {nom_ciudad}. Cantidad: {cantidad}")
                else:
                    print("Esa ciudad no existe en el stock de este juego")

                return

    if not encontrado:
        print("El id no existe")

def opcion5(listado):
    nom_ciudad=input("Introduzca el nombre de la ciudad que quieres buscar")
    encontrado=False

    for juego in listado:
        if nom_ciudad in juego.stock_por_tienda:
            encontrado=True
            cantidad=juego.stock_por_tienda[nom_ciudad]
            if cantidad>0:
                print("Nombre: ",juego.nombre, "plataforma: ",juego.plataforma, "unidades disponibles: ",cantidad)
            else:
                print("No tiene unidades disponibles")

        if not encontrado:
            print("Esa ciudad no existe")

def menu():

    inventario=[]
    while True:
        print("========= Menu ==========")
        print("[1] Registrar nuevo juego")
        print("[2] Mostrar numero total de unidades")
        print("[3] Eliminar juego")
        print("[4] Si hay stock del juego")
        print("[5] Genenerar listado")
        print("[6] Salir")
        print("======== FIN Menu ==========")
        print("")
        opcion=int(input("Ingrese su opcion"))

        if opcion==1:
            cl=opcion1(inventario)
            inventario.append(cl)
        elif opcion==2:
            opcion2(inventario)
        elif opcion==3:
            opcion3(inventario)
        elif opcion==4:
            opcion4(inventario)
        elif opcion==5:
            opcion5(inventario)
        elif opcion==6:
            break



menu()