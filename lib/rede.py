from typing import List

from .utils import Base
from .camada import Camada


class Rede(Base):
    def __init__(self, 
        numero_camadas_centrais = 1, 
        quantidade_neuronios_centrais = 5, 
        quantidade_neuronios_entrada = 1, 
        quantidade_neuronios_saida = 1, 
        *args
    ):
        super().__init__(*args)
        self.numero_camadas = numero_camadas_centrais + 2

        self.camada_entrada = Camada(quantidade_neuronios_entrada, *args)
        self.camadas_centrais = [Camada(quantidade_neuronios_centrais, *args) for _ in range(0, self.numero_camadas - 2)]
        self.camada_saida = Camada(quantidade_neuronios_saida, *args)

        self.camadas: List[Camada] = [
            self.camada_entrada, 
            *self.camadas_centrais, 
            self.camada_saida
        ]

    def treinar(self, _entrada: List[float]):
        entrada = _entrada
        
        for camada in self.camadas:
            saida = camada.treinar(entrada)
            entrada = saida

        return saida
