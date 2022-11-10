from functools import reduce

from lib.rede import Rede
from lib.utils import sigmoid

base_data_matriz = [
    [1, 0],
    [0, 1],
    [1, 1],
    [0, 0]
]
base_results = [1, 1, 0, 0]


data_matriz, results = [], []
for i in range(0, 100):
  data_matriz.extend(base_data_matriz)
  results.extend(base_results)


if __name__ == "__main__":
    nn = Rede(
        numero_camadas_centrais=2, 
        quantidade_neuronios_centrais=5, 
        quantidade_neuronios_entrada=2, 
        quantidade_neuronios_saida=1
    )

    __import__("ipdb").set_trace()

    for i, data in enumerate(data_matriz):
        print(nn.treinar(data, results[i]), results[i])
        
    __import__("ipdb").set_trace()
    
    print("Fim do teste!")