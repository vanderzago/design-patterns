class Subtracao:

    def __init__(self, expressao_esquerda, expressao_direita):
        self.__expressao_esquerda = expressao_esquerda
        self.__expressao_direita = expressao_direita

    def avalia(self):
        return self.__expressao_esquerda.avalia() - self.__expressao_direita.avalia()

    @property
    def expressao_esquerda(self):
        return self.__expressao_esquerda

    @property
    def expressao_direita(self):
        return self.__expressao_direita

    def aceita(self,visitor):
        visitor.visita_subtracao(self)

class Soma:

    def __init__(self, expressao_esquerda, expressao_direita):
        self.__expressao_esquerda = expressao_esquerda
        self.__expressao_direita = expressao_direita

    def avalia(self):
        return self.__expressao_esquerda.avalia() + self.__expressao_direita.avalia()

    @property
    def expressao_esquerda(self):
        return self.__expressao_esquerda

    @property
    def expressao_direita(self):
        return self.__expressao_direita

    def aceita(self,visitor):
        visitor.visita_soma(self)

class Numero:

    def __init__(self,numero):
        self.__numero = numero
    
    def avalia(self):
        return self.__numero

    def aceita(self,visitor):
        visitor.visita_numero(self)

if __name__ == '__main__':

    from impressao import Impressao

    expressao_esquerda = Soma(Soma(Numero(10),Numero(20)),Soma(Numero(50),Numero(4)))
    expressao_direita = Soma(Numero(5),Numero(2))
    expressao_conta = Soma(expressao_esquerda,expressao_direita)
    print expressao_conta.avalia()

    #expressao_conta = Subtracao(Numero(100),Numero(70))
    #print expressao_conta.avalia()

    impressao = Impressao()

    expressao_conta.aceita(impressao)