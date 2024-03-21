from ponto import *

class Rn:

    '''
    Classe base tratando um espaço arbitrário como um R^n
    '''

    def __init__(self) -> None:
        self.__pontos = list()

    @property
    def pontos(self) -> list:
        return self.__pontos


class PlanoCartesiano(Rn):

    '''
    Plano Cartesiano comum com origem em (0, 0)
    '''

    def __init__(self, com_origem : bool = False) -> None:
        '''
        Inicializa um plano cartesiano. Se com_origem for True, adiciona um ponto (0.0, 0.0).
        '''
        super().__init__()
        self.__origem = None
        if com_origem:
            self.__origem = Ponto(0.0, 0.0)
            self.pontos.append(self.__origem)
        self.__qtd_eixos = 2
    
    @property
    def dimensao(self) -> int:
        return self.__qtd_eixos
    
    @property
    def origem(self) -> Ponto:
        '''
        Se o plano foi criado com com_origem False, retorna None.
        '''
        return self.__origem

    @property
    def O(self) -> Ponto:
        '''
        Outra forma de acessar a origem. Se o plano foi criado com com_origem False, retorna None.
        '''
        return self.__origem

    def novo_ponto(self, x, y) -> Ponto:
        if not isinstance(x, float) or not isinstance(y, float):
            raise ValueError("Esperava-se coordenadas x e y como floats.")
        
        P = Ponto(x, y)
        self.pontos.append(P)
        return P