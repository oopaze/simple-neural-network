from typing import List

from .utils import get_random_float, Base


class Neuronio(Base):
    def __init__(self, *args):
        super().__init__(*args)
        self.peso = get_random_float()

    def feed_foward(self, entrada: List[float], bias: float):
        saida = sum(map(lambda x: x * self.peso, entrada)) + bias
        return self.activation_function(saida)
