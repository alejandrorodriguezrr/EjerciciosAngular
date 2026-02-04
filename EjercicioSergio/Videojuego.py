class Producto:
    def __init__(self, codigo=None, nombre=None):
        self.__codigo = codigo
        self.__nombre = nombre
    @property
    def codigo(self):
        return self.__codigo
    @property
    def nombre(self):
        return self.__nombre
    @codigo.setter
    def codigo(self,codigo):
        self.__codigo = codigo
    @nombre.setter
    def nombre(self,nombre):
        self.__nombre = nombre


class Videojuego(Producto):
    def __init__(self, codigo=None, nombre=None, plataforma=None, stock_por_tienda=None):
        super().__init__(codigo, nombre)
        self.__plataforma = plataforma
        self.__stock_por_tienda = stock_por_tienda
    @property
    def plataforma(self):
        return self.__plataforma
    @property
    def stock_por_tienda(self):
        return self.__stock_por_tienda
    @plataforma.setter
    def plataforma(self,plataforma):
        self.__plataforma = plataforma
    @stock_por_tienda.setter
    def stock_por_tienda(self,stock_por_tienda):
        self.__stock_por_tienda = stock_por_tienda
    def totalunidadesdisponible(self):
        total=0
        for stock in self.__stock_por_tienda.values():
            total+=stock
        return total
    def uddisponiblesciudad(self,ciudad):
        if ciudad not in self.__stock_por_tienda.keys():
            print("No existe esa tienda para ventas en este videojuego")
            return 0, False
        else:
            if self.__stock_por_tienda[ciudad]==0:
                print("No hay unidades disponibles en esa ciudad")
            return self.__stock_por_tienda[ciudad], True

