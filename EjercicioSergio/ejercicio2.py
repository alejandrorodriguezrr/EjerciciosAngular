from Videojuego import Videojuego

def validarcodigo(codigo,listado):
    if not listado:
        return True
    else:
        for videojuego in listado:
            if codigo==videojuego.codigo:
                return False
        return True
def registrar(listado):
    videojuego=Videojuego()
    videojuego.codigo=input("Introduce el codigo:")
    if not validarcodigo(videojuego.codigo,listado):
        print("Codigo repetido intentelo de nuevo")
        return
    videojuego.nombre=input("Introduce el nombre del videojuego")
    videojuego.plataforma=input("Introduce el nombre del plataforma")
    videojuego.stock_por_tienda={}
    while True:
        nombre=input("Introduce el nombre de la ciudad")
        stock=0
        me=0
        if nombre in videojuego.stock_por_tienda.keys():
            print("Ciudad repetida")
        else:
            while True:
                try:
                    stock=int(input("Introduzca cantidad del stock"))
                    break
                except:
                    print("Error número")
            videojuego.stock_por_tienda[nombre]=stock
        while True:
            try:
                me=int(input("1 añadir más ciudades\n"
                             "2 terminar"))
                if me!=1 and me!=2:
                    ("Valor invalido")
                else:
                    break
            except ValueError:
                print("Formato número")
        if me==2:
            break
    listado.append(videojuego)
    return videojuego


def udporvideojuego(listado):
    codigo=input("Introduzca el codigo")
    ok=False
    for videojuego in listado:
        if videojuego.codigo==codigo:
            total=videojuego.totalunidadesdisponible()
            print("Total de unidades disponibles:",total)
            ok=True
    if not ok:
        print("Videojuego no encontrado")

def eliminar(listado):
    codborrar=input("Introduzca el codigo a borrar")
    listadonuevo=[]
    ok=False
    for videojuego in listado:
        if videojuego.codigo==codborrar:
            print("Videojuego borrado")
            ok=True
        else:
            listadonuevo.append(videojuego)
    if not ok:
        print("No se encontró el videojuego")
        return
    else:

        return listadonuevo

def unidadesporciudad(listado):
    codigo=input("Introduzca el codigo")
    for videojuego in listado:
        if videojuego.codigo==codigo:
            ciudad=input("Introduzca el nombre de la ciudad")
            cantidad, ok=videojuego.uddisponiblesciudad(ciudad)
            if ok:
                print(f"Ciudad {ciudad} - cantidad:{cantidad}")
            return
    return

def videojuegosporciudad(listado):
    ciudad=input("Introduzca el nombre de la ciudad")
    videojuegos=[]
    for videojuego in listado:
        for ciudades in videojuego.stock_por_tienda.keys():
            if ciudad==ciudades:
                videojuegos.append(videojuego.nombre)
    for v in videojuegos:
        print(v)



#main
listado=[]
while True:
    menu=""
    while True:
        try:
            menu=int(input("1 Registrar nuevo juego\n"
                           "2 Calcular y mostrar el número de ud disponibles de un videojuego\n"
                           "3 Eliminar un videojuego por codigo\n"
                           "4 Dado un codigo de videojuego y una ciduad comprobar el stock\n"
                           "5 Dado una ciduda generar un listado de videojuegos disponibles\n"
                           "6 Finalizar"))
            if menu<1 or menu>6:
                print("Opcion invalida")
            else:
                break
        except ValueError:
            print("Valor invalido")
    match menu:
        case 1:
            registrar(listado)
        case 2:
            udporvideojuego(listado)
        case 3:
            listado=eliminar(listado)
        case 4:
            unidadesporciudad(listado)
        case 5:
            videojuegosporciudad(listado)
        case 6:
            print("Saliendo")
            break
        case _:
            print("Opcion invalida")


