class Propriedades:

    def __init__(self, base, parametro):
        self.__base = base
        self.__parametro = parametro

    def valor(self):
        return self.__base.avalia() +"."+ self.__parametro.avalia()

    @property
    def base(self):
        return self.__base

    @property
    def parametro(self):
        return self.__parametro

    def aceita(self,visitor):
        visitor.visita_subtracao(self)
