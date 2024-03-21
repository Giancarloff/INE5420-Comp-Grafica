class Ponto:

    def __init__(self, *coords: float) -> None:
        '''
        Exemplo: um ponto P em R³ seria inicializado como P = Ponto(x, y, z) com x, y e z floats
        '''
        dim = len(coords)
        if dim < 1:
            raise ValueError("Espera-se pelo menos uma coordenada para o ponto.")
        
        for x in coords:
            if not isinstance(x, float):
                raise TypeError("Espera-se coordenadas numéricas.")

        self.__coordenadas = coords
        self.__dimensao = dim

    def __repr__(self) -> str:
        P = "("
        for i, c in enumerate(self.coordenadas):
            if (i < self.dimensao - 1):
                P += f"{c}, "
            else:
                P += f"{c})"
        return P

    @property
    def dimensao(self) -> int:
        '''
        Em qual dimensão o ponto se encontra. Num plano, dimensao = 2. Num espaço, dimensao = 3 etc.
        '''
        return self.__dimensao

    @property
    def coordenadas(self) -> tuple:
        '''
        Tupla de coordenadas do ponto.
        '''
        return self.__coordenadas

    def coordenada_em(self, eixo: int) -> float:
        '''
        Qual o valor da coordenada deste ponto no eixo dado. 
        '''
        if (eixo < self.dimensao):
            return self.__coordenadas
        else:
            raise IndexError(f"Esse ponto não tem coordenada no eixo {eixo}.")
    
