from typing import Callable
from math import exp
from random import randint


def get_random_float():
  return randint(100, 1000) / 1000

def sigmoid(x):
    return  1.0/(1.0 + exp(-x))


class Base:
    def __init__(
        self, 
        activation_function: Callable = sigmoid, 
        learning_hating: float = 0.1
    ):
        self.activation_function = activation_function
        self.learning_hating = learning_hating
