from functools import reduce
from typing import Callable
from math import exp
from random import randint


def get_random_float():
  return randint(100, 1000) / 1000

def sigmoid(x):
    return  1.0/(1.0 + exp(-x))

def dev_sigmoid(x):
    return sigmoid(x) * (1 - sigmoid(x))


class Base:
    def __init__(
        self, 
        activation_function: Callable = sigmoid,
        derivate_activation_function: Callable = dev_sigmoid,
        step_functon: Callable = lambda x: round(reduce(lambda prev, curr: prev + curr, x, 0)),
        learning_hating: float = 0.1
    ):
        self.activation_function = activation_function
        self.derivate_activation_function = derivate_activation_function
        self.step_function = step_functon
        self.learning_hating = learning_hating
