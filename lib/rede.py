from typing import List

from .utils import Base
from .camada import Camada


class Rede(Base):
    def __init__(self, 
        numero_camadas_centrais = 1, 
        quantidade_neuronios_centrais = 5, 
        quantidade_neuronios_entrada = 1, 
        quantidade_neuronios_saida = 1,
        **kwargs
    ):
        super().__init__(**kwargs)
        self.numero_camadas = numero_camadas_centrais + 2

        self.camada_entrada = Camada(quantidade_neuronios_entrada, **kwargs)
        self.camadas_centrais = [Camada(quantidade_neuronios_centrais, **kwargs) for _ in range(0, self.numero_camadas - 2)]
        self.camada_saida = Camada(quantidade_neuronios_saida, **kwargs)

        self.camadas: List[Camada] = [
            self.camada_entrada, 
            *self.camadas_centrais, 
            self.camada_saida
        ]
        
        self.taxa_de_aprendizagem = .1
        
    def testar(self, entrada):
        return self.feed_foward(entrada)
        
    def treinar(self, entrada: List[float], saida_esperada: int):
        saida_obtida = self.feed_foward(entrada)
        self.back_foward(saida_obtida, saida_esperada)
        return saida_obtida
        
    def feed_foward(self, _entrada: List[float]):
        entrada = _entrada
        
        for camada in self.camadas:
            saida = camada.feed_foward(entrada)
            entrada = saida

        return self.step_function(saida)
    
    def back_foward(self, saida_obtida: float, saida_esperada: float):
        camadas_invertidas = self.camadas
        camadas_invertidas.reverse()

        erro = saida_obtida - saida_esperada
        
        camadas_invertidas[0].back_foward(erro, self.taxa_de_aprendizagem)
        for camada in camadas_invertidas[0:-1]:
            camada.back_foward(erro, self.taxa_de_aprendizagem)

        camadas_invertidas.reverse()
