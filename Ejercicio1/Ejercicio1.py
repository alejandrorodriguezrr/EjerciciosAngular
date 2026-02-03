class Alumno:

    def __init__(self, identificador=0, nombre="", edad=0, calificaciones=None):
        self.identificador = identificador
        self.nombre = nombre
        self.edad = edad
        self.calificaciones = calificaciones if calificaciones is not None else {}

    def pedirDatos(self):
        identificador = int(input("Ingrese el identificador del alumno: "))
        nombre = input("Ingrese el nombre del alumno: ")
        edad = int(input("Ingrese la edad del alumno: "))

        calificaciones = {}
        respuesta = "si"

        while respuesta.lower().strip() != "no":
            asignatura = input("Ingrese la asignatura del alumno: ").strip()
            nota = float(input("Ingrese la nota del alumno: ").replace(",", "."))
            calificaciones[asignatura] = nota
            respuesta = input("¿Desea añadir una asignatura nueva? (si/no): ")

        return Alumno(identificador, nombre, edad, calificaciones)


# ===== PROGRAMA PRINCIPAL (FUERA DE LA CLASE) =====
alumnos = []

cantidad = int(input("Ingrese la cantidad de alumnos: "))

for i in range(cantidad):
    print(f"\n--- Alumno {i+1} ---")
    alumno = Alumno().pedirDatos()
    alumnos.append(alumno)

print("\n=== ALUMNOS REGISTRADOS ===")
for alumno in alumnos:
    print(alumno, alumno.nombre, alumno.edad, alumno.calificaciones)
