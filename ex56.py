

def matriz_indices():
    linhas=int(input("Digite o número de linhas: "))
    colunas=int(input("Digite o número de colunas: "))

    matriz= []

    for i in range(linhas):
        linha= []
        for j in range(colunas):
            linha.append(i * j)
        matriz.append(linha)

    print("\n Matriz gerada:")
    for linha in matriz:
        print(" ".join(f"{num:4}" for num in linha))

matriz_indices()
