from typing import List

from .utils import get_random_float, Base
from .neuronio import Neuronio


class Camada(Base): 
    def __init__(self, numero_neuronios: int, *args):
        super().__init__(*args)

        self.bias = get_random_float()
        self.neuronios: List[Neuronio] = [
            Neuronio(*args) for _ in range(0, numero_neuronios)
        ]

    def treinar(self, entrada: List[float]):
        return list(map(
            lambda neuronio: neuronio.feed_foward(entrada, self.bias),
            self.neuronios
        ))
