from lib.rede import Rede


data_matriz = [
    [1, 9],
    [2, 3],
    [5, 20],
    [8, 7],
    [6, 13],
    [21, 16],
    [15, 3],
    [11, 17],
    [7, 2],
    [5, 19],
]

results = [1, 0, 0, 0, 0, 0, 1, 1, 1, 1]

if __name__ == "__main__":
    nn = Rede(
        numero_camadas_centrais=2, 
        quantidade_neuronios_centrais=5, 
        quantidade_neuronios_entrada=2
    )

    for data in data_matriz:
        print(nn.treinar(data))