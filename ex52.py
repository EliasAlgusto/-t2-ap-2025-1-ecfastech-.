
def diagonais_matriz():
    n=int(input("Digite o tamanho da matriz (n x n): "))
    matriz= []

    for i in range(n):
        linha= []
        for j in range(n):
            valor= int(input(f"Elemento [{i+1}][{j+1}]: "))
            linha.append(valor)
        matriz.append(linha)

    soma_principal = sum(matriz[i][i] for i in range(n))
    soma_secundaria = sum(matriz[i][n - 1 - i] for i in range(n))

    print("\n Resultados:")
    print(f"Soma diagonal principal: {soma_principal}")
    print(f"Soma diagonal secundária: {soma_secundaria}")
