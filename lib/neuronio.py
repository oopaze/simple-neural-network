from typing import List

from .utils import get_random_float, Base


class Neuronio(Base):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.peso = get_random_float()
        self.ultima_saida = None
        self.ultimo_erro = None

    def feed_foward(self, entrada: List[float], bias: float):
        saida = sum(map(lambda x: x * self.peso, entrada)) + bias
        self.ultima_saida = self.activation_function(saida)
        return self.ultima_saida
    
    def back_foward(self, erro: float, taxa_aprendizagem: float):
        self.peso = self.peso - erro * taxa_aprendizagem 
