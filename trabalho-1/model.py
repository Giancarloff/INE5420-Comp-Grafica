class Ponto:
    '''
    Basicamente uma tupla de floats
    '''

    def __init__(self, nome: str, *coords: float) -> None:
        '''
        Exemplo: um ponto P em R³ seria inicializado como P = Ponto(x, y, z) com x, y e z floats
        '''
        dim = len(coords)
        if dim < 1:
            raise ValueError("Espera-se pelo menos uma coordenada para o ponto.")
        
        for x in coords:
            if not isinstance(x, float) and not isinstance(x, int):
                raise TypeError("Espera-se coordenadas numéricas.")

        self.__coordenadas = coords
        self.__dimensao = dim
        self.__nome = nome

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

    @property
    def nome(self):
        return self.__nome

    def coordenada_em(self, eixo: int) -> float:
        '''
        Qual o valor da coordenada deste ponto no eixo dado. 
        '''
        if (eixo < self.dimensao):
            return self.__coordenadas
        else:
            raise IndexError(f"Esse ponto não tem coordenada no eixo {eixo}.")

    def mover(self, dx, dy):
        coords_antigas = self.coordenadas
        self.__coordenadas = (self.coordenadas[0] + dx, self.coordenadas[1] + dy)
        del coords_antigas
    

class Reta:
    '''
    Segmento de reta
    '''

    def __init__(self, nome: str, pontos: list[Ponto]) -> None:
        self.__nome = nome
        self.__pontos = pontos

    @property
    def pontos(self):
        return self.__pontos

class Wireframe:
    '''
    Pontos com retas traçadas entre eles
    '''
    def __init__(self, nome: str, pontos: list[Ponto], retas: dict) -> None:
        self.__pontos = pontos
        self.__retas = retas
        self.__nome = nome

    @property
    def pontos(self):
        return self.__pontos
    
    @property
    def retas(self):
        return self.__retas
    
    @property
    def nome(self):
        return self.__nome
    
class DisplayFile:
    '''
    Lista de todos os objetos representados (pex. pontos, retas e polígonos)
    '''

    def __init__(self, objetos: list[Ponto | Reta | Wireframe]) -> None:
        self.__objetos = objetos
        self.__contador = 0

    @property
    def objetos(self):
        return self.__objetos
    
    def novo_ponto_2d(self, x, y):
        for obj in self.__objetos:
            if isinstance(obj, Ponto):
                if obj.coordenadas == (x, y): # XXX: Essa comparação é arriscada e só funciona em 2D
                    return
        
        self.__contador += 1
        ponto = Ponto(str(self.__contador), x, y)
        self.objetos.append(ponto)
        print(f"PONTO {self.__contador} ADD {x} {y}")
        return ponto
    
    def nova_reta_2d(self, pontos: list[Ponto]):
        self.__contador += 1
        reta = Reta(str(self.__contador), pontos)
        for obj in self.objetos:
            if isinstance(obj, Reta):
                if not isinstance(obj.pontos, Ponto): # XXX: Não sei por que precisa desse if, mas não funciona de outra forma
                    p1, p2 = obj.pontos
                    r1, r2 = reta.pontos
                    if p1 == p2 and r1 == r2:
                        del reta
                        return
            
        self.objetos.append(reta)
        return reta