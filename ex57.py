
def verificar_matriz_quadrada(matriz):
    linhas = len(matriz)
    quadrada = True

    for linha in matriz:
        if len(linha) != linhas:
            quadrada = False
            break

    print(quadrada)

matriz = [
    [10, 20],
    [30, 40],
    [50, 60]
]
verificar_matriz_quadrada(matriz)  # Saída esperada: False
