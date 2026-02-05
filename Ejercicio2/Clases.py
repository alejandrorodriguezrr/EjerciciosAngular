class empresa():
    cont=0
    def __init__(self, id=None,nombre=None):
        self.__id = id
        self.__nombre = nombre

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self,id):
        self.__id = id
    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self,nombre):
        self.__nombre = nombre

class videojuegos(empresa):

    def __init__(self, id=None,nombre=None, plataforma=None, stock_por_tienda=None):
        super().__init__(id,nombre)
        self.__plataforma = plataforma
        self.__stock_por_tienda = stock_por_tienda if stock_por_tienda is not None else {}

    @property
    def plataforma(self):
        return self.__plataforma

    @plataforma.setter
    def plataforma(self,plataforma):
        self.__plataforma = plataforma

    @property
    def stock_por_tienda(self):
        return self.__stock_por_tienda

    @stock_por_tienda.setter
    def stock_por_tienda(self,stock_por_tienda):
        self.__stock_por_tienda = stock_por_tienda

