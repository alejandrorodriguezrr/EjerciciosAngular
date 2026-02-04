class alumno:
    def __init__(self, identificador=None, nombre="", edad=None, calificaciones=None):
        self.__identificador = identificador
        self.__nombre = nombre
        self.__edad = edad
        self.__calificaciones = calificaciones if calificaciones is not None else {}

    @property
    def identificador(self):
        return self.__identificador

    @identificador.setter
    def identificador(self, valor):
        self.__identificador = valor

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):
        self.__nombre = valor

    @property
    def edad(self):
        return self.__edad

    @edad.setter
    def edad(self, valor):
        self.__edad = valor

    @property
    def calificaciones(self):
        return self.__calificaciones

    @calificaciones.setter
    def calificaciones(self, valor):
        self.__calificaciones = valor

