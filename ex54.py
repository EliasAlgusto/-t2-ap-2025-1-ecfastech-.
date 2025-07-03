
def gerar_transposta():
    linhas=int(input("Digite o número de linhas da matriz original: "))
    colunas=int(input("Digite o número de colunas da matriz original: "))

    matriz= []

    for i in range(linhas):
        linha= []
        for j in range(colunas):
            valor = input(f"Elemento [{i+1}][{j+1}]: ")
            linha.append(valor)
        matriz.append(linha)

    transposta= []
    for j in range(colunas):
        nova_linha= []
        for i in range(linhas):
            nova_linha.append(matriz[i][j])
        transposta.append(nova_linha)

    print("\n Matriz transposta:")
    for linha in transposta:
        print(" ".join(str(item) for item in linha))

gerar_transposta()
