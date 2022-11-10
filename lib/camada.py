from typing import List, Union

from .utils import get_random_float, Base
from .neuronio import Neuronio


class Camada(Base): 
    def __init__(self, numero_neuronios: int, **kwargs):
        super().__init__(**kwargs)

        self.bias = get_random_float()
        self.neuronios: List[Neuronio] = [
            Neuronio(**kwargs) for _ in range(0, numero_neuronios)
        ]
        
    @property
    def ultimas_saidas(self):
        return [neuronio.ultima_saida for neuronio in self.neuronios]
    
    @property
    def ultimos_erros(self):
        return [neuronio.ultimo_erro for neuronio in self.neuronios]

    def feed_foward(self, entrada: List[float]):
        return list(map(
            lambda neuronio: neuronio.feed_foward(entrada, self.bias),
            self.neuronios
        ))
        
    def back_foward(self, erro: Union[float, List[float]], taxa_aprendizagem: float):
        for i, neuronio in enumerate(self.neuronios):
            if isinstance(erro, (float, int)):
                neuronio.back_foward(erro, taxa_aprendizagem)
            else:
                neuronio.back_foward(erro[i], taxa_aprendizagem) 
                    
