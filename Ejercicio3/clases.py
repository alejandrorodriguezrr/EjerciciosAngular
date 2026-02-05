class libro:
    def __init__(self, codigo, titulo, autores, stock):
        self.__codigo = codigo
        self.__titulo = titulo
        self.__autores = autores if autores is not None else []
        self.__stock = stock if stock is not None else []

    @property
    def codigo(self):
        return self.__codigo
    @codigo.setter
    def codigo(self, codigo):
        self.__codigo = codigo

    @property
    def titulo(self):
        return self.__titulo
    @titulo.setter
    def titulo(self, titulo):
        self.__titulo = titulo

    @property
    def autores(self):
        return self.__autores
    @autores.setter
    def autores(self, autores):
        self.__autores = autores

    @property
    def stock(self):
        return self.__stock
    @stock.setter
    def nombre(self, stock):
        self.__stock = stock

    def __str__(self):
        return f"Libro(codigo='{self.codigo}', titulo='{self.titulo}', autores={self.autores}, stock={[str(s) for s in self.stock]})"


class StockSucursal:
    def __init__(self, nombre_sucursal: str, ejemplares: int):
        self.__nombre_sucursal = nombre_sucursal
        self.__ejemplares = ejemplares

    @property
    def nombre_sucursal(self):
        return self.__nombre_sucursal
    @nombre_sucursal.setter
    def nombre_sucursal(self, nombre_sucursal):
        self.__nombre_sucursal = nombre_sucursal

    @property
    def ejemplares(self):
        return self.__ejemplares
    @ejemplares.setter
    def ejemplares(self, ejemplares):
        self.__ejemplares = ejemplares

    def __str__(self):
        return f"{self.nombre_sucursal}: {self.ejemplares}"
