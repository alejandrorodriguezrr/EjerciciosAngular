from Alumno import alumno

def añadiralumno():
    al = alumno()
    al.identificador=int(input("Ingrese el id del alumno"))
    al.nombre=input("Ingrese el nombre")
    al.edad=int(input("Ingrese la edad"))
    al.calificaciones={}

    num_asig=int(input("Ingrese el numero de asignaturas"))

    for i in range(num_asig):
        asignatura = input(f"Nombre de la asignatura {i+1}: ")
        nota=float(input("Ingrese la nota"))
        al.calificaciones[asignatura]=nota

    return al

def mostraralumnos(alumnos):
    for al in alumnos:
        print(al.identificador,al.nombre,al.edad,al.calificaciones)

def buscaralumno(alumnos):
    id=int(input("Ingrese el id del alumno a buscar"))
    for al in alumnos:
        if al.identificador == id:
            print(al.identificador,al.nombre,al.edad,al.calificaciones)
            return

def calcularmedia(alumnos):
    id=int(input("Ingrese el id del alumno a buscar"))

    for al in alumnos:
        if al.identificador == id:
            media=sum(al.calificaciones.values())/len(al.calificaciones)
            print(al.nombre,"tiene una media de",media)

def eliminaralumno(alumnos):
    id=int(input("Ingrese el id del alumno a eliminar"))
    for al in alumnos:
        if al.identificador == id:
            alumnos.remove(al)

def menu():
    alumnos=[]

    while True:
        print("========== MENU ==========")
        print("1.- AÑADIR ALUMNO")
        print("2.- MOSTRAR ALUMNOS")
        print("3.- BUSCAR ALUMNO")
        print("4.- CALCULAR MEDIA")
        print("5.- ELIMINAR ALUMNO")
        print("6.- SAIR")
        print("========= END MENU ==========")
        print("")
        opcion=int(input("Ingrese la opcion del menu"))

        if opcion==1:
            al = añadiralumno()
            alumnos.append(al)
        elif opcion==2:
            mostraralumnos(alumnos)
        elif opcion==3:
            buscaralumno(alumnos)
        elif opcion==4:
            calcularmedia(alumnos)
        elif opcion==5:
            eliminaralumno(alumnos)
        elif opcion==6:
            break

menu()